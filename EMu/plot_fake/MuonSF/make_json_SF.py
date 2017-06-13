import ROOT
import math

def write_json(dic_in,file_name):
    f1 = open(file_name,"w")
    f1.write(str(dic_in))


def GetMuonTriggerSF(pt_in,eta_in):
    pt = pt_in
    eta = math.fabs(eta_in)
    mark_pt_1 = -1
    mark_eta_1 = -1
    eff_1 = 1.0
    f1 = ROOT.TFile.Open("MuonSF/Trigger/SF_Cat1-5_2016RunB-H.root","READ")
    h1 = f1.Get("SF_Cat5_2016RunBCDEFGH")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        if pt < h1.GetXaxis().GetBinUpEdge(i):
            mark_pt_1 = i
            break
    for i in range(1,h1.GetYaxis().GetNbins()+1):
        if eta < h1.GetYaxis().GetBinUpEdge(i):
            mark_eta_1 = i
            break
    if mark_pt_1 < 0 or mark_eta_1 < 0:
        eff_1 = 1.0
    else:
        eff_1 = h1.GetBinContent(mark_pt_1,mark_eta_1)

    eff = eff_1
    return eff



def GetMuonISOSF(pt_in, eta_in):
    pt = pt_in
    eta = math.fabs(eta_in)
    mark_pt_1 = -1
    mark_eta_1 = -1
    eff_1 = 1.0
    f1 = ROOT.TFile.Open("MuonSF/ISO/EfficienciesAndSF_BCDEF.root","READ")
    h1 = f1.Get("tkLooseISO_highptID_newpt_eta/pair_ne_ratio")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        if pt < h1.GetXaxis().GetBinUpEdge(i):
            mark_pt_1 = i
            break
    for i in range(1,h1.GetYaxis().GetNbins()+1):
        if eta < h1.GetYaxis().GetBinUpEdge(i):
            mark_eta_1 = i
            break
    if mark_pt_1 < 0 or mark_eta_1 < 0:
        eff_1 = 1.0
    else:
        eff_1 = h1.GetBinContent(mark_pt_1,mark_eta_1)

    mark_pt_2 = -1
    mark_eta_2 = -1
    eff_2 = 1.0
    f2 = ROOT.TFile.Open("MuonSF/ISO/EfficienciesAndSF_GH.root","READ")
    h2 = f2.Get("tkLooseISO_highptID_newpt_eta/pair_ne_ratio")
    for i in range(1,h2.GetXaxis().GetNbins()+1):
        if pt < h2.GetXaxis().GetBinUpEdge(i):
            mark_pt_2 = i
            break
    for i in range(1,h2.GetYaxis().GetNbins()+1):
        if eta < h2.GetYaxis().GetBinUpEdge(i):
            mark_eta_2 = i
            break
    if mark_pt_2 < 0 or mark_eta_2 < 0:
        eff_2 = 1.0
    else:
        eff_2 = h2.GetBinContent(mark_pt_2,mark_eta_2)

    eff = (20.0/36.0)*eff_1 + (16.0/36.0)*eff_2
    return eff

def GetMuonIDSF(pt_in, eta_in):
    pt = pt_in
    eta = math.fabs(eta_in)
    mark_pt_1 = -1
    mark_eta_1 = -1
    eff_1 = 1.0
    f1 = ROOT.TFile.Open("MuonSF/ID/EfficienciesAndSF_BCDEF.root","READ")
    h1 = f1.Get("MC_NUM_HighPtID_DEN_genTracks_PAR_newpt_eta/pair_ne_ratio")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        if pt < h1.GetXaxis().GetBinUpEdge(i):
            mark_pt_1 = i
            break
    for i in range(1,h1.GetYaxis().GetNbins()+1):
        if eta < h1.GetYaxis().GetBinUpEdge(i):
            mark_eta_1 = i
            break
    if mark_pt_1 < 0 or mark_eta_1 < 0:
        eff_1 = 1.0
    else:
        eff_1 = h1.GetBinContent(mark_pt_1,mark_eta_1)

    mark_pt_2 = -1
    mark_eta_2 = -1
    eff_2 = 1.0
    f2 = ROOT.TFile.Open("MuonSF/ID/EfficienciesAndSF_GH.root","READ")
    h2 = f2.Get("MC_NUM_HighPtID_DEN_genTracks_PAR_newpt_eta/pair_ne_ratio")
    for i in range(1,h2.GetXaxis().GetNbins()+1):
        if pt < h2.GetXaxis().GetBinUpEdge(i):
            mark_pt_2 = i
            break
    for i in range(1,h2.GetYaxis().GetNbins()+1):
        if eta < h2.GetYaxis().GetBinUpEdge(i):
            mark_eta_2 = i
            break
    if mark_pt_2 < 0 or mark_eta_2 < 0:
        eff_2 = 1.0
    else:
        eff_2 = h2.GetBinContent(mark_pt_2,mark_eta_2)

    eff = (20.0/36.0)*eff_1 + (16.0/36.0)*eff_2
    return eff

