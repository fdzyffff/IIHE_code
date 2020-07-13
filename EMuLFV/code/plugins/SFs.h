
#ifndef SFs_h
#define SFs_h

#include <iostream>
#include <fstream>
#include <math.h>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH1.h>
#include <TH2.h>
#include <TH1F.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TGraphAsymmErrors.h>
class SFs{

    private: 
    TH2F  *sf_Ele_Reco_Map_2016;
    TH2D  *sf_Muon_ID_B2F_Map_2016;
    TH2D  *sf_Muon_ID_GH_Map_2016 ;
    TH2D  *sf_Muon_Iso_B2F_Map_2016;
    TH2D  *sf_Muon_Iso_GH_Map_2016 ;
    float lumi_B2F_2016;
    float lumi_GH_2016;

    TH2F  *sf_Ele_Reco_Map_2017;
    TH2F  *sf_Muon_Trig_2017;
    TH2D  *sf_Muon_ID_Map_2017 ;
    TH2D  *sf_Muon_Iso_Map_2017 ;

    TH2F  *sf_Ele_Reco_Map_2018;
    TH2F  *sf_Muon_Trig_2018;
    TH2D  *sf_Muon_ID_Map_2018 ;
    TH2D  *sf_Muon_Iso_Map_2018 ;
    public:
    SFs();
    ~SFs();
    template<typename T1>
    float scale_factor ( T1 h, float pt, float Eta , TString uncert, bool isAbsEta, bool isXetaYpt);
    float scale_factor_graph( TGraphAsymmErrors* gr, float eta, TString uncert);
    float get_ele_reco_sf  (TString Year, TString uncert, float pt, float eta); 
    float get_ele_ID_sf    (TString Year, TString uncert, float pt, float eta); 
    float get_mu_ID_sf     (TString Year, TString uncert, float pt, float eta); 
    float get_mu_Iso_sf    (TString Year, TString uncert, float pt, float eta); 
    float get_mu_Trigger_sf(bool trig_muon_fired, TString Year, TString uncert, float pt, float eta);
    float get_NNPDF_sf(TString Year, float mass, bool ttbar_reweight);
};

