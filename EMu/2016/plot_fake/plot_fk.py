import sys
try:
    sys.path.append("C:/root_v5.34.30/bin")
except:
    pass
import ROOT
import time
from math import *
from array import array
import os

from MuonSF.make_json_SF import *

def read_MuonSF_dic():
    dic_Trigger = writeMuonTriggerSF()
    dic_ISO = writeMuonISOSF()
    dic_ID = writeMuonIDSF()
    return dic_Trigger, dic_ISO, dic_ID

def GetMuonSF(dic_in, pt_in, eta_in):
    pt = pt_in
    eta = fabs(eta_in)
#    print pt
#    print eta
    eff = 1.0
    for (pt_l, pt_u) in dic_in:
        if pt>pt_l and pt<pt_u:
            for (eta_l, eta_u) in dic_in[(pt_l,pt_u)]:
                if eta>eta_l and eta<eta_u:
                    eff = dic_in[(pt_l,pt_u)][(eta_l,eta_u)]
                    return eff
#    print "***"
    return eff

def contain(x):
    if x>0:
        return 1
    else:
        return -1

def my_setzero(h2):
    for i in range(1,h2.GetNbinsX()+1):
        h2.SetBinContent(i,0.0)

def getYmax(h1):
    tmp_max = 0
    for i in range(1,h1.GetNbinsX()+1):
        if tmp_max < h1.GetBinContent(i):
            tmp_max = h1.GetBinContent(i)
    return tmp_max*1.5

def my_dicset(fnamedic_part1,fnamedic_part2,fnamedic_data,fnamedic_mc):
    fnamedic_data.clear()
    fnamedic_mc.clear()
    for (fname_in,fname_out) in fnamedic_part1:
        if fnamedic_part1[(fname_in,fname_out)][3][0]==1:
            fnamedic_data[(fname_in,fname_out)]=fnamedic_part1[(fname_in,fname_out)]
        else:
            fnamedic_mc[(fname_in,fname_out)]=fnamedic_part1[(fname_in,fname_out)]
    for (fname_in,fname_out) in fnamedic_part2:
        if fnamedic_part2[(fname_in,fname_out)][3][0]==1:
            fnamedic_data[(fname_in,fname_out)]=fnamedic_part2[(fname_in,fname_out)]
        else:
            fnamedic_mc[(fname_in,fname_out)]=fnamedic_part2[(fname_in,fname_out)]

def my_tongbu(fnamedic_data,fnamedic_mc,fnamedic_part1,fnamedic_part2):
    for (fname_in,fname_out) in fnamedic_data:
        if (fname_in,fname_out) in fnamedic_part1:
            fnamedic_part1[(fname_in,fname_out)]=fnamedic_data[(fname_in,fname_out)]
        elif (fname_in,fname_out) in fnamedic_part2:
            fnamedic_part2[(fname_in,fname_out)]=fnamedic_data[(fname_in,fname_out)]
    for (fname_in,fname_out) in fnamedic_mc:
        if (fname_in,fname_out) in fnamedic_part1:
            fnamedic_part1[(fname_in,fname_out)]=fnamedic_mc[(fname_in,fname_out)]
        elif (fname_in,fname_out) in fnamedic_part2:
            fnamedic_part2[(fname_in,fname_out)]=fnamedic_mc[(fname_in,fname_out)]

