from dependencies import *
from input_setting import *

Muon50_trig_fire = True
TkMu50_trig_fire = True
OldMu100_trig_fire = False
Ele115_trig_fire = False
Photon175_trig_fire = True

#Cross sections:
xsection_ttbar2l2u = 87.31
xsection_ttbar2l2u_M500to800 = 0.326
xsection_ttbar2l2u_M800to1200 = 0.0326
xsection_ttbar2l2u_M1200to1800 = 0.00305
xsection_ttbar2l2u_M1800toInf = 0.000174

xsection_WW2l2u = 12.178
xsection_WW2l2u_M200to600 = 1.39
xsection_WW2l2u_M600to1200 = 0.057
xsection_WW2l2u_M1200to2500 = 0.0036
xsection_WW2l2u_M2500toInf = 0.000054

xsection_DYToLL = 5765.4
xsection_WZ = 47.13
xsection_ZZ = 16.523
xsection_ST = 19.47 + 19.47

#N raw event:
nrawevent_ttbar2l2u = 79140880
nrawevent_ttbar2l2u_M500to800 = 200000
nrawevent_ttbar2l2u_M800to1200 = 199800
nrawevent_ttbar2l2u_M1200to1800 = 200000
nrawevent_ttbar2l2u_M1800toInf = 40829

nrawevent_WW2l2u = 1999000
nrawevent_WW2l2u_M200to600 = 200000
nrawevent_WW2l2u_M600to1200 = 200000
nrawevent_WW2l2u_M1200to2500 = 200000
nrawevent_WW2l2u_M2500toInf = 38969

nrawevent_DYToLL = 29137162
nrawevent_WZ = 3997571
nrawevent_ZZ = 1988098
nrawevent_ST = 8681541 + 8681495

pre_plot_dic={}
pre_plot_dic["compare_1"] = {}

pre_plot_dic["compare_1"]["data"] = {
					"data_list":["data"],
					"color":1,
					"legend_title":"Data (2016)",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}

pre_plot_dic["compare_2"] = {}

