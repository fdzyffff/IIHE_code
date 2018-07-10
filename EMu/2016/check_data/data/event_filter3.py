import os
import ROOT

input_file ='data_2016_SingleMuon_SinglePhoton.root'
output_file ='data_2016_SingleMuon_SinglePhoton2.root'

def event_filter3(input_file, output_file):
    file_in = ROOT.TFile(input_file,'READ')
    tree_in = file_in.Get('tap')
    n_event_1 = tree_in.GetEntries()

    file_out = ROOT.TFile(output_file,"RECREATE")
    tree_out = tree_in.CloneTree(0)
    tree_out.GetCurrentFile().Write()
    n_total = tree_out.GetEntries()
    
    event_list = []
    for i in range(0,tree_in.GetEntries()):
        if i%1000 == 0:
            print "%d / %d processed"%(i, tree_in.GetEntries())
        tree_in.GetEntry(i)
        run=tree_in.ev_run_out
        luminosityBlock=tree_in.ev_luminosityBlock_out
        event=tree_in.ev_event_out & 0xffffffff
        n_event = tree_in.Draw("","ev_run_out == %s && ev_event_out == %s"%(run,event))
        if n_event == 1:
            tree_out.Fill()
            n_total += 1
        elif n_event > 1 and tree_out.Draw("","ev_run_out == %s && ev_event_out == %s"%(run,event)) == 0:
            tree_out.Fill()
            n_total += 1
        else:
            continue

    print "%d events in file: %s"%(n_event_1, input_file)
    print "%d events total in output file: %s"%(n_total, output_file)
    tree_out.GetCurrentFile().Write()
    tree_out.GetCurrentFile().Close()
    file_out.Close()
          
event_filter3(input_file, output_file)
