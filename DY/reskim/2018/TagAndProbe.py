#import array, 
import math

from mod_settings import *
from mod_variable import variables
from mod_fit      import fit_object
from mod_sample   import samples, sample_object
from mod_plot     import kinematic_plots, compare_plot , compare_plot_xmas

##########################################################################################
#                             Import ROOT and apply settings                             #
##########################################################################################
import ROOT
ROOT.gROOT.SetBatch(ROOT.kTRUE)

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetFrameBorderMode(ROOT.kWhite)
#ROOT.gStyle.SetFrameFillColor(ROOT.kWhite)
ROOT.gStyle.SetCanvasBorderMode(ROOT.kWhite)
#ROOT.gStyle.SetCanvasColor(ROOT.kWhite)
ROOT.gStyle.SetPadBorderMode(ROOT.kWhite)
#ROOT.gStyle.SetPadColor(ROOT.kWhite)
ROOT.gStyle.SetStatColor(ROOT.kWhite)

##########################################################################################
#                                 Tools for making plots                                 #
##########################################################################################
class histogram_wrapper:
    def __init__(self, histogram, legend_entry, style):
        self.h = histogram
        self.legend = legend_entry
        self.style = style
        self.style.style_histogram(self.h)

class SF_object:
    def __init__(self, name, title, hw_numer, hw_denom, strategy):
        self.hw_numer = hw_numer
        self.hw_denom = hw_denom
        self.name  = name
        self.title = title
        
        self.min =  1e6
        self.max = -1e6
        
        for h in [self.hw_numer.h,self.hw_denom.h]:
            for bin in range(1, h.GetNbinsX()+1):
                value = h.GetBinContent(bin)
                error = h.GetBinError  (bin)
                if value < 1e-3:
                    continue
                if value - error < self.min:
                    self.min = value - error
                if value + error > self.max:
                    self.max = value + error
        
        hName_ratio = '%s_%s_ratio'%(self.hw_numer.h.GetName(), self.name)
        h_ratio = self.hw_numer.h.Clone(hName_ratio)
        for bin in range(1,h_ratio.GetNbinsX()+1):
            h_ratio.SetBinContent(bin,abs(h_ratio.GetBinContent(bin))
        h_ratio.Divide(self.hw_denom.h)
        self.hw_numer.h.GetYaxis().SetTitle('Efficiency')
        self.hw_denom.h.GetYaxis().SetTitle('Efficiency')
        h_ratio.GetYaxis().SetTitle('Scale factor')
        
        h_ratio.GetYaxis().SetTitleSize(0.18)
        h_ratio.GetYaxis().SetTitleOffset(0.3)
        
        h_ratio.GetYaxis().SetLabelSize(0.15)
        h_ratio.GetXaxis().SetLabelSize(0.15)
        h_ratio.GetXaxis().SetTitleSize(0.15)
        h_ratio.GetXaxis().SetTitleOffset(1.0)
        h_ratio.GetXaxis().SetTickLength(0.1)
        h_ratio.GetXaxis().SetMoreLogLabels()
        h_ratio.GetXaxis().SetNoExponent()
        self.hw_ratio = histogram_wrapper(h_ratio, 'ratio', self.hw_numer.style)
        
        # Fit a flat line.
        self.fConstant = ROOT.TF1('fConstant_%s'%self.hw_ratio.h.GetName(), '[0]')
        self.fConstant.SetParameters(1.0,0.0)
        self.fConstant.SetLineColor(self.hw_ratio.h.GetLineColor())
        self.fConstant.SetLineStyle(ROOT.kDashed)
        self.fConstant.SetLineWidth(2)
        self.hw_ratio.h.Fit(self.fConstant)
        self.chi2 = self.fConstant.GetChisquare()
        self.ndof = self.hw_ratio.h.GetNbinsX()-1

        self.a_value = self.fConstant.GetParameter(0)
        self.a_error = self.fConstant.GetParError (0)

        if self.ndof < 0:
            self.ndof = 0
        self.chi2_label   = ROOT.TLatex(0.15, 0.85, '#chi^{2}/ndof = %.2f/%d'%(self.chi2,self.ndof))
        self.params_label = ROOT.TLatex(0.85, 0.85, 'SF = %.3f (#pm %.3f)'%(self.a_value, self.a_error))
        self.chi2_label  .SetNDC()
        self.params_label.SetNDC()
        self.chi2_label  .SetTextAlign(12)
        self.params_label.SetTextAlign(32)
        self.chi2_label  .SetTextSize(0.12)
        self.params_label.SetTextSize(0.12)

##########################################################################################
#                                    Now do the study                                    #
##########################################################################################

ScaleFactors = {}

for card in deck_of_cards:
    print card.name , card.options
    
    for sname in samples:
        samples[sname].set_card(card)
    for vname in card.variable_names:
        variables[vname].set_card(card)

    if card.options['base_histograms']:
        fBase = ROOT.TFile('hBase.root','RECREATE')
        for vname in card.variable_names:
            v = variables[vname]
            v.hBase_1D_fine.Write()
            v.hBase_2D_fine.Write()
            for rname in card.region_names:
                v.hBase_1D_fit[rname].Write()
                v.hBase_2D_fit[rname].Write()
                v.hBase_1D_cut[rname].Write()
                v.hBase_2D_cut[rname].Write()
        fBase.Close()
    
    for sname in samples:
        samples[sname].load_histograms_from_file()

    if card.options['do_analysis'] and (card.options['do_fits'] or card.options['do_cuts']):
        fOut = ROOT.TFile(card.filename_histos,'UPDATE')
    
        fOut.cd()
        cut_eff_histograms = {}
        fit_eff_histograms = {}
        if card.options['do_fits']:
            canvas.Print('%s/h_fit_eff_%s.pdf['%(card.plot_prefix,card.name))
            canvas.Print('%s/h_fit_2D_%s.pdf[' %(card.plot_prefix,card.name))
        if card.options['do_cuts']:
            canvas.Print('%s/h_cut_eff_%s.pdf['%(card.plot_prefix,card.name))
            canvas.Print('%s/h_cut_2D_%s.pdf[' %(card.plot_prefix,card.name))
        for vname in card.variable_names:
            v = variables[vname]
            for rname in card.region_names:
                for cname in card.charge_names:
                    for tname in card.tagCharge_names:
                        for aname in card.altCut_names:
                            for OSSSname in card.OSSS_names:
                                for strname in strategyNames:
                                    for PUname in card.PUW_names:
                                        v.fit_spectrum(samples, rname, cname, tname, strname, aname, OSSSname, PUname, fit_eff_histograms, cut_eff_histograms, fOut)
        if card.options['do_fits']:
            canvas.Print('%s/h_fit_eff_%s.pdf]'%(card.plot_prefix,card.name))
            canvas.Print('%s/h_fit_2D_%s.pdf]' %(card.plot_prefix,card.name))
        if card.options['do_cuts']:
            canvas.Print('%s/h_cut_eff_%s.pdf]'%(card.plot_prefix,card.name))
            canvas.Print('%s/h_cut_2D_%s.pdf]' %(card.plot_prefix,card.name))

        fOut.Close()
    
    if card.options['do_compare']:
        fCompare_out = ROOT.TFile(card.compare_histos ,'RECREATE')
        fCompare     = ROOT.TFile(card.filename_histos,'READ'    )
    
        methodNames = []
        if card.options['do_fits']:
            methodNames.append('fit')
        if card.options['do_cuts']:
            methodNames.append('cut')
    
        for mname in methodNames:
            for vname in card.variable_names:
                for rname in card.region_names:
                    for cname in card.charge_names:
                        for tname in card.tagCharge_names:
                            for aname in card.altCut_names:
                                for OSSSname in card.OSSS_names:
                                    for PUWname in card.PUW_names:
                                        for strname in ['exc','inc']:
                                            # Get histograms.
                                            suffix = '%s_%s_%s_pass_%s_%s_%s'%(strname, rname, cname, OSSSname, aname, PUWname)
                                            hName_data = 'h_%s_eff_%s_data_%s'%(mname,vname,suffix)
                                            hName_MC   = 'h_%s_eff_%s_MC_%s'  %(mname,vname,suffix)
                                            
                                            h_data = fCompare.Get(hName_data)
                                            h_MC   = fCompare.Get(hName_MC  )
                                            
                                            labels = make_labels(args=['CMS',OSSSname,aname,rname,cname,strname], lumi=card.lumi)
                                            
                                            suffix = '%s_%s_%s_%s_%s_%s_%s_%s_%s'%(mname,vname,rname,cname,tname,strname,OSSSname,aname,PUWname)
                                
                                            data_legend = 'Data' if strname=='inc' else 'Data (non DY subtracted)'
                                            MC_legend   = 'DY'   if strname=='exc' else 'DY+non-DY'
                                            
                                            if not h_data or not h_MC:
                                                fCompare.ls()
                                                print hName_data
                                                print hName_MC
                                                print '!!'
                                            
                                            hw_data = histogram_wrapper(h_data, data_legend, styles['data_%s'%strname])
                                            hw_MC   = histogram_wrapper(h_MC  ,   MC_legend, styles[  'MC_%s'%strname])
                                    
                                            SF = SF_object('', '', hw_data, hw_MC, strname)
                                            ScaleFactors[(mname,vname,rname,cname,tname,aname,OSSSname,strname,PUWname)] = SF
                                    
                                            #compare_plot_xmas([SF], labels, vname, suffix, card, fCompare_out)
                                            compare_plot([SF], labels, vname, suffix, card, fCompare_out)
                                
                                        # Get histograms.
                                        suffix = '%s_%s_pass_%s_%s_%s'%(rname, cname, OSSSname, aname, PUWname)
                                        hName_data_inc = 'h_%s_eff_%s_data_inc_%s'%(mname,vname,suffix)
                                        hName_data_exc = 'h_%s_eff_%s_data_exc_%s'%(mname,vname,suffix)
                                        hName_MC_inc   = 'h_%s_eff_%s_MC_inc_%s'  %(mname,vname,suffix)
                                        hName_MC_exc   = 'h_%s_eff_%s_MC_exc_%s'  %(mname,vname,suffix)
                            
                                        h_data_inc = fCompare.Get(hName_data_inc)
                                        h_MC_inc   = fCompare.Get(hName_MC_inc  )
                                        h_data_exc = fCompare.Get(hName_data_exc)
                                        h_MC_exc   = fCompare.Get(hName_MC_exc  )
                            
                                        if not h_data_inc or not h_MC_inc:
                                                fCompare.ls()
                                                print hName_data_inc
                                                print hName_MC_inc
                            
                                        labels = make_labels(args=[OSSSname,aname,'CMS',rname,cname], lumi=card.lumi)
                                
                                        suffix = '%s_%s_%s_%s_%s_%s_%s_%s'%(mname,vname,rname,cname,tname,OSSSname,aname,PUWname)
                            
                                        data_legend = 'Data' if strname=='inc' else 'Data (non DY subtracted)'
                                        MC_legend   = 'DY'   if strname=='exc' else 'DY+non-DY'
                                        hw_data_inc = histogram_wrapper(h_data_inc, 'Data'                    , styles['data_inc'])
                                        hw_MC_inc   = histogram_wrapper(h_MC_inc  , 'DY+non-DY'               , styles[  'MC_inc'])
                                        hw_data_exc = histogram_wrapper(h_data_exc, 'Data (non DY subtracted)', styles['data_exc'])
                                        hw_MC_exc   = histogram_wrapper(h_MC_exc  , 'DY'                      , styles[  'MC_exc'])
                            
                                        SF_inc = SF_object('inc', 'non-DY included'  , hw_data_inc, hw_MC_inc, strname)
                                        SF_exc = SF_object('exc', 'non-DY subtracted', hw_data_exc, hw_MC_exc, strname)
                            
                                        #compare_plot_xmas([SF_inc,SF_exc], labels, vname, suffix, card, None)
                                        compare_plot([SF_inc,SF_exc], labels, vname, suffix, card, None)
    
    if card.options['print_effs']:
        for vname in ['phi']:
            v = variables[vname]
            for rname in card.region_names:
                for cname in card.charge_names:
                    for tname in card.tagCharge_names:
                        #for aname in ['nominal']:
                        for aname in card.altCut_names:
                            for PUWname in card.PUW_names:
                                for OSSSname in ['AS']:
                                    nEvents  = {}
                                    variance = {}
                                    eff_value = {}
                                    eff_error = {}
                        
                                    print '%4s  %10s  %2s  %2s  %20s  %2s'%(vname, rname, cname, tname, aname, OSSSname)
                                    for strname in strategyNames:
                                        nEvents [strname] = {}
                                        variance[strname] = {}
                            
                                        for HEEPname in card.HEEP_names:
                                            args = (vname, rname, cname, tname, HEEPname, OSSSname, aname, PUWname)
                                            histos = get_histos_from_args(args, strname, samples, card)
                                            h_2D_cut = histos['cut']
                                
                                            nEvents[strname][HEEPname] = h_2D_cut.GetSumOfWeights()
                                            error = 0
                                            for binX in range(1, h_2D_cut.GetNbinsX()+1):
                                                for binY in range(1, h_2D_cut.GetNbinsY()+1):
                                                    error += math.pow(h_2D_cut.GetBinError(binX,binY),2)
                                            variance[strname][HEEPname] = error

                                    for strname in strategyNames:
                                        eff_value[strname] = 1
                                        eff_error[strname] = 0
                                        if nEvents[strname]['probes'] > 0 and nEvents[strname]['pass'] > 0:
                                            N1 = nEvents[strname]['probes']
                                            N2 = nEvents[strname]['pass'  ]
                                            e1 = math.sqrt(variance[strname]['probes'])/N1
                                            e2 = math.sqrt(variance[strname]['pass'  ])/N2
                                            eff = eff_value[strname]
                                            err = math.sqrt(abs((1-2*eff)*e2*e2+math.pow(eff*e1,2)/(N2*N2)))
                                    
                                            eff_value[strname] = nEvents[strname]['pass']/nEvents[strname]['probes']
                                            eff_error[strname] = err
                                    
                                            print '%10s  %5.2f%% +- %5.2f%%'%(strname, 100*eff_value[strname], 100*eff_error[strname])
                        
                        
                                    SF_value = {}
                                    SF_error = {}
                                    for strname in ['inc','exc']:
                                        deff = eff_value['data_%s'%strname]
                                        Meff = eff_value[  'MC_%s'%strname]
                                        derr = eff_error['data_%s'%strname]
                                        Merr = eff_error[  'MC_%s'%strname]
                                        SF_value[strname] = deff/Meff
                                        SF_error[strname] = SF_value[strname]*math.sqrt(math.pow(derr/deff,2)+math.pow(Merr/Meff,2))
                                        print 'SF (%3s)  %5.3f  +- %5.3f'%(strname,SF_value[strname],SF_error[strname])
                                    print

    if card.options['kinematics']:
        kinematic_plots(card)
    
    if card.options['do_PUStudy']:
        hBase_SF_variations_PUW = ROOT.TH1F('hBase_SF_variations_PUW', '', 10, 0.5, 40.5)
        hBase_SF_variations_PUW.GetXaxis().SetNdivisions(010,False)
        hBase_SF_variations_PUW.SetMinimum(0.95)
        hBase_SF_variations_PUW.SetMaximum(1.15)
        hBase_SF_variations_PUW.GetXaxis().SetTitle('PU weight')
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 1, '(N-1)/(N-1)')
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 2, '(N-1)/(N)'  )
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 3, '(N-1)/(N+1)')
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 4,   '(N)/(N-1)')
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 5,   '(N)/(N)'  )
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 6,   '(N)/(N+1)')
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 7, '(N+1)/(N-1)')
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 8, '(N+1)/(N)'  )
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel( 9, '(N+1)/(N+1)')
        hBase_SF_variations_PUW.GetXaxis().SetBinLabel(10, '1.0'        )
    
        hBase_SF_variations_var = ROOT.TH1F('hBase_SF_variations_var', '', 40, 0.5, 40.5)
        hBase_SF_variations_Et   = hBase_SF_variations_var.Clone('hBase_SF_variations_Et'  )
        hBase_SF_variations_eta  = hBase_SF_variations_var.Clone('hBase_SF_variations_eta' )
        hBase_SF_variations_phi  = hBase_SF_variations_var.Clone('hBase_SF_variations_phi' )
        hBase_SF_variations_nVtx = hBase_SF_variations_var.Clone('hBase_SF_variations_nVtx')
    
        styles[  'Et'].style_histogram(hBase_SF_variations_Et  )
        styles[ 'eta'].style_histogram(hBase_SF_variations_eta )
        styles[ 'phi'].style_histogram(hBase_SF_variations_phi )
        styles['nVtx'].style_histogram(hBase_SF_variations_nVtx)
    
        legend_variation = ROOT.TLegend(0.15, 0.85, 0.85, 0.8)
        legend_variation.SetFillColor(0)
        legend_variation.SetBorderSize(0)
        legend_variation.SetShadowColor(0)
        legend_variation.SetNColumns(4)
        legend_variation.AddEntry(hBase_SF_variations_Et  , 'E_{T}'  , 'pe')
        legend_variation.AddEntry(hBase_SF_variations_eta , '#eta'   , 'pe')
        legend_variation.AddEntry(hBase_SF_variations_phi , '#phi'   , 'pe')
        legend_variation.AddEntry(hBase_SF_variations_nVtx, 'n_{Vtx}', 'pe')
    
    
        h_SF_variations_Et   = {}
        h_SF_variations_eta  = {}
        h_SF_variations_phi  = {}
        h_SF_variations_nVtx = {}
        for strname in ['inc','exc']:
            for rname in card.region_names:
                h_SF_variations_Et  [(rname,strname)] = hBase_SF_variations_Et  .Clone('h_SF_variations_Et_%s_%s'  %(rname,strname))
                h_SF_variations_eta [(rname,strname)] = hBase_SF_variations_eta .Clone('h_SF_variations_eta_%s_%s' %(rname,strname))
                h_SF_variations_phi [(rname,strname)] = hBase_SF_variations_phi .Clone('h_SF_variations_phi_%s_%s' %(rname,strname))
                h_SF_variations_nVtx[(rname,strname)] = hBase_SF_variations_nVtx.Clone('h_SF_variations_nVtx_%s_%s'%(rname,strname))
                
                PUcounter = 1
                for PUWname in card.PUW_names:
                    SF_Et   = ScaleFactors[('cut','Et'  ,rname,'ea','ta','nominal','AS',strname,PUWname)]
                    SF_eta  = ScaleFactors[('cut','eta' ,rname,'ea','ta','nominal','AS',strname,PUWname)]
                    SF_phi  = ScaleFactors[('cut','phi' ,rname,'ea','ta','nominal','AS',strname,PUWname)]
                    SF_nVtx = ScaleFactors[('cut','nVtx',rname,'ea','ta','nominal','AS',strname,PUWname)]
            
                    bin0 = 4*PUcounter-3
                    h_SF_variations_Et  [(rname,strname)].SetBinContent(bin0+0, SF_Et  .a_value)
                    h_SF_variations_Et  [(rname,strname)].SetBinError  (bin0+0, SF_Et  .a_error)
            
                    h_SF_variations_eta [(rname,strname)].SetBinContent(bin0+1, SF_eta .a_value)
                    h_SF_variations_eta [(rname,strname)].SetBinError  (bin0+1, SF_eta .a_error)
            
                    h_SF_variations_phi [(rname,strname)].SetBinContent(bin0+2, SF_phi .a_value)
                    h_SF_variations_phi [(rname,strname)].SetBinError  (bin0+2, SF_phi .a_error)
            
                    h_SF_variations_nVtx[(rname,strname)].SetBinContent(bin0+3, SF_nVtx.a_value)
                    h_SF_variations_nVtx[(rname,strname)].SetBinError  (bin0+3, SF_nVtx.a_error)
                    
                    PUcounter += 1
    
    
        canvas_variation = ROOT.TCanvas('canvas_variation', '', 100, 100, 1000, 600)
        canvas_variation.SetGridx()
        canvas_variation.SetGridy()
        for strname in ['inc','exc']:
            for rname in card.region_names:
                canvas_variation.Clear()
                hBase_SF_variations_PUW.Draw()
                h_SF_variations_Et  [(rname,strname)].Draw('sames:pe')
                h_SF_variations_eta [(rname,strname)].Draw('sames:pe')
                h_SF_variations_phi [(rname,strname)].Draw('sames:pe')
                h_SF_variations_nVtx[(rname,strname)].Draw('sames:pe')
                legend_variation.Draw()
                hBase_SF_variations_PUW.Draw('sames:axis')
                canvas_variation.Print('%s/variations_%s_%s.eps'%(card.plot_prefix,rname,strname))
                canvas_variation.Print('%s/variations_%s_%s.png'%(card.plot_prefix,rname,strname))
    
    if False:
        for sname in samples:
            s = samples[sname]
            w = card.lumi/s.effectiveLumi
            print '%20s  %8.4f pb^-1  %10f'%(s.name , s.effectiveLumi, w)