def Getweight(fnamedic_data,fnamedic_mc):
    sum_lumi=0.0
    for (fname_in,fname_out) in fnamedic_data:
        sum_lumi+=fnamedic_data[(fname_in,fname_out)][0][1]
    print 'sum lumi = ',sum_lumi

    print "*"*30  
    print 'Channel  ,   lumi scaled factor ,     lumi , normalized events    ,    N/data'
    print "*"*30  

    ndata=0
    for (fname_in,fname_out) in fnamedic_data:
        ndata+=fnamedic_data[(fname_in,fname_out)][1][0]

    n=0
    for (fname_in,fname_out) in fnamedic_data:
        print '%-25s %-8.2f\t%-8.2f\t%-8.2f\t%0.2f %%'%(fname_in,fnamedic_data[(fname_in,fname_out)][0][0],fnamedic_data[(fname_in,fname_out)][0][1],fnamedic_data[(fname_in,fname_out)][1][0],float(fnamedic_data[(fname_in,fname_out)][1][0])/ndata*100)
        n+=fnamedic_data[(fname_in,fname_out)][1][0]
        
    print 'total of data : %d '%n
    print "*"*30
    n=0
    for (fname_in,fname_out) in fnamedic_mc:
        #factor = data lumi * Xection / total number
        if fnamedic_mc[(fname_in,fname_out)][0][3]!=0:
            fnamedic_mc[(fname_in,fname_out)][0][1]=fnamedic_mc[(fname_in,fname_out)][0][3]/fnamedic_mc[(fname_in,fname_out)][0][2]
            fnamedic_mc[(fname_in,fname_out)][0][0]=fnamedic_mc[(fname_in,fname_out)][0][2]*sum_lumi/fnamedic_mc[(fname_in,fname_out)][0][3]
        if isUpdate:fnamedic_mc[(fname_in,fname_out)][1][0]*=fnamedic_mc[(fname_in,fname_out)][0][0]
        print '%-25s %-8.2f\t%-8.2f\t%-8.2f\t%0.2f %%'%(fname_in,fnamedic_mc[(fname_in,fname_out)][0][0],fnamedic_mc[(fname_in,fname_out)][0][1],fnamedic_mc[(fname_in,fname_out)][1][0],float(fnamedic_mc[(fname_in,fname_out)][1][0])/ndata*100)
        n+=fnamedic_mc[(fname_in,fname_out)][1][0]
        if not isUpdate:
            fnamedic_mc[(fname_in,fname_out)][0][0]=1

    print 'total of MC (no PU reweight)  :  %0.1f'%n
    print "*"*30
    n=0
    for (fname_in,fname_out) in fnamedic_mc:
        #factor = data lumi * Xection / total number
        if fnamedic_mc[(fname_in,fname_out)][0][3]!=0:
            fnamedic_mc[(fname_in,fname_out)][0][1]=fnamedic_mc[(fname_in,fname_out)][0][3]/fnamedic_mc[(fname_in,fname_out)][0][2]
            fnamedic_mc[(fname_in,fname_out)][0][0]=fnamedic_mc[(fname_in,fname_out)][0][2]*sum_lumi/fnamedic_mc[(fname_in,fname_out)][0][3]
        if isUpdate:fnamedic_mc[(fname_in,fname_out)][1][1]*=fnamedic_mc[(fname_in,fname_out)][0][0]
        print '%-25s %-8.2f\t%-8.2f\t%-8.2f\t%0.2f %%'%(fname_in,fnamedic_mc[(fname_in,fname_out)][0][0],fnamedic_mc[(fname_in,fname_out)][0][1],fnamedic_mc[(fname_in,fname_out)][1][1],float(fnamedic_mc[(fname_in,fname_out)][1][1])/ndata*100)
        n+=fnamedic_mc[(fname_in,fname_out)][1][1]
        if not isUpdate:
            fnamedic_mc[(fname_in,fname_out)][0][0]=1
    print 'total of MC (with PU reweight)  :  %0.1f'%n
    print "*"*30



def getbinwidth(x,x1):
    for i in range(len(x1)):
        if x < x1[i] and i>0:
            return (x1[i]-x1[i-1])
        elif x < x1[i]:
            return -1.0
    return -1.0

def setzero():
    return 0

