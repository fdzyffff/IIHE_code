import sys
try:
    sys.path.append("C:/root_v5.34.30/bin")
except:
    pass
import ROOT
import time
from math import *
from array import array
import os

from optparse import OptionParser

ROOT.TH1.AddDirectory(ROOT.kFALSE)
#ROOT.gROOT.SetBatch(ROOT.kTRUE)

def get_part_plot(input_list):
	Flag_first = True
	h1 = ROOT.TH1F()
	for part in input_list:
		file_tmp = ROOT.TFile(part[0],"read")
		if Flag_first:
			h1 = file_tmp.Get(part[1])
			h1.Scale(part[2])
			Flag_first = False
		else:
			tmp_h = file_tmp.Get(part[1])
			tmp_h.Scale(part[2])
			h1.Add(h1,tmp_h,1,1)
	return h1

def get_plot(input_0b_data, input_0b_before, input_0b_after, input_1b_before, input_1b_after, out_dir, label):
	h_0b_data = get_part_plot(input_0b_data)
	#h_0b_before = get_part_plot(input_0b_before)
	h_0b_after = get_part_plot(input_0b_after)
	h_1b_before = get_part_plot(input_1b_before)
	h_1b_after = get_part_plot(input_1b_after)

	#Normalize hists:
	h_0b_data.Scale(1.0/h_0b_data.Integral())
	#h_0b_before.Scale(1.0/h_0b_before.Integral())
	h_0b_after.Scale(1.0/h_0b_after.Integral())
	h_1b_before.Scale(1.0/h_1b_before.Integral())
	h_1b_after.Scale(1.0/h_1b_after.Integral())

	c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 50,50,865,780 )
	h_0b_data.SetMarkerColor(1)
	h_0b_data.Draw("PE")
	h_0b_data.SetStats(0)
	h_0b_data.SetMarkerColor(2)
	h_0b_data.SetLineColor(2)
	h_0b_data.SetMarkerStyle(20)

	h_0b_after.Draw("same")
	h_0b_after.SetMarkerStyle(24)
	h_0b_after.SetMarkerColor(6)
	h_0b_after.SetLineColor(6)

	h_1b_before.Draw("hist:same")
	h_1b_before.SetLineColor(1)

	h_1b_after.Draw("same")
	h_1b_after.SetMarkerStyle(22)
	h_1b_after.SetMarkerColor(4)
	h_1b_after.SetLineColor(4)

	legend2=ROOT.TLegend(0.7,0.7,0.9,0.8)
	legend2.AddEntry(h_0b_data,"data driven DY" ,"lp")
	legend2.AddEntry(h_0b_after,"0b DY after Nvtx reweight" ,"lp")
	legend2.AddEntry(h_1b_before,"DY before Nvtx reweight" ,"lp")
	legend2.AddEntry(h_1b_after,"DY after Nvtx reweight" ,"lp")
	legend2.Draw()

	c1.Update()
	time.sleep(100)

plot_dic = {
"step1":[
[["_EE_80_0b/_EE_80_0b_hist_data.root","data_MET_T1Txy_Pt_out",1.0]],
[["_EE_80_0b/_EE_80_0b_hist_DYToLL_10to50.root","DYToLL_10to50_MET_T1Txy_Pt_out",18610./29168419.],["_EE_80_0b/_EE_80_0b_hist_DYToLL_50.root","DYToLL_50_MET_T1Txy_Pt_out",5765.4/81589928]],
[["_EE_80_0b/_EE_80_0b_hist_DYToLL_10to50.root","DYToLL_10to50_MET_T1Txy_Pt_out",18610./29168419.],["_EE_80_0b/_EE_80_0b_hist_DYToLL_50.root","DYToLL_50_MET_T1Txy_Pt_out",5765.4/81589928]],
[["_noNvtx_EE_80_1b/_noNvtx_EE_80_1b_hist_DYToLL_10to50.root","DYToLL_10to50_MET_T1Txy_Pt_out",18610./29168419.],["_noNvtx_EE_80_1b/_noNvtx_EE_80_1b_hist_DYToLL_50.root","DYToLL_50_MET_T1Txy_Pt_out",5765.4/81589928]],
[["_EE_80_1b/_EE_80_1b_hist_DYToLL_10to50.root","DYToLL_10to50_MET_T1Txy_Pt_out",18610./29168419.],["_EE_80_1b/_EE_80_1b_hist_DYToLL_50.root","DYToLL_50_MET_T1Txy_Pt_out",5765.4/81589928]],
"",""
],
}

for plot in plot_dic:
	get_plot(plot_dic[plot][0],plot_dic[plot][1],plot_dic[plot][2],plot_dic[plot][3],plot_dic[plot][4],plot_dic[plot][5],plot_dic[plot][6])