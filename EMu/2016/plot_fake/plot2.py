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

from MuonSF.make_json_SF import *


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
				ratio=float((g1.GetY()[ibin]-g2.GetY()[ibin])/g2.GetY()[ibin])
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

def read_MuonSF_dic():
	dic_Trigger = writeMuonTriggerSF()
	dic_ISO = writeMuonISOSF()
	dic_ID = writeMuonIDSF()
	return dic_Trigger, dic_ISO, dic_ID

def Get_SF(dic_in, pt_in, eta_in):
	pt = pt_in
	eta = fabs(eta_in)
#	print pt
#	print eta
	eff = 1.0
	for (pt_l, pt_u) in dic_in:
		if pt>pt_l and pt<pt_u:
			for (eta_l, eta_u) in dic_in[(pt_l,pt_u)]:
				if eta>eta_l and eta<eta_u:
					eff = dic_in[(pt_l,pt_u)][(eta_l,eta_u)]
					return eff
#    print "***"
	return eff

def getbinwidth(x,x1):
	for i in range(len(x1)):
		if x < x1[i] and i>0:
			return (x1[i]-x1[i-1])
		elif x < x1[i]:
			return -1.0
	return -1.0

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
	for event in t1:
		n_process += 1
		if(n_process%50000==0):print n_process,'processed\n'
	#	if n_process >1000:break
		exec 'passed = (%s)'%(cut_dic[cut])
		if not passed: continue 
		for path in value_dic:
			tmp_value_dic = {}
			if isData:
				tmp_value_dic = value_dic[path]["Data_value_dic"]
			else:
				tmp_value_dic = value_dic[path]["MC_value_dic"]
			for value in tmp_value_dic:
				exec 'passed = (%s)'%(tmp_value_dic[value])
				if not passed: continue 
				total_weight = 1.0
				MuonSF_weight = 1.0
				ElectronSF_weight = 1.0
				pu_weight = 1.0
				fake_weight = 1.0
				bin_weight = 1.0
				if not isData:
					MuonSF_weight *= Get_SF(MuonTriggerSF_dic,getattr(event,"muon_pt"),getattr(event,"muon_eta"))
					MuonSF_weight *= Get_SF(MuonISOSF_dic,getattr(event,"muon_pt"),getattr(event,"muon_eta"))
					MuonSF_weight *= Get_SF(MuonIDSF_dic,getattr(event,"muon_pt"),getattr(event,"muon_eta"))
					ElectronSF_weight *= Get_SF(ElectronIDSF_dic,getattr(event,"t_Et"),getattr(event,"t_eta"))
					if value_dic[path]["PU_reweight"]:
						pu_weight = getattr(event,"w_PU_combined")
					else:
						pu_weight = pm(getattr(event,"w_PU_combined"))
				if isFake:
					fake_weight = getattr(event,"fake_weight")
				if value_dic[path]["use_array"]:
					bin_weight = 1.0/getbinwidth(getattr(event,value),value_dic[path]["hist_para"][1])
				total_weight = MuonSF_weight * ElectronSF_weight * pu_weight * fake_weight * bin_weight
				sample_dic["hist"][path].Fill(getattr(event,value),total_weight)

def Get_hist_from_tmp(sample, sample_dic, value_dic, cut):
	root_file = "%s/%s_hist.root"%(cut,cut)
	f1 = ROOT.TFile(root_file,"read")
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
		if sample_dic["isFromRoot"] and sample_dic["isUpdate"]:
			Fill_hist(sample_dic, value_dic, cut)
		elif sample_dic["isFromRoot"]:
			Get_hist_from_tmp(sample, sample_dic, value_dic, cut)
		elif not sample_dic["isFromRoot"]:
			Get_hist_from_file(sample, sample_dic, value_dic)
		if "pv_n" in value_dic :
			sample_dic["N_total"] = sample_dic["hist"]["pv_n"].Integral()

