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
    tchain.Add('ntuples/data_MuonEG.root')
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
    ev_event = getattr(event,'ev_event_out') & 0xffffffff
    ev_run = getattr(event,'ev_run_out')# & 0xffffffff
    if ev_event <0: print ev_event
    ev_luminosityBlock = getattr(event,'ev_luminosityBlock_out')
    M_ll = getattr(event,'M_ll')
    isEMu = getattr(event,'isEMu')
    isEE = getattr(event,'isEE')
    isMuMu = getattr(event,'isMuMu')
    pass_trigger_EMu = getattr(event,'pass_trigger_EMu')
    pass_trigger_EE = getattr(event,'pass_trigger_EE')
    pass_trigger_MuMu = getattr(event,'pass_trigger_MuMu')
    pass_step1 = getattr(event,'pass_step1')
    if isEMu and pass_trigger_EMu and pass_step1:
        tmp_list = [ev_run, ev_luminosityBlock, ev_event]
        List_from_me.append(tmp_list)
    iEntry+=1

print '************ read from file finish **************'

List_from_me.sort()

print len(List_from_me)

write_to_file('data_EMu.list',List_from_me)
