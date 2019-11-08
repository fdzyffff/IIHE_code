from input_setting import *

if GLOBAL_YEAR == "2016":
	from input_card_2016 import *
if GLOBAL_YEAR == "2017":
	from input_card_2017 import *
if GLOBAL_YEAR == "2018":
	from input_card_2018 import *

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
        "bin_weight":False,
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
                "bin_weight":False,
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