import os
import datetime
import ROOT
from mod_particle import electron_object
from mod_trigger  import match_trigger

PU_prefix = '~/public/HEEP/data2015/PUHistograms/'
f_PU = {}
h_PU = {}
f_PU['golden'     ] = ROOT.TFile('%sdataPUBin_25ns_complete_golden.root'          %PU_prefix, 'READ')
f_PU['silver_down'] = ROOT.TFile('%sdataPUBin_25ns_complete_silver_minus1Sig.root'%PU_prefix, 'READ')
f_PU['silver_up'  ] = ROOT.TFile('%sdataPUBin_25ns_complete_silver_plus1Sig.root' %PU_prefix, 'READ')
f_PU['silver'     ] = ROOT.TFile('%sdataPUBin_25ns_complete_silver.root'          %PU_prefix, 'READ')
f_PU_MC             = ROOT.TFile('%smcPUDist25ns.root'                            %PU_prefix, 'READ')
h_PU_MC = f_PU_MC.Get('mcPUDist')

for PUname in f_PU:
    h = f_PU[PUname].Get('pileup')
    h.Scale(1.0/h.GetSumOfWeights())
    h.Divide(h_PU_MC)
    h_PU[PUname] = h

class dataset_object:
    def __init__(self, name, path, type):
        self.name = name
        self.path = path
        self.type = type
        self.filenames = os.listdir(self.path)
        self.HLT_names = []
    
    def count_events(self):
        nEvents = 0
        for fname in self.filenames:
            file_in = ROOT.TFile('%s/%s'%(self.path,fname),'READ')
            tree_in = file_in.Get('meta')
            tree_in.GetEntry(0)
            nEvents += tree_in.nEventsRaw
        print '%20s : %8d'%(self.name, nEvents)
    
    def analyse_trigger(self):
        for fname in self.filenames:
            if '_1.root' not in fname:
                continue
            if 'Single' not in fname:
                continue
            file_in = ROOT.TFile('%s%s'%(self.path,fname),'READ')
            tree_in = file_in.Get('IIHEAnalysis')
            tree_in.GetEntry(0)
            run = tree_in.ev_run
            if run in triggers_by_run:
                continue
            print run , fname
            leaves = tree_in.GetListOfLeaves()
            triggers = []
            for leaf in leaves:
                lname = leaf.GetName()
                if 'trig_HLT_Ele27' not in lname:
                    continue
                if '_accept' not in lname:
                    continue
                if 'Loose' not in lname:
                    continue
                if 'Boost' in lname:
                    continue
                triggers.append(lname)
            triggers_by_run[run] = triggers
        
    def analyse_all_files(self):
        if self.type=='MC':
            if self.name=='ZToTT':
                self.type = 'ZToTT'
            chain = ROOT.TChain('IIHEAnalysis')
            chain.Add('%s/*.root'%self.path)
            filename = 'ntuples/skim/%s.root'%(self.name)
            print self.name , filename
            self.analyse_tree(filename, chain, self.type)
        else:            
            for fname in self.filenames:
                if self.name=='25ns_golden_2015C':
                    if '2015C' not in fname:
                        continue
                    if 'Single' not in fname:
                        continue
                if self.name=='25ns_golden_2015D':
                    if '2015D' not in fname:
                        continue
                    if 'Single' not in fname:
                        continue
                if self.name=='25ns_silver_not_golden':
                    if '2015D' not in fname:
                        continue
                    if 'Single' not in fname:
                        continue
                self.analyse_file(fname,self.type)
    
    def analyse_file(self, filename, type):
        print filename, type
        filename_out = 'ntuples/skim/%s/%s'%(self.name,filename)
        
        file_in = ROOT.TFile('%s%s'%(self.path,filename),'READ')
        tree_in = file_in.Get('IIHEAnalysis')
        
        if tree_in.GetEntries() == 0:
            return
        self.analyse_tree(filename_out, tree_in, type)
        
    
    def analyse_tree(self, filename, tree_in, type):
        print datetime.datetime.now().strftime('%a %b %H:%M:%S %Y')
    
        tree_in.SetBranchStatus('*',0)
        if type=='Data':
            tree_in.SetBranchStatus('trig_HLT_Ele27*Loose*',1)
        if type!='Data':
            tree_in.SetBranchStatus('mc_*',1)
        tree_in.SetBranchStatus('Zee_*',1)
        tree_in.SetBranchStatus('pv_n',1)
        tree_in.SetBranchStatus('gsf_n',1)
        tree_in.SetBranchStatus('gsf_phi',1)
        tree_in.SetBranchStatus('gsf_charge',1)
        tree_in.SetBranchStatus('gsf_energy',1)
        tree_in.SetBranchStatus('gsf_caloEnergy',1)
        tree_in.SetBranchStatus('gsf_mc*',1)
        tree_in.SetBranchStatus('HEEP_cutflow60*',1)
        
        file_out = ROOT.TFile(filename,'RECREATE')
        tree_out = ROOT.TTree('IIHEAnalysis', 'Skimmed TTree')
        
        v_pv_n      = ROOT.vector('int')()
        v_PU_true   = ROOT.vector('int')()
        v_HLT_Ele27 = ROOT.vector('int')()
        
        v_Zee_mass_HEEP = ROOT.vector('double')()
        v_Zee_OS        = ROOT.vector('int')()
        
        v_w_PU_golden      = ROOT.vector('double')()
        v_w_PU_silver      = ROOT.vector('double')()
        v_w_PU_silver_up   = ROOT.vector('double')()
        v_w_PU_silver_down = ROOT.vector('double')()
        
        v_e1_Et     = ROOT.vector('double')()
        v_e1_eta    = ROOT.vector('double')()
        v_e1_phi    = ROOT.vector('double')()
        v_e1_charge = ROOT.vector('int')()
        v_e1_Et35   = ROOT.vector('double')()
        v_e1_Et20   = ROOT.vector('double')()
        v_e1_region = ROOT.vector('int')()
        v_e1_ID_tag         = ROOT.vector('int')()
        v_e1_ID_noDEtaIn    = ROOT.vector('int')()
        v_e1_ID_EcalDriven  = ROOT.vector('int')()
        v_e1_ID_noIsolation = ROOT.vector('int')()
        v_e1_ID_vanilla     = ROOT.vector('int')()
        v_e1_HLT_Ele27      = ROOT.vector('int')()
        v_e1_istag          = ROOT.vector('int')()
        v_e1_truthmatch     = ROOT.vector('int')()
        
        v_e2_Et     = ROOT.vector('double')()
        v_e2_eta    = ROOT.vector('double')()
        v_e2_phi    = ROOT.vector('double')()
        v_e2_charge = ROOT.vector('int')()
        v_e2_Et35   = ROOT.vector('double')()
        v_e2_Et20   = ROOT.vector('double')()
        v_e2_region = ROOT.vector('int')()
        v_e2_ID_tag         = ROOT.vector('int')()
        v_e2_ID_noDEtaIn    = ROOT.vector('int')()
        v_e2_ID_EcalDriven  = ROOT.vector('int')()
        v_e2_ID_noIsolation = ROOT.vector('int')()
        v_e2_ID_vanilla     = ROOT.vector('int')()
        v_e2_HLT_Ele27      = ROOT.vector('int')()
        v_e2_istag          = ROOT.vector('int')()
        v_e2_truthmatch     = ROOT.vector('int')()
        
        tree_out.Branch('pv_n', v_pv_n)
        tree_out.Branch('PU_true', v_PU_true)
        tree_out.Branch('HLT_Ele27', v_HLT_Ele27)
        
        tree_out.Branch('Zee_mass_HEEP', v_Zee_mass_HEEP)
        tree_out.Branch('Zee_OS', v_Zee_OS)
        
        tree_out.Branch('w_PU_golden'     , v_w_PU_golden     )
        tree_out.Branch('w_PU_silver'     , v_w_PU_silver     )
        tree_out.Branch('w_PU_silver_up'  , v_w_PU_silver_up  )
        tree_out.Branch('w_PU_silver_down', v_w_PU_silver_down)
        
        tree_out.Branch('e1_Et'    , v_e1_Et    )
        tree_out.Branch('e1_eta'   , v_e1_eta   )
        tree_out.Branch('e1_phi'   , v_e1_phi   )
        tree_out.Branch('e1_charge', v_e1_charge)
        tree_out.Branch('e1_Et35'  , v_e1_Et35  )
        tree_out.Branch('e1_Et20'  , v_e1_Et20  )
        tree_out.Branch('e1_region', v_e1_region)
        tree_out.Branch('e1_ID_tag'        , v_e1_ID_tag        )
        tree_out.Branch('e1_ID_noDEtaIn'   , v_e1_ID_noDEtaIn   )
        tree_out.Branch('e1_ID_EcalDriven' , v_e1_ID_EcalDriven )
        tree_out.Branch('e1_ID_noIsolation', v_e1_ID_noIsolation)
        tree_out.Branch('e1_ID_vanilla'    , v_e1_ID_vanilla    )
        tree_out.Branch('e1_HLT_Ele27'     , v_e1_HLT_Ele27     )
        tree_out.Branch('e1_istag'         , v_e1_istag         )
        tree_out.Branch('e1_truthmatch'    , v_e1_truthmatch    )
        
        tree_out.Branch('e2_Et'    , v_e2_Et    )
        tree_out.Branch('e2_eta'   , v_e2_eta   )
        tree_out.Branch('e2_phi'   , v_e2_phi   )
        tree_out.Branch('e2_charge', v_e2_charge)
        tree_out.Branch('e2_Et35'  , v_e2_Et35  )
        tree_out.Branch('e2_Et20'  , v_e2_Et20  )
        tree_out.Branch('e2_region', v_e2_region)
        tree_out.Branch('e2_ID_tag'        , v_e2_ID_tag        )
        tree_out.Branch('e2_ID_noDEtaIn'   , v_e2_ID_noDEtaIn   )
        tree_out.Branch('e2_ID_EcalDriven' , v_e2_ID_EcalDriven )
        tree_out.Branch('e2_ID_noIsolation', v_e2_ID_noIsolation)
        tree_out.Branch('e2_ID_vanilla'    , v_e2_ID_vanilla    )
        tree_out.Branch('e2_HLT_Ele27'     , v_e2_HLT_Ele27     )
        tree_out.Branch('e2_istag'         , v_e2_istag         )
        tree_out.Branch('e2_truthmatch'    , v_e2_truthmatch    )
        
        nEntries = tree_in.GetEntries()
        for iEntry in range(0,nEntries):
            if iEntry % 10000 == 0:
                print iEntry , '/' , nEntries
        
            v_Zee_mass_HEEP.clear()
            v_Zee_OS.clear()
            v_pv_n.clear()
            v_PU_true.clear()
            v_w_PU_golden     .clear()
            v_w_PU_silver     .clear()
            v_w_PU_silver_up  .clear()
            v_w_PU_silver_down.clear()
            v_HLT_Ele27       .clear()
        
            v_e1_Et .clear()
            v_e1_eta.clear()
            v_e1_phi.clear()
            v_e1_Et35.clear()
            v_e1_Et20.clear()
            v_e1_charge.clear()
            v_e1_region.clear()
            v_e1_ID_tag        .clear()
            v_e1_ID_noDEtaIn   .clear()
            v_e1_ID_EcalDriven .clear()
            v_e1_ID_noIsolation.clear()
            v_e1_ID_vanilla    .clear()
            v_e1_HLT_Ele27     .clear()
            v_e1_istag         .clear()
            v_e1_truthmatch    .clear()
            
            v_e2_Et .clear()
            v_e2_eta.clear()
            v_e2_phi.clear()
            v_e2_charge.clear()
            v_e2_Et35.clear()
            v_e2_Et20.clear()
            v_e2_region.clear()
            v_e2_ID_tag        .clear()
            v_e2_ID_noDEtaIn   .clear()
            v_e2_ID_EcalDriven .clear()
            v_e2_ID_noIsolation.clear()
            v_e2_ID_vanilla    .clear()
            v_e2_HLT_Ele27     .clear()
            v_e2_istag         .clear()
            v_e2_truthmatch    .clear()
            
            tree_in.GetEntry(iEntry)
            
            accept_event = True
            if type=='ZToTT':
                accept_event = False
                has_taup = False
                has_taum = False
                for iMC in range(0,tree_in.mc_n):
                    if tree_in.mc_pdgId[iMC]== 15:
                        has_taum = True
                    if tree_in.mc_pdgId[iMC]==-15:
                        has_taup = True
                if has_taup and has_taum:
                    accept_event = True
            if accept_event == False:
                continue
                    
            accept_Zee = False
            for iZee in range(0,tree_in.Zee_n):
                e1 = electron_object(tree_in, tree_in.Zee_i1[iZee])
                e2 = electron_object(tree_in, tree_in.Zee_i2[iZee])
                
                if e1.isTag == False and e2.isTag == False:
                    continue
                
                e1.triggerMatch = False
                e2.triggerMatch = False
                if e1.isTag:
                    e1.triggerMatch = match_trigger(tree_in, e1.Et, e1.eta, e1.phi, type=='Data')
                if e2.isTag:
                    e2.triggerMatch = match_trigger(tree_in, e2.Et, e2.eta, e2.phi, type=='Data')
                
                e1.isTag = e1.isTag and e1.triggerMatch
                e2.isTag = e2.isTag and e2.triggerMatch
                
                if e1.isTag == False and e2.isTag == False:
                    continue
                
                if type=='Data':
                    v_PU_true.push_back(-1)
                    v_w_PU_golden     .push_back(1)
                    v_w_PU_silver     .push_back(1)
                    v_w_PU_silver_up  .push_back(1)
                    v_w_PU_silver_down.push_back(1)
                else:
                    PU = tree_in.mc_trueNumInteractions
                    v_PU_true.push_back(PU)
                    if PU >=1 and PU < h_PU_MC.GetNbinsX():
                        v_w_PU_golden     .push_back(h_PU['golden'     ].GetBinContent(PU))
                        v_w_PU_silver     .push_back(h_PU['silver_down'].GetBinContent(PU))
                        v_w_PU_silver_up  .push_back(h_PU['silver_up'  ].GetBinContent(PU))
                        v_w_PU_silver_down.push_back(h_PU['silver'     ].GetBinContent(PU))
                    else:
                        v_w_PU_golden     .push_back(0)
                        v_w_PU_silver     .push_back(0)
                        v_w_PU_silver_up  .push_back(0)
                        v_w_PU_silver_down.push_back(0)
                
                v_e1_truthmatch.push_back(e1.truthmatch)
                v_e2_truthmatch.push_back(e2.truthmatch)
                
                v_pv_n.push_back(tree_in.pv_n)
                v_HLT_Ele27.push_back(1)
                
                v_Zee_mass_HEEP.push_back(tree_in.Zee_mass_HEEP[iZee])
                
                v_e1_Et .push_back(e1.Et )
                v_e1_eta.push_back(e1.eta)
                v_e1_phi.push_back(e1.phi)
                v_e1_charge.push_back(e1.charge)
                v_e1_Et35.push_back(e1.Et35)
                v_e1_Et20.push_back(e1.Et20)
                
                e1_region = -1
                if e1.region == 'Barrel':
                    e1_region = 0
                elif e1.region == 'Transition':
                    e1_region = 1
                elif e1.region == 'Endcap':
                    e1_region = 2
                v_e1_region.push_back(e1_region)
        
                v_e1_ID_tag        .push_back(e1.accept_tag_ID        )
                v_e1_ID_noDEtaIn   .push_back(e1.accept_noDEtaIn_ID   )
                v_e1_ID_EcalDriven .push_back(e1.accept_EcalDriven    )
                v_e1_ID_noIsolation.push_back(e1.accept_noIsolation_ID)
                v_e1_ID_vanilla    .push_back(e1.accept_vanilla_ID    )
                v_e1_HLT_Ele27     .push_back(e1.triggerMatch)
                v_e1_istag.push_back(e1.accept_tag_ID and e1.region=='Barrel' and e1.Et35)
                
                v_e2_Et .push_back(e2.Et )
                v_e2_eta.push_back(e2.eta)
                v_e2_phi.push_back(e2.phi)
                v_e2_charge.push_back(e2.charge)
                v_e2_Et35.push_back(e2.Et35)
                v_e2_Et20.push_back(e2.Et20)
                
                e2_region = -1
                if e2.region == 'Barrel':
                    e2_region = 0
                elif e2.region == 'Transition':
                    e2_region = 1
                elif e2.region == 'Endcap':
                    e2_region = 2
                v_e2_region.push_back(e2_region)
        
                v_e2_ID_tag        .push_back(e2.accept_tag_ID        )
                v_e2_ID_noDEtaIn   .push_back(e2.accept_noDEtaIn_ID   )
                v_e2_ID_EcalDriven .push_back(e2.accept_EcalDriven    )
                v_e2_ID_noIsolation.push_back(e2.accept_noIsolation_ID)
                v_e2_ID_vanilla    .push_back(e2.accept_vanilla_ID    )
                v_e2_HLT_Ele27     .push_back(e2.triggerMatch)
                v_e2_istag.push_back(e2.accept_tag_ID and e2.region=='Barrel' and e2.Et35)
                
                accept_Zee = True
                
            if accept_Zee:
                tree_out.Fill()
        
        tree_out.Write()
        file_out.Close()
        
        time_end = time.time()
        print datetime.datetime.now().strftime('%a %b %H:%M:%S %Y')