def writeMuonTriggerSF():
    SF_dic = {}
    f1 = ROOT.TFile.Open("MuonSF/Trigger/SF_Cat1-5_2016RunB-H.root","READ")
    h1 = f1.Get("SF_Cat5_2016RunBCDEFGH")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        tmp_pt_dic = {}
        pt_u = h1.GetXaxis().GetBinUpEdge(i)
        pt_l = h1.GetXaxis().GetBinLowEdge(i)
        pt_in = h1.GetXaxis().GetBinCenter(i)
        for j in range(1,h1.GetYaxis().GetNbins()+1):
            eta_u = h1.GetYaxis().GetBinUpEdge(j)
            eta_l = h1.GetYaxis().GetBinLowEdge(j)
            eta_in = h1.GetYaxis().GetBinCenter(j)
            tmp_pt_dic[(eta_l,eta_u)] = GetMuonTriggerSF(pt_in,eta_in)
        #print str((pt_l,pt_u))
        #print str(tmp_pt_dic)
        SF_dic[(pt_l,pt_u)]=tmp_pt_dic
    write_json(SF_dic,"MuonSF/Json/Trigger_SF_json.txt")
    #print "*"*50
    return SF_dic
    
def writeMuonISOSF():
    SF_dic = {}
    f1 = ROOT.TFile.Open("MuonSF/ISO/EfficienciesAndSF_GH.root","READ")
    h1 = f1.Get("tkLooseISO_highptID_newpt_eta/pair_ne_ratio")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        tmp_pt_dic = {}
        pt_u = h1.GetXaxis().GetBinUpEdge(i)
        pt_l = h1.GetXaxis().GetBinLowEdge(i)
        pt_in = h1.GetXaxis().GetBinCenter(i)
        for j in range(1,h1.GetYaxis().GetNbins()+1):
            eta_u = h1.GetYaxis().GetBinUpEdge(j)
            eta_l = h1.GetYaxis().GetBinLowEdge(j)
            eta_in = h1.GetYaxis().GetBinCenter(j)
            tmp_pt_dic[(eta_l,eta_u)] = GetMuonISOSF(pt_in,eta_in)
        #print str((pt_l,pt_u))
        #print str(tmp_pt_dic)
        SF_dic[(pt_l,pt_u)]=tmp_pt_dic
    write_json(SF_dic,"MuonSF/Json/ISO_SF_json.txt")
    #print "*"*50
    return SF_dic
    
def writeMuonIDSF():
    SF_dic = {}
    f1 = ROOT.TFile.Open("MuonSF/ID/EfficienciesAndSF_BCDEF.root","READ")
    h1 = f1.Get("MC_NUM_HighPtID_DEN_genTracks_PAR_newpt_eta/pair_ne_ratio")
    for i in range(1,h1.GetXaxis().GetNbins()+1):
        tmp_pt_dic = {}
        pt_u = h1.GetXaxis().GetBinUpEdge(i)
        pt_l = h1.GetXaxis().GetBinLowEdge(i)
        pt_in = h1.GetXaxis().GetBinCenter(i)
        for j in range(1,h1.GetYaxis().GetNbins()+1):
            eta_u = h1.GetYaxis().GetBinUpEdge(j)
            eta_l = h1.GetYaxis().GetBinLowEdge(j)
            eta_in = h1.GetYaxis().GetBinCenter(j)
            tmp_pt_dic[(eta_l,eta_u)] = GetMuonIDSF(pt_in,eta_in)
        #print str((pt_l,pt_u))
        #print str(tmp_pt_dic)
        SF_dic[(pt_l,pt_u)]=tmp_pt_dic
    write_json(SF_dic,"MuonSF/Json/ID_SF_json.txt")
    #print "*"*50
    return SF_dic
    
#writeMuonTriggerSF()
#writeMuonISOSF()
#writeMuonIDSF()
