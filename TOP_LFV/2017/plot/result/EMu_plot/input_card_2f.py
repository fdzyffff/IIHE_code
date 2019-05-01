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

isUpdate = False
isUpdate = True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getP4(pt, eta, phi, isE, isMu):
	p4 = ROOT.TLorentzVector()
	if isE:
		p4.SetPtEtaPhiM(pt,eta,phi,0.000511)
	else:
		p4.SetPtEtaPhiM(pt,eta,phi,0.10566)
	return p4

def getbinwidth(x,x1):
	for i in range(len(x1)):
		if x < x1[i] and i>0:
			return (x1[i]-x1[i-1])
		elif x < x1[i]:
			return -1.0
	return -1.0

def map_value_2f(path,event, h2, tmp_value_dic, event_weight_factor):
	bin_weight = 1.0
	if path == "":
		return
	else:
		for value_x in tmp_value_dic["xaxis"]:
			exec 'passed = (%s)'%(tmp_value_dic["xaxis"][value_x])
			if not passed: continue
			for value_y in tmp_value_dic["yaxis"]:
				exec 'passed = (%s)'%(tmp_value_dic["yaxis"][value_y])
				if not passed: continue 
				#print "passed"
				bin_weight = 1.0
				if value_dic_2f[path]["use_array"]:
					bin_weight = 1.0/getbinwidth(getattr(event,value_x),value_dic[path]["hist_para"][1],getattr(event,value_y),value_dic[path]["hist_para"][5])
				total_weight = event_weight_factor * bin_weight
				h2.Fill(getattr(event,value_x),getattr(event,value_y),total_weight)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x_emu_new = array('f')
n_index = 0
x_emu_new.append(50)
for i in range(55,120,5):
	x_emu_new.append(i)
	n_index += 1
for i in range(120,150,5):
	x_emu_new.append(i)
	n_index += 1
for i in range(150,200,10):
	x_emu_new.append(i)
	n_index += 1
for i in range(200,600,20):
	x_emu_new.append(i)
	n_index += 1
for i in range(600,900,30):
	x_emu_new.append(i)
	n_index += 1
for i in range(900,1250,50):
	x_emu_new.append(i)
	n_index += 1
for i in range(1250,1610,60):
	x_emu_new.append(i)
	n_index += 1
for i in range(1610,1890,70):
	x_emu_new.append(i)
	n_index += 1
for i in range(1890,3890,80):
	x_emu_new.append(i)
	n_index += 1
x_emu_new.append(4000)
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
mass_bin = array('f')
mass_bin.append(0)
mass_bin.append(500)
mass_bin.append(1000)
mass_bin.append(1500)
mass_bin.append(2500)
value_dic_2f={
#'key':[[['branch1 name','branch2 name'],'hist name','hist title','nbin','array of bin','start bin','end bin','min x','max x'],['x label',x label size,'y label',y label size,pad1 legend x drift,y drift],[if x log,if y log, if userdefined x axis][if PU reweighted]],
"Mll_MET":{
		"Data_value_dic":{"xaxis":{"M_ll":True},"yaxis":{"MET_Et":True}},
		"MC_value_dic":{"xaxis":{"M_ll":True},"yaxis":{"MET_Et":True}},
				"hist_name":"M_ll",
				"hist_title":"Invirant mass(Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[200,x_emu_new,0,200,40,x_emu_new,0,80,],
				"y_axis":["null","null"],
				"x_label":['M_{ll} (Gev/c^{2})',0.1],
				"y_label":['MET (Gev)',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
					"useLegend":True,
					"position":[],
					},
			},
"Mll_MET_sig":{
		"Data_value_dic":{"xaxis":{"M_ll":True},"yaxis":{"MET_significance":True}},
		"MC_value_dic":{"xaxis":{"M_ll":True},"yaxis":{"MET_significance":True}},
				"hist_name":"M_ll",
				"hist_title":"Invirant mass(Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[200,x_emu_new,0,200,50,x_emu_new,0,10],
				"y_axis":["null","null"],
				"x_label":['M_{ll} (Gev/c^{2})',0.1],
				"y_label":['MET_{significance}',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
					"useLegend":True,
					"position":[],
					},
			},
"mass_err_stat_2f":{
		"Data_value_dic":{"xaxis":{"pv_n":True},"yaxis":{"pv_n":True}},
		"MC_value_dic":{"xaxis":{"pv_n":True},"yaxis":{"pv_n":True}},
		"hist_name":"N_stat",
		"hist_title":"",
		"use_array":False,
		"PU_reweight":True,
		"hist_para":[1,mass_bin,1,100,1,mass_bin,1,100],
		"y_axis":["null","null"],
		"x_label":['N_stat',0.1],
		"y_label":['Event ',0.05],
		"x_log":False,
		"y_log":False,
		"lenend":{
				"useLegend":True,
				"position":[],
				},
			},
}

#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
input_dic_2f={
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
