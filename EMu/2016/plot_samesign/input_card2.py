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
def getP4_ele(Et, eta, phi):
	p4 = ROOT.TLorentzVector()
	p4.SetPtEtaPhiM(Et,eta,phi,0.000511)
	return p4

def getP4_muon(pt, eta, phi):
	p4 = ROOT.TLorentzVector()
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
	pi = 3.1415926
	bin_weight = 1.0
	if path == "":
		return
	elif path == "Pt_ll":
		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
		tmp_pt = (tmp_ele_p4 + tmp_muon_p4).Pt()
		#print tmp_pt
		if tmp_pt < 259:
			h1.Fill(tmp_pt,event_weight_factor)
		else:
			h1.Fill(259,event_weight_factor)
	elif path == "rapidity_ll":
		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
		tmp_rapidity = (tmp_ele_p4 + tmp_muon_p4).Rapidity()
		h1.Fill(tmp_rapidity,event_weight_factor)
	elif path == "phi_ll":
		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
		tmp_phi = (tmp_ele_p4 + tmp_muon_p4).Phi()
		h1.Fill(tmp_phi,event_weight_factor)
	elif path == "deltaR_ll":
		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
		tmp_muon_p4 = getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
		tmp_dR = tmp_ele_p4.DeltaR(tmp_muon_p4)
		h1.Fill(tmp_dR,event_weight_factor)
	elif path == "delta_eta_ll":
		delta_eta = fabs(getattr(event, "ele_eta") - getattr(event, "muon_eta"))
		h1.Fill(delta_eta,event_weight_factor)
	elif path == "delta_phi_ll":
		delta_phi = fabs(getattr(event, "ele_phi") - getattr(event, "muon_phi"))
		if delta_phi > pi:delta_phi = 2*pi - delta_phi
		h1.Fill(delta_phi,event_weight_factor)
	elif path == "n_jet_bjet":
		n_jet = getattr(event,"n_jet")
		n_bjet = getattr(event,"n_bjet")
		if n_jet <=4:
			h1.Fill(n_jet_bjet_dic["(%s,%s)"%(n_jet,n_bjet)][0],event_weight_factor)
		else:
			h1.Fill(n_jet_bjet_dic["(>4,n)"][0],event_weight_factor)
	elif path == "HT":
		tmp_HT = 0
		jet_pt_vector = getattr(event,"jet_pt")
		jet_eta_vector = getattr(event,"jet_eta")
		#jet_ID_vector = getattr(event,"jet_IDLoose")
		jet_pass_vector = getattr(event,"jet_passed")
		for i in range(len(jet_pt_vector)):
			if jet_pass_vector[i]:
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
		jet_pass_vector = getattr(event,"jet_passed")
		#jet_ID_vector = getattr(event,"jet_IDLoose")
		for i in range(len(jet_pt_vector)):
			#if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
			if jet_pass_vector[i]:
				tmp_HT += jet_pt_vector[i]
		tmp_ele_p4 = getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
		tmp_HT += tmp_ele_p4.Pt() + getattr(event,"muon_pt")
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
#x_emu_new = array('f')
#n_index = 0
#x_emu_new.append(50)
#for i in range(50,200,10):
#        x_emu_new.append(i)
#        n_index += 1
#for i in range(200,600,25):
#        x_emu_new.append(i)
#        n_index += 1
#for i in range(600,1000,50):
#        x_emu_new.append(i)
#        n_index += 1
#for i in range(1000,1500,100):
#        x_emu_new.append(i)
#        n_index += 1
#for i in range(1500,2100,200):
#        x_emu_new.append(i)
#        n_index += 1
#for i in range(2100,4100,400):
#        x_emu_new.append(i)
#        n_index += 1
#x_emu_new.append(4100)
#n_index += 1

#x_emu_new = array('f')
#n_index = 0
#x_emu_new.append(50)
#for i in range(55,120,5):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(120,150,5):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(150,200,10):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(200,600,20):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(600,900,30):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(900,1250,50):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(1250,1610,60):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(1610,1890,70):
#	x_emu_new.append(i)
#	n_index += 1
#for i in range(1890,3890,80):
#	x_emu_new.append(i)
#	n_index += 1
#x_emu_new.append(4000)
#n_index += 1

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
x_emu_new.append(4100)
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