SFs::SFs(){
    std::cout<<"SFs construct"<<std::endl;
    TH1::AddDirectory(kFALSE);
  
    ///////////////////////////// 2016 SF//////////////////////////
    lumi_B2F_2016= 19720.82;
    lumi_GH_2016 = 16146.18;

    TFile *f_Ele_Reco_Map_2016 = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2016/Electron/reco/EGM2D_BtoH_GT20GeV_RecoSF_Legacy2016.root");
    sf_Ele_Reco_Map_2016       = (TH2F*)f_Ele_Reco_Map_2016->Get("EGamma_SF2D");
    f_Ele_Reco_Map_2016->Close();
    
    TFile *f_Muon_ID_B2F_Map_2016  = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2016/Muon/ID/RunBCDEF_SF_ID.root");
    sf_Muon_ID_B2F_Map_2016        = (TH2D*)f_Muon_ID_B2F_Map_2016->Get("NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt");
    f_Muon_ID_B2F_Map_2016->Close() ;

    TFile *f_Muon_Iso_B2F_Map_2016 = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2016/Muon/Iso/RunBCDEF_SF_ISO.root");
    sf_Muon_Iso_B2F_Map_2016       = (TH2D*)f_Muon_Iso_B2F_Map_2016->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt");
    f_Muon_Iso_B2F_Map_2016->Close();

    TFile *f_Muon_ID_GH_Map_2016  = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2016/Muon/ID/RunGH_SF_ID.root");
    sf_Muon_ID_GH_Map_2016        = (TH2D*)f_Muon_ID_GH_Map_2016->Get("NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt");
    f_Muon_ID_GH_Map_2016->Close()  ;

    TFile *f_Muon_Iso_GH_Map_2016 = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2016/Muon/Iso/RunGH_SF_ISO.root");
    sf_Muon_Iso_GH_Map_2016       = (TH2D*)f_Muon_Iso_GH_Map_2016->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt");
    f_Muon_Iso_GH_Map_2016->Close() ;


    //////////////////// 2017 ///////////////////////////

    TFile *f_Ele_Reco_Map_2017  = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2017/Electron/reco/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root");
    sf_Ele_Reco_Map_2017        = (TH2F*)f_Ele_Reco_Map_2017->Get("EGamma_SF2D");
    f_Ele_Reco_Map_2017->Close();

    TFile *f_Muon_Trig_Map_2017 = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2017/Muon/Trigger/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root");
    sf_Muon_Trig_2017           = (TH2F*)f_Muon_Trig_Map_2017->Get("Muon50PtEtaBins/pt_abseta_ratio");
    f_Muon_Trig_Map_2017->Close() ;

    TFile *f_Muon_ID_Map_2017   = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2017/Muon/ID/RunBCDEF_SF_ID_syst.root");
    sf_Muon_ID_Map_2017         = (TH2D*)f_Muon_ID_Map_2017->Get("NUM_HighPtID_DEN_genTracks_pair_newTuneP_probe_pt_abseta");
    f_Muon_ID_Map_2017->Close() ;

    TFile *f_Muon_Iso_Map_2017  = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2017/Muon/Iso/RunBCDEF_SF_ISO_syst.root");
    sf_Muon_Iso_Map_2017        = (TH2D*)f_Muon_Iso_Map_2017->Get("NUM_HighPtID_DEN_genTracks_pair_newTuneP_probe_pt_abseta");
    f_Muon_Iso_Map_2017->Close() ;

    //////////////////// 2018 ///////////////////////////
    TFile *f_Ele_Reco_Map_2018 = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2018/Electron/reco/egammaEffi.txt_EGM2D_updatedAll.root");
    sf_Ele_Reco_Map_2018       = (TH2F*)f_Ele_Reco_Map_2018->Get("EGamma_SF2D");
    f_Ele_Reco_Map_2018->Close();

    TFile *f_Muon_Trig_Map_2018 = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2018/Muon/Trigger/EfficienciesAndSF_2018Data_AfterMuonHLTUpdate.root");
    sf_Muon_Trig_2018           = (TH2F*)f_Muon_Trig_Map_2018->Get("Mu50_OR_OldMu100_OR_TkMu100_PtEtaBins/pt_abseta_ratio");
    f_Muon_Trig_Map_2018->Close() ;

    TFile *f_Muon_ID_Map_2018  = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2018/Muon/ID/RunABCD_SF_ID.root");
    sf_Muon_ID_Map_2018        = (TH2D*)f_Muon_ID_Map_2018->Get("NUM_HighPtID_DEN_TrackerMuons_pair_newTuneP_probe_pt_abseta");
    f_Muon_ID_Map_2018->Close() ;

    TFile *f_Muon_Iso_Map_2018  = new TFile("/user/xgao/CMSSW_9_2_6/src/EMuLFV/SF_json/SF_json_2018/Muon/Iso/RunABCD_SF_ISO.root");
    sf_Muon_Iso_Map_2018        = (TH2D*)f_Muon_Iso_Map_2018->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_pair_newTuneP_probe_pt_abseta");
    f_Muon_Iso_Map_2018->Close() ;

}
SFs::~SFs(){
    std::cout<<"SFs deconstruct"<<std::endl;
    return;
}


template<typename T1>
float SFs::scale_factor( T1 h, float pt, float Eta , TString uncert, bool isAbsEta, bool isXetaYpt){
    float eta=Eta;
    if(isAbsEta)eta=fabs(Eta);
    int NbinsX=h->GetXaxis()->GetNbins();
    int NbinsY=h->GetYaxis()->GetNbins();
    float x_min=h->GetXaxis()->GetBinLowEdge(1);
    float x_max=h->GetXaxis()->GetBinLowEdge(NbinsX)+h->GetXaxis()->GetBinWidth(NbinsX);
    float y_min=h->GetYaxis()->GetBinLowEdge(1);
    float y_max=h->GetYaxis()->GetBinLowEdge(NbinsY)+h->GetYaxis()->GetBinWidth(NbinsY);
    TAxis *Xaxis = h->GetXaxis();
    TAxis *Yaxis = h->GetYaxis();
    Int_t binx=1;
    Int_t biny=1;
    if(isXetaYpt){
        if(x_min < eta && eta < x_max) {binx = Xaxis->FindBin(eta);}
        else {binx= (eta<=x_min) ? 1 : NbinsX ;}
        if(y_min < pt && pt < y_max) {biny = Yaxis->FindBin(pt);}
        else {biny= (pt<=y_min) ? 1 : NbinsY ;}
    }
    else{
        if(x_min < pt && pt < x_max) {binx = Xaxis->FindBin(pt);}
        else {binx= (pt<=x_min) ? 1 : NbinsX ;}
        if(y_min < eta && eta < y_max) {biny = Yaxis->FindBin(eta);}
        else {biny= (eta<=y_min) ? 1 : NbinsY ;}
    }
    if     (uncert=="up")   {return (h->GetBinContent(binx, biny)+h->GetBinError(binx, biny));}
    else if(uncert=="down") {return (h->GetBinContent(binx, biny)-h->GetBinError(binx, biny));}
    else                    {return  h->GetBinContent(binx, biny);}
}

