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
from input_card_2f import *

from optparse import OptionParser

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")

(options,args)=parser.parse_args()


ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

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

def my_abs_2f(h2):
	for i in range(1,h2.GetNbinsX()+1):
		for j in range(1,h2.GetNbinY()+1):
			if h2.GetBinContent(i,j)<0:
				h2.SetBinContent(i,j,0.0)

def Load_json(dic_name):
	return eval(open(dic_name).read().replace("\n",""))

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
		if pt>pt_l and pt<pt_u:
			for (eta_l, eta_u) in dic_in[(pt_l,pt_u)]:
				if eta>eta_l and eta<eta_u:
					eff = dic_in[(pt_l,pt_u)][(eta_l,eta_u)]
					return eff
	return eff

def Get_SF_1D(dic_in, value_in):
	value = value_in
	eff = 1.0
	for (value_l, value_u) in dic_in:
		if value>value_l and value<value_u:
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

def Fill_hist_2f(sample_dic, value_dic_2f, cut):
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
		#if n_process >1000:break
		exec 'passed = (%s)'%(cut_dic_2f[cut])
		if not passed: continue 
		event_weight = 1.0
		leading_SF_weight = 1.0
		sub_leading_SF_weight = 1.0
		pu_weight = 1.0
		fake_weight = 1.0
		bin_weight = 1.0
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

			#print "isData : %s , leading weight : %f , subleading weight : %f"%(isData, leading_SF_weight, sub_leading_SF_weight)
		if isFake:
			fake_weight = getattr(event,"fake_weight")

		for path in value_dic_2f:
			tmp_value_dic_2f = {}
			if isData:
				tmp_value_dic_2f = value_dic_2f[path]["Data_value_dic"]
			else:
				tmp_value_dic_2f = value_dic_2f[path]["MC_value_dic"]

			if value_dic_2f[path]["PU_reweight"]:
				pu_weight = getattr(event,"w_PU_combined")
			else:
				pu_weight = pm(getattr(event,"w_PU_combined"))

			event_weight = leading_SF_weight * sub_leading_SF_weight * pu_weight * fake_weight
			map_value_2f(path, event, sample_dic["hist"][path],tmp_value_dic_2f,event_weight)

