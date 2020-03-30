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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pre_plot_dic=collections.OrderedDict()
pre_plot_dic["compare_1"] = collections.OrderedDict()
pre_plot_dic["compare_2"] = collections.OrderedDict()
pre_plot_dic["compare_3"] = collections.OrderedDict()

pre_plot_dic_ss=collections.OrderedDict()
pre_plot_dic_ss["compare_1"] = collections.OrderedDict()
pre_plot_dic_ss["compare_2"] = collections.OrderedDict()

pre_value_dic=collections.OrderedDict()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#pre_plot_dic["compare_3"]["ZPrimeToEMu_M900"] = {
#	"data_list":["_ZPrimeToEMu_M900"],
#	"color":12,
#	"legend_title":"none",
#	"line_style":3,
#	"N_total":0.0,
#	"hist":{},
#	"ABS":False,
#	}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
pre_input_dic = {}
pre_input_dic["data"] = {
		"isFromRoot":True,
		"input_file":"data_2016_EMu.root",
		"isData":True,
		"isFake":False,
		"isSS":False,
		"useToNorm":True,
		"lumi":35868,
		"Xsection":1000.0,
		"N_total": 0.0,
		"Raw_total":1.0,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":38,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}

if QCD_JET_BKG_TYPE == "same sign":
	pre_input_dic["ss_data"] = {
		"isFromRoot":True,
		"input_file":"data_2016_EMu.root",
		"isData":True,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0,
		"Xsection":1000.0,
		"N_total": 0.0,
		"Raw_total":1.0,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":38,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}

#pre_input_dic["_ZPrimeToEMu_M5000"] = {
#        "isFromRoot":True,
#        "input_file":"ZPrimeToEMu_M5000.root",
#        "isData":False,
#        "isFake":False,
#        "useToNorm":False,
#        "lumi":0.0,
#        "Xsection":xsection_ZPrimeToEMu_M5000,
#        "N_total": 0.0,
#        "Raw_total":15000.0,
#        "N_norm":1.0,
#        "Norm_Factor":1,
#        "Fill_color":30,
#        "weight_factor":1,
#        "hist":{},
#        "isUpdate":isUpdate
#        }