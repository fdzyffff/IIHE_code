This package performs the tag and probe scale factor study for the HEEP ID V6.0.
It is written mostly in python, with C++ doing the heavy lifting.  The scale factors are
measured using a cut and count method, and cross checked by fits to the Z peak.

Most of the settings are written in mod_settings.py .  Here you can choose which
selections to use.  The selections split the histograms up by:

Charge:
  em: electron
  ep: positron
  ea: electron and positron (sum of em and ep)

Sign:
  OS: Opposite sign tag and probe pairs
  SS: Same sign tag and probe pairs
  AS: Opposite and same sine tag and probe pairs (sum of OS and SS)

Probe status:
  pass: Probe passes the ID
  fail: Probe fails the ID
  probes: All probes (sum of pass and fail)

Region:
  Barrel: |eta(probe)| < 1.4442
  Transition: 1.4442 < |eta(probe)| < 1.566
  Endcap: 1.566 < |eta(probe)| < 2.5

"Alternative cuts" are used as cross checks, or as requested by analysts.  These include:
  nominal: Normal HEEP ID V6.0
  noDEtaIn: The probe is not required to pass the DEtaIn cut in the endcap (to take 
    misalignment in the endcap in Run2015 B/C into account)
  gsfEcalDriven: The probe is required to be EcalDriven (to remove a discontinuity in the
    Et spectrum of the probe at 50 GeV)
  noIsolation: The probe is not required to pass the isolation requirements (as
    requested by a boost Z analysis)

The scale factors are estimated as functions of four variables:
  Et: gsf->caloEnergy()*sin(gsf->theta())
  eta: gsf->supercluster->eta()
  phi: gsf->phi()
  nVtx: Number of primary vertices in the event
Adding a new variable is easy.  Each variable has its own binnings which are region
dependent.  You will need to add your variables to the skimmed TTrees and histograms (see
below for instructions.)

You can choose which selections and variables to use in mod_setttings.py .

To run the analysis there are several steps:

  1. Make the base histograms (python)
  Set all the configuration flags in mod_settings.py to False, except
  do_make_base_histograms, which should be True.  Then run:
  > python TagAndProbe.py
  This will make a file called hBase.root that contains the base histograms.

  2. Reskim the ntuples (C++)
  This step takes the longest and it skims the large IIHEAnalysis TTrees into very small
  tap (tag and probe) TTrees.
  > root -b
  [0] .L reskim.C+
  [1] .L reskim_all.C
  [2] reskim_all()
  [3] .q
  This makes TFiles in the directory ntuples/reskim .
  
  3. Make and fill the histograms (C++)
  Now that we have the base histograms and the skimmed TTrees we can make and fill the
  histograms.  This is done in ROOT to speed up the process.  Change the name of the
  campaign in fill_all_histograms.C and make sure the directory ntuples/out/<CAMPAIGN>
  exists.  (You must choose a campaign here to get the PU weights for the MC correct.)
  > root -b
  [0] .L fill_histograms.C+
  [1] .L fill_all_histograms.C
  [2] fill_all_histograms()
  [3] .q
  This makes TFiles in the directory ntuples/out/<CAMPAIGN>
  
  4. Perform analysis
  We are now ready to perform the analysis!  Set the configuration flags in
  mod_settings.py to the following values:
  
    # Configuration flags:
    do_make_histograms      = False # This is a slow python based method
    do_analysis             = True  # This the analysis flag
    do_fits                 = True  # Set to False if you want to skip the fits
    do_cuts                 = True  # Set to False if you want to skip the cut method
    do_print_efficiencies   = True  # Print to the efficiencies to screen
    do_compare              = True  # Make the comparison histograms
    test_fits               = True  # Only do a subset of the analysis
    do_make_base_histograms = False # This can be True or False, it doesn't matter
  
  Update the date in mod_setings.py and make the directory plots/<DATE>/<CAMPAIGN>
  
  You can then run the main program:
  > python TagAndProbe.py
  This will make some TFiles in ntuples/out/<CAMPAIGN> and plots in
  plots/<DATE>/<CAMPAIGN>.
  
  5. Write the analysis note
  To get the different cross checks you will need to change the settings in
  mod_settings.py (eg run a job with OS instead of AS) and rerun TagAndProbe.py with the
  new histograms.  Keep doing this until you have all the plots you need.


To do list:
  Add with/without truthmatching.
  Scale backgrounds up and down.
