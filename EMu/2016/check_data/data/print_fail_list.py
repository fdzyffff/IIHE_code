import sys
import os
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%d %d %d \n'%(line[0],line[1],line[2]))


List_from_sam = []
List_from_me = []

dir_list = [
'../../Data_SingleMuon/sync/ntuples/pk_batchdata_loop_1/',
'../../Data_SinglePhoton/sync/ntuples/pk_batchdata_loop_1/'
]

for root_dir in dir_list:
    
    for file_in in os.listdir(root_dir):
        tchain = ROOT.TChain('IIHEAnalysis')
        tchain.Add("%s/%s"%(root_dir,file_in))
        iEntry = 0
        totalEntry = tchain.GetEntries()
        for event in tchain:
        #    if iEntry >1000:break
            if iEntry%50000==0 and iEntry > 0:
                print '%d / %d  Prossed'%(iEntry,totalEntry)
            ev_event = getattr(event,'ev_event') & 0xffffffff
            ev_run = getattr(event,'ev_run')# & 0xffffffff
            if ev_event <0: print ev_event
            ev_luminosityBlock = getattr(event,'ev_luminosityBlock')
            tmp_list = [ev_run, ev_luminosityBlock, ev_event]
            List_from_me.append(tmp_list)
            iEntry+=1

print '************ read from file finish **************'

List_from_me.sort()

print len(List_from_me)

write_to_file('my_missed.list',List_from_me)
