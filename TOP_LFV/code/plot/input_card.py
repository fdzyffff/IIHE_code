from input_setting import *

if GLOBAL_YEAR == "2016":
	from input_card_2016 import *
if GLOBAL_YEAR == "2017":
	from input_card_2017 import *
if GLOBAL_YEAR == "2018":
	from input_card_2018 import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pre_plot_dic["compare_1"]["data"] = {
					"data_list":["data"],
					"color":1,
					"legend_title":"Data (%s)"%(GLOBAL_YEAR),
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}

pre_plot_dic["compare_2"]["_ttbar"] = {
					"data_list":["TTGJets","TTTo2L2Nu","TTWJetsToLNu","TTWJetsToQQ","TTZToLLNuNu_10","TTZToQQ"],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_2"]["_tW"] = {
					"data_list":["tW","tW_anti"],
					"color":ROOT.kOrange-3,
					"legend_title":"tW",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_2"]["_ZG_jets"] = {
					"data_list":["DYToLL_10to50","DYToLL_50"],
					"color":ROOT.kBlue-3,
					"legend_title":"Z/#gamma^{*}+jets",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_2"]["_others"] = {
					"data_list":["WGToLNuG","WWTo2L2Nu","WZTo2L2Q","WZTo3LNu","ZZTo2L2Nu","ZZTo4L"],
					"color":ROOT.kGreen,
					"legend_title":"Diboson",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
#----fke jet----
if QCD_JET_BKG_TYPE == "same sign":
	pre_plot_dic["compare_2"]["qcd_jet"] = {
					"data_list":["ss_data","ss_TTGJets","ss_TTTo2L2Nu","ss_TTWJetsToLNu","ss_TTWJetsToQQ","ss_TTZToLLNuNu_10","ss_TTZToQQ","ss_tW","ss_tW_anti","ss_DYToLL_10to50","ss_DYToLL_50","ss_WGToLNuG","ss_WWTo2L2Nu","ss_WZTo2L2Q","ss_WZTo3LNu","ss_ZZTo2L2Nu","ss_ZZTo4L"],
					"color":ROOT.kYellow,
					"legend_title":"Jets",
					"N_total":0.0,
					"hist":{},
					"ABS":True,
					"weight_factor":1,
					}

if QCD_JET_BKG_TYPE == "MC":
	pre_plot_dic["compare_2"]["qcd_jet"] = {
					"data_list":["WGToLNuG"],
					"color":ROOT.kYellow,
					"legend_title":"Jets",
					"N_total":0.0,
					"hist":{},
					"ABS":True,
					}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pre_plot_dic_ss["compare_1"]["data"] = {
					"data_list":["ss_data"],
					"color":1,
					"legend_title":"Data (%s)"%(GLOBAL_YEAR),
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}		
pre_plot_dic_ss["compare_2"]["_ttbar"] = {
					"data_list":["ss_TTGJets","ss_TTTo2L2Nu","ss_TTWJetsToLNu","ss_TTWJetsToQQ","ss_TTZToLLNuNu_10","ss_TTZToQQ"],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic_ss["compare_2"]["_tW"] = {
					"data_list":["ss_tW","ss_tW_anti"],
					"color":ROOT.kOrange-3,
					"legend_title":"DY",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic_ss["compare_2"]["_ZG_jets"] = {
					"data_list":["ss_DYToLL_10to50","ss_DYToLL_50"],
					"color":ROOT.kBlue-3,
					"legend_title":"Z/#gamma^{*}+jets",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic_ss["compare_2"]["_others"] = {
					"data_list":["ss_WGToLNuG","ss_WWTo2L2Nu","ss_WZTo2L2Q","ss_WZTo3LNu","ss_ZZTo2L2Nu","ss_ZZTo4L"],
					"color":ROOT.kGreen,
					"legend_title":"Other",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tmp_sample_t = sample_t("DYToLL_10to50")
tmp_sample_t.input_file = "80_DYToLL_10to50.root"
tmp_sample_t.Xsection = xsection_DYToLL_10to50
tmp_sample_t.Raw_total = nevent_DYToLL_10to50
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("DYToLL_50")
tmp_sample_t.input_file = "80_DYToLL_50.root"
tmp_sample_t.Xsection = xsection_DYToLL_50
tmp_sample_t.Raw_total = nevent_DYToLL_50
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TTGJets")
tmp_sample_t.input_file = "80_TTGJets.root"
tmp_sample_t.Xsection = xsection_TTGJets
tmp_sample_t.Raw_total = nevent_TTGJets
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TTTo2L2Nu")
tmp_sample_t.input_file = "80_TTTo2L2Nu.root"
tmp_sample_t.Xsection = xsection_TTTo2L2Nu
tmp_sample_t.Raw_total = nevent_TTTo2L2Nu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TTWJetsToLNu")
tmp_sample_t.input_file = "80_TTWJetsToLNu.root"
tmp_sample_t.Xsection = xsection_TTWJetsToLNu
tmp_sample_t.Raw_total = nevent_TTWJetsToLNu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TTWJetsToQQ")
tmp_sample_t.input_file = "80_TTWJetsToQQ.root"
tmp_sample_t.Xsection = xsection_TTWJetsToQQ
tmp_sample_t.Raw_total = nevent_TTWJetsToQQ
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TTZToLLNuNu_10")
tmp_sample_t.input_file = "80_TTZToLLNuNu_10.root"
tmp_sample_t.Xsection = xsection_TTZToLLNuNu_10
tmp_sample_t.Raw_total = nevent_TTZToLLNuNu_10
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TTZToQQ")
tmp_sample_t.input_file = "80_TTZToQQ.root"
tmp_sample_t.Xsection = xsection_TTZToQQ
tmp_sample_t.Raw_total = nevent_TTZToQQ
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("WGToLNuG")
tmp_sample_t.input_file = "80_WGToLNuG.root"
tmp_sample_t.Xsection = xsection_WGToLNuG
tmp_sample_t.Raw_total = nevent_WGToLNuG
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("WJetsToLNu")
tmp_sample_t.input_file = "80_WJetsToLNu.root"
tmp_sample_t.Xsection = xsection_WJetsToLNu
tmp_sample_t.Raw_total = nevent_WJetsToLNu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("WWTo2L2Nu")
tmp_sample_t.input_file = "80_WWTo2L2Nu.root"
tmp_sample_t.Xsection = xsection_WWTo2L2Nu
tmp_sample_t.Raw_total = nevent_WWTo2L2Nu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("WZTo2L2Q")
tmp_sample_t.input_file = "80_WZTo2L2Q.root"
tmp_sample_t.Xsection = xsection_WZTo2L2Q
tmp_sample_t.Raw_total = nevent_WZTo2L2Q
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("WZTo3LNu")
tmp_sample_t.input_file = "80_WZTo3LNu.root"
tmp_sample_t.Xsection = xsection_WZTo3LNu
tmp_sample_t.Raw_total = nevent_WZTo3LNu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("ZZTo2L2Nu")
tmp_sample_t.input_file = "80_ZZTo2L2Nu.root"
tmp_sample_t.Xsection = xsection_ZZTo2L2Nu
tmp_sample_t.Raw_total = nevent_ZZTo2L2Nu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("ZZTo4L")
tmp_sample_t.input_file = "80_ZZTo4L.root"
tmp_sample_t.Xsection = xsection_ZZTo4L
tmp_sample_t.Raw_total = nevent_ZZTo4L
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("tW")
tmp_sample_t.input_file = "80_tW.root"
tmp_sample_t.Xsection = xsection_tw
tmp_sample_t.Raw_total = nevent_tw
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("tW_anti")
tmp_sample_t.input_file = "80_tW_anti.root"
tmp_sample_t.Xsection = xsection_tw_anti
tmp_sample_t.Raw_total = nevent_tw_anti
pre_input_dic[tmp_sample_t.label] = tmp_sample_t


if QCD_JET_BKG_TYPE == "same sign":

	tmp_sample_t = sample_t("ss_DYToLL_10to50")
	tmp_sample_t.input_file = "80_DYToLL_10to50.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_DYToLL_10to50
	tmp_sample_t.Raw_total = nevent_DYToLL_10to50
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_DYToLL_50")
	tmp_sample_t.input_file = "80_DYToLL_50.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_DYToLL_50
	tmp_sample_t.Raw_total = nevent_DYToLL_50
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_TTGJets")
	tmp_sample_t.input_file = "80_TTGJets.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_TTGJets
	tmp_sample_t.Raw_total = nevent_TTGJets
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_TTTo2L2Nu")
	tmp_sample_t.input_file = "80_TTTo2L2Nu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_TTTo2L2Nu
	tmp_sample_t.Raw_total = nevent_TTTo2L2Nu
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_TTWJetsToLNu")
	tmp_sample_t.input_file = "80_TTWJetsToLNu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_TTWJetsToLNu
	tmp_sample_t.Raw_total = nevent_TTWJetsToLNu
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_TTWJetsToQQ")
	tmp_sample_t.input_file = "80_TTWJetsToQQ.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_TTWJetsToQQ
	tmp_sample_t.Raw_total = nevent_TTWJetsToQQ
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_TTZToLLNuNu_10")
	tmp_sample_t.input_file = "80_TTZToLLNuNu_10.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_TTZToLLNuNu_10
	tmp_sample_t.Raw_total = nevent_TTZToLLNuNu_10
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_TTZToQQ")
	tmp_sample_t.input_file = "80_TTZToQQ.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_TTZToQQ
	tmp_sample_t.Raw_total = nevent_TTZToQQ
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_WGToLNuG")
	tmp_sample_t.input_file = "80_WGToLNuG.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_WGToLNuG
	tmp_sample_t.Raw_total = nevent_WGToLNuG
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_WJetsToLNu")
	tmp_sample_t.input_file = "80_WJetsToLNu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_WJetsToLNu
	tmp_sample_t.Raw_total = nevent_WJetsToLNu
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_WWTo2L2Nu")
	tmp_sample_t.input_file = "80_WWTo2L2Nu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_WWTo2L2Nu
	tmp_sample_t.Raw_total = nevent_WWTo2L2Nu
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_WZTo2L2Q")
	tmp_sample_t.input_file = "80_WZTo2L2Q.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_WZTo2L2Q
	tmp_sample_t.Raw_total = nevent_WZTo2L2Q
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_WZTo3LNu")
	tmp_sample_t.input_file = "80_WZTo3LNu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_WZTo3LNu
	tmp_sample_t.Raw_total = nevent_WZTo3LNu
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_ZZTo2L2Nu")
	tmp_sample_t.input_file = "80_ZZTo2L2Nu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_ZZTo2L2Nu
	tmp_sample_t.Raw_total = nevent_ZZTo2L2Nu
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_ZZTo4L")
	tmp_sample_t.input_file = "80_ZZTo4L.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_ZZTo4L
	tmp_sample_t.Raw_total = nevent_ZZTo4L
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_tW")
	tmp_sample_t.input_file = "80_tW.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_tw
	tmp_sample_t.Raw_total = nevent_tw
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t
	
	tmp_sample_t = sample_t("ss_tW_anti")
	tmp_sample_t.input_file = "80_tW_anti.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.Xsection = xsection_tw_anti
	tmp_sample_t.Raw_total = nevent_tw_anti
	tmp_sample_t.weight_factor = -1.0
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tmp_value_t = value_t("M_ll")
tmp_value_t.branch_name = "M_ll"
tmp_value_t.hist_name = "M_ll"
tmp_value_t.hist_title = "Invirant mass(Di-lepton)"
tmp_value_t.hist_para = [20,None,0,200]
tmp_value_t.x_label = ['M_{ll} (GeV/c^{2})',0.1]
tmp_value_t.y_label = ['Event / 10 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("M_ll_zmass")
tmp_value_t.branch_name = "M_ll"
tmp_value_t.hist_name = "M_ll_zmass"
tmp_value_t.hist_title = "Invirant mass(Di-lepton)"
tmp_value_t.hist_para = [12,None,60,120]
tmp_value_t.x_label = ['M_{ll} (GeV/c^{2})',0.1]
tmp_value_t.y_label = ['Event / 5 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("Pt_ll")
tmp_value_t.hist_name = "Pt_ll"
tmp_value_t.hist_title = "Pt (Di-lepton)"
tmp_value_t.hist_para = [10,None,0,200]
tmp_value_t.x_label = ['P_{T}^{ll} (GeV/c^{2})',0.1]
tmp_value_t.y_label = ['Event / 20 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("phi_ll")
tmp_value_t.hist_name = "phi_ll"
tmp_value_t.hist_title = "Pt (Di-lepton)"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['#phi^{ll} ',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("deltaR_ll")
tmp_value_t.hist_name = "deltaR_ll"
tmp_value_t.hist_title = "Pt (Di-lepton)"
tmp_value_t.hist_para = [15,None,0,6]
tmp_value_t.x_label = ['#Delta R(l,l)',0.1]
tmp_value_t.y_label = ['Event / 0.4',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("rapidity_ll")
tmp_value_t.hist_name = "rapidity_ll"
tmp_value_t.hist_title = "Pt (Di-lepton)"
tmp_value_t.hist_para = [10,None,-3,3]
tmp_value_t.x_label = ['Rapidity^{ll}',0.1]
tmp_value_t.y_label = ['Event / 1',0.6]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("leading_pt")
tmp_value_t.branch_name = "leading_pt"
tmp_value_t.hist_name = "leading_pt"
tmp_value_t.hist_title = "Leading Lepton Pt"
tmp_value_t.hist_para = [10,None,0,200]
tmp_value_t.x_label = ['P_{T}^{leading lep} (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 20 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("pt_muon")
tmp_value_t.hist_name = "muon_pt"
tmp_value_t.hist_title = "Leading Lepton Pt"
tmp_value_t.hist_para = [10,None,0,200]
tmp_value_t.x_label = ['P_{T}^{leading muon} (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 20 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("pt_ele")
tmp_value_t.hist_name = "ele_pt"
tmp_value_t.hist_title = "Leading Lepton Pt"
tmp_value_t.hist_para = [10,None,0,200]
tmp_value_t.x_label = ['P_{T}^{leading ele} (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 20 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("eta_muon")
tmp_value_t.hist_name = "muon_eta"
tmp_value_t.hist_title = "Leading muon #eta"
tmp_value_t.hist_para = [10,None,-2.5,2.5]
tmp_value_t.x_label = ['#eta^{leading muon}',0.1]
tmp_value_t.y_label = ['Event / 0.5',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("eta_ele")
tmp_value_t.hist_name = "electron_eta"
tmp_value_t.hist_title = "Leading electron #eta"
tmp_value_t.hist_para = [10,None,-2.5,2.5]
tmp_value_t.x_label = ['#eta^{leading electron}',0.1]
tmp_value_t.y_label = ['Event / 0.5',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("leading_eta")
tmp_value_t.branch_name = "leading_eta"
tmp_value_t.hist_name = "leading_eta"
tmp_value_t.hist_title = "Leading Lepton #eta"
tmp_value_t.hist_para = [10,None,-2.5,2.5]
tmp_value_t.x_label = ['#eta^{leading lepton}',0.1]
tmp_value_t.y_label = ['Event / 0.5',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("leading_phi")
tmp_value_t.branch_name = "leading_phi"
tmp_value_t.hist_name = "leading_phi"
tmp_value_t.hist_title = "Leading Lepton #phi"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['#phi^{leading lepton}',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("sub_leading_pt")
tmp_value_t.branch_name = "sub_leading_pt"
tmp_value_t.hist_name = "sub_leading_pt"
tmp_value_t.hist_title = "Sub-Leading Lepton Pt"
tmp_value_t.hist_para = [10,None,0,200]
tmp_value_t.x_label = ['P_{T}^{subleading lepton} (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 20 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("sub_leading_eta")
tmp_value_t.branch_name = "sub_leading_eta"
tmp_value_t.hist_name = "sub_leading_eta"
tmp_value_t.hist_title = "sub_Leading Lepton #eta"
tmp_value_t.hist_para = [10,None,-2.5,2.5]
tmp_value_t.x_label = ['#eta^{subleading lepton}',0.1]
tmp_value_t.y_label = ['Event / 0.5',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("sub_leading_phi")
tmp_value_t.branch_name = "sub_leading_phi"
tmp_value_t.hist_name = "sub_leading_phi"
tmp_value_t.hist_title = "sub-Leading Lepton #phi"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['#phi^{subleading lepton}',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_pt")
tmp_value_t.branch_name = "MET_FinalCollection_Pt"
tmp_value_t.hist_name = "MET_Pt"
tmp_value_t.hist_title = "MET Pt"
tmp_value_t.hist_para = [20,None,0,120]
tmp_value_t.x_label = ['MET (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 6 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_phi")
tmp_value_t.branch_name = "MET_FinalCollection_phi"
tmp_value_t.hist_name = "MET_phi"
tmp_value_t.hist_title = "MET #phi"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['MET_{#phi}',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_significance")
tmp_value_t.branch_name = "MET_FinalCollection_significance"
tmp_value_t.hist_name = "MET_significance"
tmp_value_t.hist_title = "MET significance"
tmp_value_t.hist_para = [10,None,0,20]
tmp_value_t.x_label = ['MET_{significance}',0.1]
tmp_value_t.y_label = ['Event / 2',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_pt_corr")
tmp_value_t.branch_name = "MET_OfflineCorrect_Pt"
tmp_value_t.hist_name = "MET_pt_corr"
tmp_value_t.hist_title = "MET Pt"
tmp_value_t.hist_para = [20,None,0,120]
tmp_value_t.x_label = ['MET Offline Corr (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 6 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_phi_corr")
tmp_value_t.branch_name = "MET_OfflineCorrect_phi"
tmp_value_t.hist_name = "MET_phi_corr"
tmp_value_t.hist_title = "MET #phi"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['MET_{#phi} Offline Corr',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_T1Txy_pt")
tmp_value_t.branch_name = "MET_T1Txy_Pt"
tmp_value_t.hist_name = "MET_T1Txy_Pt"
tmp_value_t.hist_title = "MET T1Txy Pt"
tmp_value_t.hist_para = [20,None,0,120]
tmp_value_t.x_label = ['MET^{T1Txy} (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 6 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_T1Txy_phi")
tmp_value_t.branch_name = "MET_T1Txy_phi"
tmp_value_t.hist_name = "MET_T1Txy_phi"
tmp_value_t.hist_title = "MET T1Txy #phi"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['MET^{T1Txy}_{#phi}',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("Z_MET_T1Txy_delta_phi")
tmp_value_t.branch_name = "MET_T1Txy_phi"
tmp_value_t.hist_name = "Z_MET_T1Txy_delta_phi"
tmp_value_t.hist_title = "MET T1Txy #phi"
tmp_value_t.hist_para = [10,None,0,3.5]
tmp_value_t.x_label = ['#delta #phi(MET^{T1Txy},ll)',0.1]
tmp_value_t.y_label = ['Event / 0.35',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("MET_T1Txy_significance")
tmp_value_t.branch_name = "MET_T1Txy_significance"
tmp_value_t.hist_name = "MET_T1Txy_significance"
tmp_value_t.hist_title = "MET T1Txy significance"
tmp_value_t.hist_para = [10,None,0,20]
tmp_value_t.x_label = ['MET^{T1Txy}_{significance}',0.1]
tmp_value_t.y_label = ['Event / 2',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("rho")
tmp_value_t.branch_name = "ev_fixedGridRhoAll"
tmp_value_t.hist_name = "rho_all"
tmp_value_t.hist_title = "ev_fixedGridRhoAll"
tmp_value_t.hist_para = [10,None,0,50]
tmp_value_t.x_label = ['#rho',0.1]
tmp_value_t.y_label = ['Event / 5',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_jet")
tmp_value_t.branch_name = "n_jet"
tmp_value_t.hist_name = "n_jet"
tmp_value_t.hist_title = "Jet Multiplicity"
tmp_value_t.hist_para = [10,None,0,10]
tmp_value_t.x_label = ['N_{jet}',0.1]
tmp_value_t.y_label = ['Event / 1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_bjet")
tmp_value_t.branch_name = "n_bjet"
tmp_value_t.hist_name = "n_bjet"
tmp_value_t.hist_title = "Jet Multiplicity"
tmp_value_t.hist_para = [6,None,0,6]
tmp_value_t.x_label = ['N_{b jet}',0.1]
tmp_value_t.y_label = ['Event / 1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_bjet2")
tmp_value_t.hist_name = "n_bjet2"
tmp_value_t.hist_title = "Jet Multiplicity"
tmp_value_t.hist_para = [6,None,0,6]
tmp_value_t.x_label = ['N_{b jet} (p_{T} in [20,30])',0.1]
tmp_value_t.y_label = ['Event / 1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_fjet1")
tmp_value_t.hist_name = "n_fjet1"
tmp_value_t.hist_title = "Jet Multiplicity"
tmp_value_t.hist_para = [6,None,0,6]
tmp_value_t.x_label = ['N_{jet} (p_{T} > 30, |#eta| in [2.4,5.2])',0.1]
tmp_value_t.y_label = ['Event / 1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_fjet2")
tmp_value_t.hist_name = "n_fjet2"
tmp_value_t.hist_title = "Jet Multiplicity"
tmp_value_t.hist_para = [6,None,0,6]
tmp_value_t.x_label = ['N_{jet} (p_{T} > 40, |#eta| in [2.4,5.2])',0.1]
tmp_value_t.y_label = ['Event / 1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_jet_bjet")
tmp_value_t.hist_name = "n_jet_bjet"
tmp_value_t.hist_title = "Jet Multiplicity"
tmp_value_t.hist_para = [len(n_jet_bjet_dic),None,0,len(n_jet_bjet_dic)]
tmp_value_t.x_label = ['N_{(jet, b jet)}',0.1]
tmp_value_t.y_label = ['Event / 1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_jet_bjet2")
tmp_value_t.hist_name = "n_jet_bjet2"
tmp_value_t.hist_title = "Jet Multiplicity"
tmp_value_t.hist_para = [len(n_jet_bjet_dic2),None,0,len(n_jet_bjet_dic2)]
tmp_value_t.x_label = ['N_{(jet, b jet)}',0.1]
tmp_value_t.y_label = ['Event / 1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_leading_pt")
tmp_value_t.hist_name = "jet_leading_pt"
tmp_value_t.hist_title = "Leading Jet Pt"
tmp_value_t.hist_para = [10,None,0,200]
tmp_value_t.x_label = ['P_{T}^{leading jet} (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 20 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_leading_eta")
tmp_value_t.hist_name = "jet_leading_eta"
tmp_value_t.hist_title = "Leading Jet #eta"
tmp_value_t.hist_para = [10,None,-2.5,2.5]
tmp_value_t.x_label = ['#eta^{leading jet}',0.1]
tmp_value_t.y_label = ['Event / 0.5',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_leading_phi")
tmp_value_t.hist_name = "jet_leading_phi"
tmp_value_t.hist_title = "Leading Jet #phi"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['#phi^{leading jet}',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_leading_CSV")
tmp_value_t.hist_name = "jet_leading_CSV"
tmp_value_t.hist_title = "Leading Jet scv"
tmp_value_t.hist_para = [10,None,0,1.0]
tmp_value_t.x_label = ['CSV^{leading jet}',0.1]
tmp_value_t.y_label = ['Event / 0.1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_sub_leading_pt")
tmp_value_t.hist_name = "jet_sub_leading_pt"
tmp_value_t.hist_title = "Sub-Leading Jet Pt"
tmp_value_t.hist_para = [10,None,0,200]
tmp_value_t.x_label = ['P_{T}^{subleading jet} (GeV/c)',0.1]
tmp_value_t.y_label = ['Event / 20 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_sub_leading_eta")
tmp_value_t.hist_name = "jet_sub_leading_eta"
tmp_value_t.hist_title = "sub_Leading Jet #eta"
tmp_value_t.hist_para = [10,None,-2.5,2.5]
tmp_value_t.x_label = ['#eta^{subleading jet}',0.1]
tmp_value_t.y_label = ['Event / 0.5',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_sub_leading_phi")
tmp_value_t.hist_name = "jet_sub_leading_phi"
tmp_value_t.hist_title = "sub-Leading Jet #phi"
tmp_value_t.hist_para = [10,None,-3.5,3.5]
tmp_value_t.x_label = ['#phi^{subleading jet}',0.1]
tmp_value_t.y_label = ['Event / 0.7',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("jet_sub_leading_CSV")
tmp_value_t.hist_name = "jet_sub_leading_CSV"
tmp_value_t.hist_title = "sub-Leading Jet scv"
tmp_value_t.hist_para = [10,None,0,1.0]
tmp_value_t.x_label = ['CSV^{subleading jet}',0.1]
tmp_value_t.y_label = ['Event / 0.1',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("HT")
tmp_value_t.hist_name = "Ht"
tmp_value_t.hist_title = "Ht"
tmp_value_t.hist_para = [20,None,0,2000]
tmp_value_t.x_label = ['HT (GeV)',0.1]
tmp_value_t.y_label = ['Event / 10 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("HT_log")
tmp_value_t.hist_name = "Ht_log"
tmp_value_t.hist_title = "Ht"
tmp_value_t.hist_para = [20,None,0,2000]
tmp_value_t.x_label = ['HT (GeV)',0.1]
tmp_value_t.y_label = ['Event / 10 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("sys_HT")
tmp_value_t.hist_name = "sys_Ht"
tmp_value_t.hist_title = "sys Ht"
tmp_value_t.hist_para = [20,None,0,2000]
tmp_value_t.x_label = ['HT^{sys} (GeV)',0.1]
tmp_value_t.y_label = ['Event / 10 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("sys_HT_log")
tmp_value_t.hist_name = "sys_Ht_log"
tmp_value_t.hist_title = "sys Ht"
tmp_value_t.hist_para = [20,None,0,2000]
tmp_value_t.x_label = ['HT^{sys} (GeV)',0.1]
tmp_value_t.y_label = ['Event / 10 GeV',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("pv_n")
tmp_value_t.branch_name = "pv_n"
tmp_value_t.hist_name = "N_vtx_PU"
tmp_value_t.hist_title = "Number of vertex (with PU reweight)"
tmp_value_t.hist_para = [100,None,0,100]
tmp_value_t.x_label = ['N_{vtx}',0.1]
tmp_value_t.y_label = ['Event ',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("pv_n_noPU")
tmp_value_t.branch_name = "pv_n"
tmp_value_t.hist_name = "N_vtx_noPU"
tmp_value_t.hist_title = "Number of vertex (without PU reweight)"
tmp_value_t.PU_reweight= False
tmp_value_t.hist_para = [100,None,0,100]
tmp_value_t.x_label = ['N_{vtx}^{no PU}',0.1]
tmp_value_t.y_label = ['Event ',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t

tmp_value_t = value_t("n_stat")
tmp_value_t.branch_name = "pv_n"
tmp_value_t.hist_name = "N_stat"
tmp_value_t.hist_title = ""
tmp_value_t.hist_para = [1,None,0,1]
tmp_value_t.x_label = ['N_stat',0.1]
tmp_value_t.y_label = ['Event ',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t
# put TMVA in the last, make sure all needed variables are constructed correctly in each event loop


tmp_value_t = value_t("TMVA_MLP")
tmp_value_t.hist_name = "TMVA_MLP"
tmp_value_t.hist_title = ""
tmp_value_t.hist_para = [10,None,0,1]
tmp_value_t.x_label = ['MLP',0.1]
tmp_value_t.y_label = ['Event ',0.05]
pre_value_dic[tmp_value_t.label] = tmp_value_t