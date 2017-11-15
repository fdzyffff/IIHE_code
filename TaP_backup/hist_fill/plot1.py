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
from input_hist import *
from hist_setting import *

from optparse import OptionParser

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")

(options,args)=parser.parse_args()


ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def get_list_from_dir(root_dir):
	file_list = []
	for the_file in os.listdir(root_dir):
		if ".root" == the_file[-5:]:
			file_list.append(os.path.join(root_dir, the_file))
	file_list.sort()
	return file_list

def init_fit_func(func_dic):
	my_func = ROOT.TF1(func_dic['fit_function'][0],func_dic['fit_function'][1],func_dic['fit_function'][2],func_dic['fit_function'][3])
	for i in range(len(func_dic["fit_para"])):
		my_func.SetParameter(i,func_dic["fit_para"][i])
	return my_func

def Init_global_branch_dic(tree_in, global_branch_dic):
	for part in global_branch_dic:
		global_branch_dic[part] = False
	global_branch_dic.clear()
	for leaf in tree_in.GetListOfLeaves():
		global_branch_dic[leaf.GetName()] = True

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
	return tmp_max

def my_abs(h2):
	for i in range(1,h2.GetNbinsX()+1):
		if h2.GetBinContent(i)<0:
			h2.SetBinContent(i,0.0)

def constraint_float(input_x, l_limit = "null", h_limit = "null"):
	if h_limit != "null":
		if input_x > h_limit:
			return h_limit
	if l_limit != "null":
		if input_x < l_limit:
			return l_limit
	return input_x

def pm(x):
	if x>0:
		return 1
	elif x<0:
		return -1
	else:
		return 0

def Fill_hist(sample, part_sample_dic, hist_dic, cut):
	root_file_list = get_list_from_dir(part_sample_dic["input_file_dir"])

	n_process = 0
	Flag_break = False
	if isSplit_mode:
		if (options.n_range_l<0):options.n_range_l=1
		if (options.n_range_h<0):options.n_range_h=t1.GetEntries()
		print "### using split mode, get event from %d to %d"%(options.n_range_l,options.n_range_h)
	
	for root_file in root_file_list:
		f1 = ROOT.TFile(root_file,"read")
		t1 = f1.Get("tap")
		isData = part_sample_dic["isData"]
		print "Fill hist from file : %s, isData: %s"%(root_file,isData)
		Init_global_branch_dic(t1,global_branch_dic)
		for event in t1:
			n_process += 1
			if(n_process%50000==0):print n_process,'processed\n'
			if isSplit_mode:
				if (options.n_range_l > n_process):
					continue
				elif (options.n_range_h < n_process):
					Flag_break = True
					break
			#if n_process >100:break
			exec 'passed = (%s)'%(cut_dic[cut][0])
			if not passed: continue 
	
			for path in hist_dic:
				map_fill_hist(sample, event, part_sample_dic["hist"], hist_dic, path)
		f1.Close()
		if Flag_break:break

def Get_hist_from_tmp(sample, sample_dic, hist_dic, cut):
	root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
	f1 = ROOT.TFile(root_file,"Read")
	print "Get hist from file : %s"%(root_file)
	for path in hist_dic:
		for cut in hist_dic[path]["cut_dic"]:
			sample_dic[sample]["hist"][path+cut]["h_numerator"] = f1.Get("%s_%s_n_out"%(sample,hist_dic[path]["hist_name"]+cut))
			sample_dic[sample]["hist"][path+cut]["h_denominator"] = f1.Get("%s_%s_d_out"%(sample,hist_dic[path]["hist_name"]+cut))
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

def Get_hist(sample_dic, hist_dic, cut):
	for sample in sample_dic:
		part_sample_dic = sample_dic[sample]
		if isSplit_mode:
			if sample == options.sample_name:
				Fill_hist(sample, part_sample_dic, hist_dic, cut)
		elif (part_sample_dic["isFromRoot"] and part_sample_dic["isUpdate"]):
			Fill_hist(sample, part_sample_dic, hist_dic, cut)
		elif part_sample_dic["isFromRoot"]:
			Get_hist_from_tmp(sample, sample_dic, hist_dic, cut)
		elif not part_sample_dic["isFromRoot"]:
			Get_hist_from_file(sample, sample_dic, hist_dic)


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

def Fill_global_hist_dic(sample_dic, hist_dic, plot_dic):
	for path in hist_dic:
		for cut in hist_dic[path]["cut_dic"]:
			for hist in hist_list:
				for sample in sample_dic:
					global_hist_dic[path+cut][hist].Add(global_hist_dic[path+cut][hist], sample_dic[sample]["hist"][path+cut][hist], 1, 1)

