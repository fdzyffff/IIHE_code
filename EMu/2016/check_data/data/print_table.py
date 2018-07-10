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

def print_event_table(tchain, event_dic):
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
        M_emu = getattr(event,'M_emu')
        ele_pt = getattr(event,'t_Et')
        ele_eta = getattr(event,'t_eta')
        ele_phi = getattr(event,'t_phi')
        ele_region = getattr(event,'t_region')
        muon_pt = getattr(event,'muon_pt')
        muon_eta = getattr(event,'muon_eta')
        muon_phi = getattr(event,'muon_phi')
        muon_region = getattr(event,'muon_region')
    #    if not getattr(event,'muon_trig_Flag_HBHENoiseFilter_accept'):continue
    #    if not getattr(event,'muon_trig_Flag_HBHENoiseIsoFilter_accept'):continue
    #    if not getattr(event,'muon_trig_Flag_CSCTightHaloFilter_accept'):continue
    #    if not getattr(event,'muon_trig_Flag_goodVertices_accept'):continue
    #    if not getattr(event,'muon_trig_Flag_eeBadScFilter_accept'):continue
    #    if not getattr(event,'muon_trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept'):continue
    #    if getattr(event,'muon_trig_Flag_badMuons_accept'):continue
    #    if not getattr(event,'muon_trig_Flag_chargedHadronTrackResolutionFilter_accept'):continue
        tmp_list = [ev_run, ev_luminosityBlock, ev_event, M_emu, ele_pt, ele_eta, ele_phi, muon_pt, muon_eta, muon_phi]
        if M_emu > 1200.0:
            p_List.append(tmp_list)
        for mass_range in event_dic:
            mass_low = event_dic[mass_range][0][0]
            mass_high = event_dic[mass_range][0][1]
            if M_emu >= mass_low and M_emu < mass_high:
                event_dic[mass_range][1] += 1
                if event_dic[mass_range][3]:
                    event_dic[mass_range][2].append(tmp_list)
                break
        iEntry+=1

    for mass_range in event_dic:
        print "%s : %s"%(mass_range, event_dic[mass_range][1])

def print_event_info(event_list):
    print "run, lumi, event, mass,||, Ele pt, Ele eta, Ele phi,||, Muon pt, Muon eta, Muon phi"
    for ev in event_list:
        print "%d ,%d, %d, %f,||, %f, %f, %f,||, %f, %f, %f"%(ev[0], ev[1], ev[2], ev[3], ev[4], ev[5], ev[6], ev[7], ev[8], ev[9])

def print_event_info2(event_list):
    print "mass, run, lumi, event"
    event_list.sort(key=lambda d:d[3], reverse=False)
    for ev in event_list:
        print "%f, %d ,%d, %d"%(ev[3], ev[0], ev[1], ev[2])
try:
    tchain=ROOT.TChain('tap')
    tchain.Add('data_2016_SingleMuon_SinglePhoton2.root')
except:
    print "errors!"

#[down limit, up limit],number,[event list],isprint
event_dic = {
"M_0-500"	:[[0,500],0,[],False],
"M_500-1000"	:[[500 ,1000],0,[],False],
"M_1000-1500"	:[[1000,1500],0,[],False],
"M_1500-inf"	:[[1500,50000],0,[],True],
}

p_List = []
print p_List
print_event_table(tchain, event_dic)
print "*"*50
#print_event_info(event_dic["M_1500-inf"][2])
print_event_info2(p_List)
