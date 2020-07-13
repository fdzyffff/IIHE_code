from hist_make import *
from input_sys import *


pre_hist_name = [
"ele_pt",
"ele_eta",
"ele_phi",
"mu_pt",
"mu_eta",
"mu_phi",
"M_emu",
"M_emu_Ml",
"pv_n",
"sumOfWeights",
]

plot_list = [
"Data",
"TTbar",
"ST",
"Z",
"Di_boson",
"QCD_jet",
]

def set_bincontent_zero(h1):
	for n_bin in range(1, h1.GetNbinsX()+1):
		h1.SetBinContent(n_bin,0.0)

def make_hist_sys_bkg(my_plot):
	hist_bkg = collections.OrderedDict()
	for i_hist in pre_hist_name:
		hist_bkg[i_hist] = my_plot["nominal"].get_hist_bkg(i_hist).Clone("sys_bkg")
		set_bincontent_zero(hist_bkg[i_hist])
		tmp_nominal_bkg = my_plot["nominal"].get_hist_bkg(i_hist).Clone("tmp_bkg")

		for plot_sys in my_plot:
			if plot_sys == "nominal":continue
			if not my_plot[plot_sys].use_bkg:continue
			tmp_hist = my_plot[plot_sys].get_hist_bkg(i_hist)
			for n_bin in range(1, tmp_nominal_bkg.GetNbinsX()+1):
				previous_value = hist_bkg[i_hist].GetBinContent(n_bin)
				now_value = tmp_hist.GetBinContent(n_bin)
				nominal_value = tmp_nominal_bkg.GetBinContent(n_bin)
				new_value = previous_value*previous_value + (now_value - nominal_value)*(now_value - nominal_value)
				new_value = sqrt(new_value)
				hist_bkg[i_hist].SetBinContent(n_bin, new_value)
	return hist_bkg

def Graph_Xerror0(graph_in):
	for i in range(0,graph_in.GetN()):
		graph_in.SetPointEXlow (i, 0)
		graph_in.SetPointEXhigh(i, 0)

def remove_graph_zero(gr_in):
	for i in range(gr_in.GetN()-1, 0-1,-1):
		N = gr_in.GetY()[i]
		#print "%d : %f"%(i,N)
		if N==0:
			gr_in.RemovePoint(i)
	
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

def histTograph(h_data, isWeight=False):  
	h_data_bin_value={}
	h_data_bin_width={}
	for nbin in range(1, h_data.GetNbinsX()+1):
		h_data_bin_value[nbin]=h_data.GetBinContent(nbin)*h_data.GetBinWidth(nbin) 
		h_data_bin_width[nbin]=h_data.GetBinWidth(nbin) 
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
			if h_data_bin_width[i+1] !=0:
				error_low= (N-L)/h_data_bin_width[i+1]
				error_up=(U-N)/h_data_bin_width[i+1]
			else:
				error_up=0
				error_low=0
		if N==0:
			error_up=0
			error_low=0
		g_data.SetPointEYlow (i, error_low)
		g_data.SetPointEYhigh(i, error_up)
	return g_data

def getYmax(h1):
	tmp_max = 0
	for i in range(1,h1.GetNbinsX()+1):
		if tmp_max < h1.GetBinContent(i):
			tmp_max = h1.GetBinContent(i)
	return tmp_max


