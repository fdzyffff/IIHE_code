import os
import ROOT

input_file ='fk_data_2016_SingleMuon_SinglePhoton.root'
output_file ='fk_data_2016_SingleMuon_SinglePhoton2.root'

def event_filter2(input_file, output_file):
    file_in = ROOT.TFile(input_file,'READ')
    tree_in = file_in.Get('tap')
    n_event_1 = tree_in.GetEntries()

    file_out = ROOT.TFile(output_file,"RECREATE")
    tree_out = tree_in.CloneTree(0)
    tree_out.GetCurrentFile().Write()
    n_total = tree_out.GetEntries()
    
    event_list = []
    for i in range(0,tree_in.GetEntries()):
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

    print "%d events in file: %s"%(n_event_1, input_file)
    print "%d events total in output file: %s"%(n_total, output_file)
    tree_out.GetCurrentFile().Write()
    tree_out.GetCurrentFile().Close()
    file_out.Close()
          
event_filter2(input_file, output_file)
