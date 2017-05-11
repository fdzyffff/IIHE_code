import ROOT
import os
from optparse import OptionParser

def event_filter(input_file1, output_file, ev_list,reverse=False):
#If reverse, will fill events not in list, if not reverse, will fill events in list
    file_in = ROOT.TFile(input_file1,'READ')
    tree_in = file_in.Get('tap')
    n_event_1 = tree_in.GetEntries()

    tree_tmp = tree_in.CloneTree(0)

    n_overlapped = 0
    n_pickup = 0
    for i in range(0,tree_in.GetEntries()):
        if i%10000 == 0:
            print "%d / %d processed"%(i, tree_in.GetEntries())
        tree_in.GetEntry(i)
        event=str(tree_in.ev_event_out & 0xffffffff)
        run=str(tree_in.ev_run_out & 0xffffffff)
        lumi=str(tree_in.ev_luminosityBlock_out & 0xffffffff)
        tmp_str = "%s %s %s"%(run,lumi,event)
        #print tmp_str
        if tmp_str in ev_list:
            n_overlapped += 1
            if not reverse:
                tree_tmp.Fill()
                n_pickup += 1
        else:
            if reverse:
                tree_tmp.Fill()
                n_pickup += 1
    if tree_tmp.GetEntries() > 0:
        file_out = ROOT.TFile(output_file,"RECREATE")
        tree_out = tree_tmp.CloneTree(-1)
        tree_out.GetCurrentFile().Write()

    print "%d events in file: %s, %d overlapped, %d picked up"%(n_event_1, input_file1, n_overlapped, n_pickup)

def read_event_list(file_name):
    tmp_list = []
    for line in open(file_name):
        tmp_text = line.replace("\n","")
        #print tmp_text
        tmp_list.append(tmp_text)
        #print tmp_text
    print tmp_list[0]
    return tmp_list
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
(options,args)=parser.parse_args()


print "### input file : %s"%(options.root_dir)
print "### output file : %s"%(options.output_name)
event_filter(options.root_dir,options.output_name, read_event_list("data_DoubleEG.list"),True)
#event_filter(options.root_dir,options.output_name, read_event_list("tmp.list"),True)



