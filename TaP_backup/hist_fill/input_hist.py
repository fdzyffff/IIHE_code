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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
global_branch_dic = {}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_trig_exist(branch_name):
	if not (branch_name in global_branch_dic):
		global_branch_dic[branch_name] = False
		print "check trig error: %s"%(branch_name)
	return global_branch_dic[branch_name]

def match_trigger_part(trig_eta, trig_phi, obj_eta, obj_phi, dr_in):
	tmp_trig_p4 = ROOT.TLorentzVector()
	tmp_trig_p4.SetPtEtaPhiM(10.0, trig_eta, trig_phi, 1.0)
	tmp_obj_p4 = ROOT.TLorentzVector()
	tmp_obj_p4.SetPtEtaPhiM(10.0, obj_eta, obj_phi, 1.0)
	if tmp_trig_p4.DeltaR(tmp_obj_p4) <= dr_in:
		return True
	return False

def match_trigger(event, trig_eta_str, trig_phi_str, obj_eta_str, obj_phi_str, dr_in):
	if check_trig_exist(trig_eta_str) and check_trig_exist(trig_phi_str):
		trig_eta_vector = getattr(event, trig_eta_str)
		trig_phi_vector = getattr(event, trig_phi_str)
		obj_eta = getattr(event, obj_eta_str)
		obj_phi = getattr(event, obj_phi_str)
		for i in range(len(trig_eta_vector)):
			if match_trigger_part(trig_eta_vector[i], trig_phi_vector[i], obj_eta, obj_phi, dr_in):
				return True
	return False

def pass_trigger(event, trigger_name):
	if check_trig_exist(trigger_name):
		if getattr(event, trigger_name):
			return True
	return False

def map_fill_hist(sample, event, sample_hist_dic, hist_dic, path):
	hist_cut_dic = hist_dic[path]["cut_dic"]
	for cut in hist_cut_dic:
		pass_cut = False
		isTag = False
		isProbe = False
		isProbe_fire = False
		fill_value = -999
	
		if "pvz" in path:
			exec 'pass_cut = %s'%(hist_cut_dic[cut])
			if not pass_cut:continue
			exec 'isTag = %s'%(hist_dic[path]["isTag"])
			exec 'isProbe = %s'%(hist_dic[path]["isProbe"])
			exec 'isProbe_fire = %s'%(hist_dic[path]["isProbe_fire"])
			fill_value = getattr(event,'pv_z')[0]
			#print fill_value
		else:
			exec 'pass_cut = %s'%(hist_cut_dic[cut])
			if not pass_cut:continue
			exec 'isTag = %s'%(hist_dic[path]["isTag"])
			exec 'isProbe = %s'%(hist_dic[path]["isProbe"])
			exec 'isProbe_fire = %s'%(hist_dic[path]["isProbe_fire"])
			exec 'fill_value = %s'%(hist_dic[path]["fill_value"])
		if pass_cut and isTag and isProbe:
			sample_hist_dic[path+cut]["h_denominator"].Fill(fill_value)
			if isProbe_fire:
				sample_hist_dic[path+cut]["h_numerator"].Fill(fill_value)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x_array_1 = array('f')
n_index = 0
x_array_1.append(25)
for i in range(30,200,5):
	x_array_1.append(i)
	n_index += 1
for i in range(200,1100,100):
	x_array_1.append(i)
	n_index += 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hist_list = ["h_numerator", "h_denominator"]
global_hist_dic = {}
hist_dic={
#DoubleEle33 trigger eff
"DouEle33Et_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle33Et_",
	"use_array":False,
	"hist_para":[80,x_array_1,30,50],
	"hist":{},
	},
"DouEle33ID_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle33ID_",
	"use_array":False,
	"hist_para":[31,x_array_1,35,140],
	"hist":{},
	},
"DouEle33_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle33_",
	"use_array":False,
	"hist_para":[80,x_array_1,30,50],
	"hist":{},
	},
"DouEle33Et_23_":{
	"cut_dic":{
		"runB":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runB'",
		"runC":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runC'",
		"runD":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runD'",
		"runE":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runE'",
		"runF":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runF'",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle33Et_23_",
	"use_array":False,
	"hist_para":[80,x_array_1,30,50],
	"hist":{},
	},
"DouEle33ID_23_":{
	"cut_dic":{
		"runB":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runB'",
		"runC":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runC'",
		"runD":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runD'",
		"runE":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runE'",
		"runF":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runF'",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle33ID_23_",
	"use_array":False,
	"hist_para":[31,x_array_1,35,140],
	"hist":{},
	},
"DouEle33_23_":{
	"cut_dic":{
		"runB":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runB'",
		"runC":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runC'",
		"runD":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runD'",
		"runE":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runE'",
		"runF":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runF'",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle33_23_",
	"use_array":False,
	"hist_para":[80,x_array_1,30,50],
	"hist":{},
	},
#DoubleEle33 vs pvn
"DouEle33ID_pvn_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'pv_n')",
	"hist_name":"DouEle33ID_pvn_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,100],
	"hist":{},
	},
#DoubleEle33 vs lumi
"DouEle33ID_lumi_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		"304209":"getattr(event,'ev_run') == 304209",
		"304797":"getattr(event,'ev_run') == 304797",
		"305044":"getattr(event,'ev_run') == 305044",
		"305046":"getattr(event,'ev_run') == 305046",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltEle33CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEG33EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle33_CaloIdL_MW_hltDiEle33CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'ev_luminosityBlock')",
	"hist_name":"DouEle33ID_lumi_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,1000],
	"hist":{},
	},
