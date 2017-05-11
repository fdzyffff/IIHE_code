import ROOT
import os
import time
from array import array
from math import *

update = True
update = False
label ='eff2_DoubleEle33_L1_SingleElectron_matchedMethod.png'
label2='eff2_DoubleEle33_L1_SingleElectron_matchedMethod'
#title='HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v effciency (2016G)'
title='HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v L1 effciency (2016 B-H rereco)'
my_eta_start_No = 0#etaList = [[0.0,0.79],[0.79,1.1],[1.1,1.4442],[1.556,1.7],[1.7,2.1],[2.1,2.5]]

def check_eq(f1, f2):
    if abs(float(f1)) < 0.00001 and abs(float(f2)) < 0.00001:
        return True
    elif float(f1) == 0 or float(f2) == 0:
        return False
    if abs((float(f1)-float(f2))/float(f1)) <= 0.001:
        return True
    return False

def my_sum(tmp_dic):
    n=0
    for l in tmp_dic:
        n+=tmp_dic[l]
    return n

def my_region(eta):
    if fabs(eta) < 1.4442: return 1
    elif fabs(eta) <1.566: return 2
    elif fabs(eta) <2.5:   return 3
    else: return 0

def Eff_error(p,N):
    if N == 0:
        return 0.1
    else:
        error = 0
        error = sqrt(p*(1-p)/N)
        return error

def write_log(ratio_dic,total_dic,eta1,eta2,label2):
    try:
        os.mkdir("dat")
    except:
        pass
    tmp_file = open("dat/%s_%s_%s.dat"%(label2, str(eta1), str(eta2)),"w")
    for (Et1,Et2) in ratio_dic:
        tmp_file.write("%s,%s,%s,%s\n"%(Et1,Et2,ratio_dic[(Et1,Et2)],total_dic[(Et1,Et2)]))

def getEff_log(EtList,eta1,eta2,label2):
    ratio_dic = {}
    total_dic = {}
    tmp_file = open("dat/%s_%s_%s.dat"%(label2, str(eta1), str(eta2)),"r")
    for Line in tmp_file:
        line = Line.replace("\n","").split(",")
        for Et in EtList:
            Et1 = Et[0]
            Et2 = Et[1]
            if check_eq(Et1, float(line[0])) and check_eq(Et2, float(line[1])):
                ratio_dic[(Et1,Et2)] = float(line[2])
                total_dic[(Et1,Et2)] = float(line[3])
                break

    return ratio_dic, total_dic

def getEff(EtList,eta1,eta2,tchain):
    n_total = 0
    n_processed = 0
    n_pass = 0
    total_dic = {}
    pass_dic = {}
    ratio_dic = {}
    for E in EtList:
        Et1 = E[0]
        Et2 = E[1]
        total_dic[(Et1,Et2)] = 0
        pass_dic[(Et1,Et2)] = 0

    n_total = tchain.GetEntries()
    for event in tchain:
        n_processed += 1
#        if n_processed > 3000:break
        if n_processed%100000 == 0:
            print '%d event processed, (in total: %d)'%(n_processed,n_total)
#            print total_dic
#            print pass_dic
        Et = getattr(event,'probe_pt')
        eta = fabs(getattr(event,'probe_eta'))
        pass_trig = getattr(event,'probe_L1_fired')
        M_ee = getattr(event,'M_ee')
        #if not(60 <= M_ee and M_ee <=120):continue
        if not(eta1 <= eta and eta < eta2):continue
        if not(20 <= Et and Et <=40):continue
        for E in EtList:
            Et1 = E[0]
            Et2 = E[1]
            if (Et1 <= eta and eta < Et2):
                total_dic[(Et1,Et2)]+=1
                if pass_trig !=0 :
                    pass_dic[(Et1,Et2)]+=1
    for (Et1,Et2) in total_dic:
        if total_dic[(Et1,Et2)]!=0:ratio_dic[(Et1,Et2)] = float(pass_dic[(Et1,Et2)])/float(total_dic[(Et1,Et2)])
        else:ratio_dic[(Et1,Et2)] = 0
    return ratio_dic, total_dic


try:
    tchain=ROOT.TChain('tap')
    tchain.Add('../ntuples/batchdata_loop/data_2016_SingleElectron.root')
except:
    print "errors!" 

