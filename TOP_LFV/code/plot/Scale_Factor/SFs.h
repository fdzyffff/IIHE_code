
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
    TH2D  *sf_trig_emu_Map_2016;    
    TH2F  *sf_Ele_Reco_Map_2016;
    TH2F  *sf_Ele_ID_Map_2016  ;
    TGraphAsymmErrors  *sf_Muon_track_gr_2016;
    TH2D  *sf_Muon_ID_B2F_Map_2016;
    TH2D  *sf_Muon_ID_GH_Map_2016 ;
    TH2D  *sf_Muon_Iso_B2F_Map_2016;
    TH2D  *sf_Muon_Iso_GH_Map_2016 ;
    float lumi_B2F_2016;
    float lumi_GH_2016;
    TH2F  *sf_Ele_Reco_Map_2017;
    TH2F  *sf_Ele_ID_Map_2017  ;
    TH2D  *sf_Muon_ID_Map_2017 ;
    TH2D  *sf_Muon_Iso_Map_2017 ;
    TH2F  *sf_Ele_Reco_Map_2018;
    TH2F  *sf_Ele_ID_Map_2018  ;
    TH2D  *sf_Muon_ID_Map_2018 ;
    TH2D  *sf_Muon_Iso_Map_2018 ;
    public:
    SFs();
    ~SFs();
    float trig_scale_factor ( TH2D* h, float lead_pt1, float sub_lead_pt2 , TString uncert);
    template<typename T1>
    float scale_factor ( T1 h, float pt, float Eta , TString uncert, TString sf_name, bool isAbsEta, bool isXetaYpt);
    float scale_factor_graph( TGraphAsymmErrors* gr, float eta, TString uncert, TString sf_name);
    float get_trigger_sf(TString Year, TString uncert, float lead_pt1, float sub_lead_pt2); 
    float get_trigger_sf_Pt(TString Year, TString uncert, float lep1_Pt, float lep2_Pt);
    float get_ele_reco_sf(TString Year, TString uncert, float pt, float eta); 
    float get_ele_ID_sf  (TString Year, TString uncert, float pt, float eta); 