float SFs::scale_factor_graph( TGraphAsymmErrors* gr, float eta, TString uncert){
    float x_min=gr->GetX()[0] - gr->GetErrorXlow(0);
    float x_max=gr->GetX()[gr->GetN()-1] + gr->GetErrorXhigh(gr->GetN()-1);
    int N_bin=0;
    if(eta<x_min) {
        N_bin=0;
    }
    else if(x_min<=eta && eta<=x_max){
        for(int ig=0; ig<gr->GetN(); ig++){
            if( (eta >= gr->GetX()[ig] - gr->GetErrorXlow(ig)) && (eta <= gr->GetX()[ig] + gr->GetErrorXhigh(ig)) ) {N_bin=ig;break;}
        }
    }
    else{
        N_bin=gr->GetN()-1;
    }
    if     (uncert=="up")   {return gr->GetY()[N_bin]+gr->GetErrorYhigh(N_bin);}
    else if(uncert=="down") {return gr->GetY()[N_bin]-gr->GetErrorYlow(N_bin);}
    else                    {return gr->GetY()[N_bin];}
}

///////////////////////////// get sf function/////////////////////////////////////////////////////
float SFs::get_ele_reco_sf(TString Year, TString uncert, float pt, float eta){
    if      (Year=="2016") return scale_factor<TH2F*>( sf_Ele_Reco_Map_2016,  pt,  eta ,  uncert, false, true);
    else if (Year=="2017") return scale_factor<TH2F*>( sf_Ele_Reco_Map_2017,  pt,  eta ,  uncert, false, true);
    else if (Year=="2018") return scale_factor<TH2F*>( sf_Ele_Reco_Map_2018,  pt,  eta ,  uncert, false, true);
    else {std::cout<<"wrong year"<<std::endl; return 1;}
} 

float SFs::get_ele_ID_sf(TString Year, TString uncert, float pt, float eta){
    float value = 1.0;
    if      (Year=="2016") {
        if (fabs(eta) < 1.4442) {value = 0.971;}
        else {value = 0.982;}
    }
    else if (Year=="2017") {
        if (fabs(eta) < 1.4442) {value = 0.963;}
        else {value = 0.967;}
    }
    else if (Year=="2018") {
        if (fabs(eta) < 1.4442) {value = 0.969;}
        else {value = 0.992;}
    }
    else {std::cout<<"wrong year"<<std::endl; return 1;}
    if      (uncert == "up")   {value *= 1.02;}
    else if (uncert == "down") {value *= 0.98;}
    return value;
} 

float SFs::get_mu_Trigger_sf(bool trig_muon_fired, TString Year, TString uncert, float pt, float eta){
    if (!trig_muon_fired) {return 1.0;}
    else if (Year=="2016") {return 1.0;}
    else if (Year=="2017") return scale_factor<TH2F*>( sf_Muon_Trig_2017,  pt,  eta ,  uncert, true , false) ;
    else if(Year=="2018") return scale_factor<TH2F*>( sf_Muon_Trig_2018,  pt,  eta ,  uncert, true , false) ;
    else {std::cout<<"wrong year"<<std::endl; return 1;}
} 