def Get_hist_from_together(sample, sample_dic, value_dic_2f, cut):
	root_file = "%s/%s_hist.root"%(cut,cut)
	f1 = ROOT.TFile(root_file,"read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic_2f:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic_2f[path]["hist_name"]))
	f1.Close()

def Get_hist_from_tmp_2f(sample, sample_dic, value_dic_2f, cut):
	root_file = "%s/%s_hist_%s_2f.root"%(cut,cut,sample)
	f1 = ROOT.TFile(root_file,"Read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic_2f:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic_2f[path]["hist_name"]))
	f1.Close()

def Get_hist_from_split(sample, sample_dic, value_dic_2f, cut):
	root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
	f1 = ROOT.TFile(root_file,"Read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic_2f:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic_2f[path]["hist_name"]))
	f1.Close()

def Get_hist_from_file_2f(sample,sample_dic,value_dic_2f):
	root_file = sample_dic["input_file"]
	f1 = ROOT.TFile(root_file,"read")
	isData = sample_dic["isData"]
	isFake = sample_dic["isFake"]
	print "Read hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
	for path in value_dic_2f:
		sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic_2f[path]["hist_name"]))
	f1.Close()

def Get_hist_2f(input_dic_2f, value_dic_2f, cut):
	for sample in input_dic_2f:
		sample_dic = input_dic_2f[sample]
		if isSplit_mode:
			if sample == options.sample_name:
				Fill_hist_2f(sample_dic, value_dic_2f, cut)
		elif (sample_dic["isFromRoot"] and sample_dic["isUpdate"]):
			Fill_hist_2f(sample_dic, value_dic_2f, cut)
		elif sample_dic["isFromRoot"]:
			Get_hist_from_tmp_2f(sample, sample_dic, value_dic_2f, cut)
		elif not sample_dic["isFromRoot"]:
			Get_hist_from_file_2f(sample, sample_dic, value_dic_2f)
		if "pv_n" in value_dic_2f :
			sample_dic["N_total"] = sample_dic["hist"]["pv_n"].Integral()

def Store_hist_together_2f(input_dic_2f, value_dic_2f, cut):
	try:os.mkdir(cut)
	except:pass
	root_file = "%s/%s_hist_2f.root"%(cut,cut)
	f1 = ROOT.TFile(root_file,"RECREATE")
	for sample in input_dic_2f:
		for path in value_dic_2f:
				if "_out" in input_dic_2f[sample]["hist"][path].GetName()[-4:]:
					input_dic_2f[sample]["hist"][path].SetName(input_dic_2f[sample]["hist"][path].GetName()[:-4])
				tmp_name = input_dic_2f[sample]["hist"][path].GetName()
				input_dic_2f[sample]["hist"][path].SetName("%s_out"%(input_dic_2f[sample]["hist"][path].GetName()))
				input_dic_2f[sample]["hist"][path].Write()
				input_dic_2f[sample]["hist"][path].SetName(tmp_name)
	f1.Close()

def Store_hist_2f(input_dic_2f, value_dic_2f, cut):
	try:os.mkdir(cut)
	except:pass
	for sample in input_dic_2f:
		root_file = "%s/%s_hist_%s_2f.root"%(cut,cut,sample)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for path in value_dic_2f:
				if "_out" in input_dic_2f[sample]["hist"][path].GetName()[-4:]:
					input_dic_2f[sample]["hist"][path].SetName(input_dic_2f[sample]["hist"][path].GetName()[:-4])
				tmp_name = input_dic_2f[sample]["hist"][path].GetName()
				input_dic_2f[sample]["hist"][path].SetName("%s_out"%(input_dic_2f[sample]["hist"][path].GetName()))
				input_dic_2f[sample]["hist"][path].Write()
				input_dic_2f[sample]["hist"][path].SetName(tmp_name)
		f1.Close()

def Store_hist_split_2f(input_dic_2f, value_dic_2f, cut):
	try:os.mkdir(cut)
	except:pass
	try:os.mkdir("%s/split"%(cut))
	except:pass
	for sample in input_dic_2f:
		if not sample == options.sample_name:continue
		try:os.mkdir("%s/split/%s"%(cut,sample))
		except:pass
		root_file = "%s/split/%s/%s_hist_%s_%s_%s.root"%(cut,sample,cut,sample,options.n_range_l,options.n_range_h)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for path in value_dic_2f:
				if "_out" in input_dic_2f[sample]["hist"][path].GetName()[-4:]:
					input_dic_2f[sample]["hist"][path].SetName(input_dic_2f[sample]["hist"][path].GetName()[:-4])
				tmp_name = input_dic_2f[sample]["hist"][path].GetName()
				input_dic_2f[sample]["hist"][path].SetName("%s_out"%(input_dic_2f[sample]["hist"][path].GetName()))
				input_dic_2f[sample]["hist"][path].Write()
				input_dic_2f[sample]["hist"][path].SetName(tmp_name)
		f1.Close()


def Norm_hist(input_dic_2f, value_dic_2f):
	total_lumi = Get_total_lumi(input_dic_2f)
	for sample in input_dic_2f:
		if not input_dic_2f[sample]["isData"]:
			input_dic_2f[sample]["Norm_Factor"] = total_lumi * input_dic_2f[sample]["Xsection"] / float(input_dic_2f[sample]["Raw_total"])
			for path in value_dic_2f:
				input_dic_2f[sample]["hist"][path].Scale(input_dic_2f[sample]["Norm_Factor"])
				input_dic_2f[sample]["hist"][path].Scale(input_dic_2f[sample]["weight_factor"])
		input_dic_2f[sample]["N_norm"] = input_dic_2f[sample]["N_total"] * input_dic_2f[sample]["Norm_Factor"] * input_dic_2f[sample]["weight_factor"]

def Print_table(input_dic_2f):
	total_lumi = Get_total_lumi(input_dic_2f)
	total_num = Get_total_num(input_dic_2f)
	for sample in input_dic_2f:
		if input_dic_2f[sample]["isData"] and input_dic_2f[sample]["useToNorm"]:
			print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic_2f[sample]["Norm_Factor"], input_dic_2f[sample]["N_norm"], 100.0*input_dic_2f[sample]["N_norm"]/total_num)
	print "#"*50

	for sample in input_dic_2f:
		if not (input_dic_2f[sample]["isData"] and input_dic_2f[sample]["useToNorm"]):
			print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic_2f[sample]["Norm_Factor"], input_dic_2f[sample]["N_norm"], 100.0*input_dic_2f[sample]["N_norm"]/total_num)
	print "#"*50

