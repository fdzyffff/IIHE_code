import sys
import os
try:sys.path.append("C:/root_v5.34.30/bin")
except:pass
import ROOT
import math
import time

def write_json(dic_in,file_name):
    f1 = open(file_name,"w")
    f1.write(str(dic_in))

def Load_dic(dic_name):
    return eval(open(dic_name).read().replace("\n",""))
    
def writeTightMuonTracking():
    SF_dic = {}
    f1 = ROOT.TFile.Open("Muon/Tracking/Tracking_EfficienciesAndSF_BCDEFGH.root","READ")
    gr_1 = f1.Get("ratio_eff_eta3_dr030e030_corr")
    x = []
    y = []
    for i in range(gr_1.GetN()):
        x.append(gr_1.GetX()[i])
        y.append(gr_1.GetY()[i])
        if i == 0:
            eta_l = gr_1.GetX()[i] - gr_1.GetErrorXlow(i)
            eta_u = gr_1.GetX()[i] + gr_1.GetErrorXhigh(i)
        else:
            eta_l = gr_1.GetX()[i-1] + gr_1.GetErrorXhigh(i-1)
            eta_u = gr_1.GetX()[i] + gr_1.GetErrorXhigh(i)
        SF_dic[(eta_l,eta_u)] = gr_1.GetY()[i]
    write_json(SF_dic,"Muon/Tracking/Muon_Tracking_json.txt")
    #print "*"*50
    return SF_dic
    
def writeTightMuonISOSF():
    SF_dic = {}
    f1 = ROOT.TFile.Open("Muon/ISO/EfficienciesAndSF_BCDEF.root","READ")
    h1 = f1.Get("TightISO_TightID_pt_eta/pt_abseta_ratio")
    f2 = ROOT.TFile.Open("Muon/ISO/EfficienciesAndSF_GH.root","READ")
    h2 = f2.Get("TightISO_TightID_pt_eta/pt_abseta_ratio")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        tmp_pt_dic = {}
        pt_u = h1.GetXaxis().GetBinUpEdge(i)
        pt_l = h1.GetXaxis().GetBinLowEdge(i)
        for j in range(1,h1.GetYaxis().GetNbins()+1):
            eta_u = h1.GetYaxis().GetBinUpEdge(j)
            eta_l = h1.GetYaxis().GetBinLowEdge(j)
            tmp_pt_dic[(eta_l,eta_u)] = (20.0/36.0)*h1.GetBinContent(i,j) + (16.0/36.0)*h2.GetBinContent(i,j)
        #print str((pt_l,pt_u))
        #print str(tmp_pt_dic)
        SF_dic[(pt_l,pt_u)]=tmp_pt_dic
    write_json(SF_dic,"Muon/ISO/Muon_TightISO_json.txt")
    #print "*"*50
    return SF_dic
    
def writeTightMuonIDSF():
    SF_dic = {}
    f1 = ROOT.TFile.Open("Muon/ID/EfficienciesAndSF_BCDEF.root","READ")
    h1 = f1.Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/pt_abseta_ratio")
    f2 = ROOT.TFile.Open("Muon/ID/EfficienciesAndSF_GH.root","READ")
    h2 = f2.Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/pt_abseta_ratio")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        tmp_pt_dic = {}
        pt_u = h1.GetXaxis().GetBinUpEdge(i)
        pt_l = h1.GetXaxis().GetBinLowEdge(i)
        for j in range(1,h1.GetYaxis().GetNbins()+1):
            eta_u = h1.GetYaxis().GetBinUpEdge(j)
            eta_l = h1.GetYaxis().GetBinLowEdge(j)
            tmp_pt_dic[(eta_l,eta_u)] = (20.0/36.0)*h1.GetBinContent(i,j) + (16.0/36.0)*h2.GetBinContent(i,j)
        #print str((pt_l,pt_u))
        #print str(tmp_pt_dic)
        SF_dic[(pt_l,pt_u)]=tmp_pt_dic
    write_json(SF_dic,"Muon/ID/Muon_TIghtID_json.txt")
    #print "*"*50
    return SF_dic

def writeTightEleTrackingSF():
    SF_dic = {}
    f1 = ROOT.TFile.Open("Electron/Tracking/egammaEffi.txt_EGM2D.root","READ")
    h1 = f1.Get("EGamma_SF2D")
    for j in range(1,h1.GetYaxis().GetNbins()+1):
        tmp_pt_dic = {}
        pt_u = h1.GetYaxis().GetBinUpEdge(j)
        pt_l = h1.GetYaxis().GetBinLowEdge(j)
        for i in range(1,h1.GetXaxis().GetNbins()+1):
            eta_u = h1.GetXaxis().GetBinUpEdge(i)
            eta_l = h1.GetXaxis().GetBinLowEdge(i)
            tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(i,j)
        SF_dic[(pt_l,pt_u)]=tmp_pt_dic
    write_json(SF_dic,"Electron/Tracking/Ele_Tracking_json.txt")
    #print "*"*50
    return SF_dic

def writeTightEleIDISOSF():
    SF_dic = {}
    f1 = ROOT.TFile.Open("Electron/ID-ISO/egammaEffi.txt_EGM2D.root","READ")
    h1 = f1.Get("EGamma_SF2D")
    for j in range(1,h1.GetYaxis().GetNbins()+1):
        tmp_pt_dic = {}
        pt_u = h1.GetYaxis().GetBinUpEdge(j)
        pt_l = h1.GetYaxis().GetBinLowEdge(j)
        for i in range(1,h1.GetXaxis().GetNbins()+1):
            eta_u = h1.GetXaxis().GetBinUpEdge(i)
            eta_l = h1.GetXaxis().GetBinLowEdge(i)
            tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(i,j)
        SF_dic[(pt_l,pt_u)]=tmp_pt_dic
    write_json(SF_dic,"Electron/ID-ISO/Ele_ID-ISO_json.txt")
    #print "*"*50
    return SF_dic

writeTightMuonTracking()
writeTightMuonISOSF()
writeTightMuonIDSF()
writeTightEleTrackingSF()
writeTightEleIDISOSF()
