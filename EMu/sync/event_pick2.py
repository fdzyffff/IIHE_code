import ROOT
import os
from optparse import OptionParser

def event_filter(input_file1, output_file, ev_list):
    file_in = ROOT.TFile(input_file1,'READ')
    tree_in = file_in.Get('IIHEAnalysis')
    n_event_1 = tree_in.GetEntries()

    tree_tmp = tree_in.CloneTree(0)

    n_overlapped = 0
    for i in range(0,tree_in.GetEntries()):
        if i%10000 == 0:
            print "%d / %d processed"%(i, tree_in.GetEntries())
        tree_in.GetEntry(i)
        event=str(tree_in.ev_event & 0xffffffff)
        run=str(tree_in.ev_run & 0xffffffff)
        lumi=str(tree_in.ev_luminosityBlock & 0xffffffff)
        tmp_str = "%s %s %s"%(run,lumi,event)
        #print tmp_str
        if tmp_str in ev_list:
            tree_tmp.Fill()
            n_overlapped += 1
    if tree_tmp.GetEntries() > 0:
        file_out = ROOT.TFile(output_file,"RECREATE")
        tree_out = tree_tmp.CloneTree(-1)
        tree_out.GetCurrentFile().Write()

    print "%d events in file: %s, %d pick up"%(n_event_1, input_file1, n_overlapped)

def read_event_list(file_name):
    tmp_list = []
    for line in open(file_name):
        tmp_text = line.replace("\n","")[:-1]
        #print tmp_text
        tmp_list.append(tmp_text)
        #print tmp_text
    return tmp_list
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
(options,args)=parser.parse_args()


#event_filter(options.root_dir, options.output_name, read_event_list("only_soren_result.list"))
for tmp_file in os.listdir(options.root_dir):
    out_name = "%s_%s"%(options.output_name,tmp_file)
    event_filter(os.path.join(options.root_dir,tmp_file),out_name, read_event_list("only_soren_2017-04-28_result.list"))
print '***finish***'



