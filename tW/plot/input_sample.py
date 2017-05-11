isUpdate = True
isUpdate = False

def Load_json(dic_name):
	return eval(open(dic_name).read().replace("\n",""))

dic_Muon_Tracking_eta           = Load_json("SF_json/Muon/Tracking/Muon_Tracking_json.txt")
dic_Muon_ID_pt_Abseta           = Load_json("SF_json/Muon/ID/Muon_TIghtID_json.txt")
dic_Muon_ISO_pt_Abseta          = Load_json("SF_json/Muon/ISO/Muon_TightISO_json.txt")
dic_Ele_Tracking_pt_eta         = Load_json("SF_json/Electron/Tracking/Ele_Tracking_json.txt")
dic_Ele_ID_ISO_pt_eta           = Load_json("SF_json/Electron/ID-ISO/Ele_ID-ISO_json.txt")

dic_Nvtx                        = Load_json("SF_EE_80/_EE_80_step1_hratio_pv_n.json")
#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
input_dic={
"data":{"isFromRoot":True,
		"input_file":"data_80_DoubleEG.root",
		"isData":True,
		"isFake":False,
		"useToNorm":True,
		"lumi":35854.301,
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
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":18610,
		"N_total": 0.0,
		"Raw_total":29168419,
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
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":5765.4,
		"N_total": 0.0,
		"Raw_total":81589928,
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
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":3.697,
		"N_total": 0.0,
		"Raw_total":3125711,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":83.71,
                "N_total": 0.0,
                "Raw_total":78353860,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.2043,
                "N_total": 0.0,
                "Raw_total":999098,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.4062,
                "N_total": 0.0,
                "Raw_total":303544,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.2529,
                "N_total": 0.0,
                "Raw_total":2548448,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.5297,
                "N_total": 0.0,
                "Raw_total":313867,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":489,
                "N_total": 0.0,
                "Raw_total":6489447,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":61526.7,
                "N_total": 0.0,
                "Raw_total":57025279,
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
"WZTo2L2Q":{
                "isFromRoot":True,
                "input_file":"80_WZTo2L2Q.root",
                "isData":False,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":5.595,
                "N_total": 0.0,
                "Raw_total":15879128,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":4.42965,
                "N_total": 0.0,
                "Raw_total":1993154,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":0.564,
                "N_total": 0.0,
                "Raw_total":8842251,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":1.212,
                "N_total": 0.0,
                "Raw_total":6617088,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
"tW":{
                "isFromRoot":True,
                "input_file":"80_tW.root",
                "isData":False,
                "isFake":False,
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":19.47,
                "N_total": 0.0,
                "Raw_total":3256548,
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
                "useToNorm":False,
                "lumi":0.0,
                "Xsection":19.47,
                "N_total": 0.0,
                "Raw_total":3256309,
                "N_norm":1.0,
                "Norm_Factor":1,
                "Fill_color":30,
                "weight_factor":1,
                "hist":{},
                "isUpdate":isUpdate
                },
}