data_prefix = '../../data2015/skims/'
MC_prefix   = '../../samples/RunIISpring15DR74/'            

datasets = []
datasets.append(dataset_object('25ns_silver_not_golden', '%s25ns_silver_not_golden/'%data_prefix, 'Data'))
datasets.append(dataset_object('25ns_golden'           , '%s25ns_golden/'           %data_prefix, 'Data'))
#datasets.append(dataset_object('50ns_golden'           , '%s50ns_golden/'           %data_prefix, 'Data'))
#datasets.append(dataset_object('50ns_0T_golden'        , '%s50ns_0T_golden/'        %data_prefix, 'Data'))
#datasets.append(dataset_object('25ns_0T_golden'        , '%s25ns_0T_golden/'        %data_prefix, 'Data'))

#datasets.append(dataset_object('25ns_golden_2015C', '%s25ns_golden/'           %data_prefix, 'Data'))
#datasets.append(dataset_object('25ns_golden_2015D', '%s25ns_golden/'           %data_prefix, 'Data'))

#datasets.append(dataset_object('WW'   , '%sRunIISpring15DR74_WW_25ns_v1/'           %MC_prefix, 'MC'))
#datasets.append(dataset_object('ZToEE', '%sRunIISpring15DR74_ZToEE_50_120_25ns/'    %MC_prefix, 'MC'))
#datasets.append(dataset_object('ttbar', '%sRunIISpring15DR74_powheg_TTJets_25ns_v4/'%MC_prefix, 'MC'))
#datasets.append(dataset_object('WJets', '%sRunIISpring15DR74_WJetsToLNu_25ns_v1/'   %MC_prefix, 'MC'))
#datasets.append(dataset_object('ZToTT', '%sRunIISpring15DR74_DYJetsToLL_M50_25ns/'  %MC_prefix, 'MC'))

triggers_by_run = {}

for d in datasets:
    #d.count_events()
    #d.analyse_all_files()
    d.analyse_trigger()

runs = []
for run in triggers_by_run:
    runs.append(run)

runs = sorted(runs)
for run in runs:
    print run , triggers_by_run[run]
