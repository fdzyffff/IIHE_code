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
from input_cut import *
from input_sample import *
from input_plot import *

from optparse import OptionParser

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")

(options,args)=parser.parse_args()


ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def write_json(dic_in,file_name):
    f1 = open(file_name,"w")
    f1.write(str(dic_in))

def SFtoJson(h1):
    SF_dic = {}
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        eta_u = h1.GetXaxis().GetBinUpEdge(i)
        eta_l = h1.GetXaxis().GetBinLowEdge(i)
        SF_dic[(eta_l,eta_u)] = h1.GetBinContent(i)
    return SF_dic

def get_graph_ratio(g1, g2):
	g_ratio=g1.Clone(g1.GetName())
	for ibin in range(0, g_ratio.GetN()):
		ratio=999
		err_down=0
		err_up=0
		if float(g1.GetY()[ibin]) !=0:
			if float(g2.GetY()[ibin]) !=0:
				#ratio=float((g1.GetY()[ibin]-g2.GetY()[ibin])/g2.GetY()[ibin])
				ratio=float((g1.GetY()[ibin])/g2.GetY()[ibin])
				err_down=float(g1.GetErrorYlow(ibin)/g2.GetY()[ibin])
				err_up  =float(g1.GetErrorYhigh(ibin)/g2.GetY()[ibin])
		g_ratio.SetPoint(ibin,g_ratio.GetX()[ibin],ratio)
		g_ratio.SetPointEYlow(ibin,err_down)
		g_ratio.SetPointEYhigh(ibin,err_up)
	return g_ratio

def remove_graph_zero(gr_in):
	for i in range(gr_in.GetN()-1, 0-1,-1):
		N = gr_in.GetY()[i]
		#print "%d : %f"%(i,N)
		if N==0:
			gr_in.RemovePoint(i)

def histTograph(h_data, isWeight=False):  
	h_data_bin_value={}
	h_data_bin_width={}
	for bin in range(1, h_data.GetNbinsX()+1):
		h_data_bin_value[bin]=h_data.GetBinContent(bin)*h_data.GetBinWidth(bin) 
		h_data_bin_width[bin]=h_data.GetBinWidth(bin) 
	g_data = ROOT.TGraphAsymmErrors(h_data)
	g_data.SetMarkerSize(0.5)
	g_data.SetMarkerStyle (20)
	alpha = float(1 - 0.6827)
	for i in range(0,g_data.GetN()): 
		N = g_data.GetY()[i]
		error_up=0
		error_low=0
		if isWeight:
			N = h_data_bin_value[i+1]
		L = 0
		if N==0:
			L=0
		else: 
			L= float( ROOT.Math.gamma_quantile(alpha/2,N,1.) )
		U =float( ROOT.Math.gamma_quantile_c(alpha/2,N+1,1) )
		error_low=N-L
		error_up=U-N
		if isWeight:
			error_low= (N-L)/h_data_bin_width[i+1]
			error_up=(U-N)/h_data_bin_width[i+1]
		if N==0:
			error_up=0
			error_low=0
		g_data.SetPointEYlow (i, error_low)
		g_data.SetPointEYhigh(i, error_up)
	return g_data

def Graph_Xerror0(graph_in):
	for i in range(0,graph_in.GetN()):
		graph_in.SetPointEXlow (i, 0)
		graph_in.SetPointEXhigh(i, 0)

def my_setzero(h2):
	for i in range(1,h2.GetNbinsX()+1):
		h2.SetBinContent(i,0.0)

def getYmax(h1):
	tmp_max = 0
	for i in range(1,h1.GetNbinsX()+1):
		if tmp_max < h1.GetBinContent(i):
			tmp_max = h1.GetBinContent(i)
	return tmp_max*1.5

def my_abs(h2):
	for i in range(1,h2.GetNbinsX()+1):
		if h2.GetBinContent(i)<0:
			h2.SetBinContent(i,0.0)


