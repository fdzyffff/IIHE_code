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
    
def write_Trigger_EE():
    SF_dic = {}
    f1 = ROOT.TFile.Open("triggerSummary_ee.root","READ")
    h1 = f1.Get("scalefactor_eta2d_with_syst")
    for j in range(1,h1.GetYaxis().GetNbins()+1):
        tmp_pt_dic = {}
        eta1_u = h1.GetYaxis().GetBinUpEdge(j)
        eta1_l = h1.GetYaxis().GetBinLowEdge(j)
        for i in range(1,h1.GetXaxis().GetNbins()+1):
            eta2_u = h1.GetXaxis().GetBinUpEdge(i)
            eta2_l = h1.GetXaxis().GetBinLowEdge(i)
            tmp_pt_dic[(eta2_l,eta2_u)] = h1.GetBinContent(i,j)
        SF_dic[(eta1_l,eta1_u)]=tmp_pt_dic
    write_json(SF_dic,"Trigger_EE_json.txt")
    #print "*"*50
    return SF_dic

def write_Trigger_EMu():
    SF_dic = {}
    f1 = ROOT.TFile.Open("triggerSummary_emu.root","READ")
    h1 = f1.Get("scalefactor_eta2d_with_syst")
    for j in range(1,h1.GetYaxis().GetNbins()+1):
        tmp_pt_dic = {}
        eta1_u = h1.GetYaxis().GetBinUpEdge(j)
        eta1_l = h1.GetYaxis().GetBinLowEdge(j)
        for i in range(1,h1.GetXaxis().GetNbins()+1):
            eta2_u = h1.GetXaxis().GetBinUpEdge(i)
            eta2_l = h1.GetXaxis().GetBinLowEdge(i)
            tmp_pt_dic[(eta2_l,eta2_u)] = h1.GetBinContent(i,j)
        SF_dic[(eta1_l,eta1_u)]=tmp_pt_dic
    write_json(SF_dic,"Trigger_EMu_json.txt")
    #print "*"*50
    return SF_dic

def write_Trigger_MuMu():
    SF_dic = {}
    f1 = ROOT.TFile.Open("triggerSummary_mumu.root","READ")
    h1 = f1.Get("scalefactor_eta2d_with_syst")
    for j in range(1,h1.GetYaxis().GetNbins()+1):
        tmp_pt_dic = {}
        eta1_u = h1.GetYaxis().GetBinUpEdge(j)
        eta1_l = h1.GetYaxis().GetBinLowEdge(j)
        for i in range(1,h1.GetXaxis().GetNbins()+1):
            eta2_u = h1.GetXaxis().GetBinUpEdge(i)
            eta2_l = h1.GetXaxis().GetBinLowEdge(i)
            tmp_pt_dic[(eta2_l,eta2_u)] = h1.GetBinContent(i,j)
        SF_dic[(eta1_l,eta1_u)]=tmp_pt_dic
    write_json(SF_dic,"Trigger_MuMu_json.txt")
    #print "*"*50
    return SF_dic

write_Trigger_EE()
write_Trigger_EMu()
write_Trigger_MuMu()