def pm(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0



def my_plot(fname_in,fname_out,plotlistdic,filterstring,isData,isFake=False):
    try:
        _file0 = ROOT.TFile.Open(fname_in)
        tree=ROOT.gDirectory.Get("tap")
        print "open file: ",fname_in,"#  isData :",isData,"#  isFake :",isFake
    except:
        print "errors!"
    
    for path in plotlistdic:
        exec "h_%s.GetXaxis().SetTitle('%s')" % (path+fname_out,plotlistdic[path][1][0])
        exec "h_%s.GetXaxis().SetTitleSize(%s)" % (path+fname_out,plotlistdic[path][1][1])
        exec "h_%s.GetYaxis().SetTitle('%s')" % (path+fname_out,plotlistdic[path][1][2])
        exec "h_%s.GetYaxis().SetTitleSize(%s)" % (path+fname_out,plotlistdic[path][1][3])
    nevent_process = 0
    nevent_filed = 0.0
    nevent_filed_PU = 0.0
#    print tree.GetListOfLeaves()

    sf_weight = 1
    for event in tree:
        nevent_process+=1
#        if nevent_process>1000:break
        if(nevent_process%50000==0):print nevent_process,'processed\n'
        exec 'passed = (%s)' %(filterstring)
        if not passed:continue
        MuonSF_weight = 1.0
        ElectronSF_weight = 1.0
        if not isData:
            MuonSF_weight *= GetMuonSF(MuonTriggerSF_dic,getattr(event,"muon_pt"),getattr(event,"muon_eta"))
            MuonSF_weight *= GetMuonSF(MuonISOSF_dic,getattr(event,"muon_pt"),getattr(event,"muon_eta"))
            MuonSF_weight *= GetMuonSF(MuonIDSF_dic,getattr(event,"muon_pt"),getattr(event,"muon_eta"))

            if getattr(event,"t_region")==1:
                ElectronSF_weight *= 0.971
            elif getattr(event,"t_region")==3:
                ElectronSF_weight *= 0.982
        for path in plotlistdic:
            for p in plotlistdic[path][0][0]:
                weightstring=''
                if not 'getattr' in p:
                    p='getattr(event,"%s")'%(p)
                tmp_a=-1.0
                exec 'tmp_a=%s'%(p)
                if plotlistdic[path][3][0]==1:
                #if use PU reweight
                    if plotlistdic[path][2][2]==1:
                    #if use userdefined x aix from array:
                        if isData:
                            if isFake:
                                weightstring= 'getattr(event,"fake_weight")/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                            else:
                                weightstring= 'getattr(event,"w_PU_combined")/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                        else:
                            if isFake:
                                weightstring= 'getattr(event,"w_PU_combined")*getattr(event,"fake_weight")/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                            else:
                                weightstring= 'getattr(event,"w_PU_combined")/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                    else:
                        if isData:
                            if isFake:
                                weightstring= 'getattr(event,"fake_weight")' 
                            else:
                                weightstring= 'getattr(event,"w_PU_combined")' 
                        else:
                            if isFake:
                                weightstring= 'getattr(event,"w_PU_combined")*getattr(event,"fake_weight")'
                            else: 
                                weightstring= 'getattr(event,"w_PU_combined")'
            
                else:
                #if do not use PU reweight
                    if plotlistdic[path][2][2]==1:
                    #if use userdefined x aix from array:
                        if isData:
                            if isFake:
                                weightstring= 'getattr(event,"fake_weight")/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                            else:
                                weightstring= 'getattr(event,"w_PU_combined")/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                        else:
                            if isFake:
                                weightstring= 'pm(getattr(event,"w_PU_combined"))*getattr(event,"fake_weight")/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                            else:  
                                weightstring= 'pm(getattr(event,"w_PU_combined"))/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
                    else:
                        if isData:
                            if isFake:
                                weightstring= 'getattr(event,"fake_weight")' 
                            else:
                                weightstring= 'getattr(event,"w_PU_combined")' 
                        else:
                            if isFake: 
                                weightstring= 'pm(getattr(event,"w_PU_combined"))*getattr(event,"fake_weight")'
                            else:
                                weightstring= 'pm(getattr(event,"w_PU_combined"))'    
 
                exec 'total_weight = %s'%(weightstring)
                sf_weight = 1
                if not isData:
                    sf_weight *= MuonSF_weight
                    sf_weight *= ElectronSF_weight
                    total_weight *= sf_weight
                exec 'h_%s.Fill(tmp_a,%s)' % (path+fname_out,total_weight)

        if isData :
            if isFake:
                nevent_filed += getattr(event,"w_PU_combined")*getattr(event,"fake_weight")*sf_weight
            else:
                nevent_filed += getattr(event,"w_PU_combined")*sf_weight
        elif isFake :
            nevent_filed += pm(getattr(event,"w_PU_combined"))*getattr(event,"fake_weight")*sf_weight
            nevent_filed_PU += getattr(event,"w_PU_combined")*getattr(event,"fake_weight")*sf_weight
        else:
            nevent_filed += pm(getattr(event,"w_PU_combined"))*sf_weight
            nevent_filed_PU += getattr(event,"w_PU_combined")*sf_weight

    if isData:
        fnamedic_data[(fname_in,fname_out)][1][0]=nevent_filed
    else:
        fnamedic_mc[(fname_in,fname_out)][1][0]=nevent_filed
        fnamedic_mc[(fname_in,fname_out)][1][1]=nevent_filed_PU

                
def my_get(fname_in,fname_out,plotlistdic,isData,hfile):
    for path in plotlistdic:
        exec "h_%s = hfile.Get('%s')" % (path+fname_out,plotlistdic[path][0][1]+fname_out)
    if isData:
        for path in plotlistdic:
            if plotlistdic[path][2][2]==0:
            #if not use userdefined x aix from array:
                exec "nevent_filed=h_%s.Integral()" % (path+fname_out)
                fnamedic_data[(fname_in,fname_out)][1][0]=nevent_filed
                break
    else:
        for path in plotlistdic:
            if plotlistdic[path][3][0]==1 and len(plotlistdic[path][0][0]) == 1:
            #if use PU reweight
                if plotlistdic[path][2][2]==0:
                #if not use userdefined x aix from array:
                    exec "nevent_filed=h_%s.Integral()" % (path+fname_out)
                    fnamedic_mc[(fname_in,fname_out)][1][0]=nevent_filed
                    break
        for path in plotlistdic:
            if plotlistdic[path][3][0]==0 and len(plotlistdic[path][0][0]) == 1:
            #if not use PU reweight
                if plotlistdic[path][2][2]==0:
                #if not use userdefined x aix from array:
                    exec "nevent_filed=h_%s.Integral()" % (path+fname_out)
                    fnamedic_mc[(fname_in,fname_out)][1][1]=nevent_filed
                    break

#get lumi weight
def main_plot(fnamedic_part1,fnamedic_part2,plotlistdic,isUpdate,filterstring,label):
    try:
        os.mkdir(label)
    except:
        pass

    if isUpdate:
        hfile = ROOT.TFile(label+'/kkk_fk_'+label+'.root', 'RECREATE', 'Demo ROOT file with histograms' )
    else:
        hfile = ROOT.TFile(label+'/kkk_fk_'+label+'.root', 'READ', 'Demo ROOT file with histograms' )

#    fnamedic_data={}
#    fnamedic_mc={}
    my_dicset(fnamedic_part1,fnamedic_part2,fnamedic_data,fnamedic_mc)
    #define hists and plot
    for (fname_in,fname_out) in fnamedic_data:
        for path in plotlistdic:
            if isUpdate:
                exec "my_setzero(h_%s)"% (path+fname_out)
            else:
                #exec "my_setzero(h_%s)"% (path+fname_out)
                exec "h_%s = hfile.Get('%s')" % (path+fname_out,plotlistdic[path][0][1]+fname_out)    
    #  e.g    my_plot('data_golden2015D.root','_data_golden2015D',plotlistdic)
        if isUpdate:
            if 'fk' in fname_out:
                my_plot(fname_in,fname_out,plotlistdic,filterstring,True,True)
            else:
                my_plot(fname_in,fname_out,plotlistdic,filterstring,True)
        else:
            my_get(fname_in,fname_out,plotlistdic,True,hfile)        
    
    for (fname_in,fname_out) in fnamedic_mc:
        for path in plotlistdic:
            if isUpdate:
                exec "my_setzero(h_%s)"% (path+fname_out)
            else:
                exec "my_setzero(h_%s)"% (path+fname_out)
                exec "h_%s = hfile.Get('%s')" % (path+fname_out,plotlistdic[path][0][1]+fname_out)    
        if isUpdate:
            if 'fk' in fname_out:
                my_plot(fname_in,fname_out,plotlistdic,filterstring,False,True)
            else:
                my_plot(fname_in,fname_out,plotlistdic,filterstring,False)
        else:
            my_get(fname_in,fname_out,plotlistdic,False,hfile)        
       
#    for (fname_in,fname_out) in fnamedic_part3:
#        for path in plotlistdic:
#            exec "my_setzero(h_%s)"% (path+fname_out)

    
    #getweight must after my_plot in order to get passed number of each hist
    #if isUpdate:
    Getweight(fnamedic_data,fnamedic_mc)
    my_tongbu(fnamedic_data,fnamedic_mc,fnamedic_part1,fnamedic_part2) 
    #add
    c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 800,900 )
    #c1.cd()
    pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0 , 0)#used for ratio, the hist plot
    pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for ratio, the ratio plot
    pad3=ROOT.TPad("pad3", "pad3", 0, 0.3, 1, 1.0 , 0)#used for no ratio
    
    pad1.SetLogy()
    pad1.SetLogx()
