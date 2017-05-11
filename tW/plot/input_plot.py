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

isUpdate = True
isUpdate = False
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

def map_value(path, event, h1, tmp_value_dic, event_weight_factor):
	bin_weight = 1.0
	pi = 3.1415926
	if path == "new_leading_pt" or path == "new_sub_leading_pt":
		for value in tmp_value_dic:
			exec 'passed = (%s)'%(tmp_value_dic[value])
			if not passed: continue 
			if getattr(event,value) < 149:
				h1.Fill(getattr(event,value),event_weight_factor)
			else:
				h1.Fill(149,event_weight_factor)
	elif path == "new_M_ll":
		for value in tmp_value_dic:
			exec 'passed = (%s)'%(tmp_value_dic[value])
			if not passed: continue 
			if getattr(event,value) < 299:
				h1.Fill(getattr(event,value),event_weight_factor)
			else:
				h1.Fill(299,event_weight_factor)
	elif path == "Pt_ll":
		tmp_leading_p4 = getP4(getattr(event,"leading_pt"),getattr(event,"leading_eta"),getattr(event,"leading_phi"),getattr(event,"leading_isE"),getattr(event,"leading_isMu"))
		tmp_subleading_p4 = getP4(getattr(event,"sub_leading_pt"),getattr(event,"sub_leading_eta"),getattr(event,"sub_leading_phi"),getattr(event,"sub_leading_isE"),getattr(event,"sub_leading_isMu"))
		tmp_pt = (tmp_leading_p4 + tmp_subleading_p4).Pt()
		#print tmp_pt
		if tmp_pt < 259:
			h1.Fill(tmp_pt,event_weight_factor)
		else:
			h1.Fill(259,event_weight_factor)
	elif path == "phi_ll":
		tmp_leading_p4 = getP4(getattr(event,"leading_pt"),getattr(event,"leading_eta"),getattr(event,"leading_phi"),getattr(event,"leading_isE"),getattr(event,"leading_isMu"))
		tmp_subleading_p4 = getP4(getattr(event,"sub_leading_pt"),getattr(event,"sub_leading_eta"),getattr(event,"sub_leading_phi"),getattr(event,"sub_leading_isE"),getattr(event,"sub_leading_isMu"))
		tmp_phi = (tmp_leading_p4 + tmp_subleading_p4).Phi()
		h1.Fill(tmp_phi,event_weight_factor)
	elif path == "deltaR_ll":
		tmp_leading_p4 = getP4(getattr(event,"leading_pt"),getattr(event,"leading_eta"),getattr(event,"leading_phi"),getattr(event,"leading_isE"),getattr(event,"leading_isMu"))
		tmp_subleading_p4 = getP4(getattr(event,"sub_leading_pt"),getattr(event,"sub_leading_eta"),getattr(event,"sub_leading_phi"),getattr(event,"sub_leading_isE"),getattr(event,"sub_leading_isMu"))
		tmp_dR = tmp_leading_p4.DeltaR(tmp_subleading_p4)
		h1.Fill(tmp_dR,event_weight_factor)
	elif path == "rapidity_ll":
		tmp_leading_p4 = getP4(getattr(event,"leading_pt"),getattr(event,"leading_eta"),getattr(event,"leading_phi"),getattr(event,"leading_isE"),getattr(event,"leading_isMu"))
		tmp_subleading_p4 = getP4(getattr(event,"sub_leading_pt"),getattr(event,"sub_leading_eta"),getattr(event,"sub_leading_phi"),getattr(event,"sub_leading_isE"),getattr(event,"sub_leading_isMu"))
		tmp_rapidity = (tmp_leading_p4 + tmp_subleading_p4).Rapidity()
		h1.Fill(tmp_rapidity,event_weight_factor)
	elif path == "Z_MET_T1Txy_delta_phi":
		tmp_leading_p4 = getP4(getattr(event,"leading_pt"),getattr(event,"leading_eta"),getattr(event,"leading_phi"),getattr(event,"leading_isE"),getattr(event,"leading_isMu"))
		tmp_subleading_p4 = getP4(getattr(event,"sub_leading_pt"),getattr(event,"sub_leading_eta"),getattr(event,"sub_leading_phi"),getattr(event,"sub_leading_isE"),getattr(event,"sub_leading_isMu"))
		tmp_phi = (tmp_leading_p4 + tmp_subleading_p4).Phi()
		delta_phi = fabs(tmp_phi - getattr(event,"MET_T1Txy_phi"))
		if delta_phi > pi:delta_phi = 2*pi - delta_phi
		h1.Fill(fabs(delta_phi),event_weight_factor)
	elif path == "n_jet_bjet":
		n_jet = getattr(event,"n_jet")
		n_bjet = getattr(event,"n_bjet")
		if n_jet <=4:
			h1.Fill(n_jet_bjet_dic["(%s,%s)"%(n_jet,n_bjet)][0],event_weight_factor)
		else:
			h1.Fill(n_jet_bjet_dic["(>4,n)"][0],event_weight_factor)
	elif path == "n_bjet2":
		tmp_n_bjet = 0
                jet_pt_vector = getattr(event,"jet_pt")
                jet_eta_vector = getattr(event,"jet_eta")
                jet_ID_vector = getattr(event,"jet_IDLoose")
		jet_CSVv2_vector = getattr(event,"jet_CSVv2")
                for i in range(len(jet_pt_vector)):
                        if jet_pt_vector[i] > 20 and jet_pt_vector[i] < 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i] and jet_CSVv2_vector[i] > 0.8484:
				tmp_n_bjet += 1
		h1.Fill(tmp_n_bjet,event_weight_factor)
	elif path == "n_fjet1":
		tmp_n_fjet = 0
                jet_pt_vector = getattr(event,"jet_pt")
                jet_eta_vector = getattr(event,"jet_eta")
                jet_ID_vector = getattr(event,"jet_IDLoose")
		jet_CSVv2_vector = getattr(event,"jet_CSVv2")
                for i in range(len(jet_pt_vector)):
                        if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])>2.4 and fabs(jet_eta_vector[i])<5.2 and jet_ID_vector[i]:
				tmp_n_fjet += 1
		h1.Fill(tmp_n_fjet,event_weight_factor)
	elif path == "n_fjet2":
		tmp_n_fjet = 0
                jet_pt_vector = getattr(event,"jet_pt")
                jet_eta_vector = getattr(event,"jet_eta")
                jet_ID_vector = getattr(event,"jet_IDLoose")
		jet_CSVv2_vector = getattr(event,"jet_CSVv2")
                for i in range(len(jet_pt_vector)):
                        if jet_pt_vector[i] > 40 and fabs(jet_eta_vector[i])>2.4 and fabs(jet_eta_vector[i])<5.2 and jet_ID_vector[i]:
				tmp_n_fjet += 1
		h1.Fill(tmp_n_fjet,event_weight_factor)
	elif path == "MET_pt_new":
		px = getattr(event,"leading_px") + getattr(event,"sub_leading_px") - getattr(event,"leading_2nd_px") - getattr(event,"sub_leading_2nd_px")
		py = getattr(event,"leading_py") + getattr(event,"sub_leading_py") - getattr(event,"leading_2nd_py") - getattr(event,"sub_leading_2nd_py")
		MET_x = getattr(event,"MET_Et") * cos(getattr(event,"MET_phi")) + px
		MET_y = getattr(event,"MET_Et") * sin(getattr(event,"MET_phi")) + py
		MET_new = sqrt(MET_x * MET_x + MET_y * MET_y)
		h1.Fill(MET_new,event_weight_factor)
	elif path == "MET_T1Txy_pt_new":
		px = getattr(event,"leading_px") + getattr(event,"sub_leading_px") - getattr(event,"leading_2nd_px") - getattr(event,"sub_leading_2nd_px")
		py = getattr(event,"leading_py") + getattr(event,"sub_leading_py") - getattr(event,"leading_2nd_py") - getattr(event,"sub_leading_2nd_py")
		MET_x = getattr(event,"MET_T1Txy_Pt") * cos(getattr(event,"MET_T1Txy_phi")) + px
		MET_y = getattr(event,"MET_T1Txy_Pt") * sin(getattr(event,"MET_T1Txy_phi")) + py
		MET_new = sqrt(MET_x * MET_x + MET_y * MET_y)
		h1.Fill(MET_new,event_weight_factor)
	elif path == "HT":
		tmp_HT = 0
		jet_pt_vector = getattr(event,"jet_pt")
		jet_eta_vector = getattr(event,"jet_eta")
		jet_ID_vector = getattr(event,"jet_IDLoose")
		for i in range(len(jet_pt_vector)):
			if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
				tmp_HT += jet_pt_vector[i]
		#if tmp_HT == 0:return
		if tmp_HT > 500:
			h1.Fill(499,event_weight_factor)
		else:
			h1.Fill(tmp_HT,event_weight_factor)
	elif path == "sys_HT":
		tmp_HT = 0
		jet_pt_vector = getattr(event,"jet_pt")
		jet_eta_vector = getattr(event,"jet_eta")
		jet_ID_vector = getattr(event,"jet_IDLoose")
		for i in range(len(jet_pt_vector)):
			if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
				tmp_HT += jet_pt_vector[i]
		tmp_HT += getattr(event,"leading_pt") + getattr(event,"sub_leading_pt")
		#if tmp_HT == 0:return
		if tmp_HT > 500:
			h1.Fill(499,event_weight_factor)
		else:
			h1.Fill(tmp_HT,event_weight_factor)
	else:
		for value in tmp_value_dic:
			exec 'passed = (%s)'%(tmp_value_dic[value])
			if not passed: continue 
			#print "passed"
			bin_weight = 1.0
			if value_dic[path]["use_array"]:
				bin_weight = 1.0/getbinwidth(getattr(event,value),value_dic[path]["hist_para"][1])
			total_weight = event_weight_factor * bin_weight
			h1.Fill(getattr(event,value),total_weight)
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
value_dic={
#'key':[[['branch1 name','branch2 name'],'hist name','hist title','nbin','array of bin','start bin','end bin','min x','max x'],['x label',x label size,'y label',y label size,pad1 legend x drift,y drift],[if x log,if y log, if userdefined x axis][if PU reweighted]],
"M_ll":{
		"Data_value_dic":{"M_ll":True},
		"MC_value_dic":{"M_ll":True},
				"hist_name":"M_ll",
				"hist_title":"Invirant mass(Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[60,x_emu_new,0,600],
				"y_axis":["null","null"],
				"x_label":['M_{ll} (GeV/c^{2})',0.1],
				"y_label":['Event / 10 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"new_M_ll":{
		"Data_value_dic":{"M_ll":True},
		"MC_value_dic":{"M_ll":True},
				"hist_name":"new_M_ll",
				"hist_title":"Invirant mass(Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[60,x_emu_new,0,300],
				"y_axis":["null","null"],
				"x_label":['M_{ll} (GeV/c^{2})',0.1],
				"y_label":['Event / 5 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"M_ll_zmass":{
		"Data_value_dic":{"M_ll":True},
		"MC_value_dic":{"M_ll":True},
				"hist_name":"M_ll_zmass",
				"hist_title":"Invirant mass(Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[60,x_emu_new,60,120],
				"y_axis":["null","null"],
				"x_label":['M_{ll} (GeV/c^{2})',0.1],
				"y_label":['Event / 1 GeV',0.05],
				"x_log":False,
				"y_log":False,
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
"phi_ll":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"phi_ll",
				"hist_title":"Pt (Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
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
"rapidity_ll":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"rapidity_ll",
				"hist_title":"Pt (Di-lepton)",
				"use_array":False,
				"PU_reweight":True,
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
"leading_pt":{
		"Data_value_dic":{"leading_pt":True},
		"MC_value_dic":{"leading_pt":True},
				"hist_name":"leading_pt",
				"hist_title":"Leading Lepton Pt",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[60,x_emu_new,0,300],
				"y_axis":["null","null"],
				"x_label":['P_{T}^{leading lep} (GeV/c)',0.1],
				"y_label":['Event / 5 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"new_leading_pt":{
		"Data_value_dic":{"leading_pt":True},
		"MC_value_dic":{"leading_pt":True},
				"hist_name":"new_leading_pt",
				"hist_title":"Leading Lepton Pt",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[30,x_emu_new,0,150],
				"y_axis":["null","null"],
				"x_label":['P_{T}^{leading lep} (GeV/c)',0.1],
				"y_label":['Event / 5 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"leading_eta":{
		"Data_value_dic":{"leading_eta":True},
		"MC_value_dic":{"leading_eta":True},
				"hist_name":"leading_eta",
				"hist_title":"Leading Lepton #eta",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[51,x_emu_new,-2.55,2.55],
				"y_axis":["null","null"],
				"x_label":['#eta^{leading lepton}',0.1],
				"y_label":['Event / 0.1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"leading_phi":{
		"Data_value_dic":{"leading_phi":True},
		"MC_value_dic":{"leading_phi":True},
				 "hist_name":"leading_phi",
				"hist_title":"Leading Lepton #phi",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[35,x_emu_new,-3.5,3.5],
				"y_axis":["null","null"],
				"x_label":['#phi^{leading lepton}',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"sub_leading_pt":{
		"Data_value_dic":{"sub_leading_pt":True},
		"MC_value_dic":{"sub_leading_pt":True},
				"hist_name":"sub_leading_pt",
				"hist_title":"Sub-Leading Lepton Pt",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[60,x_emu_new,0,300],
				"y_axis":["null","null"],
				"x_label":['P_{T}^{subleading lepton} (GeV/c)',0.1],
				"y_label":['Event / 5 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"new_sub_leading_pt":{
		"Data_value_dic":{"sub_leading_pt":True},
		"MC_value_dic":{"sub_leading_pt":True},
				"hist_name":"new_sub_leading_pt",
				"hist_title":"Sub-Leading Lepton Pt",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[30,x_emu_new,0,150],
				"y_axis":["null","null"],
				"x_label":['P_{T}^{subleading lepton} (GeV/c)',0.1],
				"y_label":['Event / 5 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"sub_leading_eta":{
		"Data_value_dic":{"sub_leading_eta":True},
		"MC_value_dic":{"sub_leading_eta":True},
				"hist_name":"sub_leading_eta",
				"hist_title":"sub_Leading Lepton #eta",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[51,x_emu_new,-2.55,2.55],
				"y_axis":["null","null"],
				"x_label":['#eta^{subleading lepton}',0.1],
				"y_label":['Event / 0.1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"sub_leading_phi":{
		"Data_value_dic":{"sub_leading_phi":True},
		"MC_value_dic":{"sub_leading_phi":True},
				"hist_name":"sub_leading_phi",
				"hist_title":"sub-Leading Lepton #phi",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[35,x_emu_new,-3.5,3.5],
				"y_axis":["null","null"],
				"x_label":['#phi^{subleading lepton}',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                }, 
"MET_pt":{
		"Data_value_dic":{"MET_Et":True},
		"MC_value_dic":{"MET_Et":True},
				"hist_name":"MET_Et",
				"hist_title":"MET Pt",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[20,x_emu_new,0,200],
				"y_axis":["null","null"],
				"x_label":['MET (GeV/c)',0.1],
				"y_label":['Event / 10 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
#"MET_pt_new":{
#		"Data_value_dic":{"MET_Et":True},
#		"MC_value_dic":{"MET_Et":True},
#				"hist_name":"MET_Et_new",
#				"hist_title":"MET Pt",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[20,x_emu_new,0,200],
#				"y_axis":["null","null"],
#				"x_label":['MET_{new} (GeV/c)',0.1],
#				"y_label":['Event / 10 GeV',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
"MET_phi":{
		"Data_value_dic":{"MET_phi":True},
		"MC_value_dic":{"MET_phi":True},
				"hist_name":"MET_phi",
				"hist_title":"MET #phi",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[35,x_emu_new,-3.5,3.5],
				"y_axis":["null","null"],
				"x_label":['MET_{#phi}',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"MET_significance":{
		"Data_value_dic":{"MET_significance":True},
		"MC_value_dic":{"MET_significance":True},
				"hist_name":"MET_significance",
				"hist_title":"MET significance",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[40,x_emu_new,0,20],
				"y_axis":["null","null"],
				"x_label":['MET_{significance}',0.1],
				"y_label":['Event / 0.5',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"MET_T1Txy_pt":{
		"Data_value_dic":{"MET_T1Txy_Pt":True},
		"MC_value_dic":{"MET_T1Txy_Pt":True},
				"hist_name":"MET_T1Txy_Pt",
				"hist_title":"MET T1Txy Pt",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[20,x_emu_new,0,200],
				"y_axis":["null","null"],
				"x_label":['MET^{T1Txy} (GeV/c)',0.1],
				"y_label":['Event / 10 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
#"MET_T1Txy_pt_new":{
#		"Data_value_dic":{"MET_T1Txy_Pt":True},
#		"MC_value_dic":{"MET_T1Txy_Pt":True},
#				"hist_name":"MET_T1Txy_Pt_new",
#				"hist_title":"MET T1Txy Pt",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[20,x_emu_new,0,200],
#				"y_axis":["null","null"],
#				"x_label":['MET^{T1Txy}_{new} (GeV/c)',0.1],
#				"y_label":['Event / 10 GeV',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
"MET_T1Txy_phi":{
		"Data_value_dic":{"MET_T1Txy_phi":True},
		"MC_value_dic":{"MET_T1Txy_phi":True},
				"hist_name":"MET_T1Txy_phi",
				"hist_title":"MET T1Txy #phi",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[35,x_emu_new,-3.5,3.5],
				"y_axis":["null","null"],
				"x_label":['MET^{T1Txy}_{#phi}',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"Z_MET_T1Txy_delta_phi":{
		"Data_value_dic":{"MET_T1Txy_phi":True},
		"MC_value_dic":{"MET_T1Txy_phi":True},
				"hist_name":"Z_MET_T1Txy_delta_phi",
				"hist_title":"MET T1Txy #phi",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[35,x_emu_new,0,3.5],
				"y_axis":["null","null"],
				"x_label":['#delta #phi(MET^{T1Txy},ll)',0.1],
				"y_label":['Event / 0.2',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"MET_T1Txy_significance":{
		"Data_value_dic":{"MET_T1Txy_significance":True},
		"MC_value_dic":{"MET_T1Txy_significance":True},
				"hist_name":"MET_T1Txy_significance",
				"hist_title":"MET T1Txy significance",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[40,x_emu_new,0,20],
				"y_axis":["null","null"],
				"x_label":['MET^{T1Txy}_{significance}',0.1],
				"y_label":['Event / 0.5',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"rho":{
		"Data_value_dic":{"ev_fixedGridRhoAll":True},
		"MC_value_dic":{"ev_fixedGridRhoAll":True},
				"hist_name":"rho_all",
				"hist_title":"ev_fixedGridRhoAll",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[100,x_emu_new,0,50],
				"y_axis":["null","null"],
				"x_label":['#rho',0.1],
				"y_label":['Event / 0.5',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"n_jet":{
		"Data_value_dic":{"n_jet":True},
		"MC_value_dic":{"n_jet":True},
				"hist_name":"n_jet",
				"hist_title":"Jet Multiplicity",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[10,x_emu_new,0,10],
				"y_axis":["null","null"],
				"x_label":['N_{jet}',0.1],
				"y_label":['Event / 1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"n_bjet":{
		"Data_value_dic":{"n_bjet":True},
		"MC_value_dic":{"n_bjet":True},
				"hist_name":"n_bjet",
				"hist_title":"Jet Multiplicity",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[10,x_emu_new,0,10],
				"y_axis":["null","null"],
				"x_label":['N_{b jet}',0.1],
				"y_label":['Event / 1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"n_bjet2":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"n_bjet2",
				"hist_title":"Jet Multiplicity",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[10,x_emu_new,0,10],
				"y_axis":["null","null"],
				"x_label":['N_{b jet} (p_{T} in [20,30])',0.1],
				"y_label":['Event / 1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"n_fjet1":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"n_fjet1",
				"hist_title":"Jet Multiplicity",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[10,x_emu_new,0,10],
				"y_axis":["null","null"],
				"x_label":['N_{jet} (p_{T} > 30, |#eta| in [2.4,5.2])',0.1],
				"y_label":['Event / 1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"n_fjet2":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"n_fjet2",
				"hist_title":"Jet Multiplicity",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[10,x_emu_new,0,10],
				"y_axis":["null","null"],
				"x_label":['N_{jet} (p_{T} > 40, |#eta| in [2.4,5.2])',0.1],
				"y_label":['Event / 1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"n_jet_bjet":{
		"Data_value_dic":{"n_bjet":True},
		"MC_value_dic":{"n_bjet":True},
				"hist_name":"n_jet_bjet",
				"hist_title":"Jet Multiplicity",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[16,x_emu_new,0,16],
				"y_axis":["null","null"],
				"x_label":['N_{(jet, b jet)}',0.1],
				"y_label":['Event / 1',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },

"HT":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"Ht",
				"hist_title":"Ht",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[49,x_emu_new,10,500],
				"y_axis":["null","null"],
				"x_label":['HT (GeV)',0.1],
				"y_label":['Event / 10 GeV',0.05],
				"x_log":False,
				"y_log":False,
				"lenend":{
                                "useLegend":True,
                                "position":[],
                                },
                },
"sys_HT":{
		"Data_value_dic":{"":True},
		"MC_value_dic":{"":True},
				"hist_name":"sys_Ht",
				"hist_title":"sys Ht",
				"use_array":False,
				"PU_reweight":True,
				"hist_para":[49,x_emu_new,10,500],
				"y_axis":["null","null"],
				"x_label":['HT^{sys} (GeV)',0.1],
				"y_label":['Event / 10 GeV',0.05],
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
		"hist_para":[50,'null',0,50],
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
		"hist_para":[50,'null',0,50],
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
"mass_err_stat":{
		"Data_value_dic":{"pv_n":True},
		"MC_value_dic":{"pv_n":True},
		"hist_name":"N_stat",
		"hist_title":"",
		"use_array":False,
		"PU_reweight":True,
		"hist_para":[1,mass_bin,0,100],
		"y_axis":["null","null"],
		"x_label":['N_stat',0.1],
		"y_label":['Event ',0.05],
		"x_log":False,
		"y_log":True,
		"lenend":{
				"useLegend":True,
				"position":[],
				},
		},
}
