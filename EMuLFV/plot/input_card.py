from dependencies import *


pre_para_2016 = {
	"lumi":35823,
	"lumi_sys":0.024,
}


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

nrawevent_WZTo2L2Q = 15879472
nrawevent_WZTo3LNu = 1993200
nrawevent_ZZTo2L2Nu = 8931750
nrawevent_ZZTo2L2Q = 496436
nrawevent_ZZTo4L = 6669988

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
#pre_input_dic["_WZ"] = {
#		"isFromRoot":True,
#		"input_file":"WZ.root",
#		"isData":False,
#		"isFake":False,
#		"isSS":False,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_WZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_WZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
#pre_input_dic["_ZZ"] = {
#		"isFromRoot":True,
#		"input_file":"ZZ.root",
#		"isData":False,
#		"isFake":False,
#		"isSS":False,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_ZZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_ZZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
pre_input_dic["_WZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"WZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_WZTo3LNu"] = {
		"isFromRoot":True,
		"input_file":"WZTo3LNu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo3LNu,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo3LNu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ZZTo2L2Nu"] = {
		"isFromRoot":True,
		"input_file":"ZZTo2L2Nu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Nu,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Nu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ZZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"ZZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
pre_input_dic["_ZZTo4L"] = {
		"isFromRoot":True,
		"input_file":"ZZTo4L.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo4L,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo4L,
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
#	pre_input_dic["ss_WZ"] = {
#		"isFromRoot":True,
#		"input_file":"WZ.root",
#		"isData":False,
#		"isFake":False,
#		"isSS":True,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_WZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_WZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":-1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
#	pre_input_dic["ss_ZZ"] = {
#		"isFromRoot":True,
#		"input_file":"ZZ.root",
#		"isData":False,
#		"isFake":False,
#		"isSS":True,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_ZZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_ZZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":-1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
	pre_input_dic["ss_WZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"WZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_WZTo3LNu"] = {
		"isFromRoot":True,
		"input_file":"WZTo3LNu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo3LNu,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo3LNu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ZZTo2L2Nu"] = {
		"isFromRoot":True,
		"input_file":"ZZTo2L2Nu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Nu,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Nu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ZZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"ZZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["ss_ZZTo4L"] = {
		"isFromRoot":True,
		"input_file":"ZZTo4L.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo4L,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo4L,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
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
#	pre_input_dic["fke_WZ"] = {
#		"isFromRoot":True,
#		"input_file":"fke_WZ.root",
#		"isData":False,
#		"isFake":True,
#		"isSS":False,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_WZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_WZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":-1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
#	pre_input_dic["fke_ZZ"] = {
#		"isFromRoot":True,
#		"input_file":"fke_ZZ.root",
#		"isData":False,
#		"isFake":True,
#		"isSS":False,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_ZZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_ZZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":-1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
	pre_input_dic["fke_WZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"fke_WZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_WZTo3LNu"] = {
		"isFromRoot":True,
		"input_file":"fke_WZTo3LNu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo3LNu,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo3LNu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ZZTo2L2Nu"] = {
		"isFromRoot":True,
		"input_file":"fke_ZZTo2L2Nu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Nu,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Nu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ZZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"fke_ZZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fke_ZZTo4L"] = {
		"isFromRoot":True,
		"input_file":"fke_ZZTo4L.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo4L,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo4L,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
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
#	pre_input_dic["fkm_WZ"] = {
#		"isFromRoot":True,
#		"input_file":"fkm_WZ.root",
#		"isData":False,
#		"isFake":True,
#		"isSS":False,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_WZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_WZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":-1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
#	pre_input_dic["fkm_ZZ"] = {
#		"isFromRoot":True,
#		"input_file":"fkm_ZZ.root",
#		"isData":False,
#		"isFake":True,
#		"isSS":False,
#		"useToNorm":False,
#		"lumi":0.0,
#		"Xsection":xsection_ZZ,
#		"N_total": 0.0,
#		"Raw_total":nrawevent_ZZ,
#		"N_norm":1.0,
#		"Norm_Factor":1,
#		"Fill_color":30,
#		"weight_factor":-1,
#		"hist":{},
#		"isUpdate":isUpdate
#		}
	pre_input_dic["fkm_WZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"fkm_WZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_WZTo3LNu"] = {
		"isFromRoot":True,
		"input_file":"fkm_WZTo3LNu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_WZTo3LNu,
		"N_total": 0.0,
		"Raw_total":nrawevent_WZTo3LNu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ZZTo2L2Nu"] = {
		"isFromRoot":True,
		"input_file":"fkm_ZZTo2L2Nu.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Nu,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Nu,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ZZTo2L2Q"] = {
		"isFromRoot":True,
		"input_file":"fkm_ZZTo2L2Q.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo2L2Q,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo2L2Q,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		}
	pre_input_dic["fkm_ZZTo4L"] = {
		"isFromRoot":True,
		"input_file":"fkm_ZZTo4L.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":xsection_ZZTo4L,
		"N_total": 0.0,
		"Raw_total":nrawevent_ZZTo4L,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x_emu_new = array('f')
n_index = 0
x_emu_new.append(50)
for i in range(50,100,10):
        x_emu_new.append(i)
        n_index += 1
for i in range(100,200,20):
        x_emu_new.append(i)
        n_index += 1
for i in range(200,600,40):
        x_emu_new.append(i)
        n_index += 1
for i in range(600,1000,80):
        x_emu_new.append(i)
        n_index += 1
for i in range(1000,1600,150):
        x_emu_new.append(i)
        n_index += 1
for i in range(1600,2100,250):
        x_emu_new.append(i)
        n_index += 1
for i in range(2100,4100,500):
        x_emu_new.append(i)
        n_index += 1
for i in range(4100,5700,800):
        x_emu_new.append(i)
        n_index += 1
for i in range(5700, 7900, 1100):
        x_emu_new.append(i)
        n_index += 1
x_emu_new.append(7900)
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

e_pt = array('f')
for i in range(31,65):
	e_pt.append(1.12**i)
mass_bin = array('f')
mass_bin.append(0)
mass_bin.append(200)
mass_bin.append(3200)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#{njet, nbjet):[value, ith bin, label]
n_jet_bjet_dic = {
"(0,0)":[0,1,"(0,0)"],
"(1,0)":[1,2,"(1,0)"],
"(1,1)":[2,3,"(1,1)"],
"(2,0)":[3,4,"(2,0)"],
"(2,1)":[4,5,"(2,1)"],
"(2,2)":[5,6,"(2,2)"],
"(3,0)":[6,7,"(3,0)"],
"(3,1)":[7,8,"(3,1)"],
"(3,2)":[8,9,"(3,2)"],
"(3,3)":[9,10,"(3,3)"],
"(4,0)":[10,11,"(4,0)"],
"(4,1)":[11,12,"(4,1)"],
"(4,2)":[12,13,"(4,2)"],
"(4,3)":[13,14,"(4,3)"],
"(4,4)":[14,15,"(4,4)"],
"(>4,n)":[15,16,"(>4,n)"],
}

pre_value_dic={
#'key':[[['branch1 name','branch2 name'],'hist name','hist title','nbin','array of bin','start bin','end bin','min x','max x'],['x label',x label size,'y label',y label size,pad1 legend x drift,y drift],[if x log,if y log, if userdefined x axis][if PU reweighted]],
"M_emu_massDep":{
		"Data_value_dic":{"M_emu":True},
		"MC_value_dic":{"M_emu":True},
                "hist_name":"M_EMu_new_PU",
                "hist_title":"Invirant mass(ee)",
                "use_array":True,
                "PU_reweight":True,
                "bin_weight":True,
                "hist_para":[n_index,x_emu_new,50,4000],
                "y_axis":[0.0001,"null"],
                "x_label":['Dilepton mass [GeV]',0.1],
                "y_label":['Event ',0.05],
                "x_log":True,
                "y_log":True,
                "lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"M_emu_massDep_2":{
		"Data_value_dic":{"M_emu":True},
		"MC_value_dic":{"M_emu":True},
                "hist_name":"M_EMu_new_PU_2",
                "hist_title":"Invirant mass(ee)",
                "use_array":True,
                "PU_reweight":True,
                "bin_weight":False,
                "hist_para":[n_index,x_emu_new,50,4000],
                "y_axis":[0.0001,"null"],
                "x_label":['Dilepton mass [GeV]',0.1],
                "y_label":['Event ',0.05],
                "x_log":True,
                "y_log":True,
                "lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"M_emu_Ml":{
		"Data_value_dic":{"M_emu":True},
		"MC_value_dic":{"M_emu":True},
                "hist_name":"M_EMu_new_PU_Ml",
                "hist_title":"Invirant mass(ee)",
                "use_array":False,
                "PU_reweight":True,
                "bin_weight":False,
                "hist_para":[80,None,50,4500],
                "y_axis":[0.0001,"null"],
                "x_label":['Dilepton mass [GeV]',0.1],
                "y_label":['Event ',0.05],
                "x_log":True,
                "y_log":True,
                "lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"Pt_ll":{
		"Data_value_dic":{"M_ll":True},
		"MC_value_dic":{"M_ll":True},
				"hist_name":"Pt_ll",
				"hist_title":"Pt (Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[48,x_emu_new,20,260],
				"y_axis":["null","null"],
				"x_label":['P_{T}^{ll} (GeV/c^{2})',0.1],
				"y_label":['Event / 5 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"rapidity_ll":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"rapidity_ll",
				"hist_title":"Pt (Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[80,x_emu_new,-4,4],
				"y_axis":["null","null"],
				"x_label":['Rapidity^{ll}',0.1],
				"y_label":['Event / 1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"phi_ll":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"phi_ll",
				"hist_title":"Pt (Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[35,x_emu_new,-3.5,3.5],
				"y_axis":["null","null"],
				"x_label":['#phi^{ll} ',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"deltaR_ll":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"deltaR_ll",
				"hist_title":"Pt (Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[120,x_emu_new,0,6],
				"y_axis":["null","null"],
				"x_label":['#Delta R(l,l)',0.1],
				"y_label":['Event / 0.05',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"delta_eta_ll":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"delta_eta_ll",
				"hist_title":"",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[51,x_emu_new,0,5.1],
				"y_axis":["null","null"],
				"x_label":['#Delta #eta^{(l,l)} ',0.1],
				"y_label":['Event / 0.1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"delta_phi_ll":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"delta_phi_ll",
				"hist_title":"",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[35,x_emu_new,0,3.5],
				"y_axis":["null","null"],
				"x_label":['#Delta #phi^{(l,l)} ',0.1],
				"y_label":['Event / 0.1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"Heep_Et":{
		"Data_value_dic":{"ele_Et":True},
		"MC_value_dic":{"ele_Et":True},
		"hist_name":"heep_et",
		"hist_title":"Barrel Lepton Et",
		"use_array":True,
		"PU_reweight":True,
        "bin_weight":True,
		"hist_para":[33,e_pt,20,3200],
		"y_axis":[0.0001,"null"],
		"x_label":['Et^{Heep} (GeV)',0.1],
		"y_label":['Event / 1 GeV',0.05],
		"x_log":True,
		"y_log":True,
		"lenend":{
                               "useLegend":True,
                               "position":[],
                               },
               },
"Heep_eta":{
		"Data_value_dic":{"ele_eta":True},
		"MC_value_dic":{"ele_eta":True},
				"hist_name":"ele_eta",
				"hist_title":"Leading Lepton #eta",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[51,x_emu_new,-2.55,2.55],
				"y_axis":["null","null"],
				"x_label":['#eta^{Heep}',0.1],
				"y_label":['Event / 0.1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"Heep_phi":{
		"Data_value_dic":{"ele_phi":True},
		"MC_value_dic":{"ele_phi":True},
				 "hist_name":"ele_phi",
				"hist_title":"Leading Lepton #phi",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[35,x_emu_new,-3.5,3.5],
				"y_axis":["null","null"],
				"x_label":['#phi^{Heep}',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"Muon_pt":{
		"Data_value_dic":{"muon_pt":True},
		"MC_value_dic":{"muon_pt":True},
				"hist_name":"muon_pt",
				"hist_title":"Sub-Leading Lepton Pt",
				"use_array":True,
				"PU_reweight":True,
                "bin_weight":True,
				"hist_para":[30,x_pt,60,3200],
                		"y_axis":[0.0001,"null"],
				"x_label":['P_{T}^{muon} (GeV)',0.1],
				"y_label":['Event / 1 GeV',0.05],
				"x_log":True,
				"y_log":True,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"muon_eta":{
		"Data_value_dic":{"muon_eta":True},
		"MC_value_dic":{"muon_eta":True},
				"hist_name":"muon_eta",
				"hist_title":"sub_Leading Lepton #eta",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[51,x_emu_new,-2.55,2.55],
				"y_axis":["null","null"],
				"x_label":['#eta^{muon}',0.1],
				"y_label":['Event / 0.1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"muon_phi":{
		"Data_value_dic":{"muon_phi":True},
		"MC_value_dic":{"muon_phi":True},
				"hist_name":"muon_phi",
				"hist_title":"sub-Leading Lepton #phi",
				"use_array":False,
				"PU_reweight":True,
                "bin_weight":False,
				"hist_para":[35,x_emu_new,-3.5,3.5],
				"y_axis":["null","null"],
				"x_label":['#phi^{muon}',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                }, 
"pv_n":{
		"Data_value_dic":{"pv_n":True},
		"MC_value_dic":{"pv_n":True},
		"hist_name":"N_vtx_PU",
		"hist_title":"Number of vertex (with PU reweight)",
		"use_array":False,
		"PU_reweight":True,
        "bin_weight":False,
		"hist_para":[100,'null',0,100],
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
"pv_n_noPU":{
		"Data_value_dic":{"pv_n":True},
		"MC_value_dic":{"pv_n":True},
		"hist_name":"N_vtx_noPU",
		"hist_title":"Number of vertex (without PU reweight)",
		"use_array":False,
		"PU_reweight":False,
		"bin_weight":False,
		"hist_para":[100,'null',0,100],
		"y_axis":["null","null"],
		"x_label":['N_{vtx}^{no PU}',0.1],
		"y_label":['Event ',0.05],
		"x_log":False,
		"y_log":False,
		"lenend":{
				"useLegend":True,
				"position":[],
				},
		},
"n_stat":{
		"Data_value_dic":{},
		"MC_value_dic":{},
		"hist_name":"n_stat",
		"hist_title":"Number event(with PU reweight)",
		"use_array":False,
		"PU_reweight":True,
		"bin_weight":False,
		"hist_para":[1,mass_bin,0,1],
		"y_axis":["null","null"],
		"x_label":['M_{e#mu}',0.1],
		"y_label":['Event/GeV ',0.05],
		"x_log":False,
		"y_log":False,
		"lenend":{
				"useLegend":True,
				"position":[],
				},
		},
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~