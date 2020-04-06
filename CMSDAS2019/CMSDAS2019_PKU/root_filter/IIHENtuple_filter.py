from definations import *
from optparse import OptionParser

def event_filter(input_file1, output_file, reverse=False):
#If reverse, will fill events not in list, if not reverse, will fill events in list
    file_in = ROOT.TFile(input_file1,'READ')
    tree_in = file_in.Get('IIHEAnalysis')
    n_event_1 = tree_in.GetEntries()
    tree_in.SetBranchStatus('*', 0)
    tree_in.SetBranchStatus('gsf_n', 1)
    tree_in.SetBranchStatus('gsf_charge', 1)
    tree_in.SetBranchStatus('gsf_ecalEnergyPostCorr', 1)
    tree_in.SetBranchStatus('gsf_theta', 1)
    tree_in.SetBranchStatus('gsf_eta', 1)
    tree_in.SetBranchStatus('gsf_phi', 1)
    tree_in.SetBranchStatus('gsf_sc_energy', 1)
    tree_in.SetBranchStatus('gsf_sc_eta', 1)
    tree_in.SetBranchStatus('gsf_sc_eta', 1)
    tree_in.SetBranchStatus('gsf_deltaPhiSuperClusterTrackAtVtx', 1)
    tree_in.SetBranchStatus('gsf_full5x5_sigmaIetaIeta', 1)
    tree_in.SetBranchStatus('gsf_nLostInnerHits', 1)
    tree_in.SetBranchStatus('gsf_dxy_firstPVtx', 1)
    tree_in.SetBranchStatus('gsf_hadronicOverEm', 1)
    tree_in.SetBranchStatus('gsf_full5x5_e1x5', 1)
    tree_in.SetBranchStatus('gsf_full5x5_e2x5Max', 1)
    tree_in.SetBranchStatus('gsf_full5x5_e5x5', 1)
    tree_in.SetBranchStatus('gsf_dr03EcalRecHitSumEt', 1)
    tree_in.SetBranchStatus('gsf_dr03HcalDepth1TowerSumEt', 1)
    tree_in.SetBranchStatus('gsf_heepTrkPtIso', 1)
    tree_in.SetBranchStatus('gsf_ecaldrivenSeed', 1)
    tree_in.SetBranchStatus('gsf_deltaEtaSeedClusterTrackAtVtx', 1)
    tree_in.SetBranchStatus('ev_fixedGridRhoFastjetAll', 1)
    tree_in.SetBranchStatus('pv_n', 1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta',1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi',1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta',1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi',1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta',1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi',1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta',1)
    tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi',1)
    tree_in.SetBranchStatus('trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta',1)
    tree_in.SetBranchStatus('trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi',1)
    tree_in.SetBranchStatus('trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta',1)
    tree_in.SetBranchStatus('trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi',1)

    file_out = ROOT.TFile(output_file,"RECREATE")
    tree_out = tree_in.CloneTree(0)

    n_fired = 0
    n_pickup = 0
    process_bar = ShowProcess(n_event_1)
    for i in range(0,n_event_1):
        tree_in.GetEntry(i)
        process_bar.show_process()
        tree_out.Fill()

    process_bar.close()
    tree_out.GetCurrentFile().Write()


parser=OptionParser()

parser.add_option("-i","--innput_name",dest="innput_name",default='',type="str")
parser.add_option("-o","--output_name",dest="output_name",default='',type="str")
(options,args)=parser.parse_args()


print "### input file : %s"%(options.innput_name)
print "### output file : %s"%(options.output_name)
event_filter(options.innput_name,options.output_name)



