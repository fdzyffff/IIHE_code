import ROOT
import os
from optparse import OptionParser
from array import array
from math import *
from optparse import OptionParser
from input_sample import *


def delta_phi(phi_1, phi_2):
    PI = 3.1415926
    delta_phi = fabs(phi_1 - phi_2)
    if delta_phi > PI:delta_phi = 2*PI - delta_phi
    return delta_phi

def Load_json(dic_name):
        return eval(open(dic_name).read().replace("\n",""))

def Get_lep_SF(lep_pt,lep_eta,lep_isE,lep_isMu):
        lep_SF = 0.0
        if lep_isE:
                lep_SF = Get_ele_SF(lep_pt,lep_eta)
        elif lep_isMu:
                lep_SF = Get_mu_SF(lep_pt,lep_eta)
        if lep_SF == 0.0:print 1/0
        return lep_SF

def constraint_float(input_x, l_limit = "null", h_limit = "null"):
        if h_limit != "null":
                if input_x > h_limit:
                        return h_limit
        if l_limit != "null":
                if input_x < l_limit:
                        return l_limit
        return input_x

def Get_ele_SF(lep_pt,lep_eta):
        ele_SF = 1.0
        ele_SF *= Get_SF_2D(dic_Ele_Tracking_pt_eta, constraint_float(lep_pt,25,2000), lep_eta)
        ele_SF *= Get_SF_2D(dic_Ele_ID_ISO_pt_eta, constraint_float(lep_pt,0,400), lep_eta)
        return ele_SF

def Get_mu_SF(lep_pt,lep_eta):
        mu_SF = 1.0
        mu_SF *= Get_SF_1D(dic_Muon_Tracking_eta, lep_eta)
        mu_SF *= Get_SF_2D(dic_Muon_ID_pt_Abseta, constraint_float(lep_pt,0,119), fabs(lep_eta))
        mu_SF *= Get_SF_2D(dic_Muon_ISO_pt_Abseta, constraint_float(lep_pt,0,119), fabs(lep_eta))
        return mu_SF

def Get_SF_2D(dic_in, pt_in, eta_in):
        pt = pt_in
        eta = eta_in
        eff = 1.0
        for (pt_l, pt_u) in dic_in:
                if pt>=pt_l and pt<pt_u:
                        for (eta_l, eta_u) in dic_in[(pt_l,pt_u)]:
                                if eta>=eta_l and eta<eta_u:
                                        eff = dic_in[(pt_l,pt_u)][(eta_l,eta_u)]
                                        return eff
        return eff

def Get_SF_1D(dic_in, value_in):
        value = value_in
        eff = 1.0
        for (value_l, value_u) in dic_in:
                if value>=value_l and value<value_u:
                        eff = dic_in[(value_l,value_u)]
                        return eff
        return eff

