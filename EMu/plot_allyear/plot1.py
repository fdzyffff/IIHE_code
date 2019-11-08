from hist_make import *
from input_sys import *

from optparse import OptionParser

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("-u","--sys_type",dest="sys_type",default="nominal",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")

(options,args)=parser.parse_args()


ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def get_sys_list_dic(path, sys_class_dic, compare2_sys):
	global sys_dic
	sys_value_dic = {}
	for tmp_sys_type in sys_dic:
		if tmp_sys_type == "nominal":continue
		tmp_list = [0.0]
		for i in range(1,compare2_sys.GetNbinsX()+1):
			tmp_list.append(0.0)
			if sys_dic[tmp_sys_type][2]:
				tmp_hist = sys_class_dic[tmp_sys_type].sys_sum_dic[path]
				tmp_compare = float(compare2_sys.GetBinContent(i))
				tmp_sys = float(tmp_hist.GetBinContent(i))
				if tmp_compare == 0:
					continue
				else :
					tmp_list[i] = (tmp_sys - tmp_compare)/tmp_compare
			else:
					tmp_list[i] = (sys_dic[tmp_sys_type][3])

		sys_value_dic[tmp_sys_type] = tmp_list

	return sys_value_dic

def hist_set_sys(compare2_sys, sys_value_dic):
	for i in range(1,compare2_sys.GetNbinsX()+1):
		bin_sys_err = 0.0
		tmp_total_err = [0.0,0.0]
		for tmp_sys_type in sys_dic:
			if tmp_sys_type == "nominal":continue
				#print tmp_sys_type
				#print sys_value_dic[tmp_sys_type]
			if sys_value_dic[tmp_sys_type][i] < 0.0:
				tmp_total_err[0] += sys_value_dic[tmp_sys_type][i]**2.0
			else:
				tmp_total_err[1] += sys_value_dic[tmp_sys_type][i]**2.0
		bin_sys_err = sqrt(max(tmp_total_err[0], tmp_total_err[1]))
		compare2_sys.SetBinError(i,compare2_sys.GetBinContent(i) * bin_sys_err)

def print_sys_contribution(sys_value_dic, n_bin = 1):
	for tmp_sys_type in sys_value_dic:
			print "%s : %.2f%%"%(sys_dic[tmp_sys_type][0], 100*sys_value_dic[tmp_sys_type][n_bin])

def print_rel_part(input_class, path, hist_frame, sys_type, hist_data, plot_name):

	c2 = ROOT.TCanvas( 'c2', 'Sys part hist', 50,50,865,780 )
	c2.cd()
	c2.SetLeftMargin(0.15)
	c2.SetLogx(input_class.value_dic[path]["x_log"])
	c2.SetLogy(False)
	legend1=ROOT.TLegend(0.18,0.7,0.33,0.82)
	legend1.SetBorderSize(0)
	tmp_hist = ROOT.TH1F()
	tmp_hist.SetName("tmp_%s_%s"%(path, sys_type))
	tmp_hist = hist_frame.Clone(tmp_hist.GetName())
	tmp_hist.SetMinimum(-1.0)
	tmp_hist.SetMaximum(1.0)
	tmp_hist.GetXaxis().SetLabelSize(1.0)
	#tmp_hist.GetXaxis().SetLabelOffset(0.1)
	tmp_hist.Draw()
	hist_data.Draw("same:hist")
	tmp_hist.SetLineColor(1)
	legend1.AddEntry(hist_data, sys_type, "L")
	legend1.Draw()
	c2.Update()
	c2.Print("%s/relpart_%s_%s.png"%(plot_name,path, sys_type))
	c2.Close()


#def main_plot_part_sys(input_class, path, plot_name):
#	print "sys ploting : %s"%(path)
#	#c1.SetLeftMargin(0.5)
#	global sys_class_dic
#	hist_sys_dic_rel = {}
#
#	if input_class.value_dic[path]["use_array"]:
#		compare2_sum = ROOT.TH1F("sum_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
#		compare2_sys = ROOT.TH1F("sum_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
#		common_sys = ROOT.TH1F("sum_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
#		for tmp_sys_type in sys_dic:
#			hist_sys_dic_rel[tmp_sys_type] = ROOT.TH1F("rel_%s_%s"%(tmp_sys_type, input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
#
#	else:
#		compare2_sum = ROOT.TH1F("sum_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
#		compare2_sys = ROOT.TH1F("sum_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
#		common_sys = ROOT.TH1F("sum_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
#		for tmp_sys_type in sys_dic:
#			hist_sys_dic_rel[tmp_sys_type] = ROOT.TH1F("rel_%s_%s"%(tmp_sys_type, input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
#
#	compare2_sum.Sumw2()
#	compare2_sys.Sumw2()
#	common_sys.Sumw2()
#	compare2_sum.SetStats(0)
#	compare2_sys.SetStats(0)
#	h_ratio = ROOT.TH1F()
#	h_ratio.SetName("h_ratio_%s"%(input_class.value_dic[path]["hist_name"]))
#	h_ratio_sys = ROOT.TH1F()
#	h_ratio_sys.SetName("h_ratio_sys_%s"%(input_class.value_dic[path]["hist_name"]))
#	h_stack = ROOT.THStack()	
#
#	compare2_sum.GetXaxis().SetTitle(input_class.value_dic[path]["x_label"][0])
#	compare2_sum.GetYaxis().SetTitle(input_class.value_dic[path]["y_label"][0])
#	compare2_sum.SetMarkerStyle(20)
#	compare2_sum.SetMarkerSize(1.0)
#	compare2_sum.SetLineWidth(3)
#	compare2_sum.GetYaxis().SetTitleOffset(0.88)
#	compare2_sum.GetYaxis().SetTitleSize(0.08)
#	compare2_sum.GetYaxis().SetLabelSize(0.04/0.7)
#	#compare2_sum.GetXaxis().SetLabelSize(0)
	#
#
#	for i in range(len(input_class.plot_list)):
#		plot = input_class.plot_list[len(input_class.plot_list)-1-i]
#		if plot in input_class.plot_dic["compare_2"]:
#			compare2_sys.Add(compare2_sys, input_class.plot_dic["compare_2"][plot]["hist"][path], 1, 1)
#			if "qcd_jet" in plot:
#				common_sys.Add(common_sys, input_class.plot_dic["compare_2"][plot]["hist"][path], 1, 1)
#
#	#sys case
#	for tmp_sys_type in sys_class_dic:
#		sys_class_dic[tmp_sys_type].get_sys_sum(path, common_sys)
#
#	sys_value_dic = get_sys_list_dic(path, sys_class_dic, compare2_sys)
#
#	for tmp_sys_type in sys_dic:
#		if tmp_sys_type == "nominal":continue
#		for i in range(1,compare2_sys.GetNbinsX()+1):
#			hist_sys_dic_rel[tmp_sys_type].SetBinContent(i,sys_value_dic[tmp_sys_type][i])
#
#		print_rel_part(input_class, path, compare2_sum, tmp_sys_type, hist_sys_dic_rel[tmp_sys_type], plot_name)
#
#	c1 = ROOT.TCanvas( 'c1_sys', 'A Simple Hist (sys) with error bars', 50,50,865,780 )
#	c1.SetLogx(input_class.value_dic[path]["x_log"])
#	#c1.SetLogy(input_class.value_dic[path]["y_log"])
	#
#	compare2_sum.Draw("")
#	compare2_sum.SetMaximum(1.0)
#	compare2_sum.SetMinimum(-1.0)
#
#	legend1=ROOT.TLegend(0.73,0.6,0.93,0.88)
#	legend1.SetBorderSize(0)
#	legend1.Draw()
#
#	tmp_i = 0	
#	for tmp_sys_type in sys_dic:
#		if tmp_sys_type == "nominal":continue
#		c1.cd()
#		hist_sys_dic_rel[tmp_sys_type].SetLineColor(tmp_i)
#		hist_sys_dic_rel[tmp_sys_type].Draw("same:hist")
#
#		legend1.AddEntry(hist_sys_dic_rel[tmp_sys_type],tmp_sys_type,"L")
#		tmp_i += 1
#
#	tText_2 = ROOT.TPaveText(0.15,0.83,0.4,0.83,"NDC")
#	tText_2.SetLineColor(10)
#	tText_2.SetFillColor(10)
#	tText_2.SetTextSize(0.052/0.7)
#	tText_2.SetTextAlign(12)
#	tText_2.AddText("CMS Preliminary")
#	tText_2.SetShadowColor(10)
#	tText_2.Draw()	
#	tText_3 = ROOT.TPaveText(0.62,0.95,0.9,0.95,"NDC")
#	tText_3.SetLineColor(10)
#	tText_3.SetFillColor(10)
#	tText_3.SetTextSize(0.06/0.7)
#	tText_3.SetTextAlign(12)
#	tText_3.SetTextFont(42)
#	tText_3.AddText("%0.1f fb^{-1} (13 TeV)"%(input_class.Get_total_lumi(input_class.input_dic)/1000.0))
#	tText_3.SetShadowColor(10)
#	tText_3.Draw()	
#	tText_4=ROOT.TPaveText(0.18,0.72, 0.35,0.7,"blNDC")
#	tText_4.SetBorderSize(0)
#	tText_4.SetFillStyle(0)
#	tText_4.SetTextAlign(10)
#	tText_4.SetTextColor(1)
#	tText_4.SetTextFont(32)
#	tText_4.SetTextSize(0.12)
#	if len(input_class.text_list) > 0:
#		tText_4.AddText ('%s'%(input_class.text_list[0]))
#		tText_4.Draw()	
#	tText_5=ROOT.TPaveText(0.16,0.65, 0.35,0.7,"blNDC")
#	tText_5.SetBorderSize(0)
#	tText_5.SetFillStyle(0)
#	tText_5.SetTextAlign(10)
#	tText_5.SetTextColor(1)
#	tText_5.SetTextFont(40)
#	tText_5.SetTextSize(0.03)
#	if len(input_class.text_list) > 1:
#		tText_5.AddText ('%s'%(input_class.text_list[1]))
#		tText_5.Draw()	
#	tText_6=ROOT.TPaveText(0.16,0.6, 0.35,0.65,"blNDC")
#	tText_6.SetBorderSize(0)
#	tText_6.SetFillStyle(0)
#	tText_6.SetTextAlign(10)
#	tText_6.SetTextColor(1)
#	tText_6.SetTextFont(40)
#	tText_6.SetTextSize(0.03)
#	if len(input_class.text_list) > 2:
#		tText_6.AddText ('%s'%(input_class.text_list[2]))
#		tText_6.Draw()	
#
#	c1.Update()
#	c1.Print("%s/relsys_%s_%s.png"%(plot_name,plot_name[1:],path))
#	c1.Print("%s/relsys_%s_%s.pdf"%(plot_name,plot_name[1:],path))
#	c1.Close()
		
def main_plot_part(input_class, path, plot_name):
	print "ploting : %s"%(path)
	c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 50,50,865,780 )
	c1.SetLeftMargin(0.5)
	global sys_class_dic
	pad1=ROOT.TPad("pad1", "pad1", 0, 0.315, 1, 0.99 , 0)#used for ratio, the hist plot
	pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for ratio, the ratio plot
	pad1.SetBottomMargin(0.0)
	pad1.SetLeftMargin(0.14)
	pad1.SetRightMargin(0.05)
	pad2.SetTopMargin(0.0)
	pad2.SetBottomMargin(0.4)
	pad2.SetLeftMargin(0.14)
	pad2.SetRightMargin(0.05)
	pad1.SetLogx(input_class.value_dic[path]["x_log"])
	pad1.SetLogy(input_class.value_dic[path]["y_log"])
	pad2.SetLogx(input_class.value_dic[path]["x_log"])
	if input_class.value_dic[path]["use_array"]:
		compare1_sum = ROOT.TH1F("sum1_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
		compare2_sum = ROOT.TH1F("sum2_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
		compare2_sys = ROOT.TH1F("sum3_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
		common_sys = ROOT.TH1F("sum4_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][1])
	else:
		compare1_sum = ROOT.TH1F("sum1_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
		compare2_sum = ROOT.TH1F("sum2_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
		compare2_sys = ROOT.TH1F("sum3_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
		common_sys = ROOT.TH1F("sum4_%s"%(input_class.value_dic[path]["hist_name"]), "", input_class.value_dic[path]["hist_para"][0], input_class.value_dic[path]["hist_para"][2], input_class.value_dic[path]["hist_para"][3])
	compare1_sum.Sumw2()
	compare2_sum.Sumw2()
	compare2_sys.Sumw2()
	common_sys.Sumw2()
	gr_1 = ROOT.TGraph()	
	compare2_sum.SetStats(0)
	compare2_sys.SetStats(0)
	h_ratio = ROOT.TH1F()
	h_ratio.SetName("h_ratio_%s"%(input_class.value_dic[path]["hist_name"]))
	h_ratio_sys = ROOT.TH1F()
	h_ratio_sys.SetName("h_ratio_sys_%s"%(input_class.value_dic[path]["hist_name"]))
	h_stack = ROOT.THStack()	
	legend1=ROOT.TLegend(0.73,0.6,0.93,0.88)
	for plot in input_class.plot_dic["compare_1"]:
		compare1_sum.Add(compare1_sum, input_class.plot_dic["compare_1"][plot]["hist"][path], 1, 1)
		gr_1 = input_class.histTograph(compare1_sum, input_class.value_dic[path]["use_array"])
		input_class.Graph_Xerror0(gr_1)
		input_class.remove_graph_zero(gr_1)
		gr_1.GetXaxis().SetTitle(input_class.value_dic[path]["x_label"][0])
		gr_1.GetXaxis().SetTitleSize(0.1)
		gr_1.GetXaxis().SetTitleOffset(0.95)
		gr_1.GetXaxis().SetLabelSize(input_class.value_dic[path]["x_label"][1])
		gr_1.GetYaxis().SetTitle(input_class.value_dic[path]["y_label"][0])
		gr_1.GetYaxis().SetTitleSize(0.7)
		gr_1.SetMarkerStyle(20)
		gr_1.SetMarkerSize(1.0)
		gr_1.SetLineWidth(3)
		gr_1.SetLineColor(input_class.plot_dic["compare_1"][plot]["color"])
		legend1.AddEntry(gr_1, input_class.plot_dic["compare_1"][plot]["legend_title"],"PE")	
		break
	#for p in sorted(input_class.plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = False):
		#plot = p[0]
	for i in range(len(input_class.plot_list)):
		plot = input_class.plot_list[len(input_class.plot_list)-1-i]
		if plot in input_class.plot_dic["compare_2"]:
			#print input_class.plot_dic["compare_2"][plot]["N_total"]
			compare2_sum.Add(compare2_sum, input_class.plot_dic["compare_2"][plot]["hist"][path], 1, 1)
			compare2_sys.Add(compare2_sys, input_class.plot_dic["compare_2"][plot]["hist"][path], 1, 1)
			if "qcd_jet" in plot:
				common_sys.Add(common_sys, input_class.plot_dic["compare_2"][plot]["hist"][path], 1, 1)
			h_stack.Add(input_class.plot_dic["compare_2"][plot]["hist"][path])

	#sys case
	if use_sys:
		for tmp_sys_type in sys_class_dic:
			sys_class_dic[tmp_sys_type].get_sys_sum(path, common_sys)
		sys_value_dic = get_sys_list_dic(path, sys_class_dic, compare2_sys)
		hist_set_sys(compare2_sys, sys_value_dic)
		if path == "n_stat":
			print_sys_contribution(sys_value_dic)
		if path == "M_emu_massDep":
			print_sys_contribution(sys_value_dic, 3)

	#for p in sorted(input_class.plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = True):
		#plot = p[0]
	for plot in input_class.plot_list:
		if plot in input_class.plot_dic["compare_2"]:
			legend1.AddEntry(input_class.plot_dic["compare_2"][plot]["hist"][path],input_class.plot_dic["compare_2"][plot]["legend_title"],"f")	
	c1.cd()
	pad1.Draw()
	pad1.cd()	
	if input_class.value_dic[path]["y_axis"][0]!= 'null':h_stack.SetMinimum(input_class.value_dic[path]["y_axis"][0])
	if input_class.value_dic[path]["y_axis"][1]!= 'null':h_stack.SetMaximum(input_class.value_dic[path]["y_axis"][1])
	else:
		if input_class.value_dic[path]["y_log"]:
			h_stack.SetMaximum(max(input_class.getYmax(compare1_sum),input_class.getYmax(compare2_sum))**2.2)
		else:
			h_stack.SetMaximum(max(input_class.getYmax(compare1_sum),input_class.getYmax(compare2_sum))*1.7)
	h_stack.Draw("hist")
	h_stack.GetYaxis().SetTitle(input_class.value_dic[path]["y_label"][0])
	h_stack.GetYaxis().SetTitleOffset(0.88)
	h_stack.GetYaxis().SetTitleSize(0.08)
	h_stack.GetYaxis().SetLabelSize(0.04/0.7)
	h_stack.GetXaxis().SetLabelSize(0)
	compare2_sum.Draw("same:E2")
	compare2_sum.SetFillStyle(3015)
	compare2_sum.SetFillColorAlpha(ROOT.kOrange-3,1.0)
	if use_sys:
		compare2_sys.Draw("same:E2")
		compare2_sys.SetFillStyle(3015)
		compare2_sys.SetFillColorAlpha(ROOT.kBlue,0.5)
	#compare1_sum.Draw("same:PE2")
	gr_1.Draw("PE")
	legend1.AddEntry(compare2_sum,"Stat. uncertainty","f")
	if use_sys:
		legend1.AddEntry(compare2_sys,"Sys uncertainty","f")
	legend1.SetBorderSize(0)
	legend1.Draw()
#	legend3=ROOT.TLegend(0.53,0.6,0.73,0.88)
#	for plot in input_class.plot_dic["compare_3"]:
#		input_class.plot_dic["compare_3"][plot]["hist"][path].SetFillColor(0)
#		input_class.plot_dic["compare_3"][plot]["hist"][path].SetLineWidth(3)
#		input_class.plot_dic["compare_3"][plot]["hist"][path].SetLineStyle(input_class.plot_dic["compare_3"][plot]["line_style"])
#		input_class.plot_dic["compare_3"][plot]["hist"][path].Draw("same:hist")
#		legend3.AddEntry(input_class.plot_dic["compare_3"][plot]["hist"][path],input_class.plot_dic["compare_3"][plot]["legend_title"],"l")
#	legend3.SetBorderSize(0)
#	legend3.Draw()	
	tText_2 = ROOT.TPaveText(0.15,0.83,0.4,0.83,"NDC")
	tText_2.SetLineColor(10)
	tText_2.SetFillColor(10)
	tText_2.SetTextSize(0.052/0.7)
	tText_2.SetTextAlign(12)
	tText_2.AddText("CMS Preliminary")
	tText_2.SetShadowColor(10)
	tText_2.Draw()	
	tText_3 = ROOT.TPaveText(0.62,0.95,0.9,0.95,"NDC")
	tText_3.SetLineColor(10)
	tText_3.SetFillColor(10)
	tText_3.SetTextSize(0.06/0.7)
	tText_3.SetTextAlign(12)
	tText_3.SetTextFont(42)
	tText_3.AddText("%0.1f fb^{-1} (13 TeV)"%(input_class.Get_total_lumi(input_class.input_dic)/1000.0))
	tText_3.SetShadowColor(10)
	tText_3.Draw()	
	tText_4=ROOT.TPaveText(0.18,0.72, 0.35,0.7,"blNDC")
	tText_4.SetBorderSize(0)
	tText_4.SetFillStyle(0)
	tText_4.SetTextAlign(10)
	tText_4.SetTextColor(1)
	tText_4.SetTextFont(32)
	tText_4.SetTextSize(0.12)
	if len(input_class.text_list) > 0:
		tText_4.AddText ('%s'%(input_class.text_list[0]))
		tText_4.Draw()	
	tText_5=ROOT.TPaveText(0.16,0.65, 0.35,0.7,"blNDC")
	tText_5.SetBorderSize(0)
	tText_5.SetFillStyle(0)
	tText_5.SetTextAlign(10)
	tText_5.SetTextColor(1)
	tText_5.SetTextFont(40)
	tText_5.SetTextSize(0.03)
	if len(input_class.text_list) > 1:
		tText_5.AddText ('%s'%(input_class.text_list[1]))
		tText_5.Draw()	
	tText_6=ROOT.TPaveText(0.16,0.6, 0.35,0.65,"blNDC")
	tText_6.SetBorderSize(0)
	tText_6.SetFillStyle(0)
	tText_6.SetTextAlign(10)
	tText_6.SetTextColor(1)
	tText_6.SetTextFont(40)
	tText_6.SetTextSize(0.03)
	if len(input_class.text_list) > 2:
		tText_6.AddText ('%s'%(input_class.text_list[2]))
		tText_6.Draw()	
	c1.Update()
	c1.cd()
	pad2.Draw()
	pad2.cd()	
	h_ratio = compare2_sum.Clone(h_ratio.GetName())
	h_ratio_sys = compare2_sys.Clone(h_ratio_sys.GetName())
	#h_ratio.Add(h_ratio, compare2_sum, 1, -1)
	if input_class.sys_type == "nominal":
		h_ratio.SetMinimum(0.5)
		h_ratio.SetMaximum(1.5)	
	else:
		h_ratio.SetMinimum(0.4)
		h_ratio.SetMaximum(3.0)	
	h_ratio.SetStats(0)
	h_ratio.GetXaxis().SetTitle(input_class.value_dic[path]["x_label"][0])
	h_ratio.GetXaxis().SetTitleSize(0.058/0.3)
	h_ratio.GetXaxis().SetTitleFont(42)
	h_ratio.GetXaxis().SetTickLength(0.05)
	h_ratio.GetXaxis().SetLabelSize(0.045/0.3)
	h_ratio.GetXaxis().SetLabelOffset(0.02)
	h_ratio.GetXaxis().SetTitleOffset(0.23/0.25)
	h_ratio.GetYaxis().SetTitle("Data/Pred.")
	h_ratio.GetYaxis().SetLabelSize(0.04/0.3)
	h_ratio.GetYaxis().SetTitleSize(0.045/0.3)
	h_ratio.GetYaxis().SetNdivisions(504)
	h_ratio.GetYaxis().SetLabelOffset(0.01)
	h_ratio.GetYaxis().SetTitleOffset(0.41)
	h_ratio.GetYaxis().SetTickLength(0.05)
	h_ratio.GetYaxis().SetTitleFont(42)
	if input_class.value_dic[path]["x_log"]:
		h_ratio.GetXaxis().SetNoExponent()
		h_ratio.GetXaxis().SetMoreLogLabels()
	h_ratio.SetLineWidth(2)	
	h_ratio.Divide(compare2_sum)
	h_ratio.SetMarkerSize(0.0)	
	if path == "n_jet_bjet":
		for label in n_jet_bjet_dic:
			h_ratio.GetXaxis().SetBinLabel(n_jet_bjet_dic[label][1],n_jet_bjet_dic[label][2])
	h_ratio.Draw("E2")	
	if use_sys:
		h_ratio_sys.Divide(compare2_sys)
		h_ratio_sys.Draw("same:E2")
	gr_ratio = input_class.get_graph_ratio(input_class.histTograph(compare1_sum, input_class.value_dic[path]["use_array"]), ROOT.TGraphAsymmErrors(compare2_sum))
	input_class.Graph_Xerror0(gr_ratio)
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
	c1.Print("%s/%s_hratio_%s.png"%(plot_name,plot_name[1:],path))
	c1.Print("%s/%s_hratio_%s.pdf"%(plot_name,plot_name[1:],path))
	c1.Close()
	
def init_class(input_class, input_sys_type, set_dir = True):
	#Initialize hist for sample_dic and plot_dic
	input_class.sys_type = input_sys_type
	input_class.isSplit_mode = isSplit_mode
	input_class.cut_str = cut_dic[cut]
	input_class.set_value_dic(pre_value_dic)
	if sys_dic[input_class.sys_type][1]:
		input_class.hist_input_dir = os.path.join(cut,input_sys_type)
		input_class.set_plot_dic(pre_plot_dic,"23")
		input_class.set_input_dic(pre_input_dic,"23")
	else:
		input_class.hist_input_dir = os.path.join(cut,"nominal")
		input_class.set_plot_dic(pre_plot_dic,"2")
		input_class.set_input_dic(pre_input_dic,"2")
	input_class.hist_output_dir = os.path.join(cut,input_sys_type)
	input_class.n_range_l = options.n_range_l
	input_class.n_range_h = options.n_range_h
	input_class.target_sample = options.sample_name
	if set_dir: input_class.set_dir()

def Store_limit_plot(self, plot_name, sys_class_dic):
	name_dic={}
	name_dic["_ttbar"] = "TTbar"
	name_dic["Z"] = "DY"
	name_dic["ST"] = "ST"
	name_dic["Di_boson"] = "DiBoson"
	name_dic["qcd_jet"] = "QCD"
	name_dic["data"] = "Data"

	for path in value_dic:
		if not (path in self.store_hist_plot_list):continue
		root_file = "%s/final_limit_hist_%s.root"%(plot_name, path)
		f1 = ROOT.TFile(root_file,"RECREATE")

		for tmp_sys_type in sys_class_dic:
			tmp_class = sys_class_dic[tmp_sys_type]
			hist_list = ["compare_2"]
			if tmp_sys_type == "nominal":
				for part in tmp_class.plot_dic["compare_1"]:
					tmp_hist = tmp_class.plot_dic["compare_1"][part]["hist"][path]
					pre_name = tmp_hist.GetName()
					porcess = name_dic[part]
					systematic = sys_dic[tmp_sys_type][0]
					tmp_hist.SetName("%s_%s"%(process, systematic))
					tmp_hist.Write()
					tmp_hist.SetName(pre_name)

			for part in tmp_class.plot_dic["compare_2"]:
				tmp_hist = tmp_class.plot_dic["compare_2"][part]["hist"][path]
				pre_name = tmp_hist.GetName()
				porcess = name_dic[part]
				systematic = sys_dic[tmp_sys_type][0]
				tmp_hist.SetName("%s_%s"%(process, systematic))
				tmp_hist.Write()
				tmp_hist.SetName(pre_name)
			for part in tmp_class.plot_dic["compare_3"]:
				tmp_hist = tmp_class.plot_dic["compare_3"][part]["hist"][path]
				pre_name = tmp_hist.GetName()
				porcess = name_dic[part]
				systematic = sys_dic[tmp_sys_type][0]
				tmp_hist.SetName("%s_%s"%(process, systematic))
				tmp_hist.Write()
				tmp_hist.SetName(pre_name)
		f1.Close()

def main_plot():
	global use_sys
	p_nominal = hist_make(GLOBAL_YEAR)
	init_class(p_nominal, sys_type)
	p_nominal.main_plot()
	p_nominal.Store_hist_plot_total()

	if use_sys:
		for tmp_sys_type in sys_dic:
			if tmp_sys_type == "nominal":continue
			#if sys_dic[tmp_sys_type][1]:
			if (sys_dic[tmp_sys_type][2]):
				sys_class_dic[tmp_sys_type] = hist_make(GLOBAL_YEAR)
				init_class(sys_class_dic[tmp_sys_type], tmp_sys_type)
				sys_class_dic[tmp_sys_type].total_lumi = p_nominal.Get_total_lumi(p_nominal.input_dic)
				sys_class_dic[tmp_sys_type].main_plot()
				sys_class_dic[tmp_sys_type].set_common_hist("qcd_jet", p_nominal.plot_dic["compare_2"]["qcd_jet"])
				if (sys_dic[tmp_sys_type][1]):
					sys_class_dic[tmp_sys_type].Store_hist_plot_total("23")
				else:
					sys_class_dic[tmp_sys_type].Store_hist_plot_total("2")
				#else:
				#	sys_class_dic[sys_type] = sys_dic[sys_type][3]
	#print sys_class_dic

	plot_name = cut
	Store_limit_plot(plot_name,sys_class_dic)
	#start plot

	p_nominal.text_list = []
	p_nominal.text_list.append(cut_name[cut][0])
	p_nominal.text_list.append(cut_name[cut][1])


	for path in p_nominal.value_dic:
		if path == "mass_err_stat":continue
		#if path != "M_emu_massDep":continue
		main_plot_part(p_nominal,path,plot_name)
		#main_plot_part_sys(p_nominal,path,plot_name)
	#return

	
#	#~~~~~~~~~~~~~~same sign
	pre_use_sys = use_sys
	if QCD_JET_BKG_TYPE == "same sign":
		use_sys = False
		plot_name_ss = "_SS"+cut
		p_nominal_ss = hist_make(GLOBAL_YEAR)
		p_nominal_ss.sys_type = "nominal_ss"
		p_nominal_ss.set_value_dic(pre_value_dic)
		p_nominal_ss.set_plot_dic(pre_plot_dic_ss, "12")
		p_nominal_ss.set_input_dic(pre_input_dic, "-1")
		for tmp_sample in p_nominal_ss.input_dic:
			if p_nominal_ss.input_dic[tmp_sample]["weight_factor"] < 0:
				p_nominal_ss.input_dic[tmp_sample]["weight_factor"] *= -1
		p_nominal_ss.cut_str = cut_dic[cut]
		p_nominal_ss.hist_input_dir = os.path.join(cut,"nominal")
		p_nominal_ss.hist_output_dir = os.path.join(plot_name_ss)
		p_nominal_ss.set_dir()
		p_nominal_ss.total_lumi = p_nominal.Get_total_lumi(p_nominal.input_dic)
	
		p_nominal_ss.main_plot()
		p_nominal_ss.text_list = []
		p_nominal_ss.text_list.append(cut_name[cut][0])
		p_nominal_ss.text_list.append(cut_name[cut][1])
		p_nominal_ss.text_list.append("same sign")
	
		for path in p_nominal_ss.value_dic:
			if path == "mass_err_stat":continue
			main_plot_part(p_nominal_ss, path, plot_name_ss)
	#~~~~~~~~~~~~~~fake rate electron
	if QCD_JET_BKG_TYPE == "fake rate":
		use_sys = False
		plot_name_fke = "_FKE"+cut
		p_nominal_fke = hist_make(GLOBAL_YEAR)
		p_nominal_fke.sys_type = "nominal_fke"
		p_nominal_fke.set_value_dic(pre_value_dic)
		p_nominal_fke.set_plot_dic(pre_plot_dic_fke, "12")
		p_nominal_fke.set_input_dic(pre_input_dic, "-1")
		for tmp_sample in p_nominal_fke.input_dic:
			p_nominal_fke.input_dic[tmp_sample]["weight_factor"] = 1
		p_nominal_fke.cut_str = cut_dic[cut]
		p_nominal_fke.hist_input_dir = os.path.join(cut,"nominal")
		p_nominal_fke.hist_output_dir = os.path.join(plot_name_fke)
		p_nominal_fke.set_dir()
		p_nominal_fke.total_lumi = p_nominal.Get_total_lumi(p_nominal.input_dic)
	
		p_nominal_fke.main_plot()
		p_nominal_fke.text_list = []
		p_nominal_fke.text_list.append(cut_name[cut][0])
		p_nominal_fke.text_list.append(cut_name[cut][1])
		p_nominal_fke.text_list.append("Fake electron")
	
		for path in p_nominal_fke.value_dic:
			if path == "mass_err_stat":continue
			main_plot_part(p_nominal_fke, path, plot_name_fke)
	#	#~~~~~~~~~~~~~~fake rate muon
		use_sys = False
		plot_name_fkm = "_FKM"+cut
		p_nominal_fkm = hist_make(GLOBAL_YEAR)
		p_nominal_fkm.sys_type = "nominal_fkm"
		p_nominal_fkm.set_value_dic(pre_value_dic)
		p_nominal_fkm.set_plot_dic(pre_plot_dic_fkm, "12")
		p_nominal_fkm.set_input_dic(pre_input_dic, "-1")
		for tmp_sample in p_nominal_fkm.input_dic:
			p_nominal_fkm.input_dic[tmp_sample]["weight_factor"] = 1
		p_nominal_fkm.cut_str = cut_dic[cut]
		p_nominal_fkm.hist_input_dir = os.path.join(cut,"nominal")
		p_nominal_fkm.hist_output_dir = os.path.join(plot_name_fkm)
		p_nominal_fkm.set_dir()
		p_nominal_fkm.total_lumi = p_nominal.Get_total_lumi(p_nominal.input_dic)
	
		p_nominal_fkm.main_plot()
		p_nominal_fkm.text_list = []
		p_nominal_fkm.text_list.append(cut_name[cut][0])
		p_nominal_fkm.text_list.append(cut_name[cut][1])
		p_nominal_fkm.text_list.append("Fake muon")
	
		for path in p_nominal_fkm.value_dic:
			if path == "mass_err_stat":continue
			main_plot_part(p_nominal_fkm, path, plot_name_fkm)
	
	#	#~~~~~~~~~~~~~~fake rate ele + muon
		use_sys = False
		plot_name_fk = "_FK"+cut
		p_nominal_fk = hist_make(GLOBAL_YEAR)
		p_nominal_fk.sys_type = "nominal_fk"
		p_nominal_fk.set_value_dic(pre_value_dic)
		p_nominal_fk.set_plot_dic(pre_plot_dic_fk, "12")
		p_nominal_fk.set_input_dic(pre_input_dic, "-1")
		for tmp_sample in p_nominal_fk.input_dic:
			p_nominal_fk.input_dic[tmp_sample]["weight_factor"] = 1
		p_nominal_fk.cut_str = cut_dic[cut]
		p_nominal_fk.hist_input_dir = os.path.join(cut,"nominal")
		p_nominal_fk.hist_output_dir = os.path.join(plot_name_fk)
		p_nominal_fk.set_dir()
		p_nominal_fk.total_lumi = p_nominal.Get_total_lumi(p_nominal.input_dic)
	
		p_nominal_fk.main_plot()
		p_nominal_fk.text_list = []
		p_nominal_fk.text_list.append(cut_name[cut][0])
		p_nominal_fk.text_list.append(cut_name[cut][1])
		p_nominal_fk.text_list.append("Fake rate")
	
		for path in p_nominal_fk.value_dic:
			if path == "mass_err_stat":continue
			main_plot_part(p_nominal_fk, path, plot_name_fk)
	use_sys = pre_use_sys


def main_plot_split():
	p_nominal_split = hist_make(GLOBAL_YEAR)
	init_class(p_nominal_split, sys_type)
	p_nominal_split.main_plot_split()


#main**************************************************************************

cut = ""
sys_type = options.sys_type
sys_class_dic = collections.OrderedDict()
for cut in cut_dic:
	if options.sample_name == "null":
		isSplit_mode = False
		main_plot()
	else:
		isSplit_mode = True
		print "Using split mode"
		print "    Sample: %s"%(options.sample_name)
		print "    Systematic uncertainty type: %s"%(options.sys_type)
		if options.n_range_l<0 or options.n_range_h < 0:
			print "Error, in correct entries range! set to default value"
		main_plot_split()

##########################################
