import ROOT
import time
from array import array
from math import *

label='eff3_DoubleEle33_SingleElectron_matchedMethod.png'
title='HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v3 effciency (2016)'
my_eta_start_No = 0#etaList = [[0.0,0.79],[0.79,1.1],[1.1,1.4442],[1.556,1.7],[1.7,2.1],[2.1,2.5]]
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
        pass_trig = getattr(event,'probe_fired_unseeded')
        M_ee = getattr(event,'M_ee')
        if not(60 <= M_ee and M_ee <=120):continue
        if not(eta1 <= eta and eta < eta2):continue
        for E in EtList:
            Et1 = E[0]
            Et2 = E[1]
            if (Et1 <= Et and Et < Et2):
                total_dic[(Et1,Et2)]+=1
                if pass_trig !=0 :
                    pass_dic[(Et1,Et2)]+=1
    for (Et1,Et2) in total_dic:
        if total_dic[(Et1,Et2)]!=0:ratio_dic[(Et1,Et2)] = float(pass_dic[(Et1,Et2)])/float(total_dic[(Et1,Et2)])
        else:ratio_dic[(Et1,Et2)] = 0
    return ratio_dic, total_dic


try:
    tchain=ROOT.TChain('tap')
#    tchain.Add('../ntuples/reskim/data_2016B_SingleElectron.root')
    #tchain.Add('../ntuples/reskim/data_2016B_SingleElectron_fired.root')
    tchain.Add('../ntuples/reskim/data_2016B_SingleElectron.root')
except:
    print "errors!" 

etaList = [[0.0,1.442],[1.556,2.5]]
EtList = []
step_len = 50
i = 50
while(i<900):
    tmp_List = []
    tmp_List.append(float(i)-step_len/2)
    tmp_List.append(float(i)+step_len/2)
    EtList.append(tmp_List)
    i+=step_len

n=len(EtList)
print EtList

my_func = ROOT.TF1('eff_func','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45)
my_func.SetParameters(0.3,35,1.8,0.7,35,0.5)

my_func_2 = ROOT.TF1('eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45)
my_func_2.SetParameters(0.3,35,1.8,0.7,35,0.5)

n_total = 0
x_error = 0.0

x, y = array( 'f' ), array( 'f' )
ex, ey = array( 'f' ), array( 'f' )

ratio_dic,total_dic = getEff(EtList,etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1],tchain)
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
gr.SetMarkerColor( 1 )
gr.SetMarkerStyle( 20 )
gr.SetTitle( title  )
gr.GetXaxis().SetTitle( 'E_{T}' )
gr.GetXaxis().SetRangeUser(50,1000 )
gr.GetXaxis().SetNdivisions(512)
gr.GetYaxis().SetRangeUser(0,1 )
gr.GetYaxis().SetRangeUser(0.8,1 )
gr.GetYaxis().SetTitle( 'Efficiency' )
gr.GetYaxis().SetTitleOffset(1.4)

gr.Draw( 'AP' )
c1.Update()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ratio_dic,total_dic = getEff(EtList,etaList[my_eta_start_No+1][0],etaList[my_eta_start_No+1][1],tchain)
x, y = array( 'f' ), array( 'f' )
ex, ey = array( 'f' ), array( 'f' )
for (Et1,Et2) in ratio_dic:
    x.append((float(Et1+Et2))/2)
    ex.append(x_error)
    y.append(ratio_dic[(Et1,Et2)])
    ey.append(Eff_error(ratio_dic[(Et1,Et2)],total_dic[(Et1,Et2)]))

print my_sum(total_dic)
print y
n_total+=my_sum(total_dic)
gr_2 = ROOT.TGraphErrors( n, x, y, ex, ey)
gr_2.SetMarkerColor( 4 )
gr_2.SetMarkerStyle( 22 )
gr_2.SetTitle( ''  )
gr_2.GetYaxis().SetTitleOffset(1.4)

gr_2.Draw( 'P' )
c1.Update()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

legend=ROOT.TLegend(0.12,0.75,0.3,0.9)
legend.AddEntry(gr,"%.2f<|#eta|<%.2f"%(etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1]),"pl")
legend.AddEntry(gr_2,"%.2f<|#eta|<%.2f"%(etaList[my_eta_start_No+1][0],etaList[my_eta_start_No+1][1]),"pl")
legend.Draw()

c1.Update()
c1.Print(label)
