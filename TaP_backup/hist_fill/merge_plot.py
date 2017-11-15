import ROOT
import os
from input_sample import *
from input_hist import *
from hist_setting import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-r","--input_dir",dest="input_dir",default="null",type="str")

(options,args)=parser.parse_args()

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def merge_plot(input_root_list,sample):
    for root_file in input_root_list:
        tmp_root_file = ROOT.TFile(root_file)
        for path in hist_dic:
            for cut in hist_dic[path]["cut_dic"]:
                tmp_h1 = tmp_root_file.Get("%s_%s_n_out"%(sample,hist_dic[path]["hist_name"]+cut))
                tmp_h2 = tmp_root_file.Get("%s_%s_d_out"%(sample,hist_dic[path]["hist_name"]+cut))
                #tmp_h1.Sumw2()
                sample_dic[sample]["hist"][path+cut]["h_numerator"].Add(sample_dic[sample]["hist"][path+cut]["h_numerator"],tmp_h1,1,1)
                sample_dic[sample]["hist"][path+cut]["h_denominator"].Add(sample_dic[sample]["hist"][path+cut]["h_denominator"],tmp_h2,1,1)
        tmp_root_file.Close()

def main():
    if options.input_dir == "null":print "Error, need input dir"
    else:
        Init_hist(sample_dic, hist_dic, global_hist_dic)
        for sample in sample_dic:
            input_root_list = []
            for root_file in os.listdir(os.path.join(options.input_dir,"split",sample)):
                if ".root" in root_file:
                    input_root_list.append("%s/%s"%(os.path.join(options.input_dir,"split",sample),root_file))
            merge_plot(input_root_list,sample)
        Store_hist(sample_dic, hist_dic, options.input_dir.replace("/",""))

main()