def get_value_dic(event,value_dic):
    for path in value_dic:
        value_dic[path] = 0
    jet_pt_vector = getattr(event,"jet_pt")
    jet_eta_vector = getattr(event,"jet_eta")
    jet_phi_vector = getattr(event,"jet_phi")
    jet_energy_vector = getattr(event,"jet_energy")
    jet_ID_vector = getattr(event,"jet_IDLoose")
    jet_CSVv2_vector = getattr(event,"jet_CSVv2")
    jet_p4_vector = []
    jet_p4 = ROOT.TLorentzVector()
    j1_p4 = ROOT.TLorentzVector()
    j1_p4.SetPtEtaPhiE(0,0,0,0)
    j2_p4 = ROOT.TLorentzVector()
    j2_p4.SetPtEtaPhiE(0,0,0,0)
    for i in range(len(jet_pt_vector)):
        if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
            tmp_jet_p4 = ROOT.TLorentzVector()
            tmp_jet_p4.SetPtEtaPhiE(jet_pt_vector[i], jet_eta_vector[i], jet_phi_vector[i], jet_energy_vector[i])
            if tmp_jet_p4.Pt()>j1_p4.Pt():
                j2_p4 = j1_p4
                j1_p4.SetPtEtaPhiE(jet_pt_vector[i], jet_eta_vector[i], jet_phi_vector[i], jet_energy_vector[i])
            elif tmp_jet_p4>j2_p4.Pt():
                j2_p4.SetPtEtaPhiE(jet_pt_vector[i], jet_eta_vector[i], jet_phi_vector[i], jet_energy_vector[i])
            jet_p4_vector.append(tmp_jet_p4)
            jet_p4 = jet_p4 + tmp_jet_p4
    if len(jet_p4_vector) < 1:jet_p4.SetPtEtaPhiE(0,0,0,0)
    MET_p4 = ROOT.TLorentzVector()
    MET_p4.SetPtEtaPhiM(getattr(event, "MET_T1Txy_Pt"), 0.0, getattr(event, "MET_T1Txy_phi"), 0.0)
    l1_p4 = ROOT.TLorentzVector()
    l1_p4.SetPtEtaPhiM(getattr(event, "leading_pt"), getattr(event, "leading_eta"), getattr(event, "leading_phi"), getattr(event, "leading_mass"))
    l2_p4 = ROOT.TLorentzVector()
    l2_p4.SetPtEtaPhiM(getattr(event, "sub_leading_pt"), getattr(event, "sub_leading_eta"), getattr(event, "sub_leading_phi"), getattr(event, "sub_leading_mass"))

    #PT_ll_MET_j1
    value_dic["PT_ll_MET_j1"] = (l1_p4 + l2_p4 + MET_p4 + j1_p4).Pt() 
    #PT_ll_j1
    value_dic["PT_ll_j1"] = (l1_p4 + l2_p4 + j1_p4).Pt()
    #PT_ll
    value_dic["PT_ll"] = (l1_p4 + l2_p4).Pt()
    #PT_j1j2
    value_dic["PT_j1j2"] = (j1_p4 + j2_p4).Pt()
    #PT_ll_MET
    value_dic["PT_ll_MET"] = (l1_p4 + l2_p4 + MET_p4).Pt()
    #PT_ll_MET_j1j2
    value_dic["PT_ll_MET_j1j2"] = (l1_p4 + l2_p4 + MET_p4 + j1_p4 + j2_p4).Pt()
    #PT_l1j1
    value_dic["PT_l1j1"] = (l1_p4 + j1_p4).Pt()
    #ratio_PT_ll_MET_j1
    value_dic["ratio_PT_ll_MET_j1"] = (l1_p4 + l2_p4 + MET_p4 + j1_p4).Pt()/(l1_p4.Pt() + l2_p4.Pt() + MET_p4.Pt() + j1_p4.Pt())
    #PT_j2
    value_dic["PT_j2"] = j2_p4.Pt()
    #delta_PT_ll
    value_dic["delta_PT_ll"] = l1_p4.Pt() - l2_p4.Pt()
    #delta_PT_llj1_MET
    value_dic["delta_PT_llj1_MET"] = (l1_p4 + l2_p4 + j1_p4).Pt() - MET_p4.Pt()
    #delta_PT_MET_j1
    value_dic["delta_PT_MET_j1"] = MET_p4.Pt() - j1_p4.Pt()
    #delta_PT_llMET_j1
    value_dic["delta_PT_llMET_j1"] = (l1_p4 + l2_p4 + MET_p4).Pt() - j1_p4.Pt()
    #delta_PT_l2_j2
    value_dic["delta_PT_l2_j2"] = l2_p4.Pt() - j2_p4.Pt()
    #delta_phi_ll 
    value_dic["delta_phi_ll"] = delta_phi(l1_p4.Phi(), l2_p4.Phi()) 
    #delta_phi_ll_MET 
    value_dic["delta_phi_ll_MET"] = delta_phi((l1_p4 + l2_p4).Phi(), MET_p4.Phi())
    #delta_phi_j1_MET 
    value_dic["delta_phi_j1_MET"] = delta_phi(j1_p4.Phi(), MET_p4.Phi())
    #delta_phi_ll_j1 
    value_dic["delta_phi_ll_j1"] = delta_phi((l1_p4 + l2_p4).Phi(), j1_p4.Phi())
    #delta_phi_j1_j2 
    value_dic["delta_phi_j1_j2"] = delta_phi(j1_p4.Phi(), j2_p4.Phi())
    #deltaR_l1_j1
    value_dic["deltaR_l1_j1"] = l1_p4.DeltaR(j1_p4)
    #deltaR_l2_j1
    value_dic["deltaR_l2_j1"] = l2_p4.DeltaR(j1_p4)
    #deltaR_l1_j2
    value_dic["deltaR_l1_j2"] = l1_p4.DeltaR(j2_p4)
    #deltaR_l2_j2
    value_dic["deltaR_l2_j2"] = l2_p4.DeltaR(j2_p4)
    #deltaR_ll
    value_dic["deltaR_ll"] = l1_p4.DeltaR(l2_p4)
    #deltaR_ll_j1
    value_dic["deltaR_ll_j1"] = (l1_p4 + l2_p4).DeltaR(j1_p4)
    #deltaR_ll_j2
    value_dic["deltaR_ll_j2"] = (l1_p4 + l2_p4).DeltaR(j2_p4)
    #M_l1_j1
    value_dic["M_l1_j1"] = (l1_p4 + j1_p4).Mag()
    #M_l2_j1
    value_dic["M_l2_j1"] = (l2_p4 + j1_p4).Mag()
    #M_l1_j2
    value_dic["M_l1_j2"] = (l1_p4 + j2_p4).Mag()
    #M_l2_j2
    value_dic["M_l2_j2"] = (l2_p4 + j2_p4).Mag()
    #M_j1_j2
    value_dic["M_j1_j2"] = (j1_p4 + j2_p4).Mag()
    #M_ll
    value_dic["M_ll"] = (l1_p4 + l2_p4).Mag()
    #M_ll_j2
    value_dic["M_ll_j2"] = (l1_p4 + l2_p4 + j2_p4).Mag()
    #M_ll_j1j2
    value_dic["M_ll_j1j2"] = (l1_p4 + l2_p4 + j1_p4 + j2_p4).Mag()
    #MT_j1_MET
    value_dic["MT_j1_MET"] = sqrt(2.0 * j1_p4.Pt() * MET_p4.Pt() * (1.0 - cos(delta_phi(j1_p4.Phi(), MET_p4.Phi())))) 
    #E_M_llj2
    value_dic["E_M_llj2"] = (l1_p4 + l2_p4 + j2_p4).E()/(l1_p4 + l2_p4 + j2_p4).Mag()
    #ET_sys
    value_dic["ET_sys"] = 0
    #C_ll
    value_dic["C_ll"] = (l1_p4.Pt() + l2_p4.Pt())/(l1_p4 + l2_p4).E()
    #C_l1_j1
    value_dic["C_l1_j1"] = (l1_p4.Pt() + j1_p4.Pt())/(l1_p4 + j1_p4).E()
    #C_l2_j2
    value_dic["C_l2_j2"] = (l2_p4.Pt() + j2_p4.Pt())/(l2_p4 + j2_p4).E()
    #HT_sys
    value_dic["HT_sys"] = (l1_p4.Pt() + l2_p4.Pt() + MET_p4.Pt() + j1_p4.Pt())
    #HT_ll
    value_dic["HT_ll"] = (l1_p4.Pt() + l2_p4.Pt())