def Get_lep_SF(lep_pt,lep_eta,lep_isE,lep_isMu):
	lep_SF = 0.0
	if lep_isE:
		lep_SF = Get_ele_SF(lep_pt,lep_eta)
	elif lep_isMu:
		lep_SF = Get_mu_SF(lep_pt,lep_eta)
        if lep_SF == 0.0:print 1/0
	return lep_SF

#dic_Muon_Tracking_eta
#dic_Muon_ID_pt_Abseta
#dic_Muon_ISO_pt_Abseta
#dic_Ele_Tracking_pt_eta
#dic_Ele_ID_ISO_pt_eta

def Get_ele_SF(lep_pt,lep_eta):
	ele_SF = 1.0
	ele_SF *= Get_SF_2D(dic_Ele_Tracking_pt_eta, lep_pt, lep_eta)
	ele_SF *= Get_SF_2D(dic_Ele_ID_ISO_pt_eta, lep_pt, lep_eta)
	return ele_SF

def Get_mu_SF(lep_pt,lep_eta):
	mu_SF = 1.0
	mu_SF *= Get_SF_1D(dic_Muon_Tracking_eta, lep_eta)
	mu_SF *= Get_SF_2D(dic_Muon_ID_pt_Abseta, lep_pt, fabs(lep_eta))
	mu_SF *= Get_SF_2D(dic_Muon_ISO_pt_Abseta, lep_pt, fabs(lep_eta))
	return mu_SF

def Get_SF_2D(dic_in, pt_in, eta_in):
	pt = pt_in
	eta = eta_in
	eff = 1.0
	for (pt_l, pt_u) in dic_in:
		if pt>pt_l and pt<=pt_u:
			for (eta_l, eta_u) in dic_in[(pt_l,pt_u)]:
				if eta>=eta_l and eta<eta_u:
					eff = dic_in[(pt_l,pt_u)][(eta_l,eta_u)]
					return eff
	return eff

def Get_SF_1D(dic_in, value_in):
	value = value_in
	eff = 1.0
	for (value_l, value_u) in dic_in:
		if value>=value_l and value<value_u:
			eff = dic_in[(value_l,value_u)]
			return eff
	return eff

def pm(x):
	if x>0:
		return 1
	elif x<0:
		return -1
	else:
		return 0

def Fill_hist(sample_dic, value_dic, cut):
	root_file = sample_dic["input_file"]

	f1 = ROOT.TFile(root_file,"read")
	t1 = f1.Get("tap")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Fill hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	n_process = 0
	if isSplit_mode:
		if (options.n_range_l<0):options.n_range_l=1
		if (options.n_range_h<0):options.n_range_h=t1.GetEntries()
		print "### using split mode, get event from %d to %d"%(options.n_range_l,options.n_range_h)
	for event in t1:
		n_process += 1
		if(n_process%50000==0):print n_process,'processed\n'
		if isSplit_mode:
			if (options.n_range_l > n_process):
				continue
			elif (options.n_range_h < n_process):
				break
		#if n_process >100:break
		exec 'passed = (%s)'%(cut_dic[cut])
		if not passed: continue 
		event_weight = 1.0
		leading_SF_weight = 1.0
		sub_leading_SF_weight = 1.0
		pu_weight = 1.0
		fake_weight = 1.0
		bin_weight = 1.0
		Nvtx_weight = 1.0
		top_weight = 1.0
		if not isData:
			leading_pt = getattr(event,"leading_pt")
			leading_eta = getattr(event,"leading_eta")
			leading_isE = getattr(event,"leading_isE")
			leading_isMu = getattr(event,"leading_isMu")
			leading_SF_weight = Get_lep_SF(leading_pt,leading_eta,leading_isE,leading_isMu)
			sub_leading_pt = getattr(event,"sub_leading_pt")
			sub_leading_eta = getattr(event,"sub_leading_eta")
			sub_leading_isE = getattr(event,"sub_leading_isE")
			sub_leading_isMu = getattr(event,"sub_leading_isMu")
			sub_leading_SF_weight = Get_lep_SF(sub_leading_pt,sub_leading_eta,sub_leading_isE,sub_leading_isMu)

			top_weight = getattr(event, "w_top")

			Nvtx_weight = Get_SF_1D(dic_Nvtx, getattr(event,"pv_n"))

			#print "%s : %s"%(getattr(event,"pv_n"), Nvtx_weight)
			#print "isData : %s , leading weight : %f , subleading weight : %f"%(isData, leading_SF_weight, sub_leading_SF_weight)
		if isFake:
			fake_weight = getattr(event,"fake_weight")

		for path in value_dic:
			tmp_value_dic = {}
			if isData:
				tmp_value_dic = value_dic[path]["Data_value_dic"]
			else:
				tmp_value_dic = value_dic[path]["MC_value_dic"]

			if not isData:
				if value_dic[path]["PU_reweight"]:
					pu_weight = getattr(event,"w_PU")
				else:
					pu_weight = pm(getattr(event,"w_PU"))

			event_weight = leading_SF_weight * sub_leading_SF_weight * pu_weight * fake_weight * top_weight * Nvtx_weight
			map_value(path, event, sample_dic["hist"][path],tmp_value_dic,event_weight)

