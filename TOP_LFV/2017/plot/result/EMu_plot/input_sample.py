isUpdate = True
isUpdate = False

def Load_json(dic_name):
	return eval(open(dic_name).read().replace("\n",""))

#dic_Muon_Tracking_eta           = Load_json("SF_json/Muon/Tracking/Muon_Tracking_json.txt")
dic_Muon_ID_pt_Abseta           = Load_json("SF_json/Muon/ID/Muon_TightID_json_pt_abseta.txt")
dic_Muon_ISO_pt_Abseta          = Load_json("SF_json/Muon/ISO/Muon_TightISO_json_pt_abseta.txt")
dic_Ele_Tracking_pt_eta         = Load_json("SF_json/Electron/Tracking/Ele_Tracking_json_pt_eta.txt")
dic_Ele_ID_ISO_pt_eta           = Load_json("SF_json/Electron/ID-ISO/Ele_ID-ISO_json_pt_eta.txt")
dic_EE_Trigger             = Load_json("SF_json/Trigger/Trigger_EE_json.txt")
dic_EMu_Trigger            = Load_json("SF_json/Trigger/Trigger_EMu_json.txt")
dic_MuMu_Trigger           = Load_json("SF_json/Trigger/Trigger_MuMu_json.txt")

#dic_Nvtx                        = Load_json("SF_EE_80/_EE_80_step1_hratio_pv_n.json")
#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
input_dic={
"data_runB":{"isFromRoot":True,
		"input_file":"data_80_MuonEG_runB.root",
		"isData":True,
		"isFake":False,
		"isSS":False,
		"useToNorm":True,
		"lumi":4793.961,
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
"data_runC":{"isFromRoot":True,
                "input_file":"data_80_MuonEG_runC.root",
                "isData":True,
                "isFake":False,
                "isSS":False,
                "useToNorm":True,
                "lumi":9631.214,
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
"data_runD":{"isFromRoot":True,
                "input_file":"data_80_MuonEG_runD.root",
                "isData":True,
                "isFake":False,
                "isSS":False,
                "useToNorm":True,
                "lumi":4247.682,
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
"data_runE":{"isFromRoot":True,
                "input_file":"data_80_MuonEG_runE.root",
                "isData":True,
                "isFake":False,
                "isSS":False,
                "useToNorm":True,
                "lumi":9313.642,
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
"data_runF":{"isFromRoot":True,
                "input_file":"data_80_MuonEG_runF.root",
                "isData":True,
                "isFake":False,
                "isSS":False,
                "useToNorm":True,
                "lumi":13539.042,
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
"DYToLL_10to50":{
		"isFromRoot":True,
		"input_file":"80_DYToLL_10to50.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":18610,
		"N_total": 0.0,
		"Raw_total":39387086,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"DYToLL_50":{
		"isFromRoot":True,
		"input_file":"80_DYToLL_50.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":5765.4,
		"N_total": 0.0,
		"Raw_total":123584524,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"TTGJets":{
		"isFromRoot":True,
		"input_file":"80_TTGJets.root",
		"isData":False,
		"isFake":False,
		"isSS":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":3.697,
		"N_total": 0.0,
		"Raw_total":4818944,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":1,
		"hist":{},
		"isUpdate":isUpdate
		},
"TTTo2L2Nu":{
                "isFromRoot":True,
                "input_file":"80_TTTo2L2Nu.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":87.31,
                "N_total": 0.0,
                "Raw_total":952892,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"TTWJetsToLNu":{
                "isFromRoot":True,
                "input_file":"80_TTWJetsToLNu.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.2043,
                "N_total": 0.0,
                "Raw_total":2432071,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"TTWJetsToQQ":{
                "isFromRoot":True,
                "input_file":"80_TTWJetsToQQ.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.4062,
                "N_total": 0.0,
                "Raw_total":399254,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"TTZToLLNuNu_10":{
                "isFromRoot":True,
                "input_file":"80_TTZToLLNuNu_10.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.2529,
                "N_total": 0.0,
                "Raw_total":2998298,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"TTZToQQ":{
                "isFromRoot":True,
                "input_file":"80_TTZToQQ.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.5297,
                "N_total": 0.0,
                "Raw_total":261312,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"WGToLNuG":{
                "isFromRoot":True,
                "input_file":"80_WGToLNuG.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":489,
                "N_total": 0.0,
                "Raw_total":6203913,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"WJetsToLNu":{
                "isFromRoot":True,
                "input_file":"80_WJetsToLNu.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":61526.7,
                "N_total": 0.0,
                "Raw_total":77293834,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"WWTo2L2Nu":{
                "isFromRoot":True,
                "input_file":"80_WWTo2L2Nu.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":12.178,
                "N_total": 0.0,
                "Raw_total":1936169,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"WZTo2L2Q":{
                "isFromRoot":True,
                "input_file":"80_WZTo2L2Q.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":5.595,
                "N_total": 0.0,
                "Raw_total":16664610,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"WZTo3LNu":{
                "isFromRoot":True,
                "input_file":"80_WZTo3LNu.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":4.42965,
                "N_total": 0.0,
                "Raw_total":6820606,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ZZTo2L2Nu":{
                "isFromRoot":True,
                "input_file":"80_ZZTo2L2Nu.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.564,
                "N_total": 0.0,
                "Raw_total":8733658,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ZZTo4L":{
                "isFromRoot":True,
                "input_file":"80_ZZTo4L.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":1.212,
                "N_total": 0.0,
                "Raw_total":7755816,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
#"ggHWW":{
#                "isFromRoot":True,
#                "input_file":"80_ggHWW.root",
#                "isData":False,
#                "isFake":False,
#                "isSS":False,
#                "useToNorm":False,
#                "lumi":0.0,
#                "Xsection":2.5,
#                "N_total": 0.0,
#                "Raw_total":499466,
#                "N_norm":1.0,
#                "Norm_Factor":1,
#                "Fill_color":30,
#                "weight_factor":1,
#                "hist":{},
#                "isUpdate":isUpdate
#                },
#"VBFHWW":{
#                "isFromRoot":True,
#                "input_file":"80_VBFHWW.root",
#                "isData":False,
#                "isFake":False,
#                "isSS":False,
#                "useToNorm":False,
#                "lumi":0.0,
#                "Xsection":0.175,
#                "N_total": 0.0,
#                "Raw_total":485693,
#                "N_norm":1.0,
#                "Norm_Factor":1,
#                "Fill_color":30,
#                "weight_factor":1,
#                "hist":{},
#                "isUpdate":isUpdate
#		},
"tW":{
                "isFromRoot":True,
                "input_file":"80_tW.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":19.47,
                "N_total": 0.0,
                "Raw_total":4897485,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"tW_anti":{
                "isFromRoot":True,
                "input_file":"80_tW_anti.root",
                "isData":False,
                "isFake":False,
                "isSS":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":19.47,
                "N_total": 0.0,
                "Raw_total":5592819,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_data":{
		"isFromRoot":True,
		"input_file":"data_80_MuonEG.root",
		"isData":True,
		"isFake":False,
		"isSS":True,
		"useToNorm":False,
		"lumi":35867.0,
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
"ss_DYToLL_10to50":{
		"isFromRoot":True,
		"input_file":"80_DYToLL_10to50.root",
		"isData":False,
		"isSS":True,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":18610,
		"N_total": 0.0,
		"Raw_total":39387086,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"ss_DYToLL_50":{
		"isFromRoot":True,
		"input_file":"80_DYToLL_50.root",
		"isData":False,
		"isSS":True,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":5765.4,
		"N_total": 0.0,
		"Raw_total":123584524,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"ss_TTGJets":{
		"isFromRoot":True,
		"input_file":"80_TTGJets.root",
		"isData":False,
		"isSS":True,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":3.697,
		"N_total": 0.0,
		"Raw_total":4818944,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"ss_TTTo2L2Nu":{
                "isFromRoot":True,
                "input_file":"80_TTTo2L2Nu.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":87.31,
                "N_total": 0.0,
                "Raw_total":952892,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_TTWJetsToLNu":{
                "isFromRoot":True,
                "input_file":"80_TTWJetsToLNu.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.2043,
                "N_total": 0.0,
                "Raw_total":2432071,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_TTWJetsToQQ":{
                "isFromRoot":True,
                "input_file":"80_TTWJetsToQQ.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.4062,
                "N_total": 0.0,
                "Raw_total":399254,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_TTZToLLNuNu_10":{
                "isFromRoot":True,
                "input_file":"80_TTZToLLNuNu_10.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.2529,
                "N_total": 0.0,
                "Raw_total":2998298,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_TTZToQQ":{
                "isFromRoot":True,
                "input_file":"80_TTZToQQ.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.5297,
                "N_total": 0.0,
                "Raw_total":261312,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_WGToLNuG":{
                "isFromRoot":True,
                "input_file":"80_WGToLNuG.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":489,
                "N_total": 0.0,
                "Raw_total":6203913,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_WJetsToLNu":{
                "isFromRoot":True,
                "input_file":"80_WJetsToLNu.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":61526.7,
                "N_total": 0.0,
                "Raw_total":77293834,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_WWTo2L2Nu":{
                "isFromRoot":True,
                "input_file":"80_WWTo2L2Nu.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":12.178,
                "N_total": 0.0,
                "Raw_total":1936169,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_WZTo2L2Q":{
                "isFromRoot":True,
                "input_file":"80_WZTo2L2Q.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":5.595,
                "N_total": 0.0,
                "Raw_total":16664610,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_WZTo3LNu":{
                "isFromRoot":True,
                "input_file":"80_WZTo3LNu.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":4.42965,
                "N_total": 0.0,
                "Raw_total":6820606,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_ZZTo2L2Nu":{
                "isFromRoot":True,
                "input_file":"80_ZZTo2L2Nu.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.564,
                "N_total": 0.0,
                "Raw_total":8733658,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_ZZTo4L":{
                "isFromRoot":True,
                "input_file":"80_ZZTo4L.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":1.212,
                "N_total": 0.0,
                "Raw_total":7755816,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
#"ss_ggHWW":{
#                "isFromRoot":True,
#                "input_file":"80_ggHWW.root",
#                "isData":False,
#                "isFake":False,
#                "isSS":True,
#                "useToNorm":False,
#                "lumi":0.0,
#                "Xsection":2.5,
#                "N_total": 0.0,
#                "Raw_total":499466,
#                "N_norm":1.0,
#                "Norm_Factor":1,
#                "Fill_color":30,
#                "weight_factor":1,
#                "hist":{},
#                "isUpdate":isUpdate
#                },
#"ss_VBFHWW":{
#                "isFromRoot":True,
#                "input_file":"80_VBFHWW.root",
#                "isData":False,
#                "isFake":False,
#                "isSS":True,
#                "useToNorm":False,
#                "lumi":0.0,
#                "Xsection":0.175,
#                "N_total": 0.0,
#                "Raw_total":485693,
#                "N_norm":1.0,
#                "Norm_Factor":1,
#                "Fill_color":30,
#                "weight_factor":1,
#                "hist":{},
#                "isUpdate":isUpdate
#		},
"ss_tW":{
                "isFromRoot":True,
                "input_file":"80_tW.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":19.47,
                "N_total": 0.0,
                "Raw_total":4897485,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
"ss_tW_anti":{
                "isFromRoot":True,
                "input_file":"80_tW_anti.root",
                "isData":False,
                "isSS":True,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":19.47,
                "N_total": 0.0,
                "Raw_total":5592819,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":-1,
                "hist":{},
                "isUpdate":isUpdate
                },
}