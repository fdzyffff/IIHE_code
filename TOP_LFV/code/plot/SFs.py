from dependencies import *

class SFs():

    def __init__(self):
        self.sf_trig_emu_Map_2016 = ROOT.TH2D()
        self.sf_Ele_Reco_Map_2016 = ROOT.TH2F()
        self.sf_Ele_ID_Map_2016 = ROOT.TH2F()
        self.sf_Muon_track_gr_2016 = ROOT.TGraphAsymmErrors()
        self.sf_Muon_ID_B2F_Map_2016 = ROOT.TH2D()
        self.sf_Muon_ID_GH_Map_2016 = ROOT.TH2D()
        self.sf_Muon_Iso_B2F_Map_2016 = ROOT.TH2D()
        self.sf_Muon_Iso_GH_Map_2016 = ROOT.TH2D()
        self.sf_Ele_Reco_Map_2017 = ROOT.TH2F()
        self.sf_Ele_ID_Map_2017 = ROOT.TH2F()
        self.sf_Muon_ID_Map_2017 = ROOT.TH2D()
        self.sf_Muon_Iso_Map_2017 = ROOT.TH2D()
        self.sf_Ele_Reco_Map_2018 = ROOT.TH2F()
        self.sf_Ele_ID_Map_2018 = ROOT.TH2F()
        self.sf_Muon_ID_Map_2018 = ROOT.TH2D()
        self.sf_Muon_Iso_Map_2018 = ROOT.TH2D()
        self.lumi_B2F_2016= 19720.82
        self.lumi_GH_2016 = 16146.18

        ############################### 2016 SF ############################

        f_trig_emu_Map_2016 = ROOT.TFile("Scale_Factor/2016/TriggerSF_emu2016_pt.root")
        self.sf_trig_emu_Map_2016 = f_trig_emu_Map_2016.Get("h_lep1Pt_lep2Pt_Step3")
        f_trig_emu_Map_2016.Close()

        f_Ele_Reco_Map_2016 = ROOT.TFile("Scale_Factor/2016/EGM2D_BtoH_GT20GeV_RecoSF_Legacy2016.root")
        self.sf_Ele_Reco_Map_2016 = f_Ele_Reco_Map_2016.Get("EGamma_SF2D")
        f_Ele_Reco_Map_2016.Close()

        f_Ele_ID_Map_2016 = ROOT.TFile("Scale_Factor/2016/2016LegacyReReco_ElectronTight_Fall17V2.root")
        self.sf_Ele_ID_Map_2016 = f_Ele_ID_Map_2016.Get("EGamma_SF2D")
        f_Ele_ID_Map_2016.Close()

        ## for 2016 UL data, the tracking efficiency seems around 100%, therefore it is not used///////////////    
        ##TFile *f_Muon_track_2016   = new TFile("Scale_Factor/2016/Tracking_EfficienciesAndSF_BCDEFGH.root")
        ##sf_Muon_track_gr_2016      = (TGraphAsymmErrors*)f_Muon_track_2016.Get("ratio_eff_eta3_dr030e030_corr")
        ##f_Muon_track_2016->Close()
    
        f_Muon_ID_B2F_Map_2016 = ROOT.TFile("Scale_Factor/2016/RunBCDEF_SF_ID.root")
        self.sf_Muon_ID_B2F_Map_2016 = f_Muon_ID_B2F_Map_2016.Get("NUM_TightID_DEN_genTracks_eta_pt")
        f_Muon_ID_B2F_Map_2016.Close()

        f_Muon_Iso_B2F_Map_2016 = ROOT.TFile("Scale_Factor/2016/RunBCDEF_SF_ISO.root")
        self.sf_Muon_Iso_B2F_Map_2016 = f_Muon_Iso_B2F_Map_2016.Get("NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt")
        f_Muon_Iso_B2F_Map_2016.Close()

        f_Muon_ID_GH_Map_2016 = ROOT.TFile("Scale_Factor/2016/RunGH_SF_ID.root")
        self.sf_Muon_ID_GH_Map_2016 = f_Muon_ID_GH_Map_2016.Get("NUM_TightID_DEN_genTracks_eta_pt")
        f_Muon_ID_GH_Map_2016.Close() 

        f_Muon_Iso_GH_Map_2016 = ROOT.TFile("Scale_Factor/2016/RunGH_SF_ISO.root")
        self.sf_Muon_Iso_GH_Map_2016 = f_Muon_Iso_GH_Map_2016.Get("NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt")
        f_Muon_Iso_GH_Map_2016.Close()


        ############################### 2017 SF ############################
        f_trig_emu_Map_2017 = ROOT.TFile("Scale_Factor/2017/TriggerSF_emu2017_pt.root")
        self.sf_trig_emu_Map_2017 = f_trig_emu_Map_2017.Get("h_lep1Pt_lep2Pt_Step3")
        f_trig_emu_Map_2017.Close()

        f_Ele_Reco_Map_2017 = ROOT.TFile("Scale_Factor/2017/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root")
        self.sf_Ele_Reco_Map_2017 = f_Ele_Reco_Map_2017.Get("EGamma_SF2D")
        f_Ele_Reco_Map_2017.Close()
    
        f_Ele_ID_Map_2017 = ROOT.TFile("Scale_Factor/2017/2017_ElectronTight.root")
        self.sf_Ele_ID_Map_2017 = f_Ele_ID_Map_2017.Get("EGamma_SF2D")
        f_Ele_ID_Map_2017.Close()

        f_Muon_ID_Map_2017 = ROOT.TFile("Scale_Factor/2017/RunBCDEF_SF_ID_syst.root")
        self.sf_Muon_ID_Map_2017 = f_Muon_ID_Map_2017.Get("NUM_TightID_DEN_genTracks_pt_abseta")
        f_Muon_ID_Map_2017.Close() 
    
        f_Muon_Iso_Map_2017 = ROOT.TFile("Scale_Factor/2017/RunBCDEF_SF_ISO_syst.root")
        self.sf_Muon_Iso_Map_2017 = f_Muon_Iso_Map_2017.Get("NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta")
        f_Muon_Iso_Map_2017.Close() 

        ############################### 2018 SF ############################
        f_trig_emu_Map_2018 = ROOT.TFile("Scale_Factor/2018/TriggerSF_emu2018_pt.root")
        self.sf_trig_emu_Map_2018 = f_trig_emu_Map_2018.Get("h_lep1Pt_lep2Pt_Step3")
        f_trig_emu_Map_2018.Close()

        f_Ele_Reco_Map_2018 = ROOT.TFile("Scale_Factor/2018/egammaEffi.txt_EGM2D_updatedAll.root")
        self.sf_Ele_Reco_Map_2018 = f_Ele_Reco_Map_2018.Get("EGamma_SF2D")
        f_Ele_Reco_Map_2018.Close()
    
        f_Ele_ID_Map_2018 = ROOT.TFile("Scale_Factor/2018/2018_ElectronTight.root")
        self.sf_Ele_ID_Map_2018 = f_Ele_ID_Map_2018.Get("EGamma_SF2D")
        f_Ele_ID_Map_2018.Close()

        f_Muon_ID_Map_2018 = ROOT.TFile("Scale_Factor/2018/RunABCD_SF_ID.root")
        self.sf_Muon_ID_Map_2018 = f_Muon_ID_Map_2018.Get("NUM_TightID_DEN_TrackerMuons_pt_abseta")
        f_Muon_ID_Map_2018.Close() 
    
        f_Muon_Iso_Map_2018 = ROOT.TFile("Scale_Factor/2018/RunABCD_SF_ISO.root")
        self.sf_Muon_Iso_Map_2018 = f_Muon_Iso_Map_2018.Get("NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta")
        f_Muon_Iso_Map_2018.Close() 

        print "SFs construct"

    def trig_scale_factor(self, h, lead_pt1, sub_lead_pt2 , uncert):
        NbinsX=h.GetXaxis().GetNbins()
        NbinsY=h.GetYaxis().GetNbins()
        x_min=h.GetXaxis().GetBinLowEdge(1)
        x_max=h.GetXaxis().GetBinLowEdge(NbinsX)+h.GetXaxis().GetBinWidth(NbinsX)
        y_min=h.GetYaxis().GetBinLowEdge(1)
        y_max=h.GetYaxis().GetBinLowEdge(NbinsY)+h.GetYaxis().GetBinWidth(NbinsY)
        Xaxis = h.GetXaxis()
        Yaxis = h.GetYaxis()
        binx=1
        biny=1
        if (x_min < lead_pt1 and lead_pt1 < x_max):
            binx = Xaxis.FindBin(lead_pt1)
        elif (lead_pt1 <= x_min):
            binx = 1
        else:
            binx = NbinsX 
        if(y_min < sub_lead_pt2 and sub_lead_pt2 < y_max):
            biny = Yaxis.FindBin(sub_lead_pt2)
        elif (sub_lead_pt2<=y_min):
            biny = 1
        else:
            biny = NbinsY
        if( uncert =="TrigSF_up" ):
            return (h.GetBinContent(binx, biny)+h.GetBinError(binx, biny))
        elif( uncert=="TrigSF_down" ):
            return (h.GetBinContent(binx, biny)-h.GetBinError(binx, biny))
        else :
            return  h.GetBinContent(binx, biny)

    def scale_factor(self, h, pt, Eta , uncert, sf_name, isAbsEta, isXetaYpt):
        eta=Eta
        if(isAbsEta):eta=fabs(Eta)
        NbinsX=h.GetXaxis().GetNbins()
        NbinsY=h.GetYaxis().GetNbins()
        x_min=h.GetXaxis().GetBinLowEdge(1)
        x_max=h.GetXaxis().GetBinLowEdge(NbinsX)+h.GetXaxis().GetBinWidth(NbinsX)
        y_min=h.GetYaxis().GetBinLowEdge(1)
        y_max=h.GetYaxis().GetBinLowEdge(NbinsY)+h.GetYaxis().GetBinWidth(NbinsY)
        Xaxis = h.GetXaxis()
        Yaxis = h.GetYaxis()
        binx=1
        biny=1
        if(isXetaYpt):
            if(x_min < eta and eta < x_max):
                binx = Xaxis.FindBin(eta)
            elif (eta<=x_min):
                binx = 1
            else:
                bin = NbinsX 
            if(y_min < pt and pt < y_max):
                biny = Yaxis.FindBin(pt)
            elif (pt<=y_min):
                biny = 1
            else: 
                biny = NbinsY 
        else:
            if(x_min < pt and pt < x_max):
                binx = Xaxis.FindBin(pt)
            elif (pt<=x_min):
                binx = 1
            else: 
                binx = NbinsX 
            if(y_min < eta and eta < y_max):
                biny = Yaxis.FindBin(eta)
            elif (eta<=y_min):
                biny = 1
            else: 
                biny = NbinsY 

