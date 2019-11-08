import ROOT
from math import *

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

class make_json():
    file_name1 = ""
    tree_name1 = ""
    file_name2 = ""
    tree_name2 = ""
    weight_1 = 0
    weight_2 = 0
    out_file_name = ""
    json_name = ""
    reverse = False
    sys_type = "null"
    extra_err = 0.0

    def write_json(self,dic_in,file_name):
        f1 = open(file_name,"w")
        f1.write(str(dic_in))
    
    def main(self):
        SF_dic = {}
        f1 = ROOT.TFile.Open(self.file_name1,"READ")
        h1 = f1.Get(self.tree_name1)
        f1.Close()
        f2 = ROOT.TFile.Open(self.file_name2,"READ")
        h2 = f2.Get(self.tree_name2)
        f2.Close()
        h_out = h1.Clone()
        h_out.SetName("SF")
        x_axis = h1.GetXaxis()
        y_axis = h1.GetYaxis()
        for i in range(1,x_axis.GetNbins()+1):
            for j in range(1,y_axis.GetNbins()+1):
                mean1 = h1.GetBinContent(i,j)
                err1 = h1.GetBinError(i,j)
                mean2 = h2.GetBinContent(i,j)
                err2 = h2.GetBinError(i,j)
                h_out.SetBinContent(i,j,self.weight_1*mean1 + self.weight_2*mean2)
                h_out.SetBinError(i,j, sqrt(self.weight_1*self.weight_1*err1*err1 + self.weight_2*self.weight_2*err2*err2) )

        fout = ROOT.TFile(self.out_file_name,"RECREATE")
        fout.cd()
        h_out.Write()
        fout.Close()
    

muon_id = make_json()
muon_id.file_name1 = "Muon/ID/RunBCDEF_SF_ID.root"
muon_id.tree_name1 = "NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt"
muon_id.weight_1   = 22.0/36.0
muon_id.file_name2 = "Muon/ID/RunGH_SF_ID.root"
muon_id.tree_name2 = "NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt"
muon_id.weight_2   = 14.0/36.0
muon_id.out_file_name = "Muon/ID/Muon_2016_SF_ID.root"
muon_id.main()

muon_iso = make_json()
muon_iso.file_name1 = "Muon/Iso/RunBCDEF_SF_ISO.root"
muon_iso.tree_name1 = "NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt"
muon_iso.weight_1   = 22.0/36.0
muon_iso.file_name2 = "Muon/Iso/RunGH_SF_ISO.root"
muon_iso.tree_name2 = "NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt"
muon_iso.weight_2   = 14.0/36.0
muon_iso.out_file_name = "Muon/Iso/Muon_2016_SF_Iso.root"
muon_iso.main()
