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
    
class make_json_raw(make_json):
    file_name1 = ""
    tree_name1 = ""
    file_name2 = ""
    tree_name2 = ""
    json_name = ""

    def main(self):
        SF_dic = {}
        f1 = ROOT.TFile.Open(self.file_name1,"READ")
        h1 = f1.Get(self.tree_name1)
        f2 = ROOT.TFile.Open(self.file_name2,"READ")
        h2 = f2.Get(self.tree_name2)
        print h1.Integral()
        x1_axis = h1.GetXaxis()
        x2_axis = h2.GetXaxis()
        for i in range(1,x1_axis.GetNbins()+1):
            tmp_pt_dic = {}
            x_u = x1_axis.GetBinUpEdge(i)
            x_l = x1_axis.GetBinLowEdge(i)
            x1_in = h1.GetBinContent(i)
            x2_in = h2.GetBinContent(i)
            if x_u > 2600:break
            tmp_value = 1.0
            if (x1_in != 0 and x2_in != 0):
                tmp_value = x2_in / x1_in

            print str((x_l,x_u))
            print str(tmp_value)
            SF_dic[(x_l,x_u)] = tmp_value
        self.write_json(SF_dic,self.json_name)
        #print "*"*50
        return SF_dic

muon_trig = make_json_raw()
muon_trig.file_name1 = "/user/xgao/CMSSW_9_2_6/src/2017_ALL/EMu/EMu_42p0fb_pt53/ttbar_check/hist_ttbar.root"
muon_trig.tree_name1 = "M_emu"
muon_trig.file_name2 = "/user/xgao/CMSSW_9_2_6/src/2016_ALL/EMu/new_EMu_2016/ttbar_check/hist_ttbar.root"
muon_trig.tree_name2 = "M_emu"
muon_trig.json_name = "ttbar_NNPDF31to30_json.txt"
muon_trig.main()
