import ROOT
import os
import time
from array import array
from math import *

update = False
update = True
label ='eff_DoubleEle33_SingleMuon_L1_matchedMethod.png'
label2=label[:-4]
title='L1 effciency'

etaList = [[0.0,1.4442],[1.556,2.5]]
my_eta_start_No = 0

ROOT.TH1.AddDirectory(ROOT.kFALSE)

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

def write_log(h_pass,h_total,label2,flag):
    try:
        os.mkdir("dat")
    except:
        pass
    tmp_file = ROOT.TFile("dat/%s_%s.root"%(label2,flag),"recreate")
    tmp_file.cd()
    h_pass.Write()
    h_total.Write()
    tmp_file.Close()

def getEff_log(h_pass, h_total,label2, flag):
    tmp_file = ROOT.TFile("dat/%s_%s.root"%(label2,flag),"read")
    tmp_file.cd()
    h_pass = tmp_file.Get(h_pass.GetName())
    h_total = tmp_file.Get(h_total.GetName())
    tmp_file.Close()
    return h_pass, h_total

def getEff(h_pass, h_total, eta1,eta2,tchain):
    n_total = tchain.GetEntries()
    n_processed = 0
    for event in tchain:
        n_processed += 1
#        if n_processed > 800000:break
        if n_processed%100000 == 0:
            print '%d event processed, (in total: %d)'%(n_processed,n_total)
        Et = getattr(event,'heep_Et')
        eta = fabs(getattr(event,'heep_eta'))
        pass_flag = getattr(event,'heep_L1_fire')

        if not(eta1 <= eta and eta < eta2):continue
        if pass_flag:
            h_pass.Fill(Et)
        h_total.Fill(Et)

try:
    tchain=ROOT.TChain('tap')
    tchain.Add('../ntuples/data_SingleMuon.root')
except:
    print "errors!" 

x_List = array("f")
for i in range (30,100,10):
    x_List.append(i)
x_List.append(100)
x_List.append(150)
x_List.append(200)
x_List.append(300)
x_List.append(400)
x_List.append(500)
x_List.append(700)
x_List.append(1000)

n=len(x_List)

my_func = ROOT.TF1('eff_func','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,80)
my_func.SetParameters(0.3,35,1.8,0.7,35,0.5)

my_func_2 = ROOT.TF1('eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,80)
my_func_2.SetParameters(0.3,35,1.8,0.7,35,0.5)

n_total = 0

h_pass_1 = ROOT.TH1F("h_pass_1","",len(x_List)-1,x_List)
h_total_1 = ROOT.TH1F("h_total_1","",len(x_List)-1,x_List)
h_pass_1.Sumw2()
h_total_1.Sumw2()
if update:
    getEff(h_pass_1, h_total_1, etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1] ,tchain)
    write_log(h_pass_1,h_total_1,label2,1)
else:
    h_pass_1, h_total_1 = getEff_log(h_pass_1,h_total_1,label2,1)

print h_total_1.Integral()
n_total+=h_total_1.Integral()

c1 = ROOT.TCanvas( 'c1', title , 200, 10, 700, 500 )
c1.SetBottomMargin(0.15)
c1.SetGrid()
c1.SetLogx()
gr = ROOT.TGraphAsymmErrors()
gr.Divide(h_pass_1,h_total_1,"cl=0.683 b(1,1) mode")
gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 20 )
gr.SetLineColor( 4 )
gr.SetTitle( title  )
gr.GetXaxis().SetTitle( 'E_{T}^{Heep} (GeV)' )
gr.GetXaxis().SetNdivisions(512)
gr.GetXaxis().SetMoreLogLabels()
gr.GetXaxis().SetLabelSize(0.05)
gr.GetXaxis().SetTitleOffset(1.0)
gr.GetXaxis().SetTitleSize(0.06)

gr.GetYaxis().SetRangeUser(0.8,1.1 )
gr.GetYaxis().SetTitle( 'Efficiency' )
gr.GetYaxis().SetTitleOffset(0.75)
gr.GetYaxis().SetTitleSize(0.06)

gr.GetXaxis().SetNoExponent()
gr.Draw( 'AP' )
#gr.Fit(my_func)
#gr.GetFunction('eff_func').SetLineColor(1)
c1.Update()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
h_pass_2 = ROOT.TH1F("h_pass_2","",len(x_List)-1,x_List)
h_total_2 = ROOT.TH1F("h_total_2","",len(x_List)-1,x_List)
h_pass_2.Sumw2()
h_total_2.Sumw2()
if update:
    getEff(h_pass_2, h_total_2, etaList[my_eta_start_No+1][0],etaList[my_eta_start_No+1][1] ,tchain)
    write_log(h_pass_2,h_total_2,label2,2)
else:
    h_pass_2, h_total_2 = getEff_log(h_pass_2,h_total_2,label2,2)

print h_total_2.Integral()
n_total+=h_total_2.Integral()

gr_2 = ROOT.TGraphAsymmErrors()
gr_2.Divide(h_pass_2,h_total_2,"cl=0.683 b(1,1) mode")
gr_2.SetMarkerColor( 2 )
gr_2.SetMarkerStyle( 22 )
gr_2.SetLineColor( 2 )
gr_2.SetTitle( ''  )
gr_2.GetYaxis().SetTitleOffset(1.4)