def get_weight_SF(event):
	event_weight = 1.0
	leading_SF_weight = 1.0
	sub_leading_SF_weight = 1.0
	pu_weight = 1.0
	fake_weight = 1.0
	bin_weight = 1.0
	Nvtx_weight = 1.0
	top_weight = 1.0
	jet_BtagSF_medium_weight = 1.0
	
	leading_pt = getattr(event,"leading_pt")
	leading_eta = getattr(event,"leading_eta")
	leading_isE = getattr(event,"leading_isE")
	leading_isMu = getattr(event,"leading_isMu")
	leading_SF_weight = Get_lep_SF(leading_pt,leading_eta,leading_isE,leading_isMu)
	sub_leading_pt = getattr(event,"sub_leading_pt")
	sub_leading_eta = getattr(event,"sub_leading_eta")
	sub_leading_isE = getattr(event,"sub_leading_isE")
	sub_leading_isMu = getattr(event,"sub_leading_isMu")
	sub_leading_SF_weight = Get_lep_SF(sub_leading_pt,sub_leading_eta,sub_leading_isE,sub_leading_isMu)
	
	#Nvtx_weight = Get_SF_1D(dic_Nvtx, getattr(event,"pv_n"))
	
	jet_BtagSF_medium_weight = getattr(event, "w_Btag_medium")
	pu_weight = getattr(event,"w_PU")
	event_weight = leading_SF_weight * sub_leading_SF_weight * pu_weight * fake_weight * top_weight * jet_BtagSF_medium_weight * Nvtx_weight
    	return event_weight