#    pad1.SetBottomMargin(0.005)
    pad2.SetLogx()
    pad2.SetTopMargin(0.025)
    pad2.SetBottomMargin(0.2)
    pad3.SetLogy()
    pad3.SetLogx()
    
    
    
    #hist of sum part1
    for path in plotlistdic:
        legend_str='2016 data reMINIAOD (B-H)'
        if plotlistdic[path][2][2] == 1:
            exec "hsum_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][4])
        else:
            exec "hsum_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])
        #exec "hsum_%s.SetDefaultSumw2()" % (path)
        #exec "hsum_%s.GetXaxis().SetRangeUser(%s,%s)" % (path,plotlistdic[path][0][4],plotlistdic[path][0][5])
        for (fname_in,fname_out) in fnamedic_part1:
            exec "h_%s.SetFillColorAlpha(%s,0.35) " % (path+fname_out,str(fnamedic_part1[(fname_in,fname_out)][2][0]))
            exec "h_%s.Scale(%s)" % (path+fname_out, fnamedic_part1[(fname_in,fname_out)][0][0])
            exec "hsum_%s.Add(hsum_%s,h_%s,1,%s)" %(path,path,path+fname_out,fnamedic_part1[(fname_in,fname_out)][4][0])
            if fnamedic_part1[(fname_in,fname_out)][3][0]==0:
                legend_str+=str(fnamedic_part1[(fname_in,fname_out)][4][0]).split('1')[0]+fname_out[1:]
    print legend_str
    
    # scale with lumi factor
    for path in plotlistdic:
        for (fname_in,fname_out) in fnamedic_part2:
            exec "h_%s.SetFillColorAlpha(%s,0.35) " % (path+fname_out,str(fnamedic_part2[(fname_in,fname_out)][2][0]))
            exec "h_%s.Scale(%s)" % (path+fname_out, fnamedic_part2[(fname_in,fname_out)][0][0])

            print '%-25s %-8.2f\t%-8.2f\t%-8.2f'%(fname_in,fnamedic_mc[(fname_in,fname_out)][0][0],fnamedic_mc[(fname_in,fname_out)][0][1],fnamedic_mc[(fname_in,fname_out)][1][0])
            exec "print h_%s.Integral()" %(path+fname_out)


    #get list of hist apply to stack    
    for (fname_in,fname_out) in fnamedic_part3:
        for path in plotlistdic:
            fnamedic_part3[(fname_in,fname_out)][1][0]=0
            if plotlistdic[path][2][2] == 1:
                exec "hst_part_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path+fname_out,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][4])
            else:
                exec "hst_part_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path+fname_out,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])
            tmp_name_list = fnamedic_part3[(fname_in,fname_out)][0]
            for (fname_in_tmp, fname_out_tmp) in fnamedic_part2:
                if fname_out_tmp in tmp_name_list:
                    print '#'*30
                    print "%s in %s"%(fname_out_tmp, fname_out)
                    print '#'*30
                    exec "hst_part_%s.Add(hst_part_%s,h_%s,1,1)" %(path+fname_out,path+fname_out,path+fname_out_tmp)
                    #fnamedic_part3[(fname_in,fname_out)][1][0]+=fnamedic_part2[(fname_in_tmp,fname_out_tmp)][1][1]
            exec "hst_part_%s.SetFillColorAlpha(%s,0.35) " % (path+fname_out,str(fnamedic_part3[(fname_in,fname_out)][2][0]))
