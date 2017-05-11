import ROOT
import time
from array import array
from math import *

label='eff3_DoubleEle33_SingleElectron.png'
title='HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v3 effciency (2016)'
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

def getEff(EtaList,tchain):
    n_total = 0
    n_processed = 0
    n_pass = 0
    total_dic = {}
    pass_dic = {}
    ratio_dic = {}
    for Eta in EtaList:
        Eta1 = Eta[0]
        Eta2 = Eta[1]
        total_dic[(Eta1,Eta2)] = 0
        pass_dic[(Eta1,Eta2)] = 0

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
        pass_trig = getattr(event,'Pass_DoubleEle33')
        M_ee = getattr(event,'M_ee')
        if not(60 <= M_ee and M_ee <=120):continue
        for Eta in EtaList:
            Eta1 = Eta[0]
            Eta2 = Eta[1]
            if (Eta1 <= eta and eta < Eta2):
                total_dic[(Eta1,Eta2)]+=1
                if pass_trig !=0 :
                    pass_dic[(Eta1,Eta2)]+=1
    for (Eta1,Eta2) in total_dic:
        if total_dic[(Eta1,Eta2)]!=0:ratio_dic[(Eta1,Eta2)] = float(pass_dic[(Eta1,Eta2)])/float(total_dic[(Eta1,Eta2)])
        else:ratio_dic[(Eta1,Eta2)] = 0
    return ratio_dic, total_dic


try:
    tchain=ROOT.TChain('tap')
    #tchain.Add('../ntuples/bak/data_*_SingleElectron.root')
    tchain.Add('../ntuples/reskim/data_2016B_SingleElectron.root')
#    tchain.Add('../ntuples/reskim/data_*_DoubleEG.root')
except:
    print "errors!" 

EtaList = []
step_len = 0.05
i = 0.025
while(i<2.7):
    tmp_List = []
    tmp_List.append(float(i)-step_len/2)
    tmp_List.append(float(i)+step_len/2)
    EtaList.append(tmp_List)
    i+=step_len

n=len(EtaList)
print EtaList

my_func = ROOT.TF1('eff_func','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45)
my_func.SetParameters(0.3,35,1.8,0.7,35,0.5)

my_func_2 = ROOT.TF1('eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45)
my_func_2.SetParameters(0.3,35,1.8,0.7,35,0.5)

my_func_3 = ROOT.TF1('eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45)
my_func_3.SetParameters(0.3,35,1.8,0.7,35,0.5)

n_total = 0
x_error = step_len/2

x, y = array( 'f' ), array( 'f' )
ex, ey = array( 'f' ), array( 'f' )

ratio_dic,total_dic = getEff(EtaList,tchain)
for (Eta1,Eta2) in ratio_dic:
    x.append((float(Eta1+Eta2))/2)
    ex.append(x_error)
    y.append(ratio_dic[(Eta1,Eta2)])
    ey.append(Eff_error(ratio_dic[(Eta1,Eta2)],total_dic[(Eta1,Eta2)]))
#    print 'x : %0.2f, y : %0.2f, err : %0.2f'%((float(Et1+Et2))/2,ratio_dic[(Et1,Et2)],Eff_error(ratio_dic[(Et1,Et2)],total_dic[(Et1,Et2)]))
print my_sum(total_dic)
n_total+=my_sum(total_dic)

c1 = ROOT.TCanvas( 'c1', title , 200, 10, 700, 500 )
c1.SetGrid()
gr = ROOT.TGraphErrors( n, x, y, ex, ey)
gr.SetMarkerColor( 1 )
gr.SetMarkerStyle( 20 )
gr.SetTitle( title  )
gr.GetXaxis().SetTitle( '|#eta_{SC}|' )
gr.GetXaxis().SetRangeUser(0,2.8 )
gr.GetXaxis().SetNdivisions(512)
gr.GetYaxis().SetRangeUser(0,1 )
gr.GetYaxis().SetTitle( 'Efficiency' )
gr.GetYaxis().SetTitleOffset(1.4)

gr.Draw( 'AP' )
c1.Update()

tText_4 = ROOT.TPaveText(0.1,0.1,0.3,0.2,"blNDC")
tText_4.SetBorderSize(0)
tText_4.SetFillStyle(0)
tText_4.SetTextAlign(12)
tText_4.SetTextColor(1)
tText_4.SetTextFont(42)
tText_4.SetTextSize(0.04195804)
t1 = tText_4.AddText ("2.6 fb^{-1}, 13 TeV")
tText_4.Draw()
c1.Update()
c1.Print(label)

print n_total
time.sleep(10)