float SFs::get_mu_ID_sf(TString Year, TString uncert, float pt, float eta){
    if      (Year=="2016") { return (lumi_B2F_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>( sf_Muon_ID_B2F_Map_2016,  pt,  eta ,  uncert, false, true) + (lumi_GH_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>( sf_Muon_ID_GH_Map_2016,  pt,  eta ,  uncert, false, true);}
    else if (Year=="2017") return scale_factor<TH2D*>( sf_Muon_ID_Map_2017,  pt,  eta ,  uncert, true , false) ;
    else if(Year=="2018") return scale_factor<TH2D*>( sf_Muon_ID_Map_2018,  pt,  eta ,  uncert, true , false) ;
    else {std::cout<<"wrong year"<<std::endl; return 1;}
} 

float SFs::get_mu_Iso_sf(TString Year, TString uncert, float pt, float eta){
    if      (Year=="2016") return (lumi_B2F_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>( sf_Muon_Iso_B2F_Map_2016,  pt,  eta ,  uncert, false, true) + (lumi_GH_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>(sf_Muon_Iso_GH_Map_2016,  pt,  eta ,  uncert,  false, true);
    else if (Year=="2017") return scale_factor<TH2D*>( sf_Muon_Iso_Map_2017,  pt,  eta ,  uncert, true , false) ;
    else if (Year=="2018") return scale_factor<TH2D*>( sf_Muon_Iso_Map_2018,  pt,  eta ,  uncert, true , false) ;
    else {std::cout<<"wrong year"<<std::endl; return 1;}
}

float SFs::get_NNPDF_sf(TString Year, float mass, bool ttbar_reweight) {
    if      (Year=="2016" || !ttbar_reweight) {return 1.0;}
    else if (Year=="2017" || Year=="2018") {
        if (0.0 < mass && mass < 50.0) {return 1.0;}
        else if (50.0 < mass && mass < 60.0) {return 0.9813981902499459;}
        else if (60.0 < mass && mass < 70.0) {return 0.9611380009719884;}
        else if (70.0 < mass && mass < 80.0) {return 0.958654887941988;}
        else if (80.0 < mass && mass < 90.0) {return 0.9590738695444241;}
        else if (90.0 < mass && mass < 100.0) {return 0.9652106763561925;}
        else if (100.0 < mass && mass < 120.0) {return 0.9700352340530081;}
        else if (120.0 < mass && mass < 140.0) {return 0.9797922180747272;}
        else if (140.0 < mass && mass < 160.0) {return 0.9729072028001798;}
        else if (160.0 < mass && mass < 180.0) {return 0.9792590199734508;}
        else if (180.0 < mass && mass < 200.0) {return 0.9682079938409833;}
        else if (200.0 < mass && mass < 240.0) {return 0.9739080265098249;}
        else if (240.0 < mass && mass < 280.0) {return 0.9729173152048058;}
        else if (280.0 < mass && mass < 320.0) {return 0.9702775331129567;}
        else if (320.0 < mass && mass < 360.0) {return 0.9772284832734035;}
        else if (360.0 < mass && mass < 400.0) {return 0.977370893836097;}
        else if (400.0 < mass && mass < 440.0) {return 0.9694798809384655;}
        else if (440.0 < mass && mass < 480.0) {return 0.9750529374682331;}
        else if (480.0 < mass && mass < 520.0) {return 0.9542435445703805;}
        else if (520.0 < mass && mass < 560.0) {return 0.8977197712106587;}
        else if (560.0 < mass && mass < 600.0) {return 0.8973398844702225;}
        else if (600.0 < mass && mass < 680.0) {return 0.8989140828429507;}
        else if (680.0 < mass && mass < 760.0) {return 0.8843463646929697;}
        else if (760.0 < mass && mass < 840.0) {return 0.8864372437465602;}
        else if (840.0 < mass && mass < 920.0) {return 0.841430547544908;}
        else if (920.0 < mass && mass < 1000.0) {return 0.8423712691558474;}
        else if (1000.0 < mass && mass < 1150.0) {return 0.8318764104972942;}
        else if (1150.0 < mass && mass < 1300.0) {return 0.7666836900323273;}
        else if (1300.0 < mass && mass < 1450.0) {return 0.7910389715317062;}
        else if (1450.0 < mass && mass < 1600.0) {return 0.7714163491726237;}
        else if (1600.0 < mass && mass < 1850.0) {return 0.682164780174015;}
        else if (1850.0 < mass && mass < 2100.0) {return 0.7797289419934624;}
        else if (2100.0 < mass && mass < 2600.0) {return 0.7427499671322355;}
        else {return 1.0;}
    }
    else {std::cout<<"wrong year"<<std::endl; return 1;}
}
#endif
