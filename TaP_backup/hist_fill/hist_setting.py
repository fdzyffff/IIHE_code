import ROOT
import os
from input_hist import *


def Init_hist(sample_dic, hist_dic, global_hist_dic):
	for path in hist_dic:
		for cut in hist_dic[path]["cut_dic"]:
			for sample in sample_dic:
				sample_dic[sample]["hist"][path+cut] = {}
			global_hist_dic[path+cut]={}

	for path in hist_dic:
		for cut in hist_dic[path]["cut_dic"]:
			if hist_dic[path]["use_array"]:
				for sample in sample_dic:
					sample_dic[sample]["hist"][path+cut]["h_numerator"] = ROOT.TH1D("%s_%s_n"%(sample,hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
					sample_dic[sample]["hist"][path+cut]["h_denominator"] = ROOT.TH1D("%s_%s_d"%(sample,hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
				global_hist_dic[path+cut]["h_numerator"] = ROOT.TH1D("all_%s_n"%(hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
				global_hist_dic[path+cut]["h_denominator"] = ROOT.TH1D("all_%s_d"%(hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][1])
			else:
				for sample in sample_dic:
					sample_dic[sample]["hist"][path+cut]["h_numerator"] = ROOT.TH1D("%s_%s_n"%(sample,hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])
					sample_dic[sample]["hist"][path+cut]["h_denominator"] = ROOT.TH1D("%s_%s_d"%(sample,hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])
				global_hist_dic[path+cut]["h_numerator"] = ROOT.TH1D("all_%s_n"%(hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])
				global_hist_dic[path+cut]["h_denominator"] = ROOT.TH1D("all_%s_d"%(hist_dic[path]["hist_name"]+cut), "", hist_dic[path]["hist_para"][0], hist_dic[path]["hist_para"][2], hist_dic[path]["hist_para"][3])
	
def Set_hist(sample_dic, hist_dic, plot_dic, global_hist_dic):
	for path in hist_dic:
		for cut in hist_dic[path]["cut_dic"]:
			for sample in sample_dic:
				sample_dic[sample]["hist"][path+cut]["h_numerator"].Sumw2()
				sample_dic[sample]["hist"][path+cut]["h_denominator"].Sumw2()
			global_hist_dic[path+cut]["h_numerator"].Sumw2()
			global_hist_dic[path+cut]["h_denominator"].Sumw2()


def Store_hist_together(hist_dic, global_cut):
	try:os.mkdir(global_cut)
	except:pass
	root_file = "%s/%s_hist.root"%(global_cut,global_cut)
	f1 = ROOT.TFile(root_file,"RECREATE")
	for path in hist_dic:
		for cut in hist_dic[path]["cut_dic"]:
			for hist in hist_list:
				if "_out" in global_hist_dic[path+cut][hist].GetName()[-4:]:
					global_hist_dic[path+cut][hist].SetName(global_hist_dic[path+cut][hist].GetName()[:-4])
				tmp_name = global_hist_dic[path+cut][hist].GetName()
				global_hist_dic[path+cut][hist].SetName("%s_out"%(global_hist_dic[path+cut][hist].GetName()))
				global_hist_dic[path+cut][hist].Write()
				global_hist_dic[path+cut][hist].SetName(tmp_name)
	f1.Close()

def Store_hist(sample_dic, hist_dic, global_cut):
	try:os.mkdir(global_cut)
	except:pass
	for sample in sample_dic:
		root_file = "%s/%s_hist_%s.root"%(global_cut,global_cut,sample)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for path in hist_dic:
			for cut in hist_dic[path]["cut_dic"]:
				for hist in hist_list:
					if "_out" in sample_dic[sample]["hist"][path+cut][hist].GetName()[-4:]:
						sample_dic[sample]["hist"][path+cut][hist].SetName(sample_dic[sample]["hist"][path+cut][hist].GetName()[:-4])
					tmp_name = sample_dic[sample]["hist"][path+cut][hist].GetName()
					sample_dic[sample]["hist"][path+cut][hist].SetName("%s_out"%(sample_dic[sample]["hist"][path+cut][hist].GetName()))
					sample_dic[sample]["hist"][path+cut][hist].Write()
					sample_dic[sample]["hist"][path+cut][hist].SetName(tmp_name)
		f1.Close()