def get_weight_lumi(sample_dic):
	weight_lumi = 1.0
	if sample_dic["isData"]:
		weight_lumi = 1.0
	else:
		sample_dic["Norm_Factor"] = Target_lumi * sample_dic["Xsection"] / float(sample_dic["Raw_total"])
		weight_lumi = sample_dic["Norm_Factor"]
	return weight_lumi

def event_filter(sample_dic, input_file, output_file, cut, reverse=False):
#If reverse, will fill events not in list, if not reverse, will fill events in list
    print "### input file : %s"%(input_file)
    print "### output file : %s"%(output_file)

    file_in = ROOT.TFile(input_file,'READ')
    tree_in = file_in.Get('tap')
    n_event_1 = tree_in.GetEntries()

    file_out = ROOT.TFile(output_file,"RECREATE")
    tree_out = tree_in.CloneTree(0)
    weight_SF = array( 'f', [0] )
    weight_lumi = array( 'f', [0] )
    tree_out.Branch("weight_SF",	weight_SF,	"weight_SF/F")
    tree_out.Branch("weight_lumi",	weight_lumi,	"weight_lumi/F")
    value_dic = {
    "PT_ll_MET_j1":0,
    "PT_ll_j1":0,
    "PT_ll":0,
    "PT_j1j2":0,
    "PT_ll_MET":0,
    "PT_ll_MET_j1j2":0,
    "PT_l1j1":0,
    "ratio_PT_ll_MET_j1":0,
    "PT_j2":0,
    "delta_PT_ll":0,
    "delta_PT_llj1_MET":0,
    "delta_PT_MET_j1":0,
    "delta_PT_llMET_j1":0,
    "delta_PT_l2_j2":0,
    "delta_phi_ll":0,
    "delta_phi_ll_MET":0,
    "delta_phi_j1_MET":0,
    "delta_phi_ll_j1":0,
    "delta_phi_j1_j2":0,
    "deltaR_l1_j1":0,
    "deltaR_l2_j1":0,
    "deltaR_l1_j2":0,
    "deltaR_l2_j2":0,
    "deltaR_ll":0,
    "deltaR_ll_j1":0,
    "deltaR_ll_j2":0,
    "M_l1_j1":0,
    "M_l2_j1":0,
    "M_l1_j2":0,
    "M_l2_j2":0,
    "M_j1_j2":0,
    "M_ll":0,
    "M_l2_j1j2":0,
    "M_ll_j1j2":0,
    "MT_j1_MET":0,
    "E_M_llj2":0,
    "ET_sys":0,
    "C_ll":0,
    "C_l1_j1":0,
    "C_l2_j2":0,
    "HT_sys":0,
    "HT_ll":0,
    }
    PT_ll_MET_j1 = array( 'f', [0] )
    PT_ll_j1 = array( 'f', [0] )
    PT_ll = array( 'f', [0] )
    PT_j1j2 = array( 'f', [0] )
    PT_ll_MET = array( 'f', [0] )
    PT_ll_MET_j1j2 = array( 'f', [0] )
    PT_l1j1 = array( 'f', [0] )
    ratio_PT_ll_MET_j1 = array( 'f', [0] )
    PT_j2 = array( 'f', [0] )
    delta_PT_ll = array( 'f', [0] )
    delta_PT_llj1_MET = array( 'f', [0] )
    delta_PT_MET_j1 = array( 'f', [0] )
    delta_PT_llMET_j1 = array( 'f', [0] )
    delta_PT_l2_j2 = array( 'f', [0] )
    delta_phi_ll = array( 'f', [0] )
    delta_phi_ll_MET = array( 'f', [0] )
    delta_phi_j1_MET = array( 'f', [0] )
    delta_phi_ll_j1 = array( 'f', [0] )
    delta_phi_j1_j2 = array( 'f', [0] )
    deltaR_l1_j1 = array( 'f', [0] )
    deltaR_l2_j1 = array( 'f', [0] )
    deltaR_l1_j2 = array( 'f', [0] )
    deltaR_l2_j2 = array( 'f', [0] )
    deltaR_ll = array( 'f', [0] )
    deltaR_ll_j1 = array( 'f', [0] )
    deltaR_ll_j2 = array( 'f', [0] )
    M_l1_j1 = array( 'f', [0] )
    M_l2_j1 = array( 'f', [0] )
    M_l1_j2 = array( 'f', [0] )
    M_l2_j2 = array( 'f', [0] )
    M_j1_j2 = array( 'f', [0] )
    M_ll = array( 'f', [0] )
    M_l2_j1j2 = array( 'f', [0] )
    M_ll_j1j2 = array( 'f', [0] )
    MT_j1_MET = array( 'f', [0] )
    E_M_llj2 = array( 'f', [0] )
    ET_sys = array( 'f', [0] )
    C_ll = array( 'f', [0] )
    C_l1_j1 = array( 'f', [0] )
    C_l2_j2 = array( 'f', [0] )
    HT_sys = array( 'f', [0] )
    HT_ll = array( 'f', [0] )
    
    tree_out.Branch("PT_ll_MET_j1",	PT_ll_MET_j1,	"PT_ll_MET_j1/F")
    tree_out.Branch("PT_ll_j1",	PT_ll_j1,	"PT_ll_j1/F")
    tree_out.Branch("PT_ll",	PT_ll,	"PT_ll/F")
    tree_out.Branch("PT_j1j2",	PT_j1j2,	"PT_j1j2/F")
    tree_out.Branch("PT_ll_MET",	PT_ll_MET,	"PT_ll_MET/F")
    tree_out.Branch("PT_ll_MET_j1j2",	PT_ll_MET_j1j2,	"PT_ll_MET_j1j2/F")
    tree_out.Branch("PT_l1j1",	PT_l1j1,	"PT_l1j1/F")
    tree_out.Branch("ratio_PT_ll_MET_j1",	ratio_PT_ll_MET_j1,	"ratio_PT_ll_MET_j1/F")
    tree_out.Branch("PT_j2",	PT_j2,	"PT_j2/F")
    tree_out.Branch("delta_PT_ll",	delta_PT_ll,	"delta_PT_ll/F")
    tree_out.Branch("delta_PT_llj1_MET",	delta_PT_llj1_MET,	"delta_PT_llj1_MET/F")
    tree_out.Branch("delta_PT_MET_j1",	delta_PT_MET_j1,	"delta_PT_MET_j1/F")
    tree_out.Branch("delta_PT_llMET_j1",	delta_PT_llMET_j1,	"delta_PT_llMET_j1/F")
    tree_out.Branch("delta_PT_l2_j2",	delta_PT_l2_j2,	"delta_PT_l2_j2/F")
    tree_out.Branch("delta_phi_ll", delta_phi_ll,   "delta_phi_ll/F")
    tree_out.Branch("delta_phi_ll_MET", delta_phi_ll_MET,   "delta_phi_ll_MET/F")
    tree_out.Branch("delta_phi_j1_MET", delta_phi_j1_MET,   "delta_phi_j1_MET/F")
    tree_out.Branch("delta_phi_ll_j1",  delta_phi_ll_j1,    "delta_phi_ll_j1/F")
    tree_out.Branch("delta_phi_j1_j2",  delta_phi_j1_j2,    "delta_phi_j1_j2/F")
    tree_out.Branch("deltaR_l1_j1",	deltaR_l1_j1,	"deltaR_l1_j1/F")
    tree_out.Branch("deltaR_l2_j1",	deltaR_l2_j1,	"deltaR_l2_j1/F")
    tree_out.Branch("deltaR_l1_j2",	deltaR_l1_j2,	"deltaR_l1_j2/F")
    tree_out.Branch("deltaR_l2_j2",	deltaR_l2_j2,	"deltaR_l2_j2/F")
    tree_out.Branch("deltaR_ll",	deltaR_ll,	"deltaR_ll/F")
    tree_out.Branch("deltaR_ll_j1",	deltaR_ll_j1,	"deltaR_ll_j1/F")
    tree_out.Branch("deltaR_ll_j2",	deltaR_ll_j2,	"deltaR_ll_j2/F")
    tree_out.Branch("M_l1_j1",	M_l1_j1,	"M_l1_j1/F")
    tree_out.Branch("M_l2_j1",	M_l2_j1,	"M_l2_j1/F")
    tree_out.Branch("M_l1_j2",	M_l1_j2,	"M_l1_j2/F")
    tree_out.Branch("M_l2_j2",	M_l2_j2,	"M_l2_j2/F")
    tree_out.Branch("M_j1_j2",	M_j1_j2,	"M_j1_j2/F")
    tree_out.Branch("M_ll",	M_ll,	"M_ll/F")
    tree_out.Branch("M_l2_j1j2",	M_l2_j1j2,	"M_l2_j1j2/F")
    tree_out.Branch("M_ll_j1j2",	M_ll_j1j2,	"M_ll_j1j2/F")
    tree_out.Branch("MT_j1_MET",	MT_j1_MET,	"MT_j1_MET/F")
    tree_out.Branch("E_M_llj2",	E_M_llj2,	"E_M_llj2/F")
    tree_out.Branch("ET_sys",	ET_sys,	"ET_sys/F")
    tree_out.Branch("C_ll",	C_ll,	"C_ll/F")
    tree_out.Branch("C_l1_j1",	C_l1_j1,	"C_l1_j1/F")
    tree_out.Branch("C_l2_j2",	C_l2_j2,	"C_l2_j2/F")
    tree_out.Branch("HT_sys",	HT_sys,	"HT_sys/F")
    tree_out.Branch("HT_ll",	HT_ll,	"HT_ll/F")


    n_fired = 0
    n_pickup = 0
    n_process = -1
    weight_lumi[0] = get_weight_lumi(sample_dic)
    for event in tree_in:
	flag_store = False
        n_process += 1
        if n_process%100000 == 0:
            print "%d / %d processed"%(n_process, tree_in.GetEntries())
        exec 'passed = (%s)'%(cut_dic[cut])
        if not passed: continue
        tree_in.GetEntry(n_process)
        if tree_in.n_jet == 1 and tree_in.n_bjet == 1 and tree_in.leading_pt < 3000 and tree_in.sub_leading_pt < 3000:
            n_fired += 1
            if not reverse:
                flag_store = True
        else:
            if reverse:
                flag_store = True
        if flag_store:
            #weight
            if sample_dic["isData"]:
                weight_SF[0] = 1.0
            else:
                weight_SF[0] = get_weight_SF(event)
            #value
            get_value_dic(event, value_dic)

            PT_ll_MET_j1[0] = value_dic["PT_ll_MET_j1"]
            PT_ll_j1[0] = value_dic["PT_ll_j1"]
            PT_ll[0] = value_dic["PT_ll"]
            PT_j1j2[0] = value_dic["PT_j1j2"]
            PT_ll_MET[0] = value_dic["PT_ll_MET"]
            PT_ll_MET_j1j2[0] = value_dic["PT_ll_MET_j1j2"]
            PT_l1j1[0] = value_dic["PT_l1j1"]
            ratio_PT_ll_MET_j1[0] = value_dic["ratio_PT_ll_MET_j1"]
            PT_j2[0] = value_dic["PT_j2"]
            delta_PT_ll[0] = value_dic["delta_PT_ll"]
            delta_PT_llj1_MET[0] = value_dic["delta_PT_llj1_MET"]
            delta_PT_MET_j1[0] = value_dic["delta_PT_MET_j1"]
            delta_PT_llMET_j1[0] = value_dic["delta_PT_llMET_j1"]
            delta_PT_l2_j2[0] = value_dic["delta_PT_l2_j2"]
            delta_phi_ll[0] = value_dic["delta_phi_ll"] 
            delta_phi_ll_MET[0] = value_dic["delta_phi_ll_MET"] 
            delta_phi_j1_MET[0] = value_dic["delta_phi_j1_MET"] 
            delta_phi_ll_j1[0] = value_dic["delta_phi_ll_j1"] 
            delta_phi_j1_j2[0] = value_dic["delta_phi_j1_j2"] 
            deltaR_l1_j1[0] = value_dic["deltaR_l1_j1"]
            deltaR_l2_j1[0] = value_dic["deltaR_l2_j1"]
            deltaR_l1_j2[0] = value_dic["deltaR_l1_j2"]
            deltaR_l2_j2[0] = value_dic["deltaR_l2_j2"]
            deltaR_ll[0] = value_dic["deltaR_ll"]
            deltaR_ll_j1[0] = value_dic["deltaR_ll_j1"]
            deltaR_ll_j2[0] = value_dic["deltaR_ll_j2"]
            M_l1_j1[0] = value_dic["M_l1_j1"]
            M_l2_j1[0] = value_dic["M_l2_j1"]
            M_l1_j2[0] = value_dic["M_l1_j2"]
            M_l2_j2[0] = value_dic["M_l2_j2"]
            M_j1_j2[0] = value_dic["M_j1_j2"]
            M_ll[0] = value_dic["M_ll"]
            M_l2_j1j2[0] = value_dic["M_l2_j1j2"]
            M_ll_j1j2[0] = value_dic["M_ll_j1j2"]
            MT_j1_MET[0] = value_dic["MT_j1_MET"]
            E_M_llj2[0] = value_dic["E_M_llj2"]
            ET_sys[0] = value_dic["ET_sys"]
            C_ll[0] = value_dic["C_ll"]
            C_l1_j1[0] = value_dic["C_l1_j1"]
            C_l2_j2[0] = value_dic["C_l2_j2"]
            HT_sys[0] = value_dic["HT_sys"]
            HT_ll[0] = value_dic["HT_ll"]

            tree_out.Fill()
            n_pickup += 1

    tree_out.GetCurrentFile().Write()

    print "%d events in file: %s, %d fired, %d picked up"%(n_event_1, input_file, n_fired, n_pickup)

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")
(options,args)=parser.parse_args()