value_dic={
#'key':[[['branch1 name','branch2 name'],'hist name','hist title','nbin','array of bin','start bin','end bin','min x','max x'],['x label',x label size,'y label',y label size,pad1 legend x drift,y drift],[if x log,if y log, if userdefined x axis][if PU reweighted]],
"M_emu_massDep":{
		"Data_value_dic":{"M_emu":True},
		"MC_value_dic":{"M_emu":True},
                "hist_name":"M_EMu_new_PU",
                "hist_title":"Invirant mass(ee)",
                "use_array":True,
                "PU_reweight":True,
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
#"Pt_ll":{
#		"Data_value_dic":{"M_ll":True},
#		"MC_value_dic":{"M_ll":True},
#				"hist_name":"Pt_ll",
#				"hist_title":"Pt (Di-lepton)",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[48,x_emu_new,20,260],
#				"y_axis":["null","null"],
#				"x_label":['P_{T}^{ll} (GeV/c^{2})',0.1],
#				"y_label":['Event / 5 GeV',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"rapidity_ll":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"rapidity_ll",
#				"hist_title":"Pt (Di-lepton)",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[80,x_emu_new,-4,4],
#				"y_axis":["null","null"],
#				"x_label":['Rapidity^{ll}',0.1],
#				"y_label":['Event / 1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"phi_ll":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"phi_ll",
#				"hist_title":"Pt (Di-lepton)",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[35,x_emu_new,-3.5,3.5],
#				"y_axis":["null","null"],
#				"x_label":['#phi^{ll} ',0.1],
#				"y_label":['Event / 0.2',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"deltaR_ll":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"deltaR_ll",
#				"hist_title":"Pt (Di-lepton)",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[120,x_emu_new,0,6],
#				"y_axis":["null","null"],
#				"x_label":['#Delta R(l,l)',0.1],
#				"y_label":['Event / 0.05',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"delta_eta_ll":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"delta_eta_ll",
#				"hist_title":"",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[51,x_emu_new,0,5.1],
#				"y_axis":["null","null"],
#				"x_label":['#Delta #eta^{(l,l)} ',0.1],
#				"y_label":['Event / 0.1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"delta_phi_ll":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"delta_phi_ll",
#				"hist_title":"",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[35,x_emu_new,0,3.5],
#				"y_axis":["null","null"],
#				"x_label":['#Delta #phi^{(l,l)} ',0.1],
#				"y_label":['Event / 0.1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"Heep_Et":{
#		"Data_value_dic":{"ele_Et":True},
#		"MC_value_dic":{"ele_Et":True},
#		"hist_name":"heep_et",
#		"hist_title":"Barrel Lepton Et",
#		"use_array":True,
#		"PU_reweight":True,
#		"hist_para":[30,x_pt,60,3200],
#		"y_axis":[0.0001,"null"],
#		"x_label":['Et^{Heep} (GeV)',0.1],
#		"y_label":['Event / 1 GeV',0.05],
#		"x_log":True,
#		"y_log":True,
#		"lenend":{
#                               "useLegend":True,
#                               "position":[],
#                               },
#               },
#"Heep_eta":{
#		"Data_value_dic":{"ele_eta":True},
#		"MC_value_dic":{"ele_eta":True},
#				"hist_name":"ele_eta",
#				"hist_title":"Leading Lepton #eta",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[51,x_emu_new,-2.55,2.55],
#				"y_axis":["null","null"],
#				"x_label":['#eta^{Heep}',0.1],
#				"y_label":['Event / 0.1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"Heep_phi":{
#		"Data_value_dic":{"ele_phi":True},
#		"MC_value_dic":{"ele_phi":True},
#				 "hist_name":"ele_phi",
#				"hist_title":"Leading Lepton #phi",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[35,x_emu_new,-3.5,3.5],
#				"y_axis":["null","null"],
#				"x_label":['#phi^{Heep}',0.1],
#				"y_label":['Event / 0.2',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"Muon_pt":{
#		"Data_value_dic":{"muon_pt":True},
#		"MC_value_dic":{"muon_pt":True},
#				"hist_name":"muon_pt",
#				"hist_title":"Sub-Leading Lepton Pt",
#				"use_array":True,
#				"PU_reweight":True,
#				"hist_para":[30,x_pt,60,3200],
#                		"y_axis":[0.0001,"null"],
#				"x_label":['P_{T}^{muon} (GeV)',0.1],
#				"y_label":['Event / 1 GeV',0.05],
#				"x_log":True,
#				"y_log":True,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"muon_eta":{
#		"Data_value_dic":{"muon_eta":True},
#		"MC_value_dic":{"muon_eta":True},
#				"hist_name":"muon_eta",
#				"hist_title":"sub_Leading Lepton #eta",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[51,x_emu_new,-2.55,2.55],
#				"y_axis":["null","null"],
#				"x_label":['#eta^{muon}',0.1],
#				"y_label":['Event / 0.1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"muon_phi":{
#		"Data_value_dic":{"muon_phi":True},
#		"MC_value_dic":{"muon_phi":True},
#				"hist_name":"muon_phi",
#				"hist_title":"sub-Leading Lepton #phi",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[35,x_emu_new,-3.5,3.5],
#				"y_axis":["null","null"],
#				"x_label":['#phi^{muon}',0.1],
#				"y_label":['Event / 0.2',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                }, 
#"MET_pt":{
#		"Data_value_dic":{"MET_Et":True},
#		"MC_value_dic":{"MET_Et":True},
#				"hist_name":"MET_Et",
#				"hist_title":"MET Pt",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[20,x_emu_new,0,200],
#				"y_axis":["null","null"],
#				"x_label":['MET (GeV)',0.1],
#				"y_label":['Event / 10 GeV',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"MET_phi":{
#		"Data_value_dic":{"MET_phi":True},
#		"MC_value_dic":{"MET_phi":True},
#				"hist_name":"MET_phi",
#				"hist_title":"MET #phi",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[35,x_emu_new,-3.5,3.5],
#				"y_axis":["null","null"],
#				"x_label":['MET_{#phi}',0.1],
#				"y_label":['Event / 0.2',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"MET_significance":{
#		"Data_value_dic":{"MET_significance":True},
#		"MC_value_dic":{"MET_significance":True},
#				"hist_name":"MET_significance",
#				"hist_title":"MET significance",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[40,x_emu_new,0,20],
#				"y_axis":["null","null"],
#				"x_label":['MET_{significance}',0.1],
#				"y_label":['Event / 0.5',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"MET_T1Txy_pt":{
#		"Data_value_dic":{"MET_T1Txy_Pt":True},
#		"MC_value_dic":{"MET_T1Txy_Pt":True},
#				"hist_name":"MET_T1Txy_Pt",
#				"hist_title":"MET T1Txy Pt",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[20,x_emu_new,0,200],
#				"y_axis":["null","null"],
#				"x_label":['MET^{T1Txy} (GeV)',0.1],
#				"y_label":['Event / 10 GeV',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"MET_T1Txy_phi":{
#		"Data_value_dic":{"MET_T1Txy_phi":True},
#		"MC_value_dic":{"MET_T1Txy_phi":True},
#				"hist_name":"MET_T1Txy_phi",
#				"hist_title":"MET T1Txy #phi",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[35,x_emu_new,-3.5,3.5],
#				"y_axis":["null","null"],
#				"x_label":['MET^{T1Txy}_{#phi}',0.1],
#				"y_label":['Event / 0.2',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"MET_T1Txy_significance":{
#		"Data_value_dic":{"MET_T1Txy_significance":True},
#		"MC_value_dic":{"MET_T1Txy_significance":True},
#				"hist_name":"MET_T1Txy_significance",
#				"hist_title":"MET T1Txy significance",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[40,x_emu_new,0,20],
#				"y_axis":["null","null"],
#				"x_label":['MET^{T1Txy}_{significance}',0.1],
#				"y_label":['Event / 0.5',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"n_jet":{
#		"Data_value_dic":{"n_jet":True},
#		"MC_value_dic":{"n_jet":True},
#				"hist_name":"n_jet",
#				"hist_title":"Jet Multiplicity",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[10,x_emu_new,0,10],
#				"y_axis":["null","null"],
#				"x_label":['N_{jet}',0.1],
#				"y_label":['Event / 1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"n_bjet":{
#		"Data_value_dic":{"n_bjet":True},
#		"MC_value_dic":{"n_bjet":True},
#				"hist_name":"n_bjet",
#				"hist_title":"Jet Multiplicity",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[10,x_emu_new,0,10],
#				"y_axis":["null","null"],
#				"x_label":['N_{b jet}',0.1],
#				"y_label":['Event / 1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"n_jet_bjet":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"n_jet_bjet",
#				"hist_title":"Jet Multiplicity",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[16,x_emu_new,0,16],
#				"y_axis":["null","null"],
#				"x_label":['N_{(jet, b jet)}',0.1],
#				"y_label":['Event / 1',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"HT":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"Ht",
#				"hist_title":"Ht",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[49,x_emu_new,10,500],
#				"y_axis":["null","null"],
#				"x_label":['HT (GeV)',0.1],
#				"y_label":['Event / 10 GeV',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
#"sys_HT":{
#		"Data_value_dic":{"":True},
#		"MC_value_dic":{"":True},
#				"hist_name":"sys_Ht",
#				"hist_title":"sys Ht",
#				"use_array":False,
#				"PU_reweight":True,
#				"hist_para":[49,x_emu_new,10,500],
#				"y_axis":["null","null"],
#				"x_label":['HT^{sys} (GeV)',0.1],
#				"y_label":['Event / 10 GeV',0.05],
#				"x_log":False,
#				"y_log":False,
#				"lenend":{
#                                "useLegend":True,
#                                "position":[],
#                                },
#                },
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
		"Data_value_dic":{"M_emu":True},
		"MC_value_dic":{"M_emu":True},
		"hist_name":"M_bin",
		"hist_title":"Number event(with PU reweight)",
		"use_array":True,
		"PU_reweight":True,
		"hist_para":[len(mass_bin)-1,mass_bin,0,50],
		"y_axis":["null","null"],
		"x_label":['M_{e#mu}',0.1],
		"y_label":['Event/GeV ',0.05],
		"x_log":False,
		"y_log":True,
		"lenend":{
				"useLegend":True,
				"position":[],
				},
		},
}