#DoubleEle25 trigger eff
"DouEle25Et_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle25Et_",
	"use_array":False,
	"hist_para":[80,x_array_1,20,40],
	"hist":{},
	},
"DouEle25ID_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle25ID_",
	"use_array":False,
	"hist_para":[31,x_array_1,25,130],
	"hist":{},
	},
"DouEle25_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle25_",
	"use_array":False,
	"hist_para":[80,x_array_1,20,40],
	"hist":{},
	},
"DouEle25Et_23_":{
	"cut_dic":{
		#"runB":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runB'",
		#"runC":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runC'",
		"runD":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runD'",
		"runE":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runE'",
		"runF":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runF'",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle25Et_",
	"use_array":False,
	"hist_para":[80,x_array_1,20,40],
	"hist":{},
	},
"DouEle25ID_23_":{
	"cut_dic":{
		#"runB":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runB'",
		#"runC":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runC'",
		"runD":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runD'",
		"runE":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runE'",
		"runF":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runF'",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle25ID_",
	"use_array":False,
	"hist_para":[31,x_array_1,25,130],
	"hist":{},
	},
"DouEle25_23_":{
	"cut_dic":{
		#"runB":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runB'",
		#"runC":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runC'",
		"runD":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runD'",
		"runE":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runE'",
		"runF":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5) and sample == 'runF'",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"DouEle25_",
	"use_array":False,
	"hist_para":[80,x_array_1,20,40],
	"hist":{},
	},
#DouEle25 vs pv_n
"DouEle25ID_pvn_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'pv_n')",
	"hist_name":"DouEle25ID_pvn_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,100],
	"hist":{},
	},
#DouEle25 vs lumi
"DouEle25ID_lumi_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		"304209":"getattr(event,'ev_run') == 304209",
		"304797":"getattr(event,'ev_run') == 304797",
		"305044":"getattr(event,'ev_run') == 305044",
		"305046":"getattr(event,'ev_run') == 305046",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'ev_luminosityBlock')",
	"hist_name":"DouEle25ID_lumi_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,1000],
	"hist":{},
	},
"DouEle25ID_pvn_DiEle27_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	#"isTag":"True",
	"isTag":"sample != 'runB' and sample != 'runC' ",
	"isProbe":"match_trigger(event,'trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_eta','trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_eta','trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_phi','probe_eta','probe_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	#"isProbe_fire":"(match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)) or (match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','probe_eta','probe_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','t_eta','t_phi',0.1))",
	"isProbe_fire":"pass_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_accept')",
	"fill_value":"getattr(event,'pv_n')",
	"hist_name":"DouEle25ID_vs_pvn_DiEle27_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,100],
	"hist":{},
	},
#DouEle25 given DiEle27CaloOnly vs pv_z
"DouEle25ID_pvz_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"sample != 'runB' and sample != 'runC' ",
	"isProbe":"match_trigger(event,'trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_eta','trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_eta','trig_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_hltDiEle27L1DoubleEGWPTightHcalIsoFilter_phi','probe_eta','probe_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi','probe_eta','probe_phi',0.1)",
	#"isProbe_fire":"(match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','t_eta','t_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','probe_eta','probe_phi',0.1)) or (match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi','probe_eta','probe_phi',0.1) and match_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta','trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi','t_eta','t_phi',0.1))",
	"isProbe_fire":"pass_trigger(event,'trig_HLT_DoubleEle25_CaloIdL_MW_accept')",
	"fill_value":"getattr(event,'pv_z')",
	"hist_name":"DouEle25ID_vs_pvz_DiEle27_",
	"use_array":False,
	"hist_para":[60,x_array_1,-20,20],
	"hist":{},
	},
#HLT_Ele32_WPTight
"Ele32Et_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele32Et_",
	"use_array":False,
	"hist_para":[50,x_array_1,25,125],
	"hist":{},
	},
"Ele32ID_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele32ID_",
	"use_array":False,
	"hist_para":[20,x_array_1,25,125],
	"hist":{},
	},
"Ele32_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele32_",
	"use_array":False,
	"hist_para":[50,x_array_1,25,125],
	"hist":{},
	},
"Ele32ID_pvn_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'pv_n')",
	"hist_name":"Ele32ID_pvn_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,100],
	"hist":{},
	},
