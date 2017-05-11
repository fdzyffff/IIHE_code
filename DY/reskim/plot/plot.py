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

def contain(x):
    if x>0:
        return 1
    else:
        return -1

def my_setzero(h2):
    for i in range(1,h2.GetNbinsX()+1):
        h2.SetBinContent(i,0.0)

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

    for event in tree:
        nevent_process+=1
        if(nevent_process%50000==0):print nevent_process,'processed\n'
        exec 'passed = (%s)' %(filterstring)
        if not passed:continue
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
                                weightstring= '1/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
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
                                weightstring= '1' 
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
                                weightstring= '1/getbinwidth(tmp_a,%s)' % (plotlistdic[path][0][4])
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
                                weightstring= '1' 
                        else:
                            if isFake: 
                                weightstring= 'pm(getattr(event,"w_PU_combined"))*getattr(event,"fake_weight")'
                            else:
                                weightstring= 'pm(getattr(event,"w_PU_combined"))'    

                exec 'h_%s.Fill(tmp_a,%s)' % (path+fname_out,weightstring)

        if isData :
            if isFake:
                nevent_filed += pm(getattr(event,"fake_weight"))
            else:
                nevent_filed += 1.0
        elif isFake :
            nevent_filed += pm(getattr(event,"w_PU_combined"))*getattr(event,"fake_weight")
            nevent_filed_PU += getattr(event,"w_PU_combined")*getattr(event,"fake_weight")
        else:
            nevent_filed += pm(getattr(event,"w_PU_combined"))
            nevent_filed_PU += getattr(event,"w_PU_combined")

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
        hfile = ROOT.TFile(label+'/kkk_'+label+'.root', 'RECREATE', 'Demo ROOT file with histograms' )
    else:
        hfile = ROOT.TFile(label+'/kkk_'+label+'.root', 'READ', 'Demo ROOT file with histograms' )

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
       

    
    #getweight must after my_plot in order to get passed number of each hist
    #if isUpdate:
    Getweight(fnamedic_data,fnamedic_mc)
    my_tongbu(fnamedic_data,fnamedic_mc,fnamedic_part1,fnamedic_part2) 
    #add
    c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 800,800 )
    #c1.cd()
    pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0 , 0)#used for ratio, the hist plot
    pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for ratio, the ratio plot
    pad3=ROOT.TPad("pad3", "pad3", 0, 0.3, 1, 1.0 , 0)#used for no ratio
    
    pad1.SetLogy()
    pad1.SetLogx()
    pad1.SetBottomMargin(0.005)
    pad2.SetLogx()
    pad2.SetTopMargin(0.025)
    pad2.SetBottomMargin(0.2)
    pad3.SetLogy()
    pad3.SetLogx()
    
    
    
    #hist of sum part1
    for path in plotlistdic:
        legend_str='2016B'
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
    
    
    #hist of mc stack
    for path in plotlistdic:
        exec 'hst_%s = ROOT.THStack("hstack","%s")' % (path,plotlistdic[path][0][2]+label)
        if plotlistdic[path][2][2] == 1:
            exec "hst_sum_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][4])
        else:
            exec "hst_sum_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path,plotlistdic[path][0][1],plotlistdic[path][0][2]+label, plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])
        #exec "hst_%s.GetXaxis().SetRangeUser(%s,%s)" % (path,plotlistdic[path][0][4],plotlistdic[path][0][5])
        for p in sorted(fnamedic_part2.iteritems(),key=lambda d:d[1][1][0],reverse = False):
            (fname_in,fname_out)=p[0]
            #print fname_in+'   ,   ',fnamedic_mc[(fname_in,fname_out)][1][0]
            exec "h_%s.SetFillColorAlpha(%s,0.35) " % (path+fname_out,str(fnamedic_part2[(fname_in,fname_out)][2][0]))
            exec "h_%s.Scale(%s)" % (path+fname_out, fnamedic_part2[(fname_in,fname_out)][0][0])
            exec "hst_%s.Add(h_%s)" %(path,path+fname_out)
            exec "hst_sum_%s.Add(hst_sum_%s,h_%s,1,%s)" %(path,path,path+fname_out,fnamedic_part2[(fname_in,fname_out)][4][0])
    
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
        exec 'hst_%s.Draw("hist")'  % (path)
        exec "hst_%s.GetXaxis().SetTitle('%s')" %   (path,plotlistdic[path][1][0])
        exec "hst_%s.GetXaxis().SetTitleSize(%s)" % (path,plotlistdic[path][1][1])
        exec "hst_%s.GetYaxis().SetTitle('%s')" %   (path,plotlistdic[path][1][2])
        exec "hst_%s.GetYaxis().SetTitleSize(%s)" % (path,plotlistdic[path][1][3])

        try:   
            x_lengend=0.75-len(legend_str)/30*0.5 + plotlistdic[path][1][4] 
            y_lengend=0.85-len(fnamedic_part2)*0.03 + plotlistdic[path][1][5]
            x_lengend2=0.9 + plotlistdic[path][1][4]
            y_lengend2=0.9 + plotlistdic[path][1][5]
        except:
            x_lengend=0.75-len(legend_str)/30*0.5 
            y_lengend=0.85-len(fnamedic_part2)*0.03
            x_lengend2=0.9
            y_lengend2=0.9
        legend=ROOT.TLegend(x_lengend,y_lengend,x_lengend2,y_lengend2)
        exec 'legend.AddEntry(hsum_%s,"%s","pl")' %(path,legend_str)
        for p in sorted(fnamedic_part2.iteritems(),key=lambda d:d[1][1][0],reverse = True):
            (fname_in,fname_out)=p[0]
        #for (fname_in,fname_out) in fnamedic_mc:
            exec 'legend.AddEntry(h_%s,"%s","f")' %(path+fname_out,fname_out[1:])
    #    legend.AddEntry(gr2,"2e33","lp")
        legend.Draw()
    
        #c1.Update()
        pad1.Print(label+'/hst_%s_%s.png'%(path,label))
        
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
        #c1.Update()
        pad1.Print(label+'/hsum_%s_%s.png'%(path,label))
    
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
        c1.Print(label+'/hratio_%s_%s.png'%(path,label))
    
        time.sleep(3)
    
    
        c1.cd()
        pad3.Draw()
        pad3.cd()
        for (fname_in,fname_out) in fnamedic_data:
            exec 'h_%s.Draw("hist")' % (path+fname_out)
            c1.Update()
            pad3.Print(label+'/h_%s_%s.png'%(path+fname_out,label))
            #time.sleep(1)
        # 
        for (fname_in,fname_out) in fnamedic_mc:
            exec 'h_%s.Draw("hist")' % (path+fname_out)
            c1.Update()
            pad3.Print(label+'/h_%s_%s.png'%(path+fname_out,label))
            #time.sleep(1)
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
#'_all_charge':'True',
#'_barrel-barrel':'getattr(event,"t_region")==1 and getattr(event,"heep2_region")==1',
#'_barrel-endcap':'(getattr(event,"t_region")==1 and getattr(event,"heep2_region")==3) or (getattr(event,"t_region")==3 and getattr(event,"heep2_region")==1)',
'_barrel-barrel':'getattr(event,"t_region")==1 and getattr(event,"heep2_region")==1 and (getattr(event,"M_ee") > 60 and getattr(event,"M_ee") < 120)',
#'_endcap-endcap':'getattr(event,"t_region")==3 and getattr(event,"heep2_region")==3',
#'_endcap-endcap':'getattr(event,"t_region")==3 and getattr(event,"heep2_region")==3',
'_barrel-endcap':'(getattr(event,"t_region")==1 and getattr(event,"heep2_region")==3 and (getattr(event,"M_ee") > 60 and getattr(event,"M_ee") < 120)) or (getattr(event,"t_region")==3 and getattr(event,"heep2_region")==1 and (getattr(event,"M_ee") > 60 and getattr(event,"M_ee") < 120))',
#'_samecharge':'getattr(event,"t_charge")==getattr(event,"mu_charge")',
#'_anticharge':'getattr(event,"t_charge")!=getattr(event,"mu_charge")',
}
isUpdate = True
#isUpdate = False