etaList = [[0.0,2.5]]
EtList = []
step_len = 0.05
i = 0.025
while(i<2.5):
    tmp_List = []
    tmp_List.append(float(i)-step_len/2)
    tmp_List.append(float(i)+step_len/2)
    EtList.append(tmp_List)
    i+=step_len

n=len(EtList)
print EtList

#my_func = ROOT.TF1('eff_func','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,80)
#my_func.SetParameters(0.3,35,1.8,0.7,35,0.5)


n_total = 0
x_error = 0.0

x, y = array( 'f' ), array( 'f' )
ex, ey = array( 'f' ), array( 'f' )

if update:
    ratio_dic,total_dic = getEff(EtList,etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1],tchain)
    write_log(ratio_dic,total_dic,etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1],label2)
else:
    ratio_dic,total_dic = getEff_log(EtList,etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1],label2)

for (Et1,Et2) in ratio_dic:
    x.append((float(Et1+Et2))/2)
    ex.append(x_error)
    y.append(ratio_dic[(Et1,Et2)])
    ey.append(Eff_error(ratio_dic[(Et1,Et2)],total_dic[(Et1,Et2)]))
#    print 'x : %0.2f, y : %0.2f, err : %0.2f'%((float(Et1+Et2))/2,ratio_dic[(Et1,Et2)],Eff_error(ratio_dic[(Et1,Et2)],total_dic[(Et1,Et2)]))
print my_sum(total_dic)
n_total+=my_sum(total_dic)

c1 = ROOT.TCanvas( 'c1', title , 200, 10, 700, 500 )
c1.SetGrid()
gr = ROOT.TGraphErrors( n, x, y, ex, ey)
gr.SetMarkerColor( 2 )
gr.SetLineColor( 2 )
gr.SetMarkerStyle( 20 )
gr.SetTitle( title  )
gr.GetXaxis().SetTitle( '|#eta|' )
gr.GetXaxis().SetRangeUser(0.0,2.6 )
gr.GetXaxis().SetNdivisions(512)
gr.GetYaxis().SetRangeUser(0,1)
gr.GetYaxis().SetRangeUser(0.8,1.02 )
gr.GetYaxis().SetTitle( 'Efficiency' )
gr.GetYaxis().SetTitleOffset(1.4)

gr.Draw( 'AP' )
#gr.Fit(my_func,"","",20,80)
#gr.GetFunction('eff_func').SetLineColor(2)
c1.Update()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#legend=ROOT.TLegend(0.12,0.8,0.3,0.9)
#legend.AddEntry(gr,"%.2f<|#eta|<%.2f"%(etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1]),"pl")
#legend.Draw()


#tText = ROOT.TPaveText(0.52,0.12,0.69,0.42,"blNDC")
#tText.SetBorderSize(0)
#tText.SetFillStyle(0)
#tText.SetTextAlign(12)
#tText.SetTextColor(2)
#tText.SetTextFont(42)
#tText.SetTextSize(0.04195804)
#t1 = tText.AddText ("%.2f<|#eta|<%.2f"%(etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1]))
#t2 = tText.AddText ('P0  %0.3f'%(gr.GetFunction("eff_func").GetParameter(0)))
#t3 = tText.AddText ('P1  %0.3f'%(gr.GetFunction("eff_func").GetParameter(1)))
#t4 = tText.AddText ('P2  %0.3f'%(gr.GetFunction("eff_func").GetParameter(2)))
#t5 = tText.AddText ('P3  %0.3f'%(gr.GetFunction("eff_func").GetParameter(3)))
#t6 = tText.AddText ('P4  %0.3f'%(gr.GetFunction("eff_func").GetParameter(4)))
#t7 = tText.AddText ('P5  %0.3f'%(gr.GetFunction("eff_func").GetParameter(5)))
#tText.Draw()
#c1.Update()


tText_4 = ROOT.TPaveText(0.2,0.15,0.35,0.35,"blNDC")
tText_4.SetBorderSize(0)
tText_4.SetFillStyle(0)
tText_4.SetTextAlign(12)
tText_4.SetTextColor(1)
tText_4.SetTextFont(42)
tText_4.SetTextSize(0.04195804)
#t1 = tText_4.AddText ("4.394 fb^{-1}")
t1 = tText_4.AddText ("Run range")
t1 = tText_4.AddText ("[276453, 278822]")
t1 = tText_4.AddText ("11 fb^{-1}")
t1 = tText_4.AddText ("Et in [20, 40]")
tText_4.Draw()
c1.Update()
c1.Print(label)

print n_total
time.sleep(10)