def Get_hist_from_together(sample, sample_dic, value_dic, cut):
	root_file = "%s/%s_hist.root"%(cut,cut)
	f1 = ROOT.TFile(root_file,"read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
	f1.Close()

def Get_hist_from_tmp(sample, sample_dic, value_dic, cut):
	root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
	f1 = ROOT.TFile(root_file,"Read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
	f1.Close()

def Get_hist_from_split(sample, sample_dic, value_dic, cut):
	root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
	f1 = ROOT.TFile(root_file,"Read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
	f1.Close()

def Get_hist_from_file(sample,sample_dic,value_dic):
	root_file = sample_dic["input_file"]
	f1 = ROOT.TFile(root_file,"read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Read hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
	f1.Close()

def Get_hist(input_dic, value_dic, cut):
	for sample in input_dic:
		sample_dic = input_dic[sample]
		if isSplit_mode:
			if sample == options.sample_name:
				Fill_hist(sample_dic, value_dic, cut)
		elif (sample_dic["isFromRoot"] and sample_dic["isUpdate"]):
			Fill_hist(sample_dic, value_dic, cut)
		elif sample_dic["isFromRoot"]:
			Get_hist_from_tmp(sample, sample_dic, value_dic, cut)
		elif not sample_dic["isFromRoot"]:
			Get_hist_from_file(sample, sample_dic, value_dic)
		if "pv_n" in value_dic :
			sample_dic["N_total"] = sample_dic["hist"]["pv_n"].Integral()

def Store_hist_together(input_dic, value_dic, cut):
	try:os.mkdir(cut)
	except:pass
	root_file = "%s/%s_hist.root"%(cut,cut)
	f1 = ROOT.TFile(root_file,"RECREATE")
	for sample in input_dic:
		for path in value_dic:
				if "_out" in input_dic[sample]["hist"][path].GetName()[-4:]:
					input_dic[sample]["hist"][path].SetName(input_dic[sample]["hist"][path].GetName()[:-4])
				tmp_name = input_dic[sample]["hist"][path].GetName()
				input_dic[sample]["hist"][path].SetName("%s_out"%(input_dic[sample]["hist"][path].GetName()))
				input_dic[sample]["hist"][path].Write()
				input_dic[sample]["hist"][path].SetName(tmp_name)
	f1.Close()

def Store_hist(input_dic, value_dic, cut):
	try:os.mkdir(cut)
	except:pass
	for sample in input_dic:
		root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for path in value_dic:
				if "_out" in input_dic[sample]["hist"][path].GetName()[-4:]:
					input_dic[sample]["hist"][path].SetName(input_dic[sample]["hist"][path].GetName()[:-4])
				tmp_name = input_dic[sample]["hist"][path].GetName()
				input_dic[sample]["hist"][path].SetName("%s_out"%(input_dic[sample]["hist"][path].GetName()))
				input_dic[sample]["hist"][path].Write()
				input_dic[sample]["hist"][path].SetName(tmp_name)
		f1.Close()

def Store_hist_split(input_dic, value_dic, cut):
	try:os.mkdir(cut)
	except:pass
	try:os.mkdir("%s/split"%(cut))
	except:pass
	for sample in input_dic:
		if not sample == options.sample_name:continue
		try:os.mkdir("%s/split/%s"%(cut,sample))
		except:pass
		root_file = "%s/split/%s/%s_hist_%s_%s_%s.root"%(cut,sample,cut,sample,options.n_range_l,options.n_range_h)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for path in value_dic:
				if "_out" in input_dic[sample]["hist"][path].GetName()[-4:]:
					input_dic[sample]["hist"][path].SetName(input_dic[sample]["hist"][path].GetName()[:-4])
				tmp_name = input_dic[sample]["hist"][path].GetName()
				input_dic[sample]["hist"][path].SetName("%s_out"%(input_dic[sample]["hist"][path].GetName()))
				input_dic[sample]["hist"][path].Write()
				input_dic[sample]["hist"][path].SetName(tmp_name)
		f1.Close()


def Norm_hist(input_dic, value_dic):
	total_lumi = Get_total_lumi(input_dic)
	for sample in input_dic:
		if not input_dic[sample]["isData"]:
			input_dic[sample]["Norm_Factor"] = total_lumi * input_dic[sample]["Xsection"] / float(input_dic[sample]["Raw_total"])
			for path in value_dic:
				input_dic[sample]["hist"][path].Scale(input_dic[sample]["Norm_Factor"])
				input_dic[sample]["hist"][path].Scale(input_dic[sample]["weight_factor"])
		input_dic[sample]["N_norm"] = input_dic[sample]["N_total"] * input_dic[sample]["Norm_Factor"] * input_dic[sample]["weight_factor"]

def Print_table(input_dic):
	total_lumi = Get_total_lumi(input_dic)
	total_num = Get_total_num(input_dic)
	for sample in input_dic:
		if input_dic[sample]["isData"] and input_dic[sample]["useToNorm"]:
			print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic[sample]["Norm_Factor"], input_dic[sample]["N_norm"], 100.0*input_dic[sample]["N_norm"]/total_num)
	print "#"*50

	for sample in input_dic:
		if not (input_dic[sample]["isData"] and input_dic[sample]["useToNorm"]):
			print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic[sample]["Norm_Factor"], input_dic[sample]["N_norm"], 100.0*input_dic[sample]["N_norm"]/total_num)
	print "#"*50

def Get_part_hist(input_dic, value_dic, plot_dic):
	for path in value_dic:
		for part in plot_dic:
			for plot in plot_dic[part]:
				hist_list = plot_dic[part][plot]["data_list"]
				for sample in hist_list:
					plot_dic[part][plot]["hist"][path].Add(plot_dic[part][plot]["hist"][path], input_dic[sample]["hist"][path], 1, 1)
					plot_dic[part][plot]["N_total"]+=input_dic[sample]["N_norm"]
					if plot_dic[part][plot]["ABS"]: my_abs(plot_dic[part][plot]["hist"][path])


def Get_total_lumi(input_dic):
	total_lumi = 0.0
	for sample in input_dic:
		if input_dic[sample]["useToNorm"]:
			total_lumi += input_dic[sample]["lumi"]
	return total_lumi

def Get_total_num(input_dic):
	total_num = 0.0
	for sample in input_dic:
		if input_dic[sample]["useToNorm"]:
			total_num += input_dic[sample]["N_total"]
	return total_num

def main_plot_part(path, input_dic, cut, c1):
	pad1=ROOT.TPad("pad1", "pad1", 0, 0.315, 1, 0.99 , 0)#used for ratio, the hist plot
	pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for ratio, the ratio plot
	pad1.SetBottomMargin(0.0)
	pad1.SetLeftMargin(0.14)
	pad1.SetRightMargin(0.05)
	pad2.SetTopMargin(0.0)
	pad2.SetBottomMargin(0.4)
	pad2.SetLeftMargin(0.14)
	pad2.SetRightMargin(0.05)
	pad1.SetLogx(value_dic[path]["x_log"])
	pad1.SetLogy(value_dic[path]["y_log"])
	pad2.SetLogx(value_dic[path]["x_log"])
	if value_dic[path]["use_array"]:
		compare1_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
		compare2_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
	else:
		compare1_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])
		compare2_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])
	gr_1 = ROOT.TGraph()

	compare2_sum.SetStats(0)

	h_ratio = ROOT.TH1F()
	h_ratio.SetName("h_ratio_%s"%(value_dic[path]["hist_name"]))
	h_stack = ROOT.THStack()

	legend1=ROOT.TLegend(0.73,0.6,0.93,0.88)
	for plot in plot_dic["compare_1"]:
		compare1_sum.Add(compare1_sum, plot_dic["compare_1"][plot]["hist"][path], 1, 1)
		gr_1 = histTograph(compare1_sum, value_dic[path]["use_array"])
		Graph_Xerror0(gr_1)
		remove_graph_zero(gr_1)
		gr_1.GetXaxis().SetTitle(value_dic[path]["x_label"][0])
		gr_1.GetXaxis().SetTitleSize(0.1)
		gr_1.GetXaxis().SetTitleOffset(0.95)
		gr_1.GetXaxis().SetLabelSize(value_dic[path]["x_label"][1])
		gr_1.GetYaxis().SetTitle(value_dic[path]["y_label"][0])
		gr_1.GetYaxis().SetTitleSize(0.7)
		gr_1.SetMarkerStyle(20)
		gr_1.SetMarkerSize(1.0)
		gr_1.SetLineWidth(3)
		gr_1.SetLineColor(plot_dic["compare_1"][plot]["color"])
		legend1.AddEntry(gr_1, plot_dic["compare_1"][plot]["legend_title"],"PE")

		break
	#for p in sorted(plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = False):
	for i in range(len(plot_list)):
		plot = plot_list[len(plot_list)-1-i]
		#print plot_dic["compare_2"][plot]["N_total"]
		compare2_sum.Add(compare2_sum, plot_dic["compare_2"][plot]["hist"][path], 1, 1)
		h_stack.Add(plot_dic["compare_2"][plot]["hist"][path])
	#for p in sorted(plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = True):
	for plot in plot_list:
		legend1.AddEntry(plot_dic["compare_2"][plot]["hist"][path],plot_dic["compare_2"][plot]["legend_title"],"f")


	c1.cd()
	pad1.Draw()
	pad1.cd()

	if value_dic[path]["y_axis"][0]!= 'null':h_stack.SetMinimum(value_dic[path]["y_axis"][0])
	if value_dic[path]["y_axis"][1]!= 'null':h_stack.SetMaximum(value_dic[path]["y_axis"][1])
        else:h_stack.SetMaximum(getYmax(compare2_sum))
	#h_stack.SetMaximum(20000)
	h_stack.Draw("hist")
	h_stack.GetYaxis().SetTitle(value_dic[path]["y_label"][0])
	h_stack.GetYaxis().SetTitleOffset(0.88)
	h_stack.GetYaxis().SetTitleSize(0.08)
	h_stack.GetYaxis().SetLabelSize(0.04/0.7)
	h_stack.GetXaxis().SetLabelSize(0)
	compare2_sum.Draw("same:E2")
	compare2_sum.SetFillStyle(3015)
	compare2_sum.SetFillColorAlpha(ROOT.kOrange-3,1.0)
	legend1.AddEntry(compare2_sum,"Stat. uncertainty","f")
	#compare1_sum.Draw("same:PE2")
	gr_1.Draw("PE")
	legend1.SetBorderSize(0)
	legend1.Draw()

	tText_2 = ROOT.TPaveText(0.15,0.83,0.4,0.83,"NDC")
	tText_2.SetLineColor(10)
	tText_2.SetFillColor(10)
	tText_2.SetTextSize(0.052/0.7)
	tText_2.SetTextAlign(12)
	tText_2.AddText("CMS Preliminary")
	tText_2.SetShadowColor(10)
	tText_2.Draw("same")

	tText_3 = ROOT.TPaveText(0.62,0.95,0.9,0.95,"NDC")
	tText_3.SetLineColor(10)
	tText_3.SetFillColor(10)
	tText_3.SetTextSize(0.06/0.7)
	tText_3.SetTextAlign(12)
	tText_3.SetTextFont(42)
	tText_3.AddText("%0.1f fb^{-1} (13 TeV)"%(Get_total_lumi(input_dic)/1000.0))
	tText_3.SetShadowColor(10)
	tText_3.Draw("same")

	tText_4=ROOT.TPaveText(0.18,0.72, 0.35,0.7,"blNDC")
	tText_4.SetBorderSize(0)
	tText_4.SetFillStyle(0)
	tText_4.SetTextAlign(10)
	tText_4.SetTextColor(1)
	tText_4.SetTextFont(32)
	tText_4.SetTextSize(0.12)
	tText_4.AddText ('%s'%(cut_name[cut][0]))
	tText_4.Draw()

	tText_5=ROOT.TPaveText(0.16,0.65, 0.35,0.7,"blNDC")
	tText_5.SetBorderSize(0)
	tText_5.SetFillStyle(0)
	tText_5.SetTextAlign(10)
	tText_5.SetTextColor(1)
	tText_5.SetTextFont(40)
	tText_5.SetTextSize(0.03)
	tText_5.AddText ('%s'%(cut_name[cut][1]))
	tText_5.Draw()

	c1.Update()
	c1.cd()
	pad2.Draw()
	pad2.cd()

	h_ratio = compare2_sum.Clone(h_ratio.GetName())
	#h_ratio.Add(h_ratio, compare2_sum, 1, -1)
	h_ratio.SetMinimum(0.7)
	h_ratio.SetMaximum(1.3)

	h_ratio.SetStats(0)
	h_ratio.GetYaxis().SetTitle("Data/Pred.")
	h_ratio.GetXaxis().SetTitle(value_dic[path]["x_label"][0])
	h_ratio.GetXaxis().SetTitleSize(0.058/0.3)
	h_ratio.GetYaxis().SetTitleSize(0.045/0.3)
	h_ratio.GetXaxis().SetTitleFont(42)
	h_ratio.GetYaxis().SetTitleFont(42)
	h_ratio.GetXaxis().SetTickLength(0.05)
	h_ratio.GetYaxis().SetTickLength(0.05)
	h_ratio.GetXaxis().SetLabelSize(0.045/0.3)
	h_ratio.GetYaxis().SetLabelSize(0.04/0.3)
	h_ratio.GetXaxis().SetLabelOffset(0.02)
	h_ratio.GetYaxis().SetLabelOffset(0.01)
	h_ratio.GetYaxis().SetTitleOffset(0.41)
	h_ratio.GetXaxis().SetTitleOffset(0.23/0.25)
	h_ratio.GetYaxis().SetNdivisions(504)
	h_ratio.SetLineWidth(2)

	h_ratio.Divide(compare2_sum)
	h_ratio.SetMarkerSize(0.0)

	if path == "n_jet_bjet":
		for label in n_jet_bjet_dic:
			h_ratio.GetXaxis().SetBinLabel(n_jet_bjet_dic[label][1],n_jet_bjet_dic[label][2])
	h_ratio.Draw("E2")

	gr_ratio = get_graph_ratio(histTograph(compare1_sum, value_dic[path]["use_array"]), ROOT.TGraphAsymmErrors(compare2_sum))
	Graph_Xerror0(gr_ratio)
	legend2=ROOT.TLegend(0.2,0.7,0.5,0.9)
	#p0_ = h_ratio.GetFunction("pol0").GetParameter(0)
	h_ratio.SetLineColor(1)
	#h_ratio.GetFunction("pol0").SetLineColor(1)
	legend2.SetBorderSize(0)
	#legend2.AddEntry(h_ratio,"#Delta/MC = %0.2f"%p0_ ,"")
	#legend2.Draw()
	gr_ratio.SetMarkerStyle(20)
	gr_ratio.SetMarkerSize(1.0)
	gr_ratio.SetLineColor(1)
	gr_ratio.SetLineWidth(3)
	gr_ratio.Draw("PE")
    
	#c1.cd()
	c1.Update()
	c1.Print("%s/%s_hratio_%s.png"%(cut,cut[1:],path))
	c1.Print("%s/%s-hratio-%s.eps"%(cut,cut[1:],path))

