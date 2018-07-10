import ROOT
import math


class make_json():
    file_name = ""
    tree_name = ""
    json_name = ""
    reverse = False

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
                    tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(i,j)
                else:
                    tmp_pt_dic[(eta_l,eta_u)] = h1.GetBinContent(j,i)
            print str((pt_l,pt_u))
            print str(tmp_pt_dic)
            SF_dic[(pt_l,pt_u)]=tmp_pt_dic
        self.write_json(SF_dic,self.json_name)
        #print "*"*50
        return SF_dic
    
muon_id = make_json()
muon_id.file_name = "Muon/Trigger/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root"
muon_id.tree_name = "Mu50_PtEtaBins/pt_abseta_ratio"
muon_id.json_name = "Muon/Trigger/Muon_Trigger_run2017BCDEF_json.txt"
muon_id.main()

ele_rereco = make_json()
ele_rereco.file_name = "Electron/reco/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root"
ele_rereco.tree_name = "EGamma_SF2D"
ele_rereco.json_name = "Electron/reco/Electron_reco_run2017BCDEF_json.txt"
ele_rereco.reverse = True
ele_rereco.main()
