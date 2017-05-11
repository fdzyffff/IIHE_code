import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%d %d %d \n'%(line[0],line[1],line[2]))

try:
    tchain=ROOT.TChain('tap')
    tchain.Add('data_2016_SingleMuon_SinglePhoton2.root')
    #tchain.Add('/user/xgao/CMSSW_7_6_3/src/2016B/Dielectron/EMu_rereco_MINIAOD/Data_SinglePhoton/withCorr/ntuples/data_2016_SinglePhoton.root')
    #tchain.Add('/user/xgao/CMSSW_7_6_3/src/2016B/Dielectron/EMu_rereco_MINIAOD/Data_SingleMuon/withCorr/ntuples/data_2016_SingleMuon.root')
except:
    print "errors!"

List_from_sam = []
List_from_me = []

iEntry = 0
totalEntry = tchain.GetEntries()
for event in tchain:
#    if iEntry >1000:break
    if iEntry%50000==0 and iEntry > 0:
        print '%d / %d  Prossed'%(iEntry,totalEntry)
    ev_event = getattr(event,'ev_event_out') 
    if ev_event < 0:print ev_event
    ev_run = getattr(event,'ev_run_out')# & 0xffffffff
    ev_luminosityBlock = getattr(event,'ev_luminosityBlock_out')
    M_emu = getattr(event,'M_emu')
    heep_region = getattr(event,'ele_region')
    muon_region = getattr(event,'muon_region')
#    if not getattr(event,'muon_trig_Flag_HBHENoiseFilter_accept'):continue
#    if not getattr(event,'muon_trig_Flag_HBHENoiseIsoFilter_accept'):continue
#    if not getattr(event,'muon_trig_Flag_CSCTightHaloFilter_accept'):continue
#    if getattr(event,'trig_Flag_badMuons_accept'):
    if getattr(event,'trig_Flag_goodVertices_accept') != 1:
        print  getattr(event,'trig_Flag_goodVertices_accept')
        continue
#    if not getattr(event,'muon_trig_Flag_eeBadScFilter_accept'):continue
#    if not getattr(event,'muon_trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept'):continue
#    if getattr(event,'muon_trig_Flag_badMuons_accept'):continue
#    if not getattr(event,'muon_trig_Flag_chargedHadronTrackResolutionFilter_accept'):continue
    tmp_list = [ev_run, ev_luminosityBlock, ev_event]
    List_from_me.append(tmp_list)
    iEntry+=1

print '************ read from file finish **************'

List_from_me.sort()

print len(List_from_me)

write_to_file('my_result.list',List_from_me)