def Get_total_lumi(sample_dic):
	total_lumi = 0.0
	for sample in sample_dic:
		total_lumi += sample_dic[sample]["lumi"]
	return total_lumi

def main_plot_part(sample_dic, plot_part_dic, global_hist_dic, cut):
	#start plot
	c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 50,50,800,640 )

	para_dic = plot_part_dic["para"]
	c1.SetLogx(para_dic["x_log"])
	c1.SetLogy(para_dic["y_log"])

	h_box = ROOT.TH1F("tmp_h1",para_dic["title"],1,para_dic["xaxis"][0],para_dic["xaxis"][1])
	run_label = cut_dic[cut][1]
	title = ("%s%s"%(para_dic["title"],run_label))
	h_box.SetTitle(title)
	print title
	h_box.SetStats(0)
	h_box.GetYaxis().SetTitle(para_dic["y_title"])
	h_box.GetYaxis().SetTitleOffset(1.)
	h_box.GetYaxis().SetTitleSize(0.05)
	h_box.GetYaxis().SetLabelSize(0.03)
	h_box.GetYaxis().SetRangeUser(0.0, 1.0)
	h_box.GetYaxis().SetRangeUser(para_dic["yaxis"][0], para_dic["yaxis"][1])
	h_box.GetXaxis().SetTitle(para_dic["x_title"])
	h_box.GetXaxis().SetTitleOffset(0.68)
	h_box.GetXaxis().SetTitleSize(0.056)
	h_box.GetXaxis().SetLabelSize(0.03)
	h_box.GetXaxis().SetRangeUser(para_dic["xaxis"][0], para_dic["xaxis"][1])
	h_box.Draw()
	c1.Update()

	gr_eff_dic = {}
	fit_text_dic = {}
	legend1 = ROOT.TLegend(para_dic["legend"][0],para_dic["legend"][1],para_dic["legend"][2],para_dic["legend"][3])
	#for path in plot_part_dic["hist"]:
	for p in sorted(plot_part_dic["hist"].iteritems(),key=lambda d:d[1]["legend_order"],reverse = False):
		path = p[0]
		setting_dic = plot_part_dic["hist"][path]
		gr_eff_dic[path] = ROOT.TGraphAsymmErrors()
		gr_eff_dic[path].Divide(global_hist_dic[path]["h_numerator"],global_hist_dic[path]["h_denominator"],"cl=0.683 b(1,1) mode")
		Graph_Xerror0(gr_eff_dic[path])

		gr_eff_dic[path].SetMarkerStyle(setting_dic["MarkerStyle"])
		gr_eff_dic[path].SetMarkerColor(setting_dic["Color"])
		gr_eff_dic[path].SetLineColor(setting_dic["Color"])
		
		gr_eff_dic[path].Draw("P")
		try:
			if setting_dic["do_fit"]:
				func1_dic = setting_dic["fit_func"]
				my_func1 = init_fit_func(func1_dic)
				gr_eff_dic[path].Fit(my_func1, "", "", func1_dic["fit_function"][2], func1_dic["fit_function"][3])
				gr_eff_dic[path].GetFunction(func1_dic["fit_function"][0]).SetLineColor(setting_dic["Color"])
				if func1_dic["print_fit"]:
					fit_text_dic[path] = ROOT.TPaveText(func1_dic["position"][0],func1_dic["position"][1],func1_dic["position"][2],func1_dic["position"][3],"blNDC")
					fit_text_dic[path].SetBorderSize(0)
					fit_text_dic[path].SetFillStyle(0)
					fit_text_dic[path].SetTextAlign(12)
					fit_text_dic[path].SetTextColor(setting_dic["Color"])
					fit_text_dic[path].SetTextFont(42)
					fit_text_dic[path].SetTextSize(0.03)
					for i in range(len(func1_dic["fit_para"])):
						fit_text_dic[path].AddText('P%d  %0.4g'%(i, gr_eff_dic[path].GetFunction(func1_dic["fit_function"][0]).GetParameter(i)))
					fit_text_dic[path].Draw()

			c1.Update()

			legend1.AddEntry(gr_eff_dic[path], setting_dic["legend_title"],"LPE")
		except:
			pass

	legend1.Draw()
	text = ROOT.TPaveText(para_dic["text"][0],para_dic["text"][1],para_dic["text"][2],para_dic["text"][3],"blNDC")
	text.SetBorderSize(0)
	text.SetFillStyle(0)
	text.SetTextAlign(12)
	text.SetTextColor(2)
	text.SetTextFont(42)
	text.SetTextSize(0.04195804)
	text.AddText("%0.2f fb^{-1}"%(Get_total_lumi(sample_dic)))
	c1.Update()
	c1.Print("%s/eff_%s.png"%(cut,para_dic["plot_name"]))
	c1.Close()