//    float get_mu_reco_sf (TString Year, TString uncert, float pt, float eta); 
    float get_mu_ID_sf   (TString Year, TString uncert, float pt, float eta); 
    float get_mu_Iso_sf  (TString Year, TString uncert, float pt, float eta); 
};
SFs::SFs(){
    //std::cout<<"SFs construct"<<std::endl;
    TH1::AddDirectory(kFALSE);
  
    ///////////////////////////// 2016 SF//////////////////////////
    lumi_B2F_2016= 19720.82;
    lumi_GH_2016 = 16146.18;

    TFile *f_trig_emu_Map_2016 = new TFile("Scale_Factor/2016/TriggerSF_ee2016_pt.root");
    sf_trig_emu_Map_2016       = (TH2D*)f_trig_emu_Map_2016->Get("h_lep1Pt_lep2Pt_Step3");
    f_trig_emu_Map_2016->Close();

    TFile *f_Ele_Reco_Map_2016 = new TFile("Scale_Factor/2016/EGM2D_BtoH_GT20GeV_RecoSF_Legacy2016.root");
    sf_Ele_Reco_Map_2016       = (TH2F*)f_Ele_Reco_Map_2016->Get("EGamma_SF2D");
    f_Ele_Reco_Map_2016->Close();
    TFile *f_Ele_ID_Map_2016   = new TFile("Scale_Factor/2016/2016LegacyReReco_ElectronTight_Fall17V2.root");
    sf_Ele_ID_Map_2016         = (TH2F*)f_Ele_ID_Map_2016->Get("EGamma_SF2D");
    f_Ele_ID_Map_2016->Close();
    // for 2016 UL data, the tracking efficiency seems around 100%, therefore it is not used///////////////    
    //TFile *f_Muon_track_2016   = new TFile("Scale_Factor/2016/Tracking_EfficienciesAndSF_BCDEFGH.root");
    //sf_Muon_track_gr_2016      = (TGraphAsymmErrors*)f_Muon_track_2016->Get("ratio_eff_eta3_dr030e030_corr");
    //f_Muon_track_2016->Close();
    
    TFile *f_Muon_ID_B2F_Map_2016  = new TFile("Scale_Factor/2016/RunBCDEF_SF_ID.root");
    sf_Muon_ID_B2F_Map_2016        = (TH2D*)f_Muon_ID_B2F_Map_2016->Get("NUM_TightID_DEN_genTracks_eta_pt");
    f_Muon_ID_B2F_Map_2016->Close() ;
    TFile *f_Muon_Iso_B2F_Map_2016 = new TFile("Scale_Factor/2016/RunBCDEF_SF_ISO.root");
    sf_Muon_Iso_B2F_Map_2016       = (TH2D*)f_Muon_Iso_B2F_Map_2016->Get("NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt");
    f_Muon_Iso_B2F_Map_2016->Close();

    TFile *f_Muon_ID_GH_Map_2016  = new TFile("Scale_Factor/2016/RunGH_SF_ID.root");
    sf_Muon_ID_GH_Map_2016        = (TH2D*)f_Muon_ID_GH_Map_2016->Get("NUM_TightID_DEN_genTracks_eta_pt");
    f_Muon_ID_GH_Map_2016->Close()  ;
    TFile *f_Muon_Iso_GH_Map_2016 = new TFile("Scale_Factor/2016/RunGH_SF_ISO.root");
    sf_Muon_Iso_GH_Map_2016       = (TH2D*)f_Muon_Iso_GH_Map_2016->Get("NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt");
    f_Muon_Iso_GH_Map_2016->Close() ;


    //////////////////// 2017 ///////////////////////////

    TFile *f_Ele_Reco_Map_2017 = new TFile("Scale_Factor/2017/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root");
    sf_Ele_Reco_Map_2017       = (TH2F*)f_Ele_Reco_Map_2017->Get("EGamma_SF2D");
    f_Ele_Reco_Map_2017->Close();
    TFile *f_Ele_ID_Map_2017   = new TFile("Scale_Factor/2017/2017_ElectronTight.root");
    sf_Ele_ID_Map_2017         = (TH2F*)f_Ele_ID_Map_2017->Get("EGamma_SF2D");
    f_Ele_ID_Map_2017->Close();

    TFile *f_Muon_ID_Map_2017  = new TFile("Scale_Factor/2017/RunBCDEF_SF_ID_syst.root");
    sf_Muon_ID_Map_2017        = (TH2D*)f_Muon_ID_Map_2017->Get("NUM_TightID_DEN_genTracks_pt_abseta");
    f_Muon_ID_Map_2017->Close() ;
    TFile *f_Muon_Iso_Map_2017  = new TFile("Scale_Factor/2017/RunBCDEF_SF_ISO_syst.root");
    sf_Muon_Iso_Map_2017        = (TH2D*)f_Muon_Iso_Map_2017->Get("NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta");
    f_Muon_Iso_Map_2017->Close() ;

    //////////////////// 2018 ///////////////////////////
    TFile *f_Ele_Reco_Map_2018 = new TFile("Scale_Factor/2018/egammaEffi.txt_EGM2D_updatedAll.root");
    sf_Ele_Reco_Map_2018       = (TH2F*)f_Ele_Reco_Map_2018->Get("EGamma_SF2D");
    f_Ele_Reco_Map_2018->Close();
    TFile *f_Ele_ID_Map_2018   = new TFile("Scale_Factor/2018/2018_ElectronTight.root");
    sf_Ele_ID_Map_2018         = (TH2F*)f_Ele_ID_Map_2018->Get("EGamma_SF2D");
    f_Ele_ID_Map_2018->Close();

    TFile *f_Muon_ID_Map_2018  = new TFile("Scale_Factor/2018/RunABCD_SF_ID.root");
    sf_Muon_ID_Map_2018        = (TH2D*)f_Muon_ID_Map_2018->Get("NUM_TightID_DEN_TrackerMuons_pt_abseta");
    f_Muon_ID_Map_2018->Close() ;
    TFile *f_Muon_Iso_Map_2018  = new TFile("Scale_Factor/2018/RunABCD_SF_ISO.root");
    sf_Muon_Iso_Map_2018        = (TH2D*)f_Muon_Iso_Map_2018->Get("NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta");
    f_Muon_Iso_Map_2018->Close() ;

}
SFs::~SFs(){
    //std::cout<<"SFs deconstruct"<<std::endl;
    return;
}
/////////////////////////////// difine basic functions///////////////////////////////////////////
float SFs::trig_scale_factor( TH2D* h, float lead_pt1, float sub_lead_pt2 , TString uncert){
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
if(x_min < fabs(lead_pt1) && fabs(lead_pt1) < x_max) binx = Xaxis->FindBin(fabs(lead_pt1));
else binx= (fabs(lead_pt1)<=x_min) ? 1 : NbinsX ;
if(y_min < fabs(sub_lead_pt2) && fabs(sub_lead_pt2) < y_max) biny = Yaxis->FindBin(fabs(sub_lead_pt2));
else biny= (fabs(sub_lead_pt2)<=y_min) ? 1 : NbinsY ;
     if(uncert=="TrigSF_up"   )return (h->GetBinContent(binx, biny)+h->GetBinError(binx, biny));
else if(uncert=="TrigSF_down" )return (h->GetBinContent(binx, biny)-h->GetBinError(binx, biny));
else                           return  h->GetBinContent(binx, biny);
}


