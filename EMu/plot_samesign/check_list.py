import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT


List_file = 'Event_list_m60_120_BB_BE_EE_EnergyCorrection.txt'
only_in_me = 'event_onlyin_root.list'
only_in_sam = 'event_onlyin_sam.list'
same_event = 'same_event.list'



def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%d %d %d \n'%(line[0],line[1],line[2]))

def my_diff(list_1, list_2):
    same_list = []
    isSame = True
    n_processed = 0
    n_total = len(list_1)
    i_2_start = 0
    for i_1 in range(len(list_1)):
        L_1 = list_1[i_1]
        n_processed += 1
        n_count = 0
        isprint = True
        if n_processed%500==0 and iEntry > 0:
            print '%d / %d  Prossed'%(n_processed, n_total)
        for i_2 in range(i_2_start, len(list_2)):
            n_count += 1
            L_2 = list_2[i_2]
            isSame = True
#            if L_1[2]!=L_2[2]:
#                isSame = False
#                continue
            for i in range(len(L_2)):
                if L_1[i] != L_2[i]:
                    isSame = False
                    break
            if isprint:
#                print len(list_2)
                isprint = False
            if n_count > 500:
            	print'*'*20
            	print i_2_start
            	print n_count
            	print L_1
            	break
            if isSame:
                same_list.append(L_1)
                #print L_1
                list_1[i_1]=''
                list_2[i_2]=''
                i_2_start = i_2
#                list_2.remove(list_2[i_2])
#                print n_count
                break
    return same_list

try:
    tchain=ROOT.TChain('tap')
    tchain.Add('./data_2016_SingleMuon.root')
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
    M_ee = getattr(event,'M_emu')
    t_region = getattr(event,'t_region')
    heep2_region = getattr(event,'muon_region')
#    if 60<=M_ee and M_ee<=120 :
#        if (t_region == 1 and heep2_region == 1) or (t_region == 3 and heep2_region == 3) or (t_region == 1 and heep2_region == 3) or (t_region == 3 and heep2_region == 1):
    tmp_list = [ev_run, ev_luminosityBlock, ev_event]
    List_from_me.append(tmp_list)
    iEntry+=1

#for Line in open(List_file,'r'):
#    if '#' in Line:continue
#    line=Line.split(' ')
#    tmp_list = [int(line[0]), int(line[1]), int(line[2])]
#    List_from_sam.append(tmp_list)
print '************ read from file finish **************'

List_from_me.sort()
#List_from_sam.sort()

print len(List_from_me)
#print len(List_from_sam)

write_to_file('my_result.list',List_from_me)
#write_to_file('sam_result.list',List_from_sam)

print List_from_me[1]
#print List_from_sam[1]
print '************ check **************'



#intersection = []
#intersection = my_diff(List_from_sam, List_from_me)
#
#diffevent_me = []
#diffevent_sam = []
#for L in List_from_me:
#    if L!='':
#        diffevent_me.append(L)
#
#for L in List_from_sam:
#    if L!='':
#        diffevent_sam.append(L)
#
#write_to_file(only_in_me, diffevent_me)
#write_to_file(only_in_sam, diffevent_sam)
#write_to_file(same_event, intersection)
#    
#