gr_2.Draw( 'P' )

c1.Update()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c1.Update()

legend=ROOT.TLegend(0.62,0.75,0.9,0.9)
legend.AddEntry(gr,"Barrel","ple")
legend.AddEntry(gr_2,"Endcap","ple")
legend.Draw()


tText = ROOT.TPaveText(0.52,0.12,0.69,0.42,"blNDC")
tText.SetBorderSize(0)
tText.SetFillStyle(0)
tText.SetTextAlign(12)
tText.SetTextColor(1)
tText.SetTextFont(42)
tText.SetTextSize(0.04195804)
#t1 = tText.AddText ("%.2f<|#eta|<%.2f"%(etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1]))
#t2 = tText.AddText ('P0  %0.3f'%(gr.GetFunction("eff_func").GetParameter(0)))
#t3 = tText.AddText ('P1  %0.3f'%(gr.GetFunction("eff_func").GetParameter(1)))
#t4 = tText.AddText ('P2  %0.3f'%(gr.GetFunction("eff_func").GetParameter(2)))
#t5 = tText.AddText ('P3  %0.3f'%(gr.GetFunction("eff_func").GetParameter(3)))
#t6 = tText.AddText ('P4  %0.3f'%(gr.GetFunction("eff_func").GetParameter(4)))
#t7 = tText.AddText ('P5  %0.3f'%(gr.GetFunction("eff_func").GetParameter(5)))
#tText.Draw()
#c1.Update()



tText_2 = ROOT.TPaveText(0.1,0.22,0.9,0.32,"blNDC")
tText_2.SetBorderSize(0)
tText_2.SetFillStyle(0)
tText_2.SetTextAlign(12)
tText_2.SetTextColor(1)
tText_2.SetTextFont(42)
tText_2.SetTextSize(0.04195804)
t1 = tText_2.AddText ("hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau")
t1 = tText_2.AddText ("#Delta R < 0.3")
#tText_2.Draw()
c1.Update()

tText_4 = ROOT.TPaveText(0.72,0.35,0.85,0.45,"blNDC")
tText_4.SetBorderSize(0)
tText_4.SetFillStyle(0)
tText_4.SetTextAlign(12)
tText_4.SetTextColor(1)
tText_4.SetTextFont(42)
tText_4.SetTextSize(0.04195804)
#t1 = tText_4.AddText ("4.394 fb^{-1}")
t1 = tText_4.AddText ("Run range")
t1 = tText_4.AddText ("[276271, ]")
#tText_4.Draw()
c1.Update()
c1.Print(label)

print n_total
time.sleep(10)

#print "%.2f<|#eta|<%.2f"%(etaList[my_eta_start_No+0][0],etaList[my_eta_start_No+0][1])
#print 'P0  %0.3f'%(gr.GetFunction("eff_func").GetParameter(0))
#print 'P1  %0.3f'%(gr.GetFunction("eff_func").GetParameter(1))
#print 'P2  %0.3f'%(gr.GetFunction("eff_func").GetParameter(2))
#print 'P3  %0.3f'%(gr.GetFunction("eff_func").GetParameter(3))
#print 'P4  %0.3f'%(gr.GetFunction("eff_func").GetParameter(4))
#print 'P5  %0.3f'%(gr.GetFunction("eff_func").GetParameter(5))
#print '*'*20
#print '%0.3f, %0.3f, %0.3f, %0.3f, %0.3f, %0.3f'%(gr.GetFunction("eff_func").GetParameter(0),gr.GetFunction("eff_func").GetParameter(1),gr.GetFunction("eff_func").GetParameter(2),gr.GetFunction("eff_func").GetParameter(3),gr.GetFunction("eff_func").GetParameter(4),gr.GetFunction("eff_func").GetParameter(5))
#print '*'*20
#
#print "%.2f<|#eta|<%.2f"%(etaList[my_eta_start_No+1][0],etaList[my_eta_start_No+1][1])
#print 'P0  %0.3f'%(gr_2.GetFunction("eff_func_2").GetParameter(0))
#print 'P1  %0.3f'%(gr_2.GetFunction("eff_func_2").GetParameter(1))
#print 'P2  %0.3f'%(gr_2.GetFunction("eff_func_2").GetParameter(2))
#print 'P3  %0.3f'%(gr_2.GetFunction("eff_func_2").GetParameter(3))
#print 'P4  %0.3f'%(gr_2.GetFunction("eff_func_2").GetParameter(4))
#print 'P5  %0.3f'%(gr_2.GetFunction("eff_func_2").GetParameter(5))
#print '*'*20
#print '%0.3f, %0.3f, %0.3f, %0.3f, %0.3f, %0.3f'%(gr_2.GetFunction("eff_func_2").GetParameter(0),gr_2.GetFunction("eff_func_2").GetParameter(1),gr_2.GetFunction("eff_func_2").GetParameter(2),gr_2.GetFunction("eff_func_2").GetParameter(3),gr_2.GetFunction("eff_func_2").GetParameter(4),gr_2.GetFunction("eff_func_2").GetParameter(5))
#print '*'*20