template<typename T1>
float SFs::scale_factor( T1 h, float pt, float Eta , TString uncert, TString sf_name, bool isAbsEta, bool isXetaYpt){
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
if(x_min < eta && eta < x_max) binx = Xaxis->FindBin(eta);
else binx= (eta<=x_min) ? 1 : NbinsX ;
if(y_min < pt && pt < y_max) biny = Yaxis->FindBin(pt);
else biny= (pt<=y_min) ? 1 : NbinsY ;
}
else{
if(x_min < pt && pt < x_max) binx = Xaxis->FindBin(pt);
else binx= (pt<=x_min) ? 1 : NbinsX ;
if(y_min < eta && eta < y_max) biny = Yaxis->FindBin(eta);
else biny= (eta<=y_min) ? 1 : NbinsY ;
}
//std::cout<<h->GetName()<<",value="<<h->GetBinContent(binx, biny)<<std::endl;
     if(sf_name=="EleSFReco"     || sf_name=="EleSFID"     || sf_name=="MuonSFID"     || sf_name=="MuonSFIso"){
     if(uncert=="EleSFReco_up"   || uncert=="EleSFID_up"   || uncert=="MuonSFID_up"   || uncert=="MuonSFIso_up"  )return (h->GetBinContent(binx, biny)+h->GetBinError(binx, biny));
else if(uncert=="EleSFReco_down" || uncert=="EleSFID_down" || uncert=="MuonSFID_down" || uncert=="MuonSFIso_down")return (h->GetBinContent(binx, biny)-h->GetBinError(binx, biny));
else                              return  h->GetBinContent(binx, biny);
}
else                               return h->GetBinContent(binx, biny);
}

float SFs::scale_factor_graph( TGraphAsymmErrors* gr, float eta, TString uncert, TString sf_name){
float x_min=gr->GetX()[0] - gr->GetErrorXlow(0);
float x_max=gr->GetX()[gr->GetN()-1] + gr->GetErrorXhigh(gr->GetN()-1);
int N_bin=0;
//std::cout<<"x_min:"<<x_min<<",x_max="<<x_max<<std::endl;
if(eta<x_min){N_bin=0;
             }
else if(x_min<=eta && eta<=x_max){
                                  for(int ig=0; ig<gr->GetN(); ig++){
                                  if( (eta >= gr->GetX()[ig] - gr->GetErrorXlow(ig)) && (eta <= gr->GetX()[ig] + gr->GetErrorXhigh(ig)) ) {N_bin=ig;break;}
                                 }
                                 }
else{N_bin=gr->GetN()-1;}
if(sf_name=="MuonSFtrack"){
if(uncert=="MuonSFtrack_up")  return gr->GetY()[N_bin]+gr->GetErrorYhigh(N_bin);
if(uncert=="MuonSFtrack_down")return gr->GetY()[N_bin]-gr->GetErrorYlow(N_bin);
else                          return gr->GetY()[N_bin];
}
else                          return gr->GetY()[N_bin];
}
///////////////////////////// get sf function/////////////////////////////////////////////////////
float SFs::get_trigger_sf(TString Year, TString uncert, float lead_pt1, float sub_lead_pt2){
if     (Year=="2016") return trig_scale_factor(sf_trig_emu_Map_2016, lead_pt1, sub_lead_pt2 , uncert);
else if(Year=="2017") return trig_scale_factor(sf_trig_emu_Map_2016, lead_pt1, sub_lead_pt2 , uncert);
else if(Year=="2018") return trig_scale_factor(sf_trig_emu_Map_2016, lead_pt1, sub_lead_pt2 , uncert);
else {std::cout<<"wrong year"<<std::endl; return 1;}
}

