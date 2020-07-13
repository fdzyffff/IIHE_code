import ROOT
from math import *


class make_json():
    file_name = ""
    tree_name = ""
    json_name = ""
    reverse = False
    sys_type = "null"
    extra_err = 0.0

    def write_json(self,dic_in,file_name):
        f1 = open(file_name,"w")
        f1.write(str(dic_in))
    
    def main(self):
        SF_dic = {}
        f1 = ROOT.TFile.Open(self.file_name,"READ")
        h1 = f1.Get(self.tree_name)
        if not self.reverse:
            x_axis = h1.GetXaxis()
            y_axis = h1.GetYaxis()
        else:
            x_axis = h1.GetYaxis()
            y_axis = h1.GetXaxis()
        for i in range(1,x_axis.GetNbins()+1):
            tmp_pt_dic = {}
            pt_u = x_axis.GetBinUpEdge(i)
            pt_l = x_axis.GetBinLowEdge(i)
            pt_in = x_axis.GetBinCenter(i)
            for j in range(1,y_axis.GetNbins()+1):
                eta_u = y_axis.GetBinUpEdge(j)
                eta_l = y_axis.GetBinLowEdge(j)
                eta_in = y_axis.GetBinCenter(j)
                if not self.reverse:
                    if self.sys_type == "up" :
                        tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(i,j) + sqrt(self.extra_err * self.extra_err + h1.GetBinError(i,j) * h1.GetBinError(i,j) )
                    elif self.sys_type == "down":
                        tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(i,j) - sqrt(self.extra_err * self.extra_err + h1.GetBinError(i,j) * h1.GetBinError(i,j) )
                    else :
                        tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(i,j)
                else:
                    if self.sys_type == "up" :
                        tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(j,i) + sqrt(self.extra_err * self.extra_err + h1.GetBinError(j,i) * h1.GetBinError(j,i) )
                    elif self.sys_type == "down":
                        tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(j,i) - sqrt(self.extra_err * self.extra_err + h1.GetBinError(j,i) * h1.GetBinError(j,i) )
                    else :
                        tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(j,i)
            print str((pt_l,pt_u))
            print str(tmp_pt_dic)
            SF_dic[(pt_l,pt_u)]=tmp_pt_dic
        self.write_json(SF_dic,self.json_name)
        #print "*"*50
        return SF_dic
    
muon_trig = make_json()
muon_trig.file_name = "Muon/Trigger/EfficienciesAndSF_2018Data_AfterMuonHLTUpdate.root"
muon_trig.tree_name = "Mu50_OR_OldMu100_OR_TkMu100_PtEtaBins/pt_abseta_ratio"
muon_trig.json_name = "Muon/Trigger/Muon_Trigger_2018_SF.json"
muon_trig.main()

muon_trig_up = make_json()
muon_trig_up.file_name = "Muon/Trigger/EfficienciesAndSF_2018Data_AfterMuonHLTUpdate.root"
muon_trig_up.tree_name = "Mu50_OR_OldMu100_OR_TkMu100_PtEtaBins/pt_abseta_ratio"
muon_trig_up.json_name = "Muon/Trigger/sysu_Muon_Trigger_2018_SF.json"
muon_trig_up.sys_type = "up"
muon_trig_up.extra_err = 0.02
muon_trig_up.main()

muon_trig_down = make_json()
muon_trig_down.file_name = "Muon/Trigger/EfficienciesAndSF_2018Data_AfterMuonHLTUpdate.root"
muon_trig_down.tree_name = "Mu50_OR_OldMu100_OR_TkMu100_PtEtaBins/pt_abseta_ratio"
muon_trig_down.json_name = "Muon/Trigger/sysd_Muon_Trigger_2018_SF.json"
muon_trig_down.sys_type = "down"
muon_trig_down.extra_err = 0.02
muon_trig_down.main()

muon_id = make_json()
muon_id.file_name = "Muon/ID/RunABCD_SF_ID.root"
muon_id.tree_name = "NUM_HighPtID_DEN_TrackerMuons_pair_newTuneP_probe_pt_abseta"
muon_id.json_name = "Muon/ID/Muon_ID_2018_SF_ID.json"
muon_id.main()

muon_id_up = make_json()
muon_id_up.file_name = "Muon/ID/RunABCD_SF_ID.root"
muon_id_up.tree_name = "NUM_HighPtID_DEN_TrackerMuons_pair_newTuneP_probe_pt_abseta"
muon_id_up.json_name = "Muon/ID/sysu_Muon_ID_2018_SF_ID.json"
muon_id_up.sys_type = "up"
muon_id_up.main()

muon_id_down = make_json()
muon_id_down.file_name = "Muon/ID/RunABCD_SF_ID.root"
muon_id_down.tree_name = "NUM_HighPtID_DEN_TrackerMuons_pair_newTuneP_probe_pt_abseta"
muon_id_down.json_name = "Muon/ID/sysd_Muon_ID_2018_SF_ID.json"
muon_id_down.sys_type = "down"
muon_id_down.main()

muon_iso = make_json()
muon_iso.file_name = "Muon/Iso/RunABCD_SF_ISO.root"
muon_iso.tree_name = "NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_pair_newTuneP_probe_pt_abseta"
muon_iso.json_name = "Muon/Iso/Muon_ISO_2018_SF_ISO.json"
muon_iso.main()

muon_iso_up = make_json()
muon_iso_up.file_name = "Muon/Iso/RunABCD_SF_ISO.root"
muon_iso_up.tree_name = "NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_pair_newTuneP_probe_pt_abseta"
muon_iso_up.json_name = "Muon/Iso/sysu_Muon_ISO_2018_SF_ISO.json"
muon_iso_up.sys_type = "up"
muon_iso_up.main()

muon_iso_down = make_json()
muon_iso_down.file_name = "Muon/Iso/RunABCD_SF_ISO.root"
muon_iso_down.tree_name = "NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_pair_newTuneP_probe_pt_abseta"
muon_iso_down.json_name = "Muon/Iso/sysd_Muon_ISO_2018_SF_ISO.json"
muon_iso_down.sys_type = "down"
muon_iso_down.main()

ele_rereco = make_json()
ele_rereco.file_name = "Electron/reco/egammaEffi.txt_EGM2D_updatedAll.root"
ele_rereco.tree_name = "EGamma_SF2D"
ele_rereco.json_name = "Electron/reco/Electron_reco_run2018_json.txt"
ele_rereco.reverse = True
ele_rereco.main()