#            exec "print fname_out, hst_part_%s.Integral()" %(path+fname_out)
            exec "fnamedic_part3[(fname_in,fname_out)][1][0] = hst_part_%s.Integral()" %(path+fname_out)
                



    #hist of mc stack
    for path in plotlistdic:
        exec 'hst_%s = ROOT.THStack("hstack","%s")' % (path,plotlistdic[path][0][2]+label)
        if plotlistdic[path][2][2] == 1:
            exec "hst_sum_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][4])
            exec "hst_sum2_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][4])
        else:
            exec "hst_sum_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])
            exec "hst_sum2_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])
        #exec "hst_%s.GetXaxis().SetRangeUser(%s,%s)" % (path,plotlistdic[path][0][4],plotlistdic[path][0][5])
        for p in sorted(fnamedic_part3.iteritems(),key=lambda d:d[1][1][0],reverse = False):
            (fname_in,fname_out)=p[0]
            #print fname_in+'   ,   ',fnamedic_mc[(fname_in,fname_out)][1][0]
            exec 'hst_%s.SetTitle("")' % (path)
            exec "hst_%s.Add(hst_part_%s)" %(path,path+fname_out)
            print '#'*30
            print "%s stack in "%(path+fname_out)
            exec "hst_sum_%s.Add(hst_sum_%s,hst_part_%s,1,%s)" %(path,path,path+fname_out,fnamedic_part3[(fname_in,fname_out)][4][0])
            exec "hst_sum2_%s.Add(hst_sum2_%s,hst_part_%s,1,%s)" %(path,path,path+fname_out,fnamedic_part3[(fname_in,fname_out)][4][0]) # hist to calculate error
# error ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        n_bin = int(plotlistdic[path][0][3])
        n_error_sum = 0.0
        n_error_sum_data = 0.0
        n_number_sum = 0.0
        n_number_sum_data = 0.0

#error of data:
        for i in range(n_bin):
            exec "n_error_sum_data += (hsum_%s.GetBinError(i+1))**2" %(path)
        exec "n_number_sum_data = hsum_%s.Integral()" %(path)
        print '%s number of data: %f'%(path, n_number_sum_data)
        print '%s error of data: %f'%(path, sqrt(n_error_sum_data))

#error of MC
        for i in range(n_bin):
            exec "n_error_sum += (hst_sum2_%s.GetBinError(i+1))**2" %(path)
        exec "n_number_sum = hst_sum2_%s.Integral()" %(path)
        print '%s number of mc: %f'%(path, n_number_sum)
        print '%s error of mc: %f'%(path, sqrt(n_error_sum))