def Store_hist_split(sample_dic, hist_dic, global_cut):
	try:os.mkdir(global_cut)
	except:pass
	try:os.mkdir("%s/split"%(global_cut))
	except:pass
	for sample in sample_dic:
		if not sample == options.sample_name:continue
		try:os.mkdir("%s/split/%s"%(global_cut,sample))
		except:pass
		root_file = "%s/split/%s/%s_hist_%s_%s_%s.root"%(global_cut,sample,global_cut,sample,options.n_range_l,options.n_range_h)
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

def print_sum(input_dic):
	print "%s print sum table %s"%("#"*20,"#"*20)
	for sample in input_dic:
		if not "data" in sample:continue
		if "ss_" in sample:continue
		tmp_N = input_dic[sample]["hist"]["mass_err_stat"].GetBinContent(1)
		tmp_err = input_dic[sample]["hist"]["mass_err_stat"].GetBinError(1)
		print "%s,%s,%s"%(sample,tmp_N,tmp_err)

	for sample in input_dic:
		if "data" in sample:continue
		if "ss_" in sample:continue
		tmp_N = input_dic[sample]["hist"]["mass_err_stat"].GetBinContent(1)
		tmp_err = input_dic[sample]["hist"]["mass_err_stat"].GetBinError(1)
		print "%s,%s,%s"%(sample,tmp_N,tmp_err)

	for sample in input_dic:
		if not "data" in sample:continue
		if not "ss_" in sample:continue
		tmp_N = input_dic[sample]["hist"]["mass_err_stat"].GetBinContent(1)
		tmp_err = input_dic[sample]["hist"]["mass_err_stat"].GetBinError(1)
		print "%s,%s,%s"%(sample,tmp_N,tmp_err)

	for sample in input_dic:
		if "data" in sample:continue
		if not "ss_" in sample:continue
		tmp_N = input_dic[sample]["hist"]["mass_err_stat"].GetBinContent(1)
		tmp_err = input_dic[sample]["hist"]["mass_err_stat"].GetBinError(1)
		print "%s,%s,%s"%(sample,tmp_N,tmp_err)

	print "%s finish %s"%("#"*20,"#"*20)

def main_plot(sample_dic, hist_dic, plot_dic, cut, isPlot = True):
	#Initialize hist
	Init_hist(sample_dic, hist_dic, global_hist_dic)
	#set up hist parameters
	Set_hist(sample_dic, hist_dic, plot_dic, global_hist_dic)
	#get hist from root file using Get() or Fill()
	Get_hist(sample_dic, hist_dic, cut)
	#Store hist to root file
	Store_hist(sample_dic, hist_dic, cut)
	#print contribution of each dataset
	#Print_table(sample_dic)
	#get hist for global hist_dic
	Fill_global_hist_dic(sample_dic, hist_dic, plot_dic)
	#Store normalized combined hist
	Store_hist_together(hist_dic, cut)
	
	#print_sum(sample_dic)

	for plot_part in plot_dic:
		main_plot_part(sample_dic, plot_dic[plot_part], global_hist_dic, cut)

def main_plot_split(sample_dic, hist_dic, plot_dic, global_cut):
	#Initialize hist
	Init_hist(sample_dic, hist_dic, global_hist_dic)
	#set up hist parameters
	Set_hist(sample_dic, hist_dic, plot_dic, global_hist_dic)
	#get hist from root file using Get() or Fill()
	Get_hist(sample_dic, hist_dic, global_cut)
	#Store hist to root file
	Store_hist_split(sample_dic, hist_dic, global_cut)


#main**************************************************************************
isSplit_mode = False
for global_cut in cut_dic:
	print "######################## %s "%(global_cut)
	if options.sample_name == "null":
		isSplit_mode = False
		main_plot(sample_dic, hist_dic, plot_dic, global_cut)
	else:
		isSplit_mode = True
		print "Using split mode"
		if options.n_range_l<0 or options.n_range_h < 0:
			print "Error, in correct entries range! set to default value"
		main_plot_split(sample_dic, hist_dic, plot_dic, global_cut)
##########################################