#Ele32_WPTight vs lumi
"Ele32ID_lumi_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		"304209":"getattr(event,'ev_run') == 304209",
		"304797":"getattr(event,'ev_run') == 304797",
		"305044":"getattr(event,'ev_run') == 305044",
		"305046":"getattr(event,'ev_run') == 305046",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEG32L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta','trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'ev_luminosityBlock')",
	"hist_name":"Ele32ID_lumi_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,1000],
	"hist":{},
	},
#HLT_Ele35_WPTight
"Ele35Et_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele35Et_",
	"use_array":False,
	"hist_para":[50,x_array_1,25,125],
	"hist":{},
	},
"Ele35ID_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele35ID_",
	"use_array":True,
	"hist_para":[n_index,x_array_1,25,1000],
	"hist":{},
	},
"Ele35_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele35_",
	"use_array":False,
	"hist_para":[50,x_array_1,25,125],
	"hist":{},
	},
"Ele35ID_pvn_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'pv_n')",
	"hist_name":"Ele35ID_pvn_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,100],
	"hist":{},
	},
#Ele35_WPTight vs lumi
"Ele35ID_lumi_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		"304209":"getattr(event,'ev_run') == 304209",
		"304797":"getattr(event,'ev_run') == 304797",
		"305044":"getattr(event,'ev_run') == 305044",
		"305046":"getattr(event,'ev_run') == 305046",
		},
	"isTag":"getattr(event,'t_isTag') and match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','t_eta','t_phi',0.1)",
	"isProbe":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEG35L1SingleEGOrEtFilter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta','trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'ev_luminosityBlock')",
	"hist_name":"Ele35ID_lumi_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,1000],
	"hist":{},
	},
#Ele23_Ele12
"Ele23_Ele12_EtLeg1_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele23_Ele12_EtLeg1_",
	"use_array":False,
	"hist_para":[80,x_array_1,20,40],
	"hist":{},
	},
"Ele23_Ele12_IDLeg1_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele23_Ele12_IDLeg1_",
	"use_array":False,
	"hist_para":[16,x_array_1,20,100],
	"hist":{},
	},
"Ele23_Ele12_Leg1_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele23_Ele12_Leg1_",
	"use_array":False,
	"hist_para":[80,x_array_1,20,40],
	"hist":{},
	},
"Ele23_Ele12_EtLeg2_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele23_Ele12_EtLeg2_",
	"use_array":False,
	"hist_para":[80,x_array_1,8,28],
	"hist":{},
	},
"Ele23_Ele12_IDLeg2_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele23_Ele12_IDLeg2_",
	"use_array":False,
	"hist_para":[18,x_array_1,10,100],
	"hist":{},
	},
"Ele23_Ele12_Leg2_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"True",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'probe_pt')",
	"hist_name":"Ele23_Ele12_Leg2_",
	"use_array":False,
	"hist_para":[80,x_array_1,8,28],
	"hist":{},
	},
#Ele23_Ele12 vs pvn
"Ele23_Ele12_Leg1ID_pvn_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'pv_n')",
	"hist_name":"Ele23_Ele12_Leg1ID_pvn_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,100],
	"hist":{},
	},
"Ele23_Ele12_Leg2ID_pvn_":{
	"cut_dic":{
		"11":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 0.79)",
		"12":"(0.79 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.1)",
		"13":"(1.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"21":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.7)",
		"22":"(1.7 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.1)",
		"23":"(2.1 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'pv_n')",
	"hist_name":"Ele23_Ele12_Leg2ID_pvn_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,100],
	"hist":{},
	},
#Ele23_Ele12 vs lumi
"Ele23_Ele12_Leg1ID_lumi_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		"304209":"getattr(event,'ev_run') == 304209",
		"304797":"getattr(event,'ev_run') == 304797",
		"305044":"getattr(event,'ev_run') == 305044",
		"305046":"getattr(event,'ev_run') == 305046",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'ev_luminosityBlock')",
	"hist_name":"Ele23_Ele12_Leg1ID_lumi_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,1000],
	"hist":{},
	},
"Ele23_Ele12_Leg2ID_lumi_":{
	"cut_dic":{
		"1":"(0.0 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 1.4442)",
		"2":"(1.566 <= abs(getattr(event,'probe_sc_eta')) and abs(getattr(event,'probe_sc_eta')) < 2.5)",
		"304209":"getattr(event,'ev_run') == 304209",
		"304797":"getattr(event,'ev_run') == 304797",
		"305044":"getattr(event,'ev_run') == 305044",
		"305046":"getattr(event,'ev_run') == 305046",
		},
	"isTag":"getattr(event,'t_isTag') and True",
	"isProbe":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"isProbe_fire":"match_trigger(event,'trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_eta','trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter_phi','probe_eta','probe_phi',0.1)",
	"fill_value":"getattr(event,'ev_luminosityBlock')",
	"hist_name":"Ele23_Ele12_Leg2ID_lumi_",
	"use_array":False,
	"hist_para":[100,x_array_1,0,1000],
	"hist":{},
	},
}
