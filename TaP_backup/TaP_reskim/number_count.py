import ROOT

#ch_saved = ROOT.TChain('IIHEAnalysis')
ch_raw = ROOT.TChain('meta')
#ch_saved.Add('~aidan/public/HEEP/data2015/CMSSW_7_4_10_patch2/src/crab_projects/crab_20151222b_RunIISpring15DR74_WJetsToLNu_25ns_v1/results/*.root')
#ch_raw.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/001/*.root')
#ch_saved.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/*.root')
#ch_raw.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/ZToEE_NNPDF30_13TeV-powheg_M_50_120/*.root')
#ch_raw.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/*.root')
ch_raw.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/001/*.root')
#ch_raw.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/002/*.root')
#ch_raw.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/*.root')
#ch_saved.Add('/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/*.root')
#ch_saved.Add('/group/HEEP/25ns_golden/SingleElectron_16Dec2015ReReco_D*')
#ch_saved.Add('/group/HEEP/25ns_silver_not_golden/SingleElectron_16Dec2015ReReco_D*')

# Get weight per event from the ntuple:
w = 225892.45

nWeightedEvents = 0
nRawEvents      = 0
saved_Num_eff=0

#otherarr = new ROOT.TObjArray(*myarr);
#ch_saved.GetListOfFiles()

#for iEntry in range(0, ch_saved.GetEntries()):
#    try:
#    ch_saved.GetEntry(iEntry)
#    except SystemError:
#        print 'found error'
#        continue
#    else:
#    if ch_saved.mc_w_sign > 0:
#        sign=1
#    if ch_saved.mc_w_sign < 0:
#        sign=-1
#    saved_Num_eff = saved_Num_eff + sign
#print 'saved eff events = ' , saved_Num_eff


for iEntry in range(0, ch_raw.GetEntries()):
    ch_raw.GetEntry(iEntry)
    nRawEvents      += ch_raw.nEventsRaw
#    nWeightedEvents      += ch_raw.mc_nEventsWeighted
print 'nRawEvents = ' , nRawEvents
#print 'nWeightedEvents = ' , nWeightedEvents