x_emu = array('f')
for i in range(31,64):
    x_emu.append(1.14**i)

x_pt = array('f')
for i in range(34,65):
    x_pt.append(1.12**i)

plotlistdic={
#'key':[[['branch1 name','branch2 name'],'hist name','hist title','nbin','array of bin','start bin','end bin','min x','max x'],['x label',x label size,'y label',y label size,pad1 legend x drift,y drift],[if x log,if y log, if userdefined x axis][if PU reweighted]],
#'M_ee1':[[['M_ee'],'m_ee_PU1','Invirant mass(ee)','32','x_emu','60','3200','0.0001','100000'],['M(ee) (Gev/c^{2})',0.04,'Event / Gev',0.05],[1,1,1],[1]],
'M_ee2':[[['M_ee'],'m_ee_PU2','Invirant mass(ee)','30','x_emu','60','120','0.01','1000000'],['M(ee) (Gev/c^{2})',0.04,'Event / Gev',0.05],[0,1,0],[1]],
#'heep_Et':[[['t_Et','heep2_pt'],'et','distribution of Et','30','x_pt','50','1500','0.00001','10000'],['Et (Gev/c)',0.04,'Event / Gev',0.05],[1,1,1],[1]],
#'heep_eta':[[['t_eta','heep2_eta'],'eta','disttibution of #eta','50','x_pt','-2.5','2.5','null','null'],['#eta',0.04,'Event ',0.05,0,0],[0,0,0],[1]],
#'heep_phi':[[['t_phi','heep2_phi'],'phi','distribution of #phi ','100','x_pt','-5','5','null','null'],['#phi',0.04,'Event ',0.05],[0,0,0],[1]],
#'heep1_Et':[[['t_Et'],'Et','distribution of heep1 Et ','30','x_pt','50','1500','0.00001','10000'],['Et(e) (Gev/c)',0.04,'Event / Gev',0.05],[1,1,1],[1]],
#'heep2_Et':[[['heep2_pt'],'heep2_pt','distribution of heep2 Et','30','x_pt','50','1500','0.00001','10000'],['Et(heep2) (Gev/c)',0.04,'Event / Gev',0.05],[1,1,1],[1]],
#'heep1_eta':[[['t_eta'],'heep1_eta','distribution of eta heep1','24','x_pt','-2.5','2.5','null','null'],['eta(heep1)',0.04,'Event ',0.05],[0,0,0],[1]],
#'heep2_eta':[[['heep2_eta'],'heep2_eta','distribution of eta heep2','24','x_pt','-2.5','2.5','null','null'],['eta(heep2)',0.04,'Event ',0.05],[0,0,0],[1]],
#'heep1_phi':[[['t_phi'],'heep1_phi','distribution of #phi','30','x_pt','-3','3','null','null'],['#phi',0.04,'Event ',0.05],[0,0,0],[1]],
#'heep2_phi':[[['heep2_phi'],'heep2_phi','distribution of phi heep2','30','x_pt','-3','3','null','null'],['phi(heep2)',0.04,'Event ',0.05],[0,0,0],[1]],
#'pv_n_PU':[[['pv_n'],'N_vtx_PU','Number of vertex (with PU reweight)','35','null','0','35','null','null'],['N-vtx',0.04,'Event ',0.05],[0,0,0],[1]],
#'Delta_eta':[[['fabs(getattr(event,"t_eta")-getattr(event,"heep2_eta"))'],'D_eta','distribution of #Delta #eta ','25','x_pt','0','5','null','null'],['| #Delta #eta |',0.04,'Event ',0.05],[0,0,0],[1]],
#'Delta_phi':[[['fabs(getattr(event,"t_phi")-getattr(event,"heep2_phi"))'],'D_phi','distribution of #Delta #phi ','30','x_pt','0','6','null','null'],['| #Delta #phi |',0.04,'Event ',0.05],[0,0,0],[1]],
}