#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
input_dic={
"data":{"isFromRoot":True,
		"input_file":"data_2016_SingleMuon_SinglePhoton2.root",
		"isData":True,
		"isFake":False,
		"useToNorm":True,
		"lumi":35867,
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
"_ttbar_all":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_all.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":87.31,
		"N_total": 0.0,
		"Raw_total":78353860,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_1":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_1.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":87.31,
		"N_total": 0.0,
		"Raw_total":78353860,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_2":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_2.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.326,
		"N_total": 0.0,
		"Raw_total":199979,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_3":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_3.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.0326,
		"N_total": 0.0,
		"Raw_total":199773,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_4":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_4.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.00305,
		"N_total": 0.0,
		"Raw_total":199956,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ttbar_5":{
		"isFromRoot":True,
		"input_file":"ttbar2l2u_5.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.000174,
		"N_total": 0.0,
		"Raw_total":40816,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_1":{
		"isFromRoot":True,
		"input_file":"DYToLL_1.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":18610,
		"N_total": 0.0,
		"Raw_total":29168419,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_all":{
		"isFromRoot":True,
		"input_file":"DYToLL_all.root",
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
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_2":{
		"isFromRoot":True,
		"input_file":"DYToLL_2.root",
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
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_3":{
		"isFromRoot":True,
		"input_file":"DYToLL_3.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.4064,
		"N_total": 0.0,
		"Raw_total":151168,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_4":{
		"isFromRoot":True,
		"input_file":"DYToLL_4.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.241,
		"N_total": 0.0,
		"Raw_total":144087,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_5":{
		"isFromRoot":True,
		"input_file":"DYToLL_5.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.03606,
		"N_total": 0.0,
		"Raw_total":136874,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_6":{
		"isFromRoot":True,
		"input_file":"DYToLL_6.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.03032,
		"N_total": 0.0,
		"Raw_total":131568,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_7":{
		"isFromRoot":True,
		"input_file":"DYToLL_7.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.01924,
		"N_total": 0.0,
		"Raw_total":119990,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_8":{
		"isFromRoot":True,
		"input_file":"DYToLL_8.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.002181,
		"N_total": 0.0,
		"Raw_total":111668,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_DYToLL_9":{
		"isFromRoot":True,
		"input_file":"DYToLL_9.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.0005129,
		"N_total": 0.0,
		"Raw_total":101266,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW_all":{
		"isFromRoot":True,
		"input_file":"WW_all.root",
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
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW1":{
		"isFromRoot":True,
		"input_file":"WW1.root",
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
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW2":{
		"isFromRoot":True,
		"input_file":"WW2.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":1.386,
		"N_total": 0.0,
		"Raw_total":199991,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW3":{
		"isFromRoot":True,
		"input_file":"WW3.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.05665,
		"N_total": 0.0,
		"Raw_total":199988,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW4":{
		"isFromRoot":True,
		"input_file":"WW4.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.003557,
		"N_total": 0.0,
		"Raw_total":199981,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WW5":{
		"isFromRoot":True,
		"input_file":"WW5.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.00005395,
		"N_total": 0.0,
		"Raw_total":38969,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_WZ":{
		"isFromRoot":True,
		"input_file":"WZ.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":47.13,
		"N_total": 0.0,
		"Raw_total":921116,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ZZ":{
		"isFromRoot":True,
		"input_file":"ZZ.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":16.523,
		"N_total": 0.0,
		"Raw_total":990051,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"_ST":{
		"isFromRoot":True,
		"input_file":"ST.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":71.2,
		"N_total": 0.0,
		"Raw_total":6806148+6856399,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_data":{
		"isFromRoot":True,
		"input_file":"fk_data_2016_SingleMuon_SinglePhoton2.root",
		"isData":True,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":1.0,
		"N_total": 0.0,
		"Raw_total":0.0,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":1,
		"hist":{},
		"isUpdate":False
		},
"fk_ttbar":{
		"isFromRoot":True,
		"input_file":"fk_ttbar.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":831.76,
		"N_total": 0.0,
		"Raw_total":75897555,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_ttbar_1":{
		"isFromRoot":True,
		"input_file":"fk_ttbar2l2u_1.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":87.31,
		"N_total": 0.0,
		"Raw_total":78353860,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_ttbar_2":{
		"isFromRoot":True,
		"input_file":"fk_ttbar2l2u_2.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.326,
		"N_total": 0.0,
		"Raw_total":199979,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_ttbar_3":{
		"isFromRoot":True,
		"input_file":"fk_ttbar2l2u_3.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.0326,
		"N_total": 0.0,
		"Raw_total":199773,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_ttbar_4":{
		"isFromRoot":True,
		"input_file":"fk_ttbar2l2u_4.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.00305,
		"N_total": 0.0,
		"Raw_total":199956,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_ttbar_5":{
		"isFromRoot":True,
		"input_file":"fk_ttbar2l2u_5.root",
		"isData":False,
		"isFake":False,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.000174,
		"N_total": 0.0,
		"Raw_total":40816,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":50,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":isUpdate
		},
"fk_DYToLL_1":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_1.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":18610,
		"N_total": 0.0,
		"Raw_total":29168419,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_2":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_2.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":5765.4,
		"N_total": 0.0,
		"Raw_total":81589928,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_3":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_3.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.4064,
		"N_total": 0.0,
		"Raw_total":151168,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_4":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_4.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.241,
		"N_total": 0.0,
		"Raw_total":144087,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_5":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_5.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.03606,
		"N_total": 0.0,
		"Raw_total":136874,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_6":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_6.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.03032,
		"N_total": 0.0,
		"Raw_total":131568,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_7":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_7.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.01924,
		"N_total": 0.0,
		"Raw_total":119990,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_8":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_8.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.002181,
		"N_total": 0.0,
		"Raw_total":111668,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_9":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_9.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.0005129,
		"N_total": 0.0,
		"Raw_total":101266,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_DYToLL_all":{
		"isFromRoot":True,
		"input_file":"fk_DYToLL_all.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":5765.4,
		"N_total": 0.0,
		"Raw_total":81589928,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":5,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_WW_all":{
		"isFromRoot":True,
		"input_file":"fk_WW_all.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":12.178,
		"N_total": 0.0,
		"Raw_total":19989560,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_WW1":{
		"isFromRoot":True,
		"input_file":"fk_WW1.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":12.178,
		"N_total": 0.0,
		"Raw_total":19989560,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_WW2":{
		"isFromRoot":True,
		"input_file":"fk_WW2.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":1.386,
		"N_total": 0.0,
		"Raw_total":199991,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_WW3":{
		"isFromRoot":True,
		"input_file":"fk_WW3.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.05665,
		"N_total": 0.0,
		"Raw_total":199988,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_WW4":{
		"isFromRoot":True,
		"input_file":"fk_WW4.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.003557,
		"N_total": 0.0,
		"Raw_total":199981,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_WW5":{
		"isFromRoot":True,
		"input_file":"fk_WW5.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":0.00005395,
		"N_total": 0.0,
		"Raw_total":38968,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_WZ":{
		"isFromRoot":True,
		"input_file":"fk_WZ.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":47.13,
		"N_total": 0.0,
		"Raw_total":921116,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_ZZ":{
		"isFromRoot":True,
		"input_file":"fk_ZZ.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":16.523,
		"N_total": 0.0,
		"Raw_total":990051,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":30,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
"fk_ST":{
		"isFromRoot":True,
		"input_file":"fk_ST.root",
		"isData":False,
		"isFake":True,
		"useToNorm":False,
		"lumi":0.0,
		"Xsection":71.2,
		"N_total": 0.0,
		"Raw_total":6806148+6856399,
		"N_norm":1.0,
		"Norm_Factor":1,
		"Fill_color":70,
		"weight_factor":-1,
		"hist":{},
		"isUpdate":False
		},
}