def Store_hist(input_dic, value_dic, cut):
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
	pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0 , 0)#used for ratio, the hist plot
	pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for ratio, the ratio plot
	pad1.SetBottomMargin(0.0)
	pad1.SetRightMargin(0.02)
	pad2.SetTopMargin(0.0)
	pad2.SetBottomMargin(0.25)
	pad2.SetRightMargin(0.02)
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

	legend1=ROOT.TLegend(0.5,0.65,0.8,0.88)
	for plot in plot_dic["compare_1"]:
		compare1_sum.Add(compare1_sum, plot_dic["compare_1"][plot]["hist"][path], 1, 1)
		gr_1 = histTograph(compare1_sum, value_dic[path]["use_array"])
		Graph_Xerror0(gr_1)
		remove_graph_zero(gr_1)
		gr_1.GetXaxis().SetTitle(value_dic[path]["x_label"][0])
		gr_1.GetXaxis().SetTitleSize(0.1)
		gr_1.GetXaxis().SetTitleOffset(0.65)
		gr_1.GetXaxis().SetLabelSize(value_dic[path]["x_label"][1])
		gr_1.GetYaxis().SetTitle(value_dic[path]["y_label"][0])
		gr_1.GetYaxis().SetTitleSize(0.7)
		gr_1.SetMarkerStyle(20)
		gr_1.SetMarkerSize(1.0)
		gr_1.SetLineWidth(3)
		gr_1.SetLineColor(plot_dic["compare_1"][plot]["color"])
		legend1.AddEntry(gr_1, plot_dic["compare_1"][plot]["legend_title"],"pl")

		break
	for p in sorted(plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = False):
		plot = p[0]
		#print plot_dic["compare_2"][plot]["N_total"]
		compare2_sum.Add(compare2_sum, plot_dic["compare_2"][plot]["hist"][path], 1, 1)
		h_stack.Add(plot_dic["compare_2"][plot]["hist"][path])
	for p in sorted(plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = True):
		plot = p[0]
		legend1.AddEntry(plot_dic["compare_2"][plot]["hist"][path],plot_dic["compare_2"][plot]["legend_title"],"f")


	c1.cd()
	pad1.Draw()
	pad1.cd()

	if value_dic[path]["y_axis"][0]!= 'null':h_stack.SetMinimum(value_dic[path]["y_axis"][0])
	if value_dic[path]["y_axis"][1]!= 'null':h_stack.SetMaximum(value_dic[path]["y_axis"][1])
	h_stack.Draw("hist")
	h_stack.GetYaxis().SetTitle(value_dic[path]["y_label"][0])
	h_stack.GetYaxis().SetTitleOffset(0.7)
	h_stack.GetYaxis().SetTitleSize(0.06)
	h_ratio.GetYaxis().SetLabelSize(value_dic[path]["y_label"][1])
	compare2_sum.Draw("same:E2")
	compare2_sum.SetFillStyle(3015)
	compare2_sum.SetFillColorAlpha(ROOT.kOrange-3,1.0)
	legend1.AddEntry(compare2_sum,"Statisticl","f")
	#compare1_sum.Draw("same:PE2")
	gr_1.Draw("PE")
	legend1.SetBorderSize(0)
	legend1.Draw()

	tText_3=ROOT.TPaveText(0.7,0.9,0.85,1.0,"blNDC")
	tText_3.SetBorderSize(0)
	tText_3.SetFillStyle(0)
	tText_3.SetTextAlign(12)
	tText_3.SetTextColor(1)
	tText_3.SetTextFont(42)
	tText_3.SetTextSize(0.06)
	t1 = tText_3.AddText ("%0.1f fb^{-1}, 13 TeV"%(Get_total_lumi(input_dic)/1000.0))
	tText_3.Draw()

	tText_4=ROOT.TPaveText(0.15,0.8, 0.2,0.85,"blNDC")
	tText_4.SetBorderSize(0)
	tText_4.SetFillStyle(0)
	tText_4.SetTextAlign(12)
	tText_4.SetTextColor(1)
	tText_4.SetTextFont(42)
	tText_4.SetTextSize(0.04195804)
	tText_4.AddText ('%s'%(cut[1:]))
	tText_4.Draw()

	c1.Update()
	c1.cd()
	pad2.Draw()
	pad2.cd()

	h_ratio = compare2_sum.Clone(h_ratio.GetName())
	h_ratio.Add(h_ratio, compare2_sum, 1, -1)
	h_ratio.SetMinimum(-0.7)
	h_ratio.SetMaximum(1.3)

	h_ratio.SetStats(0)
	h_ratio.GetXaxis().SetTitle(value_dic[path]["x_label"][0])
	h_ratio.GetXaxis().SetTitleSize(0.1)
	h_ratio.GetXaxis().SetTitleOffset(0.65)
	h_ratio.GetXaxis().SetLabelSize(value_dic[path]["x_label"][1])
	h_ratio.SetMarkerStyle(20)
	h_ratio.SetLineColor(1)
	h_ratio.SetLineWidth(2)
	h_ratio.GetXaxis().SetTitleSize(0.13)
	h_ratio.GetXaxis().SetTitleOffset(0.7)
	h_ratio.GetXaxis().SetNoExponent()
	h_ratio.GetXaxis().SetMoreLogLabels()
	h_ratio.GetXaxis().SetNdivisions(1020)
	h_ratio.GetYaxis().SetTitle("(Data - MC))/MC")
	h_ratio.GetYaxis().CenterTitle()
	h_ratio.GetYaxis().SetTitleSize(0.12)
	h_ratio.GetYaxis().SetTitleOffset(0.35)
	h_ratio.GetYaxis().SetLabelSize(0.08)
	h_ratio.GetYaxis().SetNdivisions(010)
	h_ratio.Divide(compare2_sum)
	h_ratio.SetMarkerSize(0.0)
	h_ratio.Draw("E2")
	#h_ratio.Fit("pol0")

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
	c1.Print("%s/hratio_%s.png"%(cut,path))

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
	print_error(error_range_dic, input_dic, value_dic, plot_dic)

	#start plot
	c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 800,800 )
	#c1.SetLeftMargin(0.5)

	for path in value_dic:
		main_plot_part(path, input_dic, cut, c1)
	c1.Close()