def Get_part_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f):
	for path in value_dic_2f:
		for part in plot_dic_2f:
			for plot in plot_dic_2f[part]:
				hist_list = plot_dic_2f[part][plot]["data_list"]
				for sample in hist_list:
					plot_dic_2f[part][plot]["hist"][path].Add(plot_dic_2f[part][plot]["hist"][path], input_dic_2f[sample]["hist"][path], 1, 1)
					plot_dic_2f[part][plot]["N_total"]+=input_dic_2f[sample]["N_norm"]
					if plot_dic_2f[part][plot]["ABS"]: my_abs_2f(plot_dic_2f[part][plot]["hist"][path])


def Get_total_lumi(input_dic_2f):
	total_lumi = 0.0
	for sample in input_dic_2f:
		if input_dic_2f[sample]["useToNorm"]:
			total_lumi += input_dic_2f[sample]["lumi"]
	return total_lumi

def Get_total_num(input_dic_2f):
	total_num = 0.0
	for sample in input_dic_2f:
		if input_dic_2f[sample]["useToNorm"]:
			total_num += input_dic_2f[sample]["N_total"]
	return total_num

def main_plot_part_2f(path, input_dic_2f, cut, c2):
	pad1=ROOT.TPad("pad1", "pad1", 0, 0, 1, 1 , 0)#used for ratio, the hist plot
	pad1.SetBottomMargin(0.15)
	pad1.SetLeftMargin(0.14)
	pad1.SetRightMargin(0.17)
	pad1.SetLogx(value_dic_2f[path]["x_log"])
	pad1.SetLogy(value_dic_2f[path]["y_log"])

	c2.cd()
	pad1.Draw()
	pad1.cd()

	for plot in plot_dic_2f["compare_1"]:
		tmp_h2 = plot_dic_2f["compare_1"][plot]["hist"][path]
		tmp_h2.SetStats(0)
		tmp_h2.GetXaxis().SetTitle(value_dic_2f[path]["x_label"][0])
		tmp_h2.GetXaxis().SetTitleSize(0.05)
		tmp_h2.GetXaxis().SetTitleOffset(0.95)
		tmp_h2.GetXaxis().SetLabelSize(0.03)
		tmp_h2.GetYaxis().SetTitle(value_dic_2f[path]["y_label"][0])
		tmp_h2.GetYaxis().SetTitleSize(0.05)
		tmp_h2.GetYaxis().SetLabelSize(0.04)
		tmp_h2.SetMarkerStyle(20)
		tmp_h2.SetMarkerSize(1.0)
		tmp_h2.SetLineWidth(3)
		tmp_h2.SetLineColor(plot_dic_2f["compare_1"][plot]["color"])
		tmp_h2.Draw("colz")
		
		legend1=ROOT.TLegend(0.73,0.6,0.93,0.88)
		legend1.AddEntry(tmp_h2, plot_dic_2f["compare_1"][plot]["legend_title"],"PE")
		legend1.SetBorderSize(0)
		#legend1.Draw()
	
		tText_2 = ROOT.TPaveText(0.15,0.83,0.4,0.83,"NDC")
		tText_2.SetLineColor(10)
		tText_2.SetFillColor(10)
		tText_2.SetTextSize(0.052/0.7)
		tText_2.SetTextAlign(12)
		tText_2.AddText("CMS Preliminary")
		tText_2.SetShadowColor(10)
		#tText_2.Draw("same")
	
		tText_3 = ROOT.TPaveText(0.62,0.95,0.9,0.95,"NDC")
		tText_3.SetLineColor(10)
		tText_3.SetFillColor(10)
		tText_3.SetTextSize(0.06/0.7)
		tText_3.SetTextAlign(12)
		tText_3.SetTextFont(42)
		tText_3.AddText("%0.1f fb^{-1} (13 TeV)"%(Get_total_lumi(input_dic_2f)/1000.0))
		tText_3.SetShadowColor(10)
		#tText_3.Draw("same")
	
		tText_4=ROOT.TPaveText(0.18,0.72, 0.35,0.7,"blNDC")
		tText_4.SetBorderSize(0)
		tText_4.SetFillStyle(0)
		tText_4.SetTextAlign(10)
		tText_4.SetTextColor(1)
		tText_4.SetTextFont(32)
		tText_4.SetTextSize(0.12)
		tText_4.AddText ('%s'%(cut_name_2f[cut][0]))
		#tText_4.Draw()
	
		tText_5=ROOT.TPaveText(0.16,0.65, 0.35,0.7,"blNDC")
		tText_5.SetBorderSize(0)
		tText_5.SetFillStyle(0)
		tText_5.SetTextAlign(10)
		tText_5.SetTextColor(1)
		tText_5.SetTextFont(40)
		tText_5.SetTextSize(0.03)
		tText_5.AddText ('%s'%(cut_name_2f[cut][1]))
		#tText_5.Draw()

		c2.Update()
		c2.Print("%s/%s_%s_hratio_%s.png"%(cut,cut[1:],plot,path))