pre_plot_dic["compare_2"]["_ttbar"] = {
					"data_list":["_ttbar2l2u", "_ttbar2l2u_M500to800", "_ttbar2l2u_M800to1200", "_ttbar2l2u_M1200to1800", "_ttbar2l2u_M1800toInf"],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_2"]["Z"] = {
					"data_list":['_DYToLL'],
					"color":ROOT.kBlue-3,
					"legend_title":"DY",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_2"]["ST"] = {
					"data_list":['_ST'],
					"color":ROOT.kGreen,
					"legend_title":"Single top",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
pre_plot_dic["compare_2"]["Di_boson"] = {
					"data_list":['_WW2l2u', '_WW2l2u_M200to600', '_WW2l2u_M600to1200', '_WW2l2u_M1200to2500', '_WW2l2u_M2500toInf', '_WZ', '_ZZ'],
					"color":ROOT.kOrange-3,
					"legend_title":"Diboson",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}
			#----fke jet----
if QCD_JET_BKG_TYPE == "fake rate":
	pre_plot_dic["compare_2"]["qcd_jet"] = {"data_list":['fke_data','fke_ttbar2l2u','fke_ttbar2l2u_M500to800','fke_ttbar2l2u_M800to1200','fke_ttbar2l2u_M1200to1800','fke_ttbar2l2u_M1800toInf','fke_ST','fke_WW2l2u','fke_WW2l2u_M200to600','fke_WW2l2u_M600to1200','fke_WW2l2u_M1200to2500','fke_WW2l2u_M2500toInf','fke_WZ','fke_ZZ','fke_DYToLL','fkm_data','fkm_ttbar2l2u','fkm_ttbar2l2u_M500to800','fkm_ttbar2l2u_M800to1200','fkm_ttbar2l2u_M1200to1800','fkm_ttbar2l2u_M1800toInf','fkm_ST','fkm_WW2l2u','fkm_WW2l2u_M200to600','fkm_WW2l2u_M600to1200','fkm_WW2l2u_M1200to2500','fkm_WW2l2u_M2500toInf','fkm_WZ','fkm_ZZ','fkm_DYToLL'],					"color":ROOT.kYellow,
					"legend_title":"Fake ele + muon",
					"N_total":0.0,
					"hist":{},
					"ABS":True,
					"weight_factor":1,
					}
if QCD_JET_BKG_TYPE == "same sign":
	pre_plot_dic["compare_2"]["qcd_jet"] = {
					"data_list":['ss_data','ss_ttbar2l2u','ss_ttbar2l2u_M500to800','ss_ttbar2l2u_M800to1200','ss_ttbar2l2u_M1200to1800','ss_ttbar2l2u_M1800toInf','ss_ST','ss_WW2l2u','ss_WW2l2u_M200to600','ss_WW2l2u_M600to1200','ss_WW2l2u_M1200to2500','ss_WW2l2u_M2500toInf','ss_WZ','ss_ZZ','ss_DYToLL'],
					"color":ROOT.kYellow,
					"legend_title":"Same sign",
					"N_total":0.0,
					"hist":{},
					"ABS":True,
					"weight_factor":2,
					}

pre_plot_dic["compare_3"] = {}


pre_plot_dic["compare_3"]["QBHtoEMu_M200"] = {
	"data_list":["_QBHtoEMu_M200"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M400"] = {
	"data_list":["_QBHtoEMu_M400"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M600"] = {
	"data_list":["_QBHtoEMu_M600"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M800"] = {
	"data_list":["_QBHtoEMu_M800"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M1000"] = {
	"data_list":["_QBHtoEMu_M1000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M1200"] = {
	"data_list":["_QBHtoEMu_M1200"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M1400"] = {
	"data_list":["_QBHtoEMu_M1400"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M1600"] = {
	"data_list":["_QBHtoEMu_M1600"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M1800"] = {
	"data_list":["_QBHtoEMu_M1800"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M2000"] = {
	"data_list":["_QBHtoEMu_M2000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M2500"] = {
	"data_list":["_QBHtoEMu_M2500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M3000"] = {
	"data_list":["_QBHtoEMu_M3000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M3500"] = {
	"data_list":["_QBHtoEMu_M3500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M4000"] = {
	"data_list":["_QBHtoEMu_M4000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M4500"] = {
	"data_list":["_QBHtoEMu_M4500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M5000"] = {
	"data_list":["_QBHtoEMu_M5000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M5500"] = {
	"data_list":["_QBHtoEMu_M5500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M6000"] = {
	"data_list":["_QBHtoEMu_M6000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M7000"] = {
	"data_list":["_QBHtoEMu_M7000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M8000"] = {
	"data_list":["_QBHtoEMu_M8000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M9000"] = {
	"data_list":["_QBHtoEMu_M9000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["QBHtoEMu_M10000"] = {
	"data_list":["_QBHtoEMu_M10000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M200"] = {
	"data_list":["_RPVresonantToEMu_M200"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M300"] = {
	"data_list":["_RPVresonantToEMu_M300"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M400"] = {
	"data_list":["_RPVresonantToEMu_M400"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M500"] = {
	"data_list":["_RPVresonantToEMu_M500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M600"] = {
	"data_list":["_RPVresonantToEMu_M600"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M700"] = {
	"data_list":["_RPVresonantToEMu_M700"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M800"] = {
	"data_list":["_RPVresonantToEMu_M800"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M900"] = {
	"data_list":["_RPVresonantToEMu_M900"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M1000"] = {
	"data_list":["_RPVresonantToEMu_M1000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M1200"] = {
	"data_list":["_RPVresonantToEMu_M1200"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M1400"] = {
	"data_list":["_RPVresonantToEMu_M1400"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M1600"] = {
	"data_list":["_RPVresonantToEMu_M1600"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M1800"] = {
	"data_list":["_RPVresonantToEMu_M1800"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M2000"] = {
	"data_list":["_RPVresonantToEMu_M2000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M2500"] = {
	"data_list":["_RPVresonantToEMu_M2500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M3000"] = {
	"data_list":["_RPVresonantToEMu_M3000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M3500"] = {
	"data_list":["_RPVresonantToEMu_M3500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M4000"] = {
	"data_list":["_RPVresonantToEMu_M4000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M4500"] = {
	"data_list":["_RPVresonantToEMu_M4500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M5000"] = {
	"data_list":["_RPVresonantToEMu_M5000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M5500"] = {
	"data_list":["_RPVresonantToEMu_M5500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M6000"] = {
	"data_list":["_RPVresonantToEMu_M6000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["RPVresonantToEMu_M6500"] = {
	"data_list":["_RPVresonantToEMu_M6500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1000"] = {
	"data_list":["_ZPrimeToEMu_M1000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1100"] = {
	"data_list":["_ZPrimeToEMu_M1100"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1200"] = {
	"data_list":["_ZPrimeToEMu_M1200"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1300"] = {
	"data_list":["_ZPrimeToEMu_M1300"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1400"] = {
	"data_list":["_ZPrimeToEMu_M1400"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1500"] = {
	"data_list":["_ZPrimeToEMu_M1500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1600"] = {
	"data_list":["_ZPrimeToEMu_M1600"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1700"] = {
	"data_list":["_ZPrimeToEMu_M1700"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1800"] = {
	"data_list":["_ZPrimeToEMu_M1800"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M1900"] = {
	"data_list":["_ZPrimeToEMu_M1900"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M2000"] = {
	"data_list":["_ZPrimeToEMu_M2000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M2200"] = {
	"data_list":["_ZPrimeToEMu_M2200"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M2400"] = {
	"data_list":["_ZPrimeToEMu_M2400"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M2600"] = {
	"data_list":["_ZPrimeToEMu_M2600"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M2800"] = {
	"data_list":["_ZPrimeToEMu_M2800"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M3000"] = {
	"data_list":["_ZPrimeToEMu_M3000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M3500"] = {
	"data_list":["_ZPrimeToEMu_M3500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M4000"] = {
	"data_list":["_ZPrimeToEMu_M4000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M4500"] = {
	"data_list":["_ZPrimeToEMu_M4500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M5000"] = {
	"data_list":["_ZPrimeToEMu_M5000"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M500"] = {
	"data_list":["_ZPrimeToEMu_M500"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M600"] = {
	"data_list":["_ZPrimeToEMu_M600"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M700"] = {
	"data_list":["_ZPrimeToEMu_M700"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M800"] = {
	"data_list":["_ZPrimeToEMu_M800"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}
pre_plot_dic["compare_3"]["ZPrimeToEMu_M900"] = {
	"data_list":["_ZPrimeToEMu_M900"],
	"color":12,
	"legend_title":"none",
	"line_style":3,
	"N_total":0.0,
	"hist":{},
	"ABS":False,
	}


pre_plot_dic_ss={
"compare_1":{"data":{
					"data_list":["ss_data"],
					"color":1,
					"legend_title":"Data (2016)",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}		
			},
"compare_2":{
			"_ttbar":{
					"data_list":['ss_ttbar2l2u','ss_ttbar2l2u_M500to800','ss_ttbar2l2u_M800to1200','ss_ttbar2l2u_M1200to1800','ss_ttbar2l2u_M1800toInf'],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Z":{
					"data_list":['ss_DYToLL'],
					"color":ROOT.kBlue-3,
					"legend_title":"DY",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"ST":{
					"data_list":['ss_ST'],
					"color":ROOT.kGreen,
					"legend_title":"Single top",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Di_boson":{
					"data_list":['ss_WW2l2u','ss_WW2l2u_M200to600','ss_WW2l2u_M600to1200','ss_WW2l2u_M1200to2500','ss_WW2l2u_M2500toInf', 'ss_WZ', 'ss_ZZ'],
					"color":ROOT.kOrange-3,
					"legend_title":"Diboson",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			},
}

pre_plot_dic_fke={
"compare_1":{"data":{
					"data_list":["fke_data"],
					"color":1,
					"legend_title":"Data (2016)",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}		
			},
"compare_2":{
			"_ttbar":{
					"data_list":['fke_ttbar2l2u','fke_ttbar2l2u_M500to800','fke_ttbar2l2u_M800to1200','fke_ttbar2l2u_M1200to1800','fke_ttbar2l2u_M1800toInf'],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Z":{
					"data_list":['fke_DYToLL'],
					"color":ROOT.kBlue-3,
					"legend_title":"DY",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"ST":{
					"data_list":['fke_ST'],
					"color":ROOT.kGreen,
					"legend_title":"Single top",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Di_boson":{
					"data_list":['fke_WW2l2u','fke_WW2l2u_M200to600','fke_WW2l2u_M600to1200','fke_WW2l2u_M1200to2500','fke_WW2l2u_M2500toInf', 'fke_WZ', 'fke_ZZ'],
					"color":ROOT.kOrange-3,
					"legend_title":"Diboson",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			},
}

pre_plot_dic_fkm={
"compare_1":{"data":{
					"data_list":["fkm_data"],
					"color":1,
					"legend_title":"Data (2017)",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}		
			},
"compare_2":{
			"_ttbar":{
					"data_list":['fkm_ttbar2l2u','fkm_ttbar2l2u_M500to800','fkm_ttbar2l2u_M800to1200','fkm_ttbar2l2u_M1200to1800','fkm_ttbar2l2u_M1800toInf'],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Z":{
					"data_list":['fkm_DYToLL'],
					"color":ROOT.kBlue-3,
					"legend_title":"DY",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"ST":{
					"data_list":['fkm_ST'],
					"color":ROOT.kGreen,
					"legend_title":"Single top",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Di_boson":{
					"data_list":['fkm_WW2l2u','fkm_WW2l2u_M200to600','fkm_WW2l2u_M600to1200','fkm_WW2l2u_M1200to2500','fkm_WW2l2u_M2500toInf', 'fkm_WZ', 'fkm_ZZ'],
					"color":ROOT.kOrange-3,
					"legend_title":"Diboson",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			},
}

pre_plot_dic_fk={
"compare_1":{"data":{
					"data_list":["fke_data", "fkm_data"],
					"color":1,
					"legend_title":"Data (2016)",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					}		
			},
"compare_2":{
			"_ttbar":{
					"data_list":['fke_ttbar2l2u','fke_ttbar2l2u_M500to800','fke_ttbar2l2u_M800to1200','fke_ttbar2l2u_M1200to1800','fke_ttbar2l2u_M1800toInf', 'fkm_ttbar2l2u','fkm_ttbar2l2u_M500to800','fkm_ttbar2l2u_M800to1200','fkm_ttbar2l2u_M1200to1800','fkm_ttbar2l2u_M1800toInf'],
					"color":ROOT.kRed-4,
					"legend_title":"t#bar{t}",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Z":{
					"data_list":['fke_DYToLL', 'fkm_DYToLL'],
					"color":ROOT.kBlue-3,
					"legend_title":"DY",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"ST":{
					"data_list":['fke_ST', 'fkm_ST'],
					"color":ROOT.kGreen,
					"legend_title":"Single top",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			"Di_boson":{
					"data_list":['fke_WW2l2u','fke_WW2l2u_M200to600','fke_WW2l2u_M600to1200','fke_WW2l2u_M1200to2500','fke_WW2l2u_M2500toInf', 'fke_WZ', 'fke_ZZ', 'fkm_WW2l2u','fkm_WW2l2u_M200to600','fkm_WW2l2u_M600to1200','fkm_WW2l2u_M1200to2500','fkm_WW2l2u_M2500toInf', 'fkm_WZ', 'fkm_ZZ'],
					"color":ROOT.kOrange-3,
					"legend_title":"Diboson",
					"N_total":0.0,
					"hist":{},
					"ABS":False,
					},
			},
}
#def getP4_ele(Et, eta, phi):
#	p4 = ROOT.TLorentzVector()
#	p4.SetPtEtaPhiM(Et,eta,phi,0.000511)
#	return p4
#
#def getP4_muon(pt, eta, phi):
#	p4 = ROOT.TLorentzVector()
#	p4.SetPtEtaPhiM(pt,eta,phi,0.10566)
#	return p4
#
#def getbinwidth(x,x1):
#	for i in range(len(x1)):
#		if x < x1[i] and i>0:
#			return (x1[i]-x1[i-1])
#		elif x < x1[i]:
#			return -1.0
#	return -1.0
#
#def map_value(path, event, h1, tmp_value_dic, event_weight_factor):
#	pi = 3.1415926
#	bin_weight = 1.0
#	if path == "":
#		return
#	elif path == "Pt_ll":
#		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
#		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
#		tmp_pt = (tmp_ele_p4 + tmp_muon_p4).Pt()
#		#print tmp_pt
#		if tmp_pt < 259:
#			h1.Fill(tmp_pt,event_weight_factor)
#		else:
#			h1.Fill(259,event_weight_factor)
#	elif path == "rapidity_ll":
#		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
#		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
#		tmp_rapidity = (tmp_ele_p4 + tmp_muon_p4).Rapidity()
#		h1.Fill(tmp_rapidity,event_weight_factor)
#	elif path == "phi_ll":
#		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
#		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
#		tmp_phi = (tmp_ele_p4 + tmp_muon_p4).Phi()
#		h1.Fill(tmp_phi,event_weight_factor)
#	elif path == "deltaR_ll":
#		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
#		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
#		tmp_dR = tmp_ele_p4.DeltaR(tmp_muon_p4)
#		h1.Fill(tmp_dR,event_weight_factor)
#	elif path == "delta_eta_ll":
#		delta_eta = fabs(getattr(event, "ele_eta") - getattr(event, "muon_eta"))
#		h1.Fill(delta_eta,event_weight_factor)
#	elif path == "delta_phi_ll":
#		delta_phi = fabs(getattr(event, "ele_phi") - getattr(event, "muon_phi"))
#		if delta_phi > pi:delta_phi = 2*pi - delta_phi
#		h1.Fill(delta_phi,event_weight_factor)
#	elif path == "n_jet_bjet":
#		n_jet = getattr(event,"n_jet")
#		n_bjet = getattr(event,"n_bjet")
#		if n_jet <=4:
#			h1.Fill(n_jet_bjet_dic["(%s,%s)"%(n_jet,n_bjet)][0],event_weight_factor)
#		else:
#			h1.Fill(n_jet_bjet_dic["(>4,n)"][0],event_weight_factor)
#	elif path == "HT":
#		tmp_HT = 0
#		jet_pt_vector = getattr(event,"jet_pt")
#		jet_eta_vector = getattr(event,"jet_eta")
#		#jet_ID_vector = getattr(event,"jet_IDLoose")
#		jet_pass_vector = getattr(event,"jet_passed")
#		for i in range(len(jet_pt_vector)):
#			if jet_pass_vector[i]:
#				tmp_HT += jet_pt_vector[i]
#		#if tmp_HT == 0:return
#		if tmp_HT > 500:
#			h1.Fill(499,event_weight_factor)
#		else:
#			h1.Fill(tmp_HT,event_weight_factor)
#	elif path == "sys_HT":
#		tmp_HT = 0
#		jet_pt_vector = getattr(event,"jet_pt")
#		jet_eta_vector = getattr(event,"jet_eta")
#		jet_pass_vector = getattr(event,"jet_passed")
#		#jet_ID_vector = getattr(event,"jet_IDLoose")
#		for i in range(len(jet_pt_vector)):
#			#if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
#			if jet_pass_vector[i]:
#				tmp_HT += jet_pt_vector[i]
#		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
#		tmp_HT += tmp_ele_p4.Pt() + getattr(event,"muon_pt")
#		#if tmp_HT == 0:return
#		if tmp_HT > 500:
#			h1.Fill(499,event_weight_factor)
#		else:
#			h1.Fill(tmp_HT,event_weight_factor)
#	elif path == "n_stat":
#		h1.Fill(0.5, event_weight_factor)
#	else:
#		for value in tmp_value_dic:
#			exec 'passed = (%s)'%(tmp_value_dic[value])
#			if not passed: continue 
#			#print "passed"
#			bin_weight = 1.0
#			if value_dic[path]["use_array"]:
#				bin_weight = 1.0/getbinwidth(getattr(event,value),value_dic[path]["hist_para"][1])
#			total_weight = event_weight_factor * bin_weight
#			h1.Fill(getattr(event,value),total_weight)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
pre_input_dic = {}
pre_input_dic["data"] = {
		"isFromRoot":True,
		"input_file":"data_2016_all.root",
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
pre_input_dic["_ttbar2l2u"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_Mall.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ttbar2l2u_M500to800"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M500to800.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M500to800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M500to800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ttbar2l2u_M800to1200"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M800to1200.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M800to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M800to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ttbar2l2u_M1200to1800"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M1200to1800.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1200to1800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1200to1800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ttbar2l2u_M1800toInf"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M1800toInf.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1800toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1800toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_DYToLL"] = {
		"isFromRoot":True,
		"input_file":"DYToLL_all.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_DYToLL,
		"N_total": 0.0,
		"Raw_total":nrawevent_DYToLL,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_WW2l2u"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_WW2l2u_M200to600"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M200to600.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M200to600,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M200to600,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_WW2l2u_M600to1200"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M600to1200.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M600to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M600to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_WW2l2u_M1200to2500"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M1200to2500.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M1200to2500,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M1200to2500,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_WW2l2u_M2500toInf"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M2500toInf.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M2500toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M2500toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_WZ"] = {
		"isFromRoot":True,
		"input_file":"WZ.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ZZ"] = {
		"isFromRoot":True,
		"input_file":"ZZ.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ST"] = {
		"isFromRoot":True,
		"input_file":"ST.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ST,
		"N_total": 0.0,
		"Raw_total":nrawevent_ST,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}

if QCD_JET_BKG_TYPE == "same sign":
	pre_input_dic["ss_data"] = {
		"isFromRoot":True,
		"input_file":"data_2016_all.root",
		"isData":True,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":43867,
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
	pre_input_dic["ss_ttbar2l2u"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_Mall.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ttbar2l2u_M500to800"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M500to800.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M500to800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M500to800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ttbar2l2u_M800to1200"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M800to1200.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M800to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M800to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ttbar2l2u_M1200to1800"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M1200to1800.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1200to1800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1200to1800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ttbar2l2u_M1800toInf"] = {
		"isFromRoot":True,
		"input_file":"ttbar2l2u_M1800toInf.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1800toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1800toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_DYToLL"] = {
		"isFromRoot":True,
		"input_file":"DYToLL_all.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_DYToLL,
		"N_total": 0.0,
		"Raw_total":nrawevent_DYToLL,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_WW2l2u"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_WW2l2u_M200to600"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M200to600.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M200to600,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M200to600,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_WW2l2u_M600to1200"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M600to1200.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M600to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M600to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_WW2l2u_M1200to2500"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M1200to2500.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M1200to2500,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M1200to2500,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_WW2l2u_M2500toInf"] = {
		"isFromRoot":True,
		"input_file":"WW2l2u_M2500toInf.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M2500toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M2500toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_WZ"] = {
		"isFromRoot":True,
		"input_file":"WZ.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ZZ"] = {
		"isFromRoot":True,
		"input_file":"ZZ.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ST"] = {
		"isFromRoot":True,
		"input_file":"ST.root",
		"isData":False,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ST,
		"N_total": 0.0,
		"Raw_total":nrawevent_ST,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}

if QCD_JET_BKG_TYPE == "fake rate":
	pre_input_dic["fke_data"] = {
		"isFromRoot":True,
		"input_file":"fke_data_2016_all.root",
		"isData":True,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":43867,
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
	pre_input_dic["fke_ttbar2l2u"] = {
		"isFromRoot":True,
		"input_file":"fke_ttbar2l2u_Mall.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ttbar2l2u_M500to800"] = {
		"isFromRoot":True,
		"input_file":"fke_ttbar2l2u_M500to800.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M500to800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M500to800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ttbar2l2u_M800to1200"] = {
		"isFromRoot":True,
		"input_file":"fke_ttbar2l2u_M800to1200.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M800to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M800to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ttbar2l2u_M1200to1800"] = {
		"isFromRoot":True,
		"input_file":"fke_ttbar2l2u_M1200to1800.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1200to1800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1200to1800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ttbar2l2u_M1800toInf"] = {
		"isFromRoot":True,
		"input_file":"fke_ttbar2l2u_M1800toInf.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1800toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1800toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_DYToLL"] = {
		"isFromRoot":True,
		"input_file":"fke_DYToLL_all.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_DYToLL,
		"N_total": 0.0,
		"Raw_total":nrawevent_DYToLL,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_WW2l2u"] = {
		"isFromRoot":True,
		"input_file":"fke_WW2l2u.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_WW2l2u_M200to600"] = {
		"isFromRoot":True,
		"input_file":"fke_WW2l2u_M200to600.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M200to600,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M200to600,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_WW2l2u_M600to1200"] = {
		"isFromRoot":True,
		"input_file":"fke_WW2l2u_M600to1200.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M600to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M600to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_WW2l2u_M1200to2500"] = {
		"isFromRoot":True,
		"input_file":"fke_WW2l2u_M1200to2500.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M1200to2500,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M1200to2500,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_WW2l2u_M2500toInf"] = {
		"isFromRoot":True,
		"input_file":"fke_WW2l2u_M2500toInf.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M2500toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M2500toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_WZ"] = {
		"isFromRoot":True,
		"input_file":"fke_WZ.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ZZ"] = {
		"isFromRoot":True,
		"input_file":"fke_ZZ.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ST"] = {
		"isFromRoot":True,
		"input_file":"fke_ST.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ST,
		"N_total": 0.0,
		"Raw_total":nrawevent_ST,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	pre_input_dic["fkm_data"] = {
		"isFromRoot":True,
		"input_file":"fkm_data_2016_all.root",
		"isData":True,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":43867,
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
	pre_input_dic["fkm_ttbar2l2u"] = {
		"isFromRoot":True,
		"input_file":"fkm_ttbar2l2u_Mall.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ttbar2l2u_M500to800"] = {
		"isFromRoot":True,
		"input_file":"fkm_ttbar2l2u_M500to800.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M500to800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M500to800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ttbar2l2u_M800to1200"] = {
		"isFromRoot":True,
		"input_file":"fkm_ttbar2l2u_M800to1200.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M800to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M800to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ttbar2l2u_M1200to1800"] = {
		"isFromRoot":True,
		"input_file":"fkm_ttbar2l2u_M1200to1800.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1200to1800,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1200to1800,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ttbar2l2u_M1800toInf"] = {
		"isFromRoot":True,
		"input_file":"fkm_ttbar2l2u_M1800toInf.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ttbar2l2u_M1800toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_ttbar2l2u_M1800toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_DYToLL"] = {
		"isFromRoot":True,
		"input_file":"fkm_DYToLL_all.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_DYToLL,
		"N_total": 0.0,
		"Raw_total":nrawevent_DYToLL,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_WW2l2u"] = {
		"isFromRoot":True,
		"input_file":"fkm_WW2l2u.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_WW2l2u_M200to600"] = {
		"isFromRoot":True,
		"input_file":"fkm_WW2l2u_M200to600.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M200to600,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M200to600,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_WW2l2u_M600to1200"] = {
		"isFromRoot":True,
		"input_file":"fkm_WW2l2u_M600to1200.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M600to1200,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M600to1200,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_WW2l2u_M1200to2500"] = {
		"isFromRoot":True,
		"input_file":"fkm_WW2l2u_M1200to2500.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M1200to2500,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M1200to2500,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_WW2l2u_M2500toInf"] = {
		"isFromRoot":True,
		"input_file":"fkm_WW2l2u_M2500toInf.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WW2l2u_M2500toInf,
		"N_total": 0.0,
		"Raw_total":nrawevent_WW2l2u_M2500toInf,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_WZ"] = {
		"isFromRoot":True,
		"input_file":"fkm_WZ.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ZZ"] = {
		"isFromRoot":True,
		"input_file":"fkm_ZZ.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZ,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZ,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ST"] = {
		"isFromRoot":True,
		"input_file":"fkm_ST.root",
		"isData":False,
		"isFake":True,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ST,
		"N_total": 0.0,
		"Raw_total":nrawevent_ST,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		}


pre_input_dic["_QBHtoEMu_M200"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M200.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":20676.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M400"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M400.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":17171.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M600"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M600.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":18507.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M800"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M800.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":18664.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M1000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M1000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":18364.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M1200"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M1200.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":26548.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M1400"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M1400.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":20310.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M1600"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M1600.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":20242.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M1800"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M1800.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":20462.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M2000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M2000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":18983.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M2500"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M2500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":20065.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M3000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M3000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":20553.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M3500"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M3500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":20580.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M4000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M4000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":19271.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M4500"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M4500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":18836.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M5000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M5000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":19145.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M5500"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M5500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":21106.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M6000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M6000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":19900.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M7000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M7000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":16978.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M8000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M8000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":19658.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M9000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M9000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":19549.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_QBHtoEMu_M10000"] = {
        "isFromRoot":True,
        "input_file":"QBHtoEMu_M10000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":17811.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M200"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M200.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M300"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M300.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M400"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M400.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M500"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M600"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M600.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M700"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M700.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M800"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M800.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":10000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M900"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M900.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M1000"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M1000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M1200"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M1200.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M1400"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M1400.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M1600"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M1600.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M1800"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M1800.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M2000"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M2000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M2500"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M2500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M3000"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M3000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M3500"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M3500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M4000"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M4000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M4500"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M4500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M5000"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M5000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M5500"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M5500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M6000"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M6000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_RPVresonantToEMu_M6500"] = {
        "isFromRoot":True,
        "input_file":"RPVresonantToEMu_M6500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M500"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M600"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M600.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M700"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M700.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M800"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M800.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":14611.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M900"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M900.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1000"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":14400.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1100"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1100.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1200"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1200.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1300"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1300.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1400"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1400.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1500"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1600"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1600.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":14590.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1700"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1700.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":14489.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1800"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1800.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M1900"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M1900.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M2000"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M2000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M2200"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M2200.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M2400"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M2400.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M2600"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M2600.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":14202.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M2800"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M2800.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M3000"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M3000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M3500"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M3500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":14664.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M4000"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M4000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M4500"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M4500.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

pre_input_dic["_ZPrimeToEMu_M5000"] = {
        "isFromRoot":True,
        "input_file":"ZPrimeToEMu_M5000.root",
        "isData":False,
        "isFake":False,
        "useToNorm":False,
        "lumi":0.0,
        "Xsection":1000.0,
        "N_total": 0.0,
        "Raw_total":15000.0,
        "N_norm":1.0,
        "Norm_Factor":1,
        "Fill_color":30,
        "weight_factor":1,
        "hist":{},
        "isUpdate":isUpdate
        }

