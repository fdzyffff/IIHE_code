import os
import ROOT

input_file1 ='/user/xgao/CMSSW_7_6_3/src/2016B/Dielectron/EMu_rereco_MINIAOD/Data_SingleMuon/withCorr/ntuples/data_2016_SingleMuon.root'
input_file2 ='/user/xgao/CMSSW_7_6_3/src/2016B/Dielectron/EMu_rereco_MINIAOD/Data_SinglePhoton/withCorr/ntuples/data_2016_SinglePhoton.root'
output_file ='data_2016_SingleMuon_SinglePhoton.root'

def event_filter(input_file1, input_file2, output_file):
    file_in = ROOT.TFile(input_file1,'READ')
    tree_in = file_in.Get('tap')
    n_event_1 = tree_in.GetEntries()

    file_out = ROOT.TFile(output_file,"RECREATE")
    tree_out = tree_in.CloneTree(-1)
    tree_out.GetCurrentFile().Write()
    n_total = tree_out.GetEntries()
    
    file_to_filter = ROOT.TFile(input_file2,'READ')
    tree_to_filter = file_to_filter.Get('tap')
    n_event_2 = tree_to_filter.GetEntries()
    n_overlapped = 0
    for i in range(0,tree_to_filter.GetEntries()):
        if i%10000 == 0:
            print "%d / %d processed"%(i, tree_to_filter.GetEntries())
        tree_to_filter.GetEntry(i)
        event=str(tree_to_filter.ev_event_out)
        if event == "1965787424":print "KKKKKKKKKKKKKKKKKKK"
        #print event
        if tree_out.Draw("","ev_event_out == %s"%(event)):
            #print tree_out.GetEntries()
            n_overlapped += 1
            continue 
        else:
            #tree_out.CopyEntries(tree_to_filter,i)
            tree_out.Fill()
            #print tree_out.GetEntries()
            n_total += 1

    print "%d events in file: %s"%(n_event_1, input_file1)
    print "%d events in file: %s, %d overlapped"%(n_event_2, input_file2, n_overlapped)
    print "%d events total in output file: %s"%(n_total, output_file)
    tree_out.GetCurrentFile().Write()
    tree_out.GetCurrentFile().Close()
    file_out.Close()
          
def event_filter2(input_file1, input_file2, output_file):
    file_in = ROOT.TFile(input_file1,'READ')
    tree_in = file_in.Get('tap')
    n_event_1 = tree_in.GetEntries()

    event_list = []
    target = False
    file_out = ROOT.TFile(output_file,"RECREATE")
    tree_out = tree_in.CloneTree(0)
    tree_out.GetCurrentFile().Write()
    n_total = 0
    for i in range(0, tree_in.GetEntries()):
        if i%10000 == 0:
            print "%d / %d processed"%(i, tree_in.GetEntries())
        tree_in.GetEntry(i)
        run=str(tree_in.ev_run_out)
        luminosityBlock=str(tree_in.ev_luminosityBlock_out)
        event=str(tree_in.ev_event_out)
        tmp_str = "%s %s %s"%(run,luminosityBlock, event)
        if tmp_str in event_list:
            print tmp_str
            continue
        else:
            tree_out.Fill()
            event_list.append(tmp_str)
            n_total += 1

    #n_total = tree_out.GetEntries()
    print n_total
    
    file_to_filter = ROOT.TFile(input_file2,'READ')
    tree_to_filter = file_to_filter.Get('tap')
    n_event_2 = tree_to_filter.GetEntries()
    n_overlapped = 0
    for i in range(0,tree_to_filter.GetEntries()):
        if i%10000 == 0:
            print "%d / %d processed"%(i, tree_to_filter.GetEntries())
        tree_to_filter.GetEntry(i)
        run=str(tree_to_filter.ev_run_out)
        luminosityBlock=str(tree_to_filter.ev_luminosityBlock_out)
        event=str(tree_to_filter.ev_event_out)
        tmp_str = "%s %s %s"%(run,luminosityBlock, event)
        if event == "1965787424":
            print "KKKKKKKKKKKKKKKKKKK"
            target = True
        if tmp_str in event_list:
            n_overlapped += 1
            if target:print "continue"
            continue
        else:
            tree_out.Fill()
            print tree_out.GetEntries()
            event_list.append(tmp_str)
            n_total += 1
            if target: 
                print "saved"
                target = False
                #break

    print "%d events in file: %s"%(n_event_1, input_file1)
    print "%d events in file: %s, %d overlapped"%(n_event_2, input_file2, n_overlapped)
    print "%d events total in output file: %s"%(n_total, output_file)
    tree_out.GetCurrentFile().Write()
    tree_out.GetCurrentFile().Close()
    file_out.Close()


#event_filter(input_file1, input_file2, output_file)
event_filter2(input_file1, input_file2, output_file)