def Get_Nvtx_json(path, input_dic, cut):
	if value_dic[path]["use_array"]:
		compare1_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
		compare2_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
	else:
		compare1_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])
		compare2_sum = ROOT.TH1F("sum_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])

	for plot in plot_dic["compare_1"]:
		compare1_sum.Add(compare1_sum, plot_dic["compare_1"][plot]["hist"][path], 1, 1)
		break
	for i in range(len(plot_list)):
		plot = plot_list[len(plot_list)-1-i]
		compare2_sum.Add(compare2_sum, plot_dic["compare_2"][plot]["hist"][path], 1, 1)

        h_data = ROOT.TH1F()
        h_data.SetName("h_data")
        h_data = compare1_sum.Clone(h_data.GetName())
        h_data.Scale(1.0/h_data.Integral())

        h_mc = ROOT.TH1F()
        h_mc.SetName("h_mc")
        h_mc = compare2_sum.Clone(h_mc.GetName())
        h_mc.Scale(1.0/h_mc.Integral())

        h_data.Divide(h_mc)
        SF_Nvtx_dic = SFtoJson(h_data)
        file_name = "%s/%s_hratio_%s.json"%(cut,cut,path)
        write_json(SF_Nvtx_dic,file_name)

def Init_hist(input_dic, value_dic, plot_dic):
	for path in value_dic:
		if value_dic[path]["use_array"]:
			for sample in input_dic:
				input_dic[sample]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
			for part in plot_dic:
				for plot in plot_dic[part]:
					plot_dic[part][plot]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
		else:
			for sample in input_dic:
				input_dic[sample]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])
			for part in plot_dic:
				for plot in plot_dic[part]:
					plot_dic[part][plot]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])

