import ROOT
import os
from optparse import OptionParser

def event_filter(input_file1, output_file, reverse=False):
#If reverse, will fill events not in list, if not reverse, will fill events in list
    file_in = ROOT.TFile(input_file1,'READ')
    tree_in = file_in.Get('tap')
    n_event_1 = tree_in.GetEntries()

    file_out = ROOT.TFile(output_file,"RECREATE")
    tree_out = tree_in.CloneTree(0)

    n_fired = 0
    n_pickup = 0
    for i in range(0,tree_in.GetEntries()):
        if i%10000 == 0:
            print "%d / %d processed"%(i, tree_in.GetEntries())
        tree_in.GetEntry(i)
        if (tree_in.Muon50_trig_fire or tree_in.OldMu100_trig_fire) and (not tree_in.Ele115_trig_fire) and (not tree_in.Photon175_trig_fire):
            n_fired += 1
            if not reverse:
                tree_out.Fill()
                n_pickup += 1
        else:
            if reverse:
                tree_out.Fill()
                n_pickup += 1

    tree_out.GetCurrentFile().Write()

    print "%d events in file: %s, %d fired, %d picked up"%(n_event_1, input_file1, n_fired, n_pickup)

parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="fke_data_2017_SingleMuon.root",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="fke_data_2017_SingleMuon_co.root",type="str")
(options,args)=parser.parse_args()


print "### input file : %s"%(options.root_dir)
print "### output file : %s"%(options.output_name)
event_filter(options.root_dir,options.output_name)