def Init_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f):
	for path in value_dic_2f:
		if value_dic_2f[path]["use_array"]:
			for sample in input_dic_2f:
				input_dic_2f[sample]["hist"][path] = ROOT.TH2F("%s_%s"%(sample,value_dic_2f[path]["hist_name"]), "", value_dic_2f[path]["hist_para"][0], value_dic_2f[path]["hist_para"][1], value_dic_2f[path]["hist_para"][4], value_dic_2f[path]["hist_para"][5])
			for part in plot_dic_2f:
				for plot in plot_dic_2f[part]:
					plot_dic_2f[part][plot]["hist"][path] = ROOT.TH2F("%s_%s"%(sample,value_dic_2f[path]["hist_name"]), "", value_dic_2f[path]["hist_para"][0], value_dic_2f[path]["hist_para"][1], value_dic_2f[path]["hist_para"][4], value_dic_2f[path]["hist_para"][5])
		else:
			for sample in input_dic_2f:
				input_dic_2f[sample]["hist"][path] = ROOT.TH2F("%s_%s"%(sample,value_dic_2f[path]["hist_name"]), "", value_dic_2f[path]["hist_para"][0], value_dic_2f[path]["hist_para"][2], value_dic_2f[path]["hist_para"][3], value_dic_2f[path]["hist_para"][4], value_dic_2f[path]["hist_para"][6], value_dic_2f[path]["hist_para"][7])
			for part in plot_dic_2f:
				for plot in plot_dic_2f[part]:
					plot_dic_2f[part][plot]["hist"][path] = ROOT.TH2F("%s_%s"%(sample,value_dic_2f[path]["hist_name"]), "", value_dic_2f[path]["hist_para"][0], value_dic_2f[path]["hist_para"][2], value_dic_2f[path]["hist_para"][3], value_dic_2f[path]["hist_para"][4], value_dic_2f[path]["hist_para"][6], value_dic_2f[path]["hist_para"][7])