##std::cout<<h.GetName()<<",value="<<h.GetBinContent(binx, biny)<<std::endl
        if(sf_name=="EleSFReco" or sf_name=="EleSFID" or sf_name=="MuonSFID" or sf_name=="MuonSFIso"):
            if(uncert=="EleSFReco_up" or uncert=="EleSFID_up" or uncert=="MuonSFID_up" or uncert=="MuonSFIso_up"  ):
                return (h.GetBinContent(binx, biny)+h.GetBinError(binx, biny))
            elif(uncert=="EleSFReco_down" or uncert=="EleSFID_down" or uncert=="MuonSFID_down" or uncert=="MuonSFIso_down"):
                return (h.GetBinContent(binx, biny)-h.GetBinError(binx, biny))
            else:
                return  h.GetBinContent(binx, biny)
        else:
            return h.GetBinContent(binx, biny)


    def scale_factor_graph(self,  gr, eta, uncert, sf_name):
        x_min=gr.GetX()[0] - gr.GetErrorXlow(0)
        x_max=gr.GetX()[gr.GetN()-1] + gr.GetErrorXhigh(gr.GetN()-1)
        N_bin=0
        #std::cout<<"x_min:"<<x_min<<",x_max="<<x_max<<std::endl
        if(eta<x_min):
            N_bin=0
        elif(x_min<=eta and eta<=x_max):
            for ig in range (ig<gr.GetN()):
                if( (eta >= gr.GetX()[ig] - gr.GetErrorXlow(ig)) and (eta <= gr.GetX()[ig] + gr.GetErrorXhigh(ig)) ) :
                    N_bin=ig
                    break
        else:
            N_bin=gr.GetN()-1

        if(sf_name=="MuonSFtrack"):
            if(uncert=="MuonSFtrack_up"):
                return gr.GetY()[N_bin]+gr.GetErrorYhigh(N_bin)
            if(uncert=="MuonSFtrack_down"):
                return gr.GetY()[N_bin]-gr.GetErrorYlow(N_bin)
            else:
                return gr.GetY()[N_bin]
        else:
            return gr.GetY()[N_bin]

    #################################### get sf function ####################################
    def get_trigger_sf(self, Year, uncert, lead_pt1, sub_lead_pt2):
        if  (Year=="2016"): return self.trig_scale_factor( self.sf_trig_emu_Map_2016, lead_pt1, sub_lead_pt2 , uncert)
        elif(Year=="2017"): return self.trig_scale_factor( self.sf_trig_emu_Map_2017, lead_pt1, sub_lead_pt2 , uncert)
        elif(Year=="2018"): return self.trig_scale_factor( self.sf_trig_emu_Map_2018, lead_pt1, sub_lead_pt2 , uncert)
        else: 
            print "wrong year"
            return 1

    def get_ele_reco_sf(self, Year, uncert, pt, eta):
        if  (Year=="2016"): return self.scale_factor( self.sf_Ele_Reco_Map_2016,  pt,  eta ,  uncert, "EleSFReco", False, True)
        elif(Year=="2017"): return self.scale_factor( self.sf_Ele_Reco_Map_2017,  pt,  eta ,  uncert, "EleSFReco", False, True)
        elif(Year=="2018"): return self.scale_factor( self.sf_Ele_Reco_Map_2018,  pt,  eta ,  uncert, "EleSFReco", False, True)
        else: 
            print "wrong year"
            return 1

    def get_ele_ID_sf(self, Year, uncert, pt, eta):
        if  (Year=="2016"): return self.scale_factor( self.sf_Ele_ID_Map_2016,  pt,  eta ,  uncert, "EleSFID", False, True)
        elif(Year=="2017"): return self.scale_factor( self.sf_Ele_ID_Map_2017,  pt,  eta ,  uncert, "EleSFID", False, True)
        elif(Year=="2018"): return self.scale_factor( self.sf_Ele_ID_Map_2018,  pt,  eta ,  uncert, "EleSFID", False, True)
        else: 
            print "wrong year"
            return 1

    def get_mu_ID_sf(self, Year, uncert, pt, eta):
        if  (Year=="2016"): return (self.lumi_B2F_2016/(self.lumi_B2F_2016+self.lumi_GH_2016))*self.scale_factor( self.sf_Muon_ID_B2F_Map_2016,  pt,  eta ,  uncert, "MuonSFID", False, True) + (self.lumi_GH_2016/(self.lumi_B2F_2016+self.lumi_GH_2016))*self.scale_factor( self.sf_Muon_ID_GH_Map_2016,  pt,  eta ,  uncert, "MuonSFID", False, True)
        elif(Year=="2017"): return self.scale_factor( self.sf_Muon_ID_Map_2017,  pt,  eta ,  uncert, "MuonSFID", True , False) 
        elif(Year=="2018"): return self.scale_factor( self.sf_Muon_ID_Map_2018,  pt,  eta ,  uncert, "MuonSFID", True , False) 
        else: 
            print "wrong year"
            return 1

    def get_mu_Iso_sf(self, Year, uncert, pt, eta):
        if  (Year=="2016"): return (self.lumi_B2F_2016/(self.lumi_B2F_2016+self.lumi_GH_2016))*self.scale_factor( self.sf_Muon_Iso_B2F_Map_2016,  pt,  eta ,  uncert, "MuonSFIso", False, True) + (self.lumi_GH_2016/(self.lumi_B2F_2016+self.lumi_GH_2016))*self.scale_factor( self.sf_Muon_Iso_GH_Map_2016,  pt,  eta ,  uncert, "MuonSFIso", False, True)
        elif(Year=="2017"): return self.scale_factor( self.sf_Muon_Iso_Map_2017,  pt,  eta ,  uncert, "MuonSFIso", True , False) 
        elif(Year=="2018"): return self.scale_factor( self.sf_Muon_Iso_Map_2018,  pt,  eta ,  uncert, "MuonSFIso", True , False) 
        else: 
            print "wrong year"
            return 1