def Set_hist(input_dic, value_dic, plot_dic):
	for path in value_dic:
		for sample in input_dic:
			input_dic[sample]["hist"][path].Sumw2()
		for part in plot_dic:
			for plot in plot_dic[part]:
				plot_dic[part][plot]["hist"][path].Sumw2()
				plot_dic[part][plot]["hist"][path].SetFillColorAlpha(plot_dic[part][plot]["color"],0.9)
				plot_dic[part][plot]["hist"][path].SetLineColorAlpha(plot_dic[part][plot]["color"],0.9)

def print_error(error_range_dic, input_dic, value_dic, plot_dic):
	error_range_dic = {"0-500":[1,500,0,0], "500-1000":[2,500,0,0], "1000-1500":[3,500,0,0], "1500-2500":[4,1000,0,0]}
	path = "mass_err_stat"
	if value_dic[path]["use_array"]:
		h_err = ROOT.TH1F("h_err_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
	else:
		h_err = ROOT.TH1F("h_err_%s"%(value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])
	for p in sorted(plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = False):
		plot = p[0]
		h_err.Add(h_err, plot_dic["compare_2"][plot]["hist"][path], 1, 1)
	#for i in range(1,h_err.GetNbinsX()+1):
		#low_edge = h_err.GetBinLowEdge(i)
		#high_edge = low_edge+herr_GetBinWidth(i)
	for mass_range in error_range_dic:
		error_range_dic[mass_range][2] = h_err.GetBinContent(error_range_dic[mass_range][0])*error_range_dic[mass_range][1]
		error_range_dic[mass_range][3] = h_err.GetBinError(error_range_dic[mass_range][0])*error_range_dic[mass_range][1]
		print "%s : %f, %f"%(mass_range, error_range_dic[mass_range][2], error_range_dic[mass_range][3])

def print_sum(input_dic):
	print "%s print sum table %s"%("#"*20,"#"*20)
	for sample in input_dic:
		tmp_N = input_dic[sample]["hist"]["mass_err_stat"].GetBinContent(1)
		tmp_err = input_dic[sample]["hist"]["mass_err_stat"].GetBinError(1)
		print "%s,%s,%s"%(sample,tmp_N,tmp_err)
	print "%s finish %s"%("#"*20,"#"*20)


def main_plot(input_dic, value_dic, plot_dic, cut, isPlot = True):
	#Initialize hist
	Init_hist(input_dic, value_dic, plot_dic)
	#set up hist parameters
	Set_hist(input_dic, value_dic, plot_dic)
	#get hist from root file using Get() or Fill()
	Get_hist(input_dic, value_dic, cut)
	#Store hist to root file
	Store_hist(input_dic, value_dic, cut)
	#Normalize hist
	Norm_hist(input_dic, value_dic)
	#print contribution of each dataset
	Print_table(input_dic)
	#get hist for plot_dic
	Get_part_hist(input_dic, value_dic, plot_dic)
	
	#print_error(error_range_dic, input_dic, value_dic, plot_dic)
	print_sum(input_dic)

	#start plot
	c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 50,50,865,780 )
	c1.SetLeftMargin(0.5)

	for path in value_dic:
		if path == "mass_err_stat":continue
		main_plot_part(path, input_dic, cut, c1)
		if path == "pv_n":
			Get_Nvtx_json(path, input_dic, cut)
	c1.Close()