float SFs::get_trigger_sf_Pt(TString Year, TString uncert, float lep1_Pt, float lep2_Pt){
    float trigger_SF_emu = 1.0;
    if ( lep1_Pt>=0 && lep1_Pt<20){
        if (lep2_Pt>25 && lep2_Pt<=30) trigger_SF_emu=0.971871;
        if (lep2_Pt>30 && lep2_Pt<=40) trigger_SF_emu=1.00295;
        if (lep2_Pt>40 && lep2_Pt<=60) trigger_SF_emu=0.973715;
        if (lep2_Pt>60)                trigger_SF_emu=0.914005;
    }

    if ( lep1_Pt>=20 && lep1_Pt<25){
        //  if (lep2_Pt>0 && lep2_Pt<20)  trigger_SF_emu=
        //  if (lep2_Pt>20 && lep2_Pt<25) trigger_SF_emu=
        if (lep2_Pt>25 && lep2_Pt<=30) trigger_SF_emu=1.00794;
        if (lep2_Pt>30 && lep2_Pt<=40) trigger_SF_emu=0.974026;
        if (lep2_Pt>40 && lep2_Pt<=60) trigger_SF_emu=0.983675;
        if (lep2_Pt>60)                trigger_SF_emu=1.03818;
    }

    if ( lep1_Pt>=25 && lep1_Pt<30){
       if (lep2_Pt>0 && lep2_Pt<=20)  trigger_SF_emu=1.00276;
       if (lep2_Pt>20 && lep2_Pt<=25) trigger_SF_emu=0.982957;
       if (lep2_Pt>25 && lep2_Pt<=30) trigger_SF_emu=1.01241;
       if (lep2_Pt>30 && lep2_Pt<=40) trigger_SF_emu=0.981017;
       if (lep2_Pt>40 && lep2_Pt<=60) trigger_SF_emu=0.974593;
       if (lep2_Pt>60)                trigger_SF_emu=0.935986;
    }

    if ( lep1_Pt>=30 && lep1_Pt<40){
       if (lep2_Pt>0 && lep2_Pt<=20)  trigger_SF_emu=1.02315;
       if (lep2_Pt>20 && lep2_Pt<=25) trigger_SF_emu=0.976516;
       if (lep2_Pt>25 && lep2_Pt<=30) trigger_SF_emu=0.999819;
       if (lep2_Pt>30 && lep2_Pt<=40) trigger_SF_emu=0.997942;
       if (lep2_Pt>40 && lep2_Pt<=60) trigger_SF_emu=0.994555;
       if (lep2_Pt>60)                trigger_SF_emu=1.00164;
    }

    if ( lep1_Pt>=40 && lep1_Pt<60){
       if (lep2_Pt>0 && lep2_Pt<=20)  trigger_SF_emu=0.997919;
       if (lep2_Pt>20 && lep2_Pt<=25) trigger_SF_emu=1.00571;
       if (lep2_Pt>25 && lep2_Pt<=30) trigger_SF_emu=0.996047;
       if (lep2_Pt>30 && lep2_Pt<=40) trigger_SF_emu=0.998180;
       if (lep2_Pt>40 && lep2_Pt<=60) trigger_SF_emu=0.998158;
       if (lep2_Pt>60)                trigger_SF_emu=0.994763;
   }

    if ( lep1_Pt>=60){
       if (lep2_Pt>0 && lep2_Pt<=20)  trigger_SF_emu=0.992255;
       if (lep2_Pt>20 && lep2_Pt<=25) trigger_SF_emu=0.990000;
       if (lep2_Pt>25 && lep2_Pt<=30) trigger_SF_emu=0.999253;
       if (lep2_Pt>30 && lep2_Pt<=40) trigger_SF_emu=1.00148;
       if (lep2_Pt>40 && lep2_Pt<=60) trigger_SF_emu=0.999067;
       if (lep2_Pt>60)                trigger_SF_emu=0.998904;
   }
   return trigger_SF_emu;
}