# set error 0
        for i in range(n_bin):
            exec "hst_sum_%s.SetBinError(i+1,0)" %(path)
    
    #hist of ratio
    for path in plotlistdic:
        exec "hratio_%s = hsum_%s.Clone('hratio_%s')" % (path,path,path)
        exec "hratio_%s.Sumw2()" % (path)
        exec "hratio_%s.SetStats(0)" % (path)
        exec 'hratio_%s.SetTitle("")' % (path)
        exec "hratio_%s.SetTitleSize(0.7)" % (path)
        exec "hratio_%s.GetXaxis().SetTitle('%s')" % (path,plotlistdic[path][1][0])
        exec "hratio_%s.GetXaxis().SetTitleSize(0.1)" % (path)
        exec "hratio_%s.GetXaxis().SetLabelSize(0.1)" % (path)
        exec "hratio_%s.GetYaxis().SetLabelSize(0.08)" % (path)
    
    #write draw and print
    for path in plotlistdic:
        print path

        pad1.SetLogx(plotlistdic[path][2][0])
        pad2.SetLogx(plotlistdic[path][2][0])
        pad3.SetLogx(plotlistdic[path][2][0])
        pad1.SetLogy(plotlistdic[path][2][1])
        pad3.SetLogy(plotlistdic[path][2][1])

        c1.cd()
        pad1.Draw()
        c1.cd()
        pad2.Draw()
        pad1.cd()
    
        #time.sleep(3)
        #
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if plotlistdic[path][0][7]!='null':
            exec "hst_%s.SetMinimum(%s)" % (path,plotlistdic[path][0][7])
        if plotlistdic[path][0][8]!='null':
            exec "hst_%s.SetMaximum(%s)" % (path,plotlistdic[path][0][8])
        else:
            exec "hst_%s.SetMaximum(getYmax(hsum_%s))" % (path,path)
        exec 'hst_%s.Draw("hist")'  % (path)
        exec "hst_%s.GetXaxis().SetTitle('%s')" %   (path,plotlistdic[path][1][0])
        exec "hst_%s.GetXaxis().SetTitleSize(%s)" % (path,plotlistdic[path][1][1])
        exec "hst_%s.GetYaxis().SetTitle('%s')" %   (path,plotlistdic[path][1][2])
        exec "hst_%s.GetYaxis().SetTitleSize(%s)" % (path,plotlistdic[path][1][3])

        try:   
            x_lengend=0.65-len(legend_str)/30*0.5 + plotlistdic[path][1][4] 
            y_lengend=0.7-len(fnamedic_part3)*0.03 + plotlistdic[path][1][5]
            x_lengend2=0.89 + plotlistdic[path][1][4]
            y_lengend2=0.89 + plotlistdic[path][1][5]
        except:
            x_lengend=0.65-len(legend_str)/30*0.5 
            y_lengend=0.7-len(fnamedic_part3)*0.03
            x_lengend2=0.89
            y_lengend2=0.89
        legend=ROOT.TLegend(x_lengend,y_lengend,x_lengend2,y_lengend2)
        exec 'legend.AddEntry(hsum_%s,"%s","pl")' %(path,legend_str)
        for p in sorted(fnamedic_part3.iteritems(),key=lambda d:d[1][1][0],reverse = True):
            (fname_in,fname_out)=p[0]
        #for (fname_in,fname_out) in fnamedic_mc:
            exec 'legend.AddEntry(hst_part_%s,"%s","f")' %(path+fname_out,fnamedic_part3[(fname_in,fname_out)][5][0])
    #    legend.AddEntry(gr2,"2e33","lp")
        legend.SetBorderSize(0)
        legend.Draw()
#Text

        tText_3=ROOT.TPaveText(0.13,0.78,0.2,0.9,"blNDC")
        tText_3.SetBorderSize(0)
        tText_3.SetFillStyle(0)
        tText_3.SetTextAlign(12)
        tText_3.SetTextColor(1)
        tText_3.SetTextFont(42)
        tText_3.SetTextSize(0.04195804)
        t1 = tText_3.AddText ("35.9fb^{-1}, 13 TeV")
        t2 = tText_3.AddText ('%s'%(cut[1:]))
#        t3 = tText_3.AddText ('Data Energy Scale')
#        t3 = tText_3.AddText (' EB:0.989*Et, EE:0.996*Et')
#        t3 = tText_3.AddText ('MC Energy Smear')
#        t3 = tText_3.AddText (' EB:1.075%, EE:1.88%')
#        t3 = tText_3.AddText ('Default Energy')
        tText_3.Draw()

    
        #c1.Update()
#        pad1.Print(label+'/hst_%s_%s.png'%(path,label))
        
        if plotlistdic[path][0][7]!='null':
            exec "hsum_%s.SetMinimum(%s)" % (path,plotlistdic[path][0][7])
        if plotlistdic[path][0][8]!='null':
            exec "hsum_%s.SetMaximum(%s)" % (path,plotlistdic[path][0][8])
        exec "hsum_%s.SetMarkerStyle(20)" % (path)
        exec "hsum_%s.SetLineColor(1)" % (path)
        exec "hsum_%s.SetStats(0)" % (path)
        exec 'hsum_%s.Draw("sames:PE")' % (path)
        exec "hsum_%s.GetXaxis().SetTitle('%s')" %   (path,plotlistdic[path][1][0])
        exec "hsum_%s.GetXaxis().SetTitleSize(%s)" % (path,plotlistdic[path][1][1])
        exec "hsum_%s.GetYaxis().SetTitle('%s')" %   (path,plotlistdic[path][1][2])
        exec "hsum_%s.GetYaxis().SetTitleSize(%s)" % (path,plotlistdic[path][1][3])
        pad1.Print(label+'/hsum_%s_%s.png'%(path,label))
#        pad1.SetBottomMargin(0.01)
        pad1.Draw()
    
        pad2.cd()
        exec "hratio_%s.Divide(hst_sum_%s)" % (path,path)
        exec "hratio_%s.SetMinimum(0.5)" % (path)
        exec "hratio_%s.SetMaximum(2)" % (path)
        exec 'hratio_%s.Fit("pol0")' % (path)
        exec "hratio_%s.SetMarkerStyle(20)" % (path)
        exec "hratio_%s.SetLineColor(1)" % (path)
        exec 'hratio_%s.Draw("fpe")' % (path)
    
        exec 'chi_ = hratio_%s.GetFunction("pol0").GetChisquare()' %(path)
        exec 'p0_  = hratio_%s.GetFunction("pol0").GetParameter(0)' %(path)
        legend2=ROOT.TLegend(0.1,0.87,0.4,0.97)
        exec 'legend2.AddEntry(hratio_%s,"Ratio = %0.2f, #chi^{2} : %0.2f" ,"l")' % (path,p0_,chi_)
        legend2.Draw()
    
        #c1.cd()
        c1.Update()