def main_plot_split(input_dic, value_dic, plot_dic, cut, isPlot = True):
	#Initialize hist
	Init_hist(input_dic, value_dic, plot_dic)
	#set up hist parameters
	Set_hist(input_dic, value_dic, plot_dic)
	#get hist from root file using Get() or Fill()
	Get_hist(input_dic, value_dic, cut)
	#Store hist to root file
	Store_hist_split(input_dic, value_dic, cut)


#main**************************************************************************

plot_dic={
"compare_1":{"data":{
					"data_list":["data"],
					"color":1,
					"legend_title":"Data (2016)",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}		
			},
"compare_2":{
			"_ttbar":{
					"data_list":["TTGJets","TTTo2L2Nu","TTWJetsToLNu","TTWJetsToQQ","TTZToLLNuNu_10","TTZToQQ"],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"_tW":{
					"data_list":["tW","tW_anti"],
					"color":ROOT.kOrange-3,
					"legend_title":"tW",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"_ZG_jets":{
					"data_list":["DYToLL_10to50","DYToLL_50"],
					"color":ROOT.kBlue-3,
					"legend_title":"Z/#gamma^{*}+jets",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"_others":{
					"data_list":["WGToLNuG","WJetsToLNu","WWTo2L2Nu","WZTo2L2Q","WZTo3LNu","ZZTo2L2Nu","ZZTo4L"],
					"color":ROOT.kGreen,
					"legend_title":"Other",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			},
}

plot_list = ["_tW","_ttbar","_ZG_jets","_others"]

error_range_dic = {"0-500":[1,500,0], "500-1000":[2,500,0], "1000-1500":[3,500,0], "1500-2000":[4,500,0]}

isSplit_mode = False
for cut in cut_dic:
	if options.sample_name == "null":
		isSplit_mode = False
		main_plot(input_dic, value_dic, plot_dic, cut)
	else:
		isSplit_mode = True
		print "Using split mode"
		if options.n_range_l<0 or options.n_range_h < 0:
			print "Error, in correct entries range! set to default value"
			main_plot_split(input_dic, value_dic, plot_dic, cut)
		else:
			main_plot_split(input_dic, value_dic, plot_dic, cut)

##########################################
