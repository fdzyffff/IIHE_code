import ROOT
import os
from input_sample import *
from input_hist import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-r","--input_dir",dest="input_dir",default="null",type="str")

(options,args)=parser.parse_args()

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def Init_hist(sample_dic, hist_dic):
	for path in hist_dic:
		for sample in sample_dic:
			sample_dic[sample]["hist"][path] = {}
	for path in hist_dic:
		if hist_dic[path]["use_array"]:
			for sample in sample_dic:
				sample_dic[sample]["hist"][path]["h_numerator"] = ROOT.TH1D("%s_%s_n"%(sample,hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
				sample_dic[sample]["hist"][path]["h_denominator"] = ROOT.TH1D("%s_%s_d"%(sample,hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
			hist_dic[path]["hist"]["h_numerator"] = ROOT.TH1D("all_%s_n"%(hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
			hist_dic[path]["hist"]["h_denominator"] = ROOT.TH1D("all_%s_d"%(hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
		else:
			for sample in sample_dic:
				sample_dic[sample]["hist"][path]["h_numerator"] = ROOT.TH1D("%s_%s_n"%(sample,hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])
				sample_dic[sample]["hist"][path]["h_denominator"] = ROOT.TH1D("%s_%s_d"%(sample,hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])
			hist_dic[path]["hist"]["h_numerator"] = ROOT.TH1D("all_%s_n"%(hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])
			hist_dic[path]["hist"]["h_denominator"] = ROOT.TH1D("all_%s_d"%(hist_dic[path]["hist_name"]), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])

def Store_hist(sample_dic, hist_dic, cut):
	try:os.mkdir(cut)
	except:pass
	for sample in sample_dic:
		root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for path in hist_dic:
			for hist in hist_list:
				if "_out" in sample_dic[sample]["hist"][path][hist].GetName()[-4:]:
					sample_dic[sample]["hist"][path][hist].SetName(sample_dic[sample]["hist"][path][hist].GetName()[:-4])
				tmp_name = sample_dic[sample]["hist"][path][hist].GetName()
				sample_dic[sample]["hist"][path][hist].SetName("%s_out"%(sample_dic[sample]["hist"][path][hist].GetName()))
				sample_dic[sample]["hist"][path][hist].Write()
				sample_dic[sample]["hist"][path][hist].SetName(tmp_name)
		f1.Close()

def merge_plot(input_root_list,sample):
    for root_file in input_root_list:
        tmp_root_file = ROOT.TFile(root_file)
        for path in hist_dic:
            tmp_h1 = tmp_root_file.Get("%s_%s_n_out"%(sample,hist_dic[path]["hist_name"]))
            tmp_h2 = tmp_root_file.Get("%s_%s_d_out"%(sample,hist_dic[path]["hist_name"]))
            #tmp_h1.Sumw2()
            sample_dic[sample]["hist"][path]["h_numerator"].Add(sample_dic[sample]["hist"][path]["h_numerator"],tmp_h1,1,1)
            sample_dic[sample]["hist"][path]["h_denominator"].Add(sample_dic[sample]["hist"][path]["h_denominator"],tmp_h2,1,1)
        tmp_root_file.Close()

def main():
    if options.input_dir == "null":print "Error, need input dir"
    else:
        Init_hist(sample_dic, hist_dic)
        for sample in sample_dic:
            input_root_list = []
            for root_file in os.listdir(os.path.join(options.input_dir,"split",sample)):
                if ".root" in root_file:
                    input_root_list.append("%s/%s"%(os.path.join(options.input_dir,"split",sample),root_file))
            merge_plot(input_root_list,sample)
        Store_hist(sample_dic, hist_dic, options.input_dir.replace("/",""))

main()
