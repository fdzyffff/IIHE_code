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
    
def get_2D_json(file_name, hist_name, xy_convert = False, isPrint = True):
    SF_dic = {}
    f1 = ROOT.TFile.Open(file_name,"READ")
    h1 = f1.Get(hist_name)

    if xy_convert:
        y_axis = h1.GetXaxis()
        x_axis = h1.GetYaxis()
    else:
        x_axis = h1.GetXaxis()
        y_axis = h1.GetYaxis()

    for i in range(1,x_axis.GetNbins()+1):
        tmp_pt_dic = {}
        x_u = x_axis.GetBinUpEdge(i)
        x_l = x_axis.GetBinLowEdge(i)
        if isPrint:
            print "%s, %s :\n"%(x_l, x_u)
        for j in range(1,y_axis.GetNbins()+1):
            y_u = y_axis.GetBinUpEdge(j)
            y_l = y_axis.GetBinLowEdge(j)
            if xy_convert:
                tmp_pt_dic[(y_l,y_u)] = h1.GetBinContent(j,i)
            else:
                tmp_pt_dic[(y_l,y_u)] = h1.GetBinContent(i,j)
            if isPrint:
                print "     %s, %s :  %s\n"%(y_l, y_u, tmp_pt_dic[(y_l,y_u)])
        SF_dic[(x_l,x_u)]=tmp_pt_dic
    if isPrint:print SF_dic
    return SF_dic


#main()
write_json(get_2D_json("reco/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root","EGamma_SF2D",True),"reco/Electron_reco_run2017BCDEF_json.txt")
#print "*"*50
