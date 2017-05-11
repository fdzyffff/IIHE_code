import ROOT
import os
from input_card import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-r","--input_dir",dest="input_dir",default="null",type="str")

(options,args)=parser.parse_args()

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def Init_hist(input_dic, value_dic_pvn):
    for path in value_dic_pvn:
        if value_dic_pvn[path]["use_array"]:
            for sample in input_dic:
                input_dic[sample]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic_pvn[path]["hist_name"]), "", value_dic_pvn[path]["hist_para"][0], value_dic_pvn[path]["hist_para"][1])
        else:
            for sample in input_dic:
                input_dic[sample]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic_pvn[path]["hist_name"]), "", value_dic_pvn[path]["hist_para"][0], value_dic_pvn[path]["hist_para"][2], value_dic_pvn[path]["hist_para"][3])
        for sample in input_dic:
            input_dic[sample]["hist"][path].Sumw2()

def Store_hist(input_dic, value_dic_pvn, cut):
	try:os.mkdir(cut)
	except:pass
	for sample in input_dic:
		root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for path in value_dic_pvn:
				if "_out" in input_dic[sample]["hist"][path].GetName()[-4:]:
					input_dic[sample]["hist"][path].SetName(input_dic[sample]["hist"][path].GetName()[:-4])
				tmp_name = input_dic[sample]["hist"][path].GetName()
				input_dic[sample]["hist"][path].SetName("%s_out"%(input_dic[sample]["hist"][path].GetName()))
				input_dic[sample]["hist"][path].Write()
				input_dic[sample]["hist"][path].SetName(tmp_name)
		f1.Close()

def merge_plot(input_root_list,sample):
    for root_file in input_root_list:
        tmp_root_file = ROOT.TFile(root_file)
        for path in value_dic_pvn:
            tmp_h1 = tmp_root_file.Get("%s_%s_out"%(sample,value_dic_pvn[path]["hist_name"]))
            #tmp_h1.Sumw2()
            input_dic[sample]["hist"][path].Add(input_dic[sample]["hist"][path],tmp_h1,1,1)
        tmp_root_file.Close()

def main():
    if options.input_dir == "null":print "Error, need input dir"
    else:
        Init_hist(input_dic, value_dic_pvn)
        for sample in input_dic:
            input_root_list = []
            for root_file in os.listdir(os.path.join(options.input_dir,"split",sample)):
                if ".root" in root_file:
                    input_root_list.append("%s/%s"%(os.path.join(options.input_dir,"split",sample),root_file))
            merge_plot(input_root_list,sample)
        Store_hist(input_dic, value_dic_pvn, options.input_dir.replace("/",""))

value_dic_pvn={
"pv_n":{
                "Data_value_dic_pvn":{"pv_n":True},
                "MC_value_dic_pvn":{"pv_n":True},
                "hist_name":"N_vtx_PU",
                "hist_title":"Number of vertex (with PU reweight)",
                "use_array":False,
                "PU_reweight":True,
                "hist_para":[50,'null',0,50],
                "y_axis":["null","null"],
                "x_label":['N_{vtx}',0.1],
                "y_label":['Event ',0.05],
                "x_log":False,
                "y_log":False,
                "lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
}
main()
