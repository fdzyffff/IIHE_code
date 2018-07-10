import os
import ROOT
from math import *

sample_path = {}

#path = '/user/aidan/public/HEEP/data2015/CMSSW_7_4_10_patch2/src/crab_projects/crab_20151222b_RunIISpring15DR74_WJetsToLNu_25ns_v1/results'

sample_path ={
'SingleMuon_Run2016B_PromptReco_v2_AOD_1290': '/group/HEEP/Golden_2016_1290/SingleMuon_Run2016B-PromptReco-v2',
#'SingleMuon_Run2016C_PromptReco_v2_AOD_1290': '/group/HEEP/Golden_2016_1290/SingleMuon_Run2016C-PromptReco-v2',
#'SingleMuon_Run2016D_PromptReco_v2_AOD_1290': '/group/HEEP/Golden_2016_1290/SingleMuon_Run2016D-PromptReco-v2',
}

find_event = False
for sample_name in sample_path:
    filenames = os.listdir(sample_path[sample_name])
    nfiles = 0
    nEventsraw = 0
    neventsweight = 0
    nEventsStored = 0
    nEventsiihe = 0
    nprocessed = 0
    for fname in filenames:
        nfiles += 1
        if find_event:break
        filename = sample_path[sample_name] + '/' + fname
        if not '/group/HEEP/Golden_2016_1290/SingleMuon_Run2016B-PromptReco-v2/SingleMuon_Run2016B-PromptReco-v2__outfile_901.root' in filename:continue
    #    print fname
        if 'fail' in fname or not ('.root' in fname):
            continue
        f = ROOT.TFile.Open(filename)
        if not f:
    #        print 'rm -rf '+fname
            print 'not exist'+fname
        tree_in = f.Get('IIHEAnalysis')
        if nfiles%(int(len(filenames)/10))==0:print '%d / %d, %s processing' %(nfiles,len(filenames),filename)
        if tree_in.Draw('','ev_run == 274161') == 0:continue
        for event in tree_in:
            if find_event:break
            if (getattr(event,'ev_event') & 0xffffffff ) == 653892572:
                print '############# Find Event: %s'%(filename)
                gsf_n = getattr(event,'gsf_n')
                for i in range(gsf_n):
                    E = 0
                    Et = 0
                    eta = 0
                    theta = 0
                    phi = 0
                    isHeep = 0
                    HOverE = getattr(event,'gsf_hadronicOverEm')[i]
                    caloEnergy = getattr(event,'gsf_superClusterEnergy')[i]
                    e1x5 = getattr(event,'gsf_full5x5_e1x5')[i]
                    e2x5 = getattr(event,'gsf_full5x5_e2x5Max')[i]
                    e5x5 = getattr(event,'gsf_full5x5_e5x5')[i]
                    E = getattr(event,'gsf_caloEnergy')[i]
                    theta = getattr(event,'gsf_theta')[i]
                    Et = E * sin(theta)
                    eta = getattr(event,'gsf_sc_eta')[i]
                    phi = getattr(event,'gsf_phi')[i]
                    if (getattr(event,'gsf_isHeepV60')[i]):
                        isHeep = 1
                    print "*"*20
                    print 'Et (without E correction) : %f'%(Et)
                    print 'eta : %f'%(eta)
                    print 'phi : %f'%(phi)
                    print 'is Heep : %d'%(isHeep)
                    print 'HOverE accept : ',(HOverE < 0.05 + 5.0/caloEnergy)
                    print 'E1x5OverE5x5  : ',(e1x5/e5x5)
                    print 'E1x5OverE5x5 accept : ',(e1x5/e5x5>0.83)
                    print 'E2x5OverE5x5 accept : ',(e2x5/e5x5>0.94)
                mu_gt_n = getattr(event,'mu_gt_n')
                for i in range(mu_gt_n):
                    if not getattr(event,'mu_isGlobalMuon'):continue
                    Pt = 0
                    eta = 0
                    phi = 0
                    pass_trigger = 0
                
                print 'passed trigger or not %d:'%(getattr(event,'trig_HLT_Mu50_v2_accept'))
                find_event = True
if not find_event:print "doesn't find this event"
