from input_setting import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nevent_DYToLL_10to50 = 78843820
nevent_DYToLL_50 = 80826354
nevent_TTGJets = 4774447 
nevent_TTTo2L2Nu = 79140880
nevent_TTWJetsToLNu = 2716249
nevent_TTWJetsToQQ = 430310
nevent_TTZToLLNuNu_10 = 6420825
nevent_TTZToQQ = 351164 
nevent_WGToLNuG = 17643995 
nevent_WJetsToLNu = 162099279
nevent_WWTo2L2Nu = 1999000
nevent_WZTo2L2Q = 15879472
nevent_WZTo3LNu = 19993200 #XXXXXXXXXXXXXXXXXX
nevent_ZZTo2L2Nu = 8931750
nevent_ZZTo4L = 6669988
nevent_tw = 8681495
nevent_tw_anti = 8536553

nevent_ST_emutc = 500000
nevent_ST_emutu = 500000
nevent_TT_emutc = 500000
nevent_TT_emutu = 500000
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
xsection_DYToLL_10to50 = 18610
xsection_DYToLL_50 = 5765.4
xsection_TTGJets = 3.697
xsection_TTTo2L2Nu = 87.31
xsection_TTWJetsToLNu = 0.2043
xsection_TTWJetsToQQ = 0.4062
xsection_TTZToLLNuNu_10 = 0.2529
xsection_TTZToQQ = 0.5297
xsection_WGToLNuG = 489
xsection_WJetsToLNu = 61526.7
xsection_WWTo2L2Nu = 12.178
xsection_WZTo2L2Q = 5.595
xsection_WZTo3LNu = 4.42965
xsection_ZZTo2L2Nu = 0.564
xsection_ZZTo4L = 1.212
xsection_tw = 19.47
xsection_tw_anti = 19.47

xsection_ST_emutc = 0.0512
xsection_ST_emutu = 0.515
xsection_TT_emutc = 0.032
xsection_TT_emutu = 0.032
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pre_plot_dic=collections.OrderedDict()
pre_plot_dic["compare_1"] = collections.OrderedDict()
pre_plot_dic["compare_2"] = collections.OrderedDict()
pre_plot_dic["compare_3"] = collections.OrderedDict()

pre_plot_dic_ss=collections.OrderedDict()
pre_plot_dic_ss["compare_1"] = collections.OrderedDict()
pre_plot_dic_ss["compare_2"] = collections.OrderedDict()

pre_value_dic=collections.OrderedDict()
pre_input_dic=collections.OrderedDict()

tmp_sample_t = sample_t("data")
tmp_sample_t.input_file = "data_2016_EMu.root"
tmp_sample_t.isData = True
tmp_sample_t.useToNorm = True
tmp_sample_t.lumi = 35920
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

if QCD_JET_BKG_TYPE == "same sign":

	tmp_sample_t = sample_t("ss_data")
	tmp_sample_t.input_file = "data_2016_EMu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.isData = True
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t

# addition signal samples
pre_plot_dic["compare_3"]["ST_emutc"] = {
					"data_list":["ST_emutc"],
					"color":ROOT.kRed-4,
					"line_style":2,
					"legend_title":"ST_{e#mu} tc",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_3"]["ST_emutu"] = {
					"data_list":["ST_emutu"],
					"color":ROOT.kGreen,
					"line_style":2,
					"legend_title":"ST_{e#mu} tc",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_3"]["TT_emutc"] = {
					"data_list":["TT_emutc"],
					"color":ROOT.kBlue,
					"line_style":2,
					"legend_title":"TT_{e#mu} tc",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_3"]["TT_emutu"] = {
					"data_list":["TT_emutu"],
					"color":ROOT.kOrange,
					"line_style":2,
					"legend_title":"TT_{e#mu} tu",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_3"]["sum"] = {
					"data_list":["ST_emutc","ST_emutu","TT_emutc","TT_emutu"],
					"color":ROOT.kBlack,
					"line_style":0,
					"legend_title":"Sum_{e#mu} u&c",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}

tmp_sample_t = sample_t("ST_emutc")
tmp_sample_t.input_file = "ST_vector_emutc.root"
tmp_sample_t.Xsection = xsection_ST_emutc
tmp_sample_t.Raw_total = nevent_ST_emutc
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("ST_emutu")
tmp_sample_t.input_file = "ST_vector_emutu.root"
tmp_sample_t.Xsection = xsection_ST_emutu
tmp_sample_t.Raw_total = nevent_ST_emutu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TT_emutc")
tmp_sample_t.input_file = "TT_vector_emutc.root"
tmp_sample_t.Xsection = xsection_TT_emutc
tmp_sample_t.Raw_total = nevent_TT_emutc
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

tmp_sample_t = sample_t("TT_emutu")
tmp_sample_t.input_file = "TT_vector_emutu.root"
tmp_sample_t.Xsection = xsection_TT_emutu
tmp_sample_t.Raw_total = nevent_TT_emutu
pre_input_dic[tmp_sample_t.label] = tmp_sample_t