#        c1.Print(label+'/hratio_%s_%s.png'%(path,label))
    
        #time.sleep(3)
    
    
        c1.cd()
        pad3.Draw()
        pad3.cd()
#        for (fname_in,fname_out) in fnamedic_data:
#            exec 'h_%s.Draw("hist")' % (path+fname_out)
#            c1.Update()
#            pad3.Print(label+'/h_%s_%s.png'%(path+fname_out,label))
#            #time.sleep(1)
#        # 
#        for (fname_in,fname_out) in fnamedic_mc:
#            exec 'h_%s.Draw("hist")' % (path+fname_out)
#            c1.Update()
#            pad3.Print(label+'/h_%s_%s.png'%(path+fname_out,label))
#            #time.sleep(1)
        # 
    
    
    if isUpdate:
        hfile.cd()
        for path in plotlistdic:
    #        exec 'hsum_%s.Write()' % (path)
    #        exec 'hst_%s.Write()'  % (path)
            for (fname_in,fname_out) in fnamedic_data:
                exec 'h_%s.Write()' % (path+fname_out)
            for (fname_in,fname_out) in fnamedic_mc:
                exec 'h_%s.Write()' % (path+fname_out)

    
#main**************************************************************************

cutdir={
'_fake_rate_ALL':'True',
#'_fake_rate_BB':'(getattr(event,"t_region") == 1 and getattr(event,"muon_region") == 1)',
#'_fake_rate_BE':'(getattr(event,"t_region") == 1 and getattr(event,"muon_region") == 3)',
#'_fake_rate_EB':'(getattr(event,"t_region") == 3 and getattr(event,"muon_region") == 1)',
#'_fake_rate_EE':'(getattr(event,"t_region") == 3 and getattr(event,"muon_region") == 3)',
}

isUpdate = False
isUpdate = True


x_emu = array('f')
for i in range(31,64):
    x_emu.append(1.14**i)

x_pt = array('f')
for i in range(34,65):
    x_pt.append(1.12**i)

plotlistdic={
#'key':[[['branch1 name','branch2 name'],'hist name','hist title','nbin','array of bin','start bin','end bin','min x','max x'],['x label',x label size,'y label',y label size,pad1 legend x drift,y drift],[if x log,if y log, if userdefined x axis][if PU reweighted]],
'M_emu1':[[['M_emu'],'m_emu_PU1','Invirant mass(ee)','32','x_emu','60','3200','0.0001','100000'],['M(e#mu) (Gev/c^{2})',0.04,'Event / Gev',0.05],[1,1,1],[1]],
'M_emu2':[[['M_emu'],'m_ee_PU2','Invirant mass(ee)','60','x_emu','60','120','1','1000'],['M(e#mu) (Gev/c^{2})',0.04,'Event / Gev',0.05],[0,1,0],[1]],
'all_Et':[[['t_Et','muon_pt'],'et','distribution of Et','30','x_pt','50','1500','0.00001','10000'],['Et (Gev/c)',0.04,'Event / Gev',0.05],[1,1,1],[1]],
'all_eta':[[['t_eta','muon_eta'],'eta','disttibution of #eta','50','x_pt','-2.5','2.5','null','null'],['#eta',0.04,'Event ',0.05,0,0],[0,0,0],[1]],
'all_phi':[[['t_phi','muon_phi'],'phi','distribution of #phi ','35','x_pt','-3.5','3.5','null','null'],['#phi',0.04,'Event ',0.05],[0,0,0],[1]],
'heep1_Et':[[['t_Et'],'Et','distribution of heep1 Et ','30','x_pt','50','1500','0.00001','10000'],['E_{t}(e) (Gev/c)',0.04,'Event / Gev',0.05],[1,1,1],[1]],
'muon_Et':[[['muon_pt'],'muon_pt','distribution of heep2 Et','30','x_pt','50','1500','0.00001','10000'],['P_{t}(#mu) (Gev/c)',0.04,'Event / Gev',0.05],[1,1,1],[1]],
'heep1_eta':[[['t_eta'],'heep1_eta','distribution of eta heep1','51','x_pt','-2.55','2.55','null','null'],['#eta(e)',0.04,'Event ',0.05],[0,0,0],[1]],
'muon_eta':[[['muon_eta'],'muon_eta','distribution of eta heep2','51','x_pt','-2.55','2.55','null','null'],['#eta(#mu)',0.04,'Event ',0.05],[0,0,0],[1]],
'heep1_phi':[[['t_phi'],'heep1_phi','distribution of #phi','35','x_pt','-3.5','3.5','null','null'],['#phi(e)',0.04,'Event ',0.05],[0,0,0],[1]],
'muon_phi':[[['muon_phi'],'muon_phi','distribution of phi heep2','35','x_pt','-3.5','3.5','null','null'],['#phi(#mu)',0.04,'Event ',0.05],[0,0,0],[1]],
'pv_n_PU':[[['pv_n'],'N_vtx_PU','Number of vertex (with PU reweight)','35','null','0','35','null','null'],['N_{vtx}',0.04,'Event ',0.05],[0,0,0],[1]],
'Delta_eta':[[['fabs(getattr(event,"t_eta")-getattr(event,"muon_eta"))'],'D_eta','distribution of #Delta #eta ','25','x_pt','0','5','null','null'],['| #Delta #eta |',0.04,'Event ',0.05],[0,0,0],[1]],
'Delta_phi':[[['fabs(getattr(event,"t_phi")-getattr(event,"muon_phi"))'],'D_phi','distribution of #Delta #phi ','30','x_pt','0','6','null','null'],['| #Delta #phi |',0.04,'Event ',0.05],[0,0,0],[1]],
}


#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
fnamedic_part1={
('fk_data_2016_SingleMuon_SinglePhoton2.root','fk_data'):[[1, 35867,0,0],[-1],[38],[1],[1]],
}

fnamedic_part2={
('fk_ttbar.root','fkttbar'):[[1,0, 831.76, 77229341],  [-1,-1],[50],[0],[-1]],
('fk_DYToLL.root','fkDYToLL'):[[1,0, 5765.4, 49144274],  [-1,-1],[5],[0],[-1]],
#('fk_WJets.root','fkWJets'):[[1,0, 61526.7, 97393631],  [-1,-1],[8],[0],[-1]],
('fk_WW1.root','fkWW1'):      [[1,0, 12.178,   1926388],    [-1,-1],[30],[0],[-1]],
('fk_WW2.root','fkWW2'):      [[1,0, 0.1322,   200000],    [-1,-1],[30],[0],[-1]],
('fk_WW3.root','fkWW3'):      [[1,0, 0.005404,   200000],    [-1,-1],[30],[0],[-1]],
('fk_WW4.root','fkWW4'):      [[1,0, 0.00033931,   200000],    [-1,-1],[30],[0],[-1]],
('fk_WW5.root','fkWW5'):      [[1,0, 0.0000051484,   38969],    [-1,-1],[30],[0],[-1]],
('fk_WZ.root','fkWZ'):      [[1,0, 47.13,   1000000],    [-1,-1],[30],[0],[-1]],
('fk_ZZ.root','fkZZ'):      [[1,0, 16.523,  917056],    [-1,-1],[30],[0],[-1]],
('fk_ST.root','fkST'):      [[1,0, 71.2, 6035754+6012460],   [-1,-1],[7],[0],[-1]],
}

#(file name input,hist name output):[[name list],[nomilazed number],[color],[is data],[+/- factor],[legend]]
fnamedic_part3={
('ttbar.root','fkttbar'):[['fkttbar'],[0],[84],[0],[1],['t#bar{t}']],
#('WJets.root','fkWJets'):[['fkWJets'],[0],[89],[0],[1],['WJets']],
('Null','_TMP'):[['fkST','fkWW1','fkWW2','fkWW3','fkWW4','fkWW5','fkWZ','fkZZ','fkDYToLL'],[0],[64],[0],[1],['ST,WW,WZ,ZZ,DY']],
}

fnamedic_data={}
fnamedic_mc={}
fnamedic_vs={}

#define hists and plot
for (fname_in,fname_out) in fnamedic_part1:
    for path in plotlistdic:
        print path
        if plotlistdic[path][2][2] == 1:
            exec "h_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path+fname_out,plotlistdic[path][0][1]+fname_out,plotlistdic[path][0][2], plotlistdic[path][0][3], plotlistdic[path][0][4])
        else:
            exec "h_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path+fname_out,plotlistdic[path][0][1]+fname_out,plotlistdic[path][0][2], plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])

for (fname_in,fname_out) in fnamedic_part2:
    for path in plotlistdic:
        if plotlistdic[path][2][2] == 1:
            exec "h_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path+fname_out,plotlistdic[path][0][1]+fname_out,plotlistdic[path][0][2], plotlistdic[path][0][3], plotlistdic[path][0][4])
        else:
            exec "h_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path+fname_out,plotlistdic[path][0][1]+fname_out,plotlistdic[path][0][2], plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])

#run~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MuonTriggerSF_dic, MuonISOSF_dic, MuonIDSF_dic = read_MuonSF_dic()
for cut in cutdir:
    main_plot(fnamedic_part1,fnamedic_part2,plotlistdic,isUpdate,cutdir[cut],cut)

#main_plot(fnamedic_data,fnamedic_mc,plotlistdic,True,filterstring,cut)


