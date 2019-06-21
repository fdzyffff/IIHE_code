import ROOT
import os
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-r","--input_dir",dest="input_dir",default="null",type="str")

(options,args)=parser.parse_args()


def main():
    f_out = ROOT.TFile("hist_ttbar.root","RECREATE")
    input_root_list = []
    for root_file in os.listdir(options.input_dir):
        if not ".root" in root_file:continue
        tmp_root_file = ROOT.TFile(os.path.join(options.input_dir,root_file))
        for path in hist_dic:
            tmp_h1 = tmp_root_file.Get("%s"%(hist_dic[path].name))
            #tmp_h1.Sumw2()
            hist_dic[path].h1.Add(hist_dic[path].h1, tmp_h1, 1, 1)
        tmp_root_file.Close()
    f_out.cd()
    for path in hist_dic:
        hist_dic[path].h1.Write()
    f_out.Close()

main()