cut_dic={
'_EMu_80_step1_T2':'getattr(event,"isEMu") and getattr(event,"pass_trigger_EMu_step2")',
#'_EE_80_step1':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1")',
#'_MuMu_80_step1':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1")',

#'_EMu_80_step2':'getattr(event,"isEMu") and getattr(event,"pass_trigger_EMu") and getattr(event,"pass_step1") and (getattr(event,"M_ll") >= 80)',
#'_EE_80_step2':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101) and getattr(event,"MET_T1Txy_Pt")>=50',
#'_MuMu_80_step2':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101) and getattr(event,"MET_T1Txy_Pt") >=50',
}

cut = "_EMu_80_step1_T2"
Target_lumi = 35867.0

#event_filter(sample_dic, options.root_dir, options.output_name, cut)
if options.sample_name == "null":
	for sample in input_dic:
		event_filter(input_dic[sample], os.path.join("MC_data_80",input_dic[sample]["input_file"]), input_dic[sample]["input_file"][:-5]+"_1j1b"+input_dic[sample]["input_file"][-5:], cut)
else:
	sample_list = options.sample_name.replace(" ","").split(",")
	for sample in sample_list:
		event_filter(input_dic[sample], os.path.join("MC_data_80",input_dic[sample]["input_file"]), input_dic[sample]["input_file"][:-5]+"_1j1b"+input_dic[sample]["input_file"][-5:], cut)