#main**************************************************************************
isUpdate = True
isUpdate = False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x_emu_new = array('f')
n_index = 0
x_emu_new.append(50)
for i in range(55,120,5):
	x_emu_new.append(i)
	n_index += 1
for i in range(120,150,5):
	x_emu_new.append(i)
	n_index += 1
for i in range(150,200,10):
	x_emu_new.append(i)
	n_index += 1
for i in range(200,600,20):
	x_emu_new.append(i)
	n_index += 1
for i in range(600,900,30):
	x_emu_new.append(i)
	n_index += 1
for i in range(900,1250,50):
	x_emu_new.append(i)
	n_index += 1
for i in range(1250,1610,60):
	x_emu_new.append(i)
	n_index += 1
for i in range(1610,1890,70):
	x_emu_new.append(i)
	n_index += 1
for i in range(1890,3890,80):
	x_emu_new.append(i)
	n_index += 1
x_emu_new.append(4000)
n_index += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x_emu = array('f')
for i in range(31,64):
	x_emu.append(1.14**i)

x_emu2 = array('f')
for i in range(83,166):
	x_emu2.append(1.05**i)

x_pt = array('f')
for i in range(34,65):
	x_pt.append(1.12**i)
mass_bin = array('f')
mass_bin.append(0)
mass_bin.append(500)
mass_bin.append(1000)
mass_bin.append(1500)
mass_bin.append(2500)