def Set_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f):
	for path in value_dic_2f:
		for sample in input_dic_2f:
			input_dic_2f[sample]["hist"][path].Sumw2()
		for part in plot_dic_2f:
			for plot in plot_dic_2f[part]:
				plot_dic_2f[part][plot]["hist"][path].Sumw2()
				#plot_dic_2f[part][plot]["hist"][path].SetFillColorAlpha(plot_dic_2f[part][plot]["color"],0.9)
				#plot_dic_2f[part][plot]["hist"][path].SetLineColorAlpha(plot_dic_2f[part][plot]["color"],0.9)

def print_error(error_range_dic, input_dic_2f, value_dic_2f, plot_dic_2f):
	error_range_dic = {"0-500":[1,500,0,0], "500-1000":[2,500,0,0], "1000-1500":[3,500,0,0], "1500-2500":[4,1000,0,0]}
	path = "mass_err_stat"
	if value_dic_2f[path]["use_array"]:
		h_err = ROOT.TH1F("h_err_%s"%(value_dic_2f[path]["hist_name"]), "", value_dic_2f[path]["hist_para"][0], value_dic_2f[path]["hist_para"][1])
	else:
		h_err = ROOT.TH1F("h_err_%s"%(value_dic_2f[path]["hist_name"]), "", value_dic_2f[path]["hist_para"][0], value_dic_2f[path]["hist_para"][2], value_dic_2f[path]["hist_para"][3])
	for p in sorted(plot_dic_2f["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = False):
		plot = p[0]
		h_err.Add(h_err, plot_dic_2f["compare_2"][plot]["hist"][path], 1, 1)
	#for i in range(1,h_err.GetNbinsX()+1):
		#low_edge = h_err.GetBinLowEdge(i)
		#high_edge = low_edge+herr_GetBinWidth(i)
	for mass_range in error_range_dic:
		error_range_dic[mass_range][2] = h_err.GetBinContent(error_range_dic[mass_range][0])*error_range_dic[mass_range][1]
		error_range_dic[mass_range][3] = h_err.GetBinError(error_range_dic[mass_range][0])*error_range_dic[mass_range][1]
		print "%s : %f, %f"%(mass_range, error_range_dic[mass_range][2], error_range_dic[mass_range][3])

def print_sum(input_dic_2f):
	print "%s print sum table %s"%("#"*20,"#"*20)
	for sample in input_dic_2f:
		tmp_N = input_dic_2f[sample]["hist"]["mass_err_stat_2f"].GetBinContent(1)
		tmp_err = input_dic_2f[sample]["hist"]["mass_err_stat_2f"].GetBinError(1)
		print "%s,%s,%s"%(sample,tmp_N,tmp_err)
	print "%s finish %s"%("#"*20,"#"*20)


def main_plot_2f(input_dic_2f, value_dic_2f, plot_dic_2f, cut, isPlot = True):
	#Initialize hist
	Init_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f)
	#set up hist parameters
	Set_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f)
	#get hist from root file using Get() or Fill()
	Get_hist_2f(input_dic_2f, value_dic_2f, cut)
	#Store hist to root file
	Store_hist_2f(input_dic_2f, value_dic_2f, cut)
	#Normalize hist
	#Norm_hist(input_dic_2f, value_dic_2f)
	#print contribution of each dataset
	#Print_table(input_dic_2f)
	#get hist for plot_dic_2f
	Get_part_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f)
	#print_error(error_range_dic, input_dic_2f, value_dic_2f, plot_dic_2f)
	print_sum(input_dic_2f)

	#start plot
	c2 = ROOT.TCanvas( 'c2', 'A Simple Graph with error bars', 50,50,865,780 )
	c2.SetLeftMargin(0.5)

	for path in value_dic_2f:
#		if path == "mass_err_stat_2f":continue
		main_plot_part_2f(path, input_dic_2f, cut, c2)
	c2.Close()

