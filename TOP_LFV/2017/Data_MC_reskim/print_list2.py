import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%d %d %d\n'%(line[0],line[1],line[2]))

try:
    tchain=ROOT.TChain('tap')
    tchain.Add('ntuples/data_80_MuonEG.root')
except:
    print "errors!"

List_from_sam = []
List_from_me = []

iEntry = 0
totalEntry = tchain.GetEntries()
for event in tchain:
    iEntry+=1
    if iEntry%50000==0 and iEntry > 0:
        print '%d / %d  Prossed'%(iEntry,totalEntry)
    isEMu = getattr(event,"isEMu")
    pass_step1 = getattr(event,"pass_step1")
    pass_trigger_EMu = getattr(event,"pass_trigger_EMu")
    MET_T1Txy_significance = getattr(event,"MET_T1Txy_significance")
    M_ll = getattr(event,"M_ll")
    if not (isEMu and pass_step1 and pass_trigger_EMu and (M_ll > 80 or MET_T1Txy_significance>4)):continue

    ev_event = getattr(event,'ev_event_out')
    ev_run = getattr(event,'ev_run_out')
    ev_luminosityBlock = getattr(event,'ev_luminosityBlock_out')

    tmp_list = [ev_run, ev_luminosityBlock, ev_event]
    List_from_me.append(tmp_list)

print '************ read from file finish **************'

List_from_me.sort()

print len(List_from_me)

write_to_file('data_MuonEG_step2.list',List_from_me)