value_dic={
#'key':[[['branch1 name','branch2 name'],'hist name','hist title','nbin','array of bin','start bin','end bin','min x','max x'],['x label',x label size,'y label',y label size,pad1 legend x drift,y drift],[if x log,if y log, if userdefined x axis][if PU reweighted]],
"M_emu_massDep":{
		"Data_value_dic":{"M_emu":True},
		"MC_value_dic":{"M_emu":True},
                "hist_name":"M_EMu_new_PU",
                "hist_title":"Invirant mass(ee)",
                "use_array":True,
                "PU_reweight":True,
                "hist_para":[n_index,x_emu_new,50,4000],
                "y_axis":[0.0001,100000],
                "x_label":['M(e#mu) (Gev/c^{2})',0.1],
                "y_label":['Event / Gev',0.05],
                "x_log":True,
                "y_log":True,
                "lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },

#"M_emu1":{
#		"Data_value_dic":{"M_emu":True},
#		"MC_value_dic":{"M_emu":True},
#		"hist_name":"M_EMu1_PU",
#		"hist_title":"Invirant mass(ee)",
#		"use_array":True,
#		"PU_reweight":True,
#		"hist_para":[32,x_emu,60,3200],
#		"y_axis":[0.0001,100000],
#		"x_label":['M(e#mu) (Gev/c^{2})',0.1],
#		"y_label":['Event / Gev',0.05],
#		"x_log":True,
#		"y_log":True,
#		"lenend":{
#				"useLegend":True,
#				"position":[],
#				},
#		},
#"M_emu2":{
#		"Data_value_dic":{"M_emu":True},
#		"MC_value_dic":{"M_emu":True},
#		"hist_name":"M_EMu2_PU",
#		"hist_title":"Invirant mass(ee)",
#		"use_array":True,
#		"PU_reweight":True,
#		"hist_para":[82,x_emu2,60,3200],
#		"y_axis":[0.0001,100000],
#		"x_label":['M(e#mu) (Gev/c^{2})',0.1],
#		"y_label":['Event / Gev',0.05],
#		"x_log":True,
#		"y_log":True,
#		"lenend":{
#				"useLegend":True,
#				"position":[],
#				},
#		},
#
#"Barrel_Et":{
#		"Data_value_dic":{"t_Et":'getattr(event,"t_region") == 1',"muon_pt":'getattr(event,"muon_region")'},
#		"MC_value_dic":{"t_Et":'getattr(event,"t_region") == 1',"muon_pt":'getattr(event,"muon_region")'},
#		"hist_name":"Barrel_Et",
#		"hist_title":"Barrel Lepton Et",
#		"use_array":True,
#		"PU_reweight":True,
#		"hist_para":[30,x_pt,60,3200],
#		"y_axis":[0.0001,100000],
#		"x_label":['Pt (Gev/c)',0.1],
#		"y_label":['Event / Gev',0.05],
#		"x_log":True,
#		"y_log":True,
#		"lenend":{
#				"useLegend":True,
#				"position":[],
#				},
#		},
#"Heep_Et":{
#		"Data_value_dic":{"t_Et":True},
#		"MC_value_dic":{"t_Et":True},
#               "hist_name":"HEEP_Et",
#               "hist_title":"Barrel Lepton Et",
#               "use_array":True,
#               "PU_reweight":True,
#               "hist_para":[30,x_pt,60,3200],
#               "y_axis":[0.0001,100000],
#               "x_label":['HEEP Et (Gev/c)',0.1],
#               "y_label":['Event / Gev',0.05],
#               "x_log":True,
#               "y_log":True,
#               "lenend":{
#                               "useLegend":True,
#                               "position":[],
#                               },
#               },
"pv_n":{
		"Data_value_dic":{"pv_n":True},
		"MC_value_dic":{"pv_n":True},
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
"mass_err_stat":{
		"Data_value_dic":{"M_emu":True},
		"MC_value_dic":{"M_emu":True},
		"hist_name":"M_bin",
		"hist_title":"Number event(with PU reweight)",
		"use_array":True,
		"PU_reweight":True,
		"hist_para":[4,mass_bin,0,50],
		"y_axis":["null","null"],
		"x_label":['M_{e#mu}',0.1],
		"y_label":['Event/GeV ',0.05],
		"x_log":False,
		"y_log":True,
		"lenend":{
				"useLegend":True,
				"position":[],
				},
		},
}

#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
input_dic={
"data":{"isFromRoot":True,
		"input_file":"data_2016_SingleMuon_SinglePhoton2.root",
		"isData":True,
		"isFake":False,
		"useToNorm":True,
		"lumi":35867,
		"Xsection":1.0,
		"N_total": 0.0,
		"Raw_total":1.0,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":38,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_1":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_1.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":87.31,
		"N_total": 0.0,
		"Raw_total":78353860,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_2":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_2.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.326,
		"N_total": 0.0,
		"Raw_total":199979,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_3":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_3.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.0326,
		"N_total": 0.0,
		"Raw_total":199773,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_4":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_4.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.00305,
		"N_total": 0.0,
		"Raw_total":199956,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_5":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_5.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.000174,
		"N_total": 0.0,
		"Raw_total":40816,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL":{
		"isFromRoot":True,
		"input_file":"DYToLL.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":5765.4,
		"N_total": 0.0,
		"Raw_total":49009985,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW1":{
		"isFromRoot":True,
		"input_file":"WW1.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":12.178,
		"N_total": 0.0,
		"Raw_total":1998956,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW2":{
		"isFromRoot":True,
		"input_file":"WW2.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":1.386,
		"N_total": 0.0,
		"Raw_total":199991,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW3":{
		"isFromRoot":True,
		"input_file":"WW3.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.05665,
		"N_total": 0.0,
		"Raw_total":199988,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW4":{
		"isFromRoot":True,
		"input_file":"WW4.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.003557,
		"N_total": 0.0,
		"Raw_total":199981,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW5":{
		"isFromRoot":True,
		"input_file":"WW5.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.00005395,
		"N_total": 0.0,
		"Raw_total":38969,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WZ":{
		"isFromRoot":True,
		"input_file":"WZ.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":47.13,
		"N_total": 0.0,
		"Raw_total":921116,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ZZ":{
		"isFromRoot":True,
		"input_file":"ZZ.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":16.523,
		"N_total": 0.0,
		"Raw_total":990051,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ST":{
		"isFromRoot":True,
		"input_file":"ST.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":71.2,
		"N_total": 0.0,
		"Raw_total":6806148+6856399,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_data":{
		"isFromRoot":True,
		"input_file":"fk_data_2016_SingleMuon_SinglePhoton2.root",
		"isData":True,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":1.0,
		"N_total": 0.0,
		"Raw_total":0.0,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_ttbar":{
		"isFromRoot":True,
		"input_file":"fk_ttbar.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":831.76,
		"N_total": 0.0,
		"Raw_total":75897555,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_DYToLL":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":5765.4,
		"N_total": 0.0,
		"Raw_total":49009985,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_WW1":{
		"isFromRoot":True,
		"input_file":"fk_WW1.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":12.178,
		"N_total": 0.0,
		"Raw_total":19989560,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_WW2":{
		"isFromRoot":True,
		"input_file":"fk_WW2.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":1.386,
		"N_total": 0.0,
		"Raw_total":199991,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_WW3":{
		"isFromRoot":True,
		"input_file":"fk_WW3.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.05665,
		"N_total": 0.0,
		"Raw_total":199988,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_WW4":{
		"isFromRoot":True,
		"input_file":"fk_WW4.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.003557,
		"N_total": 0.0,
		"Raw_total":199981,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_WW5":{
		"isFromRoot":True,
		"input_file":"fk_WW5.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.00005395,
		"N_total": 0.0,
		"Raw_total":38968,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_WZ":{
		"isFromRoot":True,
		"input_file":"fk_WZ.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":47.13,
		"N_total": 0.0,
		"Raw_total":921116,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_ZZ":{
		"isFromRoot":True,
		"input_file":"fk_ZZ.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":16.523,
		"N_total": 0.0,
		"Raw_total":990051,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_ST":{
		"isFromRoot":True,
		"input_file":"fk_ST.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":71.2,
		"N_total": 0.0,
		"Raw_total":6806148+6856399,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
}

plot_dic={
"compare_1":{"data":{
					"data_list":["data"],
					"color":1,
					"legend_title":"data",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}		
			},
"compare_2":{
			"_ttbar":{
					"data_list":["_ttbar_1","_ttbar_2","_ttbar_3","_ttbar_4","_ttbar_5"],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Di_boson":{
					"data_list":['_ST','_WW1','_WW2','_WW3','_WW4','_WW5','_WZ','_ZZ','_DYToLL'],
					"color":ROOT.kOrange-3,
					"legend_title":"Di-Boson, ST, DY",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"fake_rate":{
					"data_list":['fk_data','fk_ttbar','fk_ST','fk_WW1','fk_WW2','fk_WW3','fk_WW4','fk_WW5','fk_WZ','fk_ZZ','fk_DYToLL'],
					"color":ROOT.kBlue-3,
					"legend_title":"Fake rate",
					"N_total":0.0,
					"hist":{},
					"ABS":True,
					},
			},
}

# start run
cut_dic={
'_ALL':'True',
#'_BB':'(getattr(event,"t_region") ==1 and getattr(event,"muon_region") == 1)',
#'_BE':'(getattr(event,"t_region") ==1 and getattr(event,"muon_region") == 3)',
#'_EB':'(getattr(event,"t_region") ==3 and getattr(event,"muon_region") == 1)',
#'_EE':'(getattr(event,"t_region") ==3 and getattr(event,"muon_region") == 3)',
}

MuonTriggerSF_dic, MuonISOSF_dic, MuonIDSF_dic = read_MuonSF_dic()
ElectronIDSF_dic = {
					(0,10000):{
								(0,1.4442):0.971,
								(1.556,2.4):0.982,
								}
					}


error_range_dic = {"0-500":[1,500,0], "500-1000":[2,500,0], "1000-1500":[3,500,0], "1500-2000":[4,500,0]}
for cut in cut_dic:
	main_plot(input_dic, value_dic, plot_dic, cut)

##########################################