#(file name input,hist name output):[[factor, lumi, cross Section, event],[nomilazed number],[color],[is data],[+/- factor]]
fnamedic_part1={
('data_2016B_DoubleEG.root','_2016B'):[[1, 589,0,0],[-1],[38],[1],[1]],
}

fnamedic_part2={
('ttbar.root','_ttbar'):[[1,0, 831.76,  34822127],  [-1,-1],[6],[0],[1]],
('DYToLL.root','_DYToLL'):[[1,0, 6025.2,11813708],  [-1,-1],[5],[0],[1]],
('WJets.root','_WJets'):[[1,0, 61526.7, 28228984],  [-1,-1],[8],[0],[1]],
('WW.root','_WW'):      [[1,0, 118.7,   993214],    [-1,-1],[30],[0],[1]],
('WZ.root','_WZ'):      [[1,0, 47.13,   967144],    [-1,-1],[30],[0],[1]],
('ZZ.root','_ZZ'):      [[1,0, 16.523,  978816],    [-1,-1],[30],[0],[1]],
('ST.root','_ST'):      [[1,0, 71.2,    1987400],   [-1,-1],[7],[0],[1]],
}

fnamedic_part3={
('Null','_TMP'):['_WW','_WZ','ZZ'],
}

fnamedic_data={}
fnamedic_mc={}
fnamedic_vs={}

#define hists and plot
for (fname_in,fname_out) in fnamedic_part1:
    for path in plotlistdic:
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

for (fname_in,fname_out) in fnamedic_part3:
    for path in plotlistdic:
        if plotlistdic[path][2][2] == 1:
            exec "h_%s = ROOT.TH1F( '%s','%s',%s,%s)" % (path+fname_out,plotlistdic[path][0][1]+fname_out,plotlistdic[path][0][2], plotlistdic[path][0][3], plotlistdic[path][0][4])
        else:
            exec "h_%s = ROOT.TH1F( '%s','%s',%s,%s,%s)" % (path+fname_out,plotlistdic[path][0][1]+fname_out,plotlistdic[path][0][2], plotlistdic[path][0][3], plotlistdic[path][0][5], plotlistdic[path][0][6])
#run~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for cut in cutdir:
    main_plot(fnamedic_part1,fnamedic_part2,plotlistdic,isUpdate,cutdir[cut],cut)

#main_plot(fnamedic_data,fnamedic_mc,plotlistdic,True,filterstring,cut)