def main_plot_split_2f(input_dic_2f, value_dic_2f, plot_dic_2f, cut, isPlot = True):
	#Initialize hist
	Init_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f)
	#set up hist parameters
	Set_hist_2f(input_dic_2f, value_dic_2f, plot_dic_2f)
	#get hist from root file using Get() or Fill()
	Get_hist_2f(input_dic_2f, value_dic_2f, cut)
	#Store hist to root file
	Store_hist_split_2f(input_dic_2f, value_dic_2f, cut)


#main**************************************************************************
plot_dic_2f={
"compare_1":{
		"_tW":{
			"data_list":["tW","tW_anti"],
			"color":1,
			"legend_title":"tW",
			"N_total":0.0,
			"hist":{},
			"ABS":False,
			},

		"_DY":{
			"data_list":["DYToLL_10to50","DYToLL_50"],
			"color":1,
			"legend_title":"DY",
			"N_total":0.0,
			"hist":{},
			"ABS":False,
			},
		},
}
plot_list = ["_tW","_ttbar","_ZG_jets","_others"]
# start run
cut_name_2f={
'_EMu_2f_80':["e#mu",""],
'_EE_2f_80':["ee",""],
'_MuMu_2f_80':["#mu#mu",""],
'_EE_2f_80_zrm':["ee","M(ll)[81,101] removed"],
'_MuMu_2f_80_zrm':["#mu#mu","M_{ll}[81,101] removed"],

'_EMu_2f_74':["e#mu","[74 regression-no scale smearing]"],
'_EE_2f_74':["ee","[74 regression-no scale smearing]"],
'_MuMu_2f_74':["#mu#mu","[74 regression-no scale smearing]"],
'_EE_2f_74_zrm':["ee","[74 regression-no scale smearing] M_{ll}[81,101] removed"],
'_MuMu_2f_74_zrm':["#mu#mu","[74 regression-no scale smearing] M_{ll}[81,101] removed"],
}

cut_dic_2f={
#'_EMu_80':'getattr(event,"isEMu") and getattr(event,"pass_trigger_EMu") and getattr(event,"pass_step1")',
'_EE_80':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1")',
#'_MuMu_2f_80':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101)',
#'_EE_2f_80_zrm':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101)',
#'_MuMu_2f_80_zrm':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1")',

#'_EMu_74':'getattr(event,"isEMu") and getattr(event,"pass_trigger_EMu") and getattr(event,"pass_step1")',
#'_EE_74':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1")',
#'_MuMu_74':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1")',
#'_EE_74_zrm':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101',
#'_MuMu_74_zrm':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101',
}

dic_Muon_Tracking_eta 		= Load_json("SF_json/Muon/Tracking/Muon_Tracking_json.txt")
dic_Muon_ID_pt_Abseta		= Load_json("SF_json/Muon/ID/Muon_TIghtID_json.txt") 
dic_Muon_ISO_pt_Abseta		= Load_json("SF_json/Muon/ISO/Muon_TightISO_json.txt")
dic_Ele_Tracking_pt_eta		= Load_json("SF_json/Electron/Tracking/Ele_Tracking_json.txt")
dic_Ele_ID_ISO_pt_eta		= Load_json("SF_json/Electron/ID-ISO/Ele_ID-ISO_json.txt") 

error_range_dic = {"0-500":[1,500,0], "500-1000":[2,500,0], "1000-1500":[3,500,0], "1500-2000":[4,500,0]}

isSplit_mode = False
for cut in cut_dic_2f:
	if options.sample_name == "null":
		isSplit_mode = False
		main_plot_2f(input_dic_2f, value_dic_2f, plot_dic_2f, cut)
	else:
		isSplit_mode = True
		print "Using split mode"
		if options.n_range_l<0 or options.n_range_h < 0:
			print "Error, in correct entries range! set to default value"
			main_plot_split_2f(input_dic_2f, value_dic_2f, plot_dic_2f, cut)
		else:
			main_plot_split_2f(input_dic_2f, value_dic_2f, plot_dic_2f, cut)

##########################################