def draw_final_plot(i_hist, my_plot_setting):

	print "ploting : %s"%(i_hist)
	c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 50,50,865,780 )
	c1.SetLeftMargin(0.5)
	pad1=ROOT.TPad("pad1", "pad1", 0, 0.315, 1, 0.99 , 0)#used for ratio, the hist plot
	pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.275 , 0)#used for ratio, the ratio plot
	pad1.SetBottomMargin(0.0)
	pad1.SetLeftMargin(0.14)
	pad1.SetRightMargin(0.05)
	pad2.SetTopMargin(0.0)
	pad2.SetBottomMargin(0.4)
	pad2.SetLeftMargin(0.14)
	pad2.SetRightMargin(0.05)
	pad1.SetLogx(my_plot_setting.x_log)
	pad1.SetLogy(my_plot_setting.y_log)
	pad2.SetLogx(my_plot_setting.x_log)

	gr_1 = ROOT.TGraph()	
	my_plot_setting.hist_data.SetStats(0)
	my_plot_setting.hist_bkg.SetStats(0)

	h_stack = ROOT.THStack()	
	legend1=ROOT.TLegend(0.63,0.6,0.8,0.88)

	gr_1 = histTograph(my_plot_setting.hist_data, my_plot_setting.is_binwidth_weighted)
	Graph_Xerror0(gr_1)
	remove_graph_zero(gr_1)
	gr_1.GetXaxis().SetTitle(my_plot_setting.x_label)
	gr_1.GetXaxis().SetTitleSize(0.1)
	gr_1.GetXaxis().SetTitleOffset(0.95)
	gr_1.GetXaxis().SetLabelSize(1.0)
	gr_1.GetYaxis().SetTitle(my_plot_setting.y_label)
	gr_1.GetYaxis().SetTitleSize(0.7)
	gr_1.SetMarkerStyle(20)
	gr_1.SetMarkerSize(1.0)
	gr_1.SetLineWidth(3)
	gr_1.SetLineColor(1)
	legend1.AddEntry(gr_1, "Data","PE")	

	my_plot_setting.hist_bkg_dic["QCD_jet"].SetFillColorAlpha(ROOT.kYellow, 1.0)
	my_plot_setting.hist_bkg_dic["QCD_jet"].SetLineColorAlpha(ROOT.kYellow, 1.0)
	my_plot_setting.hist_bkg_dic["Di_boson"].SetFillColorAlpha(ROOT.kOrange-3, 1.0)
	my_plot_setting.hist_bkg_dic["Di_boson"].SetLineColorAlpha(ROOT.kOrange-3, 1.0)
	my_plot_setting.hist_bkg_dic["ST"].SetFillColorAlpha(ROOT.kGreen, 1.0)
	my_plot_setting.hist_bkg_dic["ST"].SetLineColorAlpha(ROOT.kGreen, 1.0)
	my_plot_setting.hist_bkg_dic["Z"].SetFillColorAlpha(ROOT.kBlue-3, 1.0)
	my_plot_setting.hist_bkg_dic["Z"].SetLineColorAlpha(ROOT.kBlue-3, 1.0)
	my_plot_setting.hist_bkg_dic["TTbar"].SetFillColorAlpha(ROOT.kRed-4, 1.0)
	my_plot_setting.hist_bkg_dic["TTbar"].SetLineColorAlpha(ROOT.kRed-4, 1.0)

	h_stack.Add(my_plot_setting.hist_bkg_dic["QCD_jet"])
	h_stack.Add(my_plot_setting.hist_bkg_dic["Di_boson"])
	h_stack.Add(my_plot_setting.hist_bkg_dic["ST"])
	h_stack.Add(my_plot_setting.hist_bkg_dic["Z"])
	h_stack.Add(my_plot_setting.hist_bkg_dic["TTbar"])

	legend1.AddEntry(my_plot_setting.hist_bkg_dic["TTbar"],"t#bar{t}","f")	
	legend1.AddEntry(my_plot_setting.hist_bkg_dic["Z"],"Drell-Yan","f")	
	legend1.AddEntry(my_plot_setting.hist_bkg_dic["ST"],"Single Top","f")	
	legend1.AddEntry(my_plot_setting.hist_bkg_dic["Di_boson"],"Di-bosion","f")	
	legend1.AddEntry(my_plot_setting.hist_bkg_dic["QCD_jet"],"QCD+jet","f")	

	c1.cd()
	pad1.Draw()
	pad1.cd()	

	bkg_sys_todraw = my_plot_setting.hist_bkg.Clone("final_bkg_uncert")
	bkg_sys_todraw.SetFillStyle(3015)
	bkg_sys_todraw.SetFillColor(ROOT.kOrange-3)

	for i in range(1, bkg_sys_todraw.GetNbinsX() +1):
		stat_error_i = bkg_sys_todraw.GetBinError(i)
		sys_error_i = my_plot_setting.hist_bkg_sys.GetBinContent(i)
		fianl_error_i = sqrt(stat_error_i*stat_error_i + sys_error_i*sys_error_i)
		bkg_sys_todraw.SetBinError(i, fianl_error_i)

	if my_plot_setting.y_log:
		h_stack.SetMaximum(getYmax(my_plot_setting.hist_data)**2.2)
		h_stack.SetMinimum(0.00001)
	else:
		h_stack.SetMaximum(getYmax(my_plot_setting.hist_data)*1.7)

	h_stack.Draw("hist")
	h_stack.GetYaxis().SetTitle(my_plot_setting.y_label)
	h_stack.GetYaxis().SetTitleOffset(0.88)
	h_stack.GetYaxis().SetTitleSize(0.08)
	h_stack.GetYaxis().SetLabelSize(0.04/0.7)
	h_stack.GetXaxis().SetLabelSize(0)
	bkg_sys_todraw.Draw("same:E2")
	
	gr_1.Draw("PE")
	legend1.AddEntry(bkg_sys_todraw,"uncertainties","f")
		
	legend1.SetBorderSize(0)
	legend1.Draw()

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
	tText_3.AddText("%0.1f fb^{-1} (13 TeV)"%(my_plot_setting.lumi/1000.0))
	tText_3.SetShadowColor(10)
	tText_3.Draw()	
	tText_4=ROOT.TPaveText(0.18,0.72, 0.35,0.74,"blNDC")
	tText_4.SetBorderSize(0)
	tText_4.SetFillStyle(0)
	tText_4.SetTextAlign(10)
	tText_4.SetTextColor(1)
	tText_4.SetTextFont(32)
	tText_4.SetTextSize(0.09)

	tText_5=ROOT.TPaveText(0.26,0.72, 0.4,0.74,"blNDC")
	tText_5.SetBorderSize(0)
	tText_5.SetFillStyle(0)
	tText_5.SetTextAlign(10)
	tText_5.SetTextColor(1)
	tText_5.SetTextFont(40)
	tText_5.SetTextSize(0.05)

	tText_6=ROOT.TPaveText(0.16,0.6, 0.35,0.65,"blNDC")
	tText_6.SetBorderSize(0)
	tText_6.SetFillStyle(0)
	tText_6.SetTextAlign(10)
	tText_6.SetTextColor(1)
	tText_6.SetTextFont(40)
	tText_6.SetTextSize(0.03)

	c1.Update()
	c1.cd()
	pad2.Draw()
	pad2.cd()	
	h_ratio = bkg_sys_todraw.Clone("ratio_bkg")

	h_ratio.SetStats(0)
	h_ratio.GetXaxis().SetTitle(my_plot_setting.x_label)
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
	if my_plot_setting.x_log:
		h_ratio.GetXaxis().SetNoExponent()
		h_ratio.GetXaxis().SetMoreLogLabels()
	h_ratio.SetMinimum(0.5)
	h_ratio.SetMaximum(1.5)	
	h_ratio.SetTitle("")
	h_ratio.SetLineWidth(2)	
	h_ratio.Divide(bkg_sys_todraw)
	h_ratio.SetMarkerSize(0.0)	
	h_ratio.Draw("E2")

	gr_ratio = get_graph_ratio(histTograph(my_plot_setting.hist_data, my_plot_setting.is_binwidth_weighted), ROOT.TGraphAsymmErrors(bkg_sys_todraw))
	Graph_Xerror0(gr_ratio)
	legend2=ROOT.TLegend(0.2,0.7,0.5,0.9)
	h_ratio.SetLineColor(1)
	legend2.SetBorderSize(0)
	gr_ratio.SetMarkerStyle(20)
	gr_ratio.SetMarkerSize(1.0)
	gr_ratio.SetLineColor(1)
	gr_ratio.SetLineWidth(3)
	gr_ratio.Draw("PE")    	
	#c1.cd()
	c1.Update()
	c1.Print("%s_hratio_%s.png"%(my_plot_setting.label, i_hist))
	c1.Close()