float SFs::get_ele_reco_sf(TString Year, TString uncert, float pt, float eta){
     if(Year=="2016") return scale_factor<TH2F*>( sf_Ele_Reco_Map_2016,  pt,  eta ,  uncert, "EleSFReco", false, true);
else if(Year=="2017") return scale_factor<TH2F*>( sf_Ele_Reco_Map_2017,  pt,  eta ,  uncert, "EleSFReco", false, true);
else if(Year=="2018") return scale_factor<TH2F*>( sf_Ele_Reco_Map_2018,  pt,  eta ,  uncert, "EleSFReco", false, true);
else {std::cout<<"wrong year"<<std::endl; return 1;}
} 
float SFs::get_ele_ID_sf(TString Year, TString uncert, float pt, float eta){
     if(Year=="2016") return scale_factor<TH2F*>( sf_Ele_ID_Map_2016,  pt,  eta ,  uncert, "EleSFID", false, true);
else if(Year=="2017") return scale_factor<TH2F*>( sf_Ele_ID_Map_2017,  pt,  eta ,  uncert, "EleSFID", false, true);
else if(Year=="2018") return scale_factor<TH2F*>( sf_Ele_ID_Map_2018,  pt,  eta ,  uncert, "EleSFID", false, true);
else {std::cout<<"wrong year"<<std::endl; return 1;}
} 
/*
float SFs::get_mu_reco_sf(TString Year, TString uncert, float pt, float eta){
     if(Year=="2016") return scale_factor_graph( sf_Muon_track_gr_2016,  eta ,  uncert, "MuonSFtrack");
else if(Year=="2017") return scale_factor_graph( sf_Muon_track_gr_2016,  eta ,  uncert, "MuonSFtrack");
else if(Year=="2018") return scale_factor_graph( sf_Muon_track_gr_2016,  eta ,  uncert, "MuonSFtrack");
else {std::cout<<"wrong year"<<std::endl; return 1;}
} 
*/
float SFs::get_mu_ID_sf(TString Year, TString uncert, float pt, float eta){
     if(Year=="2016") {
return (lumi_B2F_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>( sf_Muon_ID_B2F_Map_2016,  pt,  eta ,  uncert, "MuonSFID", false, true) + (lumi_GH_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>( sf_Muon_ID_GH_Map_2016,  pt,  eta ,  uncert, "MuonSFID", false, true);}

else if(Year=="2017") return scale_factor<TH2D*>( sf_Muon_ID_Map_2017,  pt,  eta ,  uncert, "MuonSFID", true , false) ;
else if(Year=="2018") return scale_factor<TH2D*>( sf_Muon_ID_Map_2018,  pt,  eta ,  uncert, "MuonSFID", true , false) ;
else {std::cout<<"wrong year"<<std::endl; return 1;}
} 

float SFs::get_mu_Iso_sf(TString Year, TString uncert, float pt, float eta){
     if(Year=="2016") return (lumi_B2F_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>( sf_Muon_Iso_B2F_Map_2016,  pt,  eta ,  uncert, "MuonSFIso", false, true) + (lumi_GH_2016/(lumi_B2F_2016+lumi_GH_2016))*scale_factor<TH2D*>(sf_Muon_Iso_GH_Map_2016,  pt,  eta ,  uncert, "MuonSFIso", false, true);
else if(Year=="2017") return scale_factor<TH2D*>( sf_Muon_Iso_Map_2017,  pt,  eta ,  uncert, "MuonSFIso", true , false) ;
else if(Year=="2018") return scale_factor<TH2D*>( sf_Muon_Iso_Map_2018,  pt,  eta ,  uncert, "MuonSFIso", true , false) ;
else {std::cout<<"wrong year"<<std::endl; return 1;}
}

/*
void SFs::combine_stat_syst(TH2D* & map1, TH2F* & map2){
    
    int NbinsX=map2->GetXaxis()->GetNbins();
    int NbinsY=map2->GetYaxis()->GetNbins();
    float new_error = 0 ;
    for(i=1; i<=NinsX; i++){
        for(j=1; j<=NinsY; j++){
            new_error = math.sqrt(math.pow(map1->GetBinError(i,j),2)+ math.pow(map2->GetBinError(i,j),2));
            map2->SetBinError(i, j, new_error);
            }
    }
}
*/
#endif
