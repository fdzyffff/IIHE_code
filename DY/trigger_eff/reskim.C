#define reskim_cxx
#include "reskim.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TLorentzVector.h>

#include <time.h>
#include <iostream>

//#include "turnonMu50.C"
//#include "turnonTkMu50.C"
//#include "turnonPhoton175.C"
#include "MC_pileup_weight.C"

const float m_el = 0.000511 ;
const float m_mu = 0.10566 ;

struct electron_candidate{
  float Et     ;
  float eta    ;
  float phi    ;
  float gsf_eta    ;
  float gsf_phi    ;
  int   Et35   ;
  int   Et20   ;
  int   charge ;
  int   region ;
  
  int truthmatched  ;
  int pass_trigger  ;
  int match_trigger_l1_dou33 ;
  
  int accept_core_ID        ;
  int accept_isolation      ;
  int accept_heep_ID         ;
  int accept_noDEtaIn_ID    ;
  int accept_EcalDriven_ID  ;
  int accept_noIsolation_ID ;
  int accept_nominal_ID     ;

  int isHeep ;
  int L1_Et_HE_fire ;
  int L1_fire ;
  int L1_HLT_fire ;
  int L1_Et_fire ;
  
  TLorentzVector p4 ;
  TLorentzVector p4_sc ;
  
  electron_candidate(float Et_in, float gsf_eta_in, float gsf_phi_in, float eta_in, float phi_in, int charge_in){
    Et     = Et_in     ;
    eta    = eta_in    ;
    phi    = phi_in    ;
    gsf_eta    = gsf_eta_in    ;
    gsf_phi    = gsf_phi_in    ;
    charge = charge_in ;
    
    region = 0 ;
    if     (fabs(eta)<1.4442){ region = 1 ; }
    else if(fabs(eta)<1.566 ){ region = 2 ; }
    else if(fabs(eta)<2.5   ){ region = 3 ; }
    else{ region = 4 ; }
    
    p4.SetPtEtaPhiM(Et, gsf_eta, gsf_phi, m_el) ;
    p4_sc.SetPtEtaPhiM(Et, eta, phi, m_el) ;

    Et20 = (Et >= 20.0) ;
    Et35 = (Et >= 35.0) ;
    
    truthmatched = 0 ;
    pass_trigger = 0 ;
    match_trigger_l1_dou33 = 0 ;
    
    accept_core_ID        = 0 ;
    accept_isolation      = 0 ;
    accept_heep_ID        = 0 ;
    accept_noDEtaIn_ID    = 0 ;
    accept_EcalDriven_ID  = 0 ;
    accept_noIsolation_ID = 0 ;
    accept_nominal_ID     = 0 ;
    isHeep = 0 ;
    L1_Et_HE_fire = 0 ;
    L1_fire = 0 ;
    L1_HLT_fire = 0 ;
    L1_Et_fire = 0 ;
  }

  void apply_ID(bool accept_dPhiIn, bool accept_Sieie, bool accept_missingHits, bool accept_dxyFirstPV, float HOverE, float caloEnergy, float E1x5OverE5x5, float E2x5OverE5x5, bool accept_isolEMHadDepth1, bool accept_IsolPtTrks, bool accept_EcalDriven, bool accept_dEtaIn){
    bool accept_HOverE = true ;
    if     (region==1){ accept_HOverE = HOverE < 0.05 + 1.0/caloEnergy ; }
    else if(region==3){ accept_HOverE = HOverE < 0.05 + 5.0/caloEnergy ; }
    
    bool accept_E1x5OverE5x5  = E1x5OverE5x5 > 0.83 ;
    bool accept_E2x5OverE5x5  = E2x5OverE5x5 > 0.94 ;
    bool accept_showershape   = (accept_E1x5OverE5x5 || accept_E2x5OverE5x5) ;
    if(region!=1) accept_showershape = true ;
    
    accept_core_ID = (accept_dPhiIn && accept_Sieie && accept_missingHits && accept_dxyFirstPV && accept_HOverE && accept_showershape) ? 1 : 0 ;
    
    accept_isolation = (accept_isolEMHadDepth1 && accept_IsolPtTrks) ? 1 : 0 ;
  
    accept_heep_ID          = (accept_core_ID && accept_isolation && accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_noDEtaIn_ID     = (accept_core_ID && accept_isolation && accept_EcalDriven                 ) ? 1 : 0 ;
    accept_noIsolation_ID  = (accept_core_ID &&                     accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_nominal_ID      = (accept_heep_ID                                                           ) ? 1 : 0 ;
    if(region!=3) accept_noDEtaIn_ID = accept_nominal_ID ;
    accept_EcalDriven_ID = accept_EcalDriven ;
    
//    isHeep = (Et>35 && region==1 && accept_heep_ID && pass_trigger) ? 1 : 0 ;
    isHeep = (Et>35 && accept_heep_ID && pass_trigger) ? 1 : 0 ;
//    isHeep = (Et>35 && accept_heep_ID ) ? 1 : 0 ;
  }

  void apply_ID_value(float value_dPhiIn, float value_Sieie, float value_missingHits, float value_dxyFirstPV, float value_HOverE, float value_caloEnergy, float value_E1x5OverE5x5, float value_E2x5OverE5x5, float value_isolEMHadDepth1, float value_IsolPtTrks, float value_EcalDriven, float value_dEtaIn, float rho){
    bool accept_HOverE = true ;
    if     (region==1){ accept_HOverE = value_HOverE < 0.05 + 1.0/value_caloEnergy ; }
    else if(region==3){ accept_HOverE = value_HOverE < 0.05 + 5.0/value_caloEnergy ; }
    bool accept_E1x5OverE5x5  = value_E1x5OverE5x5 > 0.83 ;
    bool accept_E2x5OverE5x5  = value_E2x5OverE5x5 > 0.94 ;
    bool accept_showershape   = (accept_E1x5OverE5x5 || accept_E2x5OverE5x5) ;
    if(region!=1) accept_showershape = true ;
    bool accept_Sieie = value_Sieie < 0.03;
    if(region!=3) accept_Sieie = true;
//    bool accept_EcalDriven = value_EcalDriven == 1.0 ? 1 : 0 ;
    bool accept_EcalDriven = value_EcalDriven == 1.0 ? 1 : 0 ;
    bool accept_dEtaIn = (fabs(value_dEtaIn) < 0.004 && region==1) || (fabs(value_dEtaIn) < 0.006 && region==3) ? 1 : 0 ;
    bool accept_dPhiIn = (fabs(value_dPhiIn) < 0.06 && region==1) || (fabs(value_dPhiIn) < 0.06 && region==3) ? 1 : 0 ;
//    bool accept_dPhiIn = true;
    bool accept_isolEMHadDepth1 = true;
    if     (region==1) accept_isolEMHadDepth1 = value_isolEMHadDepth1 < 2+ 0.03*Et + 0.28*rho;
    else if(region==3) accept_isolEMHadDepth1 = ( ((value_isolEMHadDepth1 < 2.5 + 0.28*rho) && Et<50) || ((value_isolEMHadDepth1 < 2.5 + 0.03*(Et-50) + 0.28*rho) && Et>50) ) ? 1 : 0 ;
    bool accept_IsolPtTrks = value_IsolPtTrks < 5 ;
    bool accept_missingHits = value_missingHits < 2 ;
//    bool accept_missingHits = true ;
    bool accept_dxyFirstPV = (fabs(value_dxyFirstPV) < 0.02 && region==1) || (fabs(value_dxyFirstPV) < 0.05 && region==3) ;//check

    accept_core_ID = (accept_dPhiIn && accept_Sieie && accept_missingHits && accept_dxyFirstPV && accept_HOverE && accept_showershape) ? 1 : 0 ;
    accept_isolation = (accept_isolEMHadDepth1 && accept_IsolPtTrks) ? 1 : 0 ;
    accept_heep_ID          = (accept_core_ID && accept_isolation && accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_noDEtaIn_ID     = (accept_core_ID && accept_isolation && accept_EcalDriven                 ) ? 1 : 0 ;
    accept_noIsolation_ID  = (accept_core_ID &&                     accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_nominal_ID      = (accept_heep_ID                                                           ) ? 1 : 0 ;
    if(region!=3) accept_noDEtaIn_ID = accept_nominal_ID ;
    accept_EcalDriven_ID = accept_EcalDriven ;

    isHeep = ((region==1||region==3) && Et>35 && accept_heep_ID && pass_trigger ) ? 1 : 0 ;
    //isHeep = ((region==1||region==3) && Et>35 && accept_heep_ID) ? 1 : 0 ;
    
}
};

struct muon_candidate{
  float Et     ;
  float pt     ;
  float px     ;
  float py     ;
  float pz     ;
  float eta    ;
  float phi    ;
  int   Et35   ;
  int   Et20   ;
  int   charge ;
  int   region ;
  int   typ ;
  
  int truthmatched  ;
  int pass_trigger  ;
  int pass_Mu50 ;
  int pass_TkMu50 ;
  int pass_Photon175 ;

  
  int accept_core_ID        ;
  int accept_isolation      ;
  int accept_heep_ID         ;
  int accept_noDEtaIn_ID    ;
  int accept_EcalDriven_ID  ;
  int accept_noIsolation_ID ;
  int accept_nominal_ID     ;
  int isHeep                 ;


  bool passed  ; 
  bool highPT_MuID  ; 
  bool muon_isBad ;
  bool muon_isHighPtMuon ;
  bool muon_isGlobalMuon ;
 
  TLorentzVector p4 ;
  
  muon_candidate(float pt_in, float eta_in, float phi_in, int charge_in){
    pt     = pt_in     ;
    eta    = eta_in    ;
    phi    = phi_in    ;
    charge = charge_in ;
    p4.SetPtEtaPhiM(pt, eta, phi, m_mu) ;
    px = p4.Px();
    py = p4.Py();
    pz = p4.Pz();
   
    Et=p4.Et();
 
    region = 0 ;
    if     (fabs(eta)<1.2){ region = 1 ; }
    else if(fabs(eta)<2.4 ){ region = 3 ; }
    else{ region = 4 ; }
    

    highPT_MuID = false ;
    passed = false ;
    pass_trigger = false ;
    typ = 0 ;
    pass_Mu50 = false ;
    pass_TkMu50 = false ;
    pass_Photon175 = false ;
    muon_isBad = false ;
    muon_isHighPtMuon = false ;
    muon_isGlobalMuon = false ;
  }
  void highPT_MuId(bool isGlobalMuon, float dz_in, float dxy_in, float ptError_in,int numberOfMatchedStations,int numberOfValidPixelHits,int trackerLayersWithMeasurement,int numberOfValidMuonHits , float isoR03sumpt ){
//    printf("typ : %d ,  dz : %f , dxy : %f , ptratio : %f , Pt : %f\n", typ_in,fabs(dz_in),fabs(dxy_in),ptError_in/pt,pt);
//    typ = typ_in ;//1: track only; 2: global
     pass_trigger = pass_Mu50 || pass_TkMu50;
     if (isGlobalMuon && (numberOfMatchedStations>1) && (numberOfValidPixelHits>0) && (trackerLayersWithMeasurement>5) && (numberOfValidMuonHits>0))
     {
        if ((fabs(dz_in) < 0.5) && (fabs(dxy_in)<0.2) &&(ptError_in/pt < 0.3))
        {
            highPT_MuID = true ;
        }
     }
     if (highPT_MuID && (pt >= 53.0) && (fabs(eta)<2.4) && (isoR03sumpt/pt < 0.1) && pass_trigger)
     {
        passed = true ;
     }
  }
};  

struct Z_pair{
    int Z_accepted ;
    int region_e ;
    int region_m ;
    float Invariant_Mass ;
    electron_candidate* electron ;
    muon_candidate* muon ; 

    Z_pair(electron_candidate* electron_in, muon_candidate* muon_in)
    {
        electron = electron_in ;
        muon = muon_in ;
        Z_accepted = 0;
        Invariant_Mass = (electron->p4 + muon->p4).Mag() ;
        region_e = electron->region ;
        region_m = muon->region ;
//        if ((region_1 ==1 && region_2 == 1) || (region_1 ==1 && region_2 == 1) || (region_1 ==1 && region_2 == 1))
        if (muon->p4.DeltaR(electron->p4)>=0.1)
        {
            Z_accepted = 1 ;
        }
    }
};

void displayProgress(long current, long max){
  using std::cerr;

  if (max <= 1000) return;
  if (current % (max / 1000) != 0) return;

  int width = 40; // Hope the terminal is at least that wide.

  int barWidth = width - 2;
  cerr << "\x1B[2K"; // Clear line
  cerr << "\x1B[2000D"; // Cursor left
  cerr << '[';
  for(int i=0 ; i<barWidth ; ++i){ if(i<barWidth*current/max){ cerr << '=' ; }else{ cerr << ' ' ; } }
  cerr << ']';
  cerr << " " << Form("%8d/%8d (%5.2f%%)", (int)current, (int)max, 100.8*current/max) ;
  cerr.flush();
}

void reskim::Loop(TString fname){
    if (fChain == 0) return;
    std::cout << fname << std::endl ;
    
    bool isWW = false;
    if (strstr(fname,"WW1")!=NULL)
    {
       isWW = true;
       cout<<"will select only M_ll < 200GeV"<<endl;
    }
 
    time_t time_start = time(0) ;
    char* time_start_text = ctime(&time_start) ;
    std::cout << time_start_text << std::endl ;
 
    Long64_t nentries = fChain->GetEntries();
    std::cout << "In:  " << nentries << std::endl ;
    
    TFile file_out(fname,"RECREATE") ;
    TTree tree_out("tap","Streamlined heep and probe") ;
    
    float mee_out ;
    int   OS_out ;
    int   HLT_Ele33_out ;
    
    int   pv_n_out ;
    int   PU_true_out ;
    float w_PU_golden_out ;
    float w_PU_silver_out ;
    float w_PU_silver_up_out ;
    float w_PU_silver_down_out ;
    float w_PU_combined_out ;
    
    float heep_Et_out ;
    float heep_eta_out ;
    float heep_phi_out ;
    int   heep_Et35_out ;
    int   heep_Et20_out ;
    int   heep_charge_out ;
    int   heep_region_out ;
    int   heep_ID_heep_out ;
    int   heep_ID_noDEtaIn_out ;
    int   heep_ID_EcalDriven_out ;
    int   heep_ID_noIsolation_out ;
    int   heep_ID_nominal_out ;
    int   heep_isHeep_out ;
    int   heep_truthmatched_out ;
    int heep_isHeep;
    int heep_L1_Et_HE_fire ;
    int heep_L1_fire ;
    int heep_L1_HLT_fire ;
    int heep_L1_Et_fire ;
   
    float probe_Et_out ;
    float probe_eta_out ;
    float probe_phi_out ;
    int   probe_Et35_out ;
    int   probe_Et20_out ;
    int   probe_charge_out ;
    int   probe_region_out ;
    int   probe_ID_heep_out ;
    int   probe_ID_noDEtaIn_out ;
    int   probe_ID_EcalDriven_out ;
    int   probe_ID_noIsolation_out ;
    int   probe_ID_nominal_out ;
    int   probe_isHeep_out ;
    int   probe_truthmatched_out ;
   
  
    float muon_eta_out ;
    float muon_phi_out ;
    float M_emu ;
    int  muon_typ_out ;
    int  muon_charge_out ;
    int  muon_region_out ;
    int  muon_isBad ;
    int  muon_isHighPtMuon ;
    int  muon_mu_isGlobalMuon ;
 
    float muon_px ;
    float muon_py ;
    float muon_pz ;
    float muon_pt ;
    // These variables keep track of how many Z->ee candidates we have in the event.
    int Zee_index_out ;
    int heep_index_out ;
    int probe_index_out ;
 
    UInt_t ev_event_out = 0 ;
    UInt_t ev_run_out = 0 ;
    UInt_t ev_luminosityBlock_out = 0 ;

   
    tree_out.Branch("Z_index", &Zee_index_out  , "Z_index/I") ;
    tree_out.Branch("t_index", &heep_index_out  , "t_index/I") ;
    tree_out.Branch("p_index", &probe_index_out, "p_index/I") ;
    
    tree_out.Branch("mee"      , &mee_out      , "mee/F"      ) ;
    tree_out.Branch("OS"       , &OS_out       , "OS/I"       ) ;
    tree_out.Branch("HLT_Ele33", &HLT_Ele33_out, "HLT_Ele33/I") ;
 
    tree_out.Branch("ev_event_out"    , &ev_event_out    , "ev_event_out/i"    ) ;
    tree_out.Branch("ev_run_out"      , &ev_run_out      , "ev_run_out/i"    ) ;
    tree_out.Branch("ev_luminosityBlock_out"    , &ev_luminosityBlock_out    , "ev_luminosityBlock_out/i"    ) ;
 
    tree_out.Branch("pv_n"   , &pv_n_out, "pv_n/I") ;
    tree_out.Branch("PU_true", &PU_true_out , "PU_true/I"  ) ;
    
    tree_out.Branch("w_PU_golden"         , &w_PU_golden_out          , "w_PU_golden/F"          ) ;
    tree_out.Branch("w_PU_silver"         , &w_PU_silver_out          , "w_PU_silver/F"          ) ;
    tree_out.Branch("w_PU_silver_down"    , &w_PU_silver_down_out     , "w_PU_silver_down/F"     ) ;
    tree_out.Branch("w_PU_silver_up"      , &w_PU_silver_up_out       , "w_PU_silver_up/F"       ) ;
    tree_out.Branch("w_PU_combined"       , &w_PU_combined_out        , "w_PU_combined/F"        ) ;
    
    tree_out.Branch("heep_Et"    , &heep_Et_out    , "heep_Et/F"    ) ;
    tree_out.Branch("heep_eta"   , &heep_eta_out   , "heep_eta/F"   ) ;
    tree_out.Branch("heep_phi"   , &heep_phi_out   , "heep_phi/F"   ) ;
    tree_out.Branch("heep_Et35"  , &heep_Et35_out  , "heep_Et35/I"  ) ;
    tree_out.Branch("heep_Et20"  , &heep_Et20_out  , "heep_Et20/I"  ) ;
    tree_out.Branch("heep_charge", &heep_charge_out, "heep_charge/I") ;
    tree_out.Branch("heep_region", &heep_region_out, "heep_region/I") ;
    
    tree_out.Branch("heep_ID_heep"       , &heep_ID_heep_out       , "heep_ID_heep/I"        ) ;
    tree_out.Branch("heep_ID_noDEtaIn"   , &heep_ID_noDEtaIn_out   , "heep_ID_noDEtaIn/I"   ) ;
    tree_out.Branch("heep_ID_EcalDriven" , &heep_ID_EcalDriven_out , "heep_ID_EcalDriven/I" ) ;
    tree_out.Branch("heep_ID_noIsolation", &heep_ID_noIsolation_out, "heep_ID_noIsolation/I") ;
    tree_out.Branch("heep_ID_nominal"    , &heep_ID_nominal_out    , "heep_ID_nominal/I"    ) ;
    tree_out.Branch("heep_truthmatched"  , &heep_truthmatched_out  , "heep_truthmatched/I"  ) ;
    tree_out.Branch("heep_isHeep"         , &heep_isHeep            , "heep_isHeep/I");
    tree_out.Branch("heep_L1_Et_HE_fire"  , &heep_L1_Et_HE_fire     , "heep_L1_Et_HE_fire/I");
    tree_out.Branch("heep_L1_fire"        , &heep_L1_fire           , "heep_L1_fire/I");
    tree_out.Branch("heep_L1_HLT_fire"    , &heep_L1_HLT_fire       , "heep_L1_HLT_fire/I");
    tree_out.Branch("heep_L1_Et_fire"     , &heep_L1_Et_fire        , "heep_L1_Et_fire/I");
   
    tree_out.Branch("muon_eta"   , &muon_eta_out   , "muon_eta/F"   ) ;
    tree_out.Branch("muon_phi"   , &muon_phi_out   , "muon_phi/F"   ) ;
    tree_out.Branch("muon_charge", &muon_charge_out, "muon_charge/I") ;
    tree_out.Branch("muon_region", &muon_region_out, "muon_region/I") ;
    tree_out.Branch("muon_type"  , &muon_typ_out   , "muon_typ/I") ;
    
    tree_out.Branch("muon_px", &muon_px, "muon_px/F") ;
    tree_out.Branch("muon_py", &muon_py, "muon_py/F") ;
    tree_out.Branch("muon_pz", &muon_pz, "muon_pz/F") ;
    tree_out.Branch("muon_pt", &muon_pt, "muon_pt/F") ;
    tree_out.Branch("M_emu"  , &M_emu  , "M_emu/F"  ) ;
 
    tree_out.Branch("muon_isHighPtMuon", &muon_isHighPtMuon, "muon_isHighPtMuon/I");
    tree_out.Branch("muon_mu_isGlobalMuon", &muon_mu_isGlobalMuon, "muon_mu_isGlobalMuon/I");

    tree_out.Branch("Muon50_trig_fire", &Muon50_trig_fire, "Muon50_trig_fire/I");
    tree_out.Branch("TkMu50_trig_fire", &TkMu50_trig_fire, "TkMu50_trig_fire/I");
    tree_out.Branch("Photon175_trig_fire",  &Photon175_trig_fire, "Photon175_trig_fire/I");
 
    tree_out.Branch("trig_Flag_duplicateMuons_accept", &trig_Flag_duplicateMuons_accept, "trig_Flag_duplicateMuons_accept/I");
    tree_out.Branch("trig_Flag_badMuons_accept", &trig_Flag_badMuons_accept, "trig_Flag_badMuons_accept/I");
    tree_out.Branch("trig_Flag_noBadMuons_accept", &trig_Flag_noBadMuons_accept, "trig_Flag_noBadMuons_accept/I");
    tree_out.Branch("trig_Flag_HBHENoiseFilter_accept", &trig_Flag_HBHENoiseFilter_accept, "trig_Flag_HBHENoiseFilter_accept/I");
    tree_out.Branch("trig_Flag_HBHENoiseIsoFilter_accept", &trig_Flag_HBHENoiseIsoFilter_accept, "trig_Flag_HBHENoiseIsoFilter_accept/I");
    tree_out.Branch("trig_Flag_CSCTightHaloFilter_accept", &trig_Flag_CSCTightHaloFilter_accept, "trig_Flag_CSCTightHaloFilter_accept/I");
    tree_out.Branch("trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept", &trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept, "trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept/I");
    tree_out.Branch("trig_Flag_CSCTightHalo2015Filter_accept", &trig_Flag_CSCTightHalo2015Filter_accept, "trig_Flag_CSCTightHalo2015Filter_accept/I");
    tree_out.Branch("trig_Flag_globalTightHalo2016Filter_accept", &trig_Flag_globalTightHalo2016Filter_accept, "trig_Flag_globalTightHalo2016Filter_accept/I");
    tree_out.Branch("trig_Flag_globalSuperTightHalo2016Filter_accept", &trig_Flag_globalSuperTightHalo2016Filter_accept, "trig_Flag_globalSuperTightHalo2016Filter_accept/I");
    tree_out.Branch("trig_Flag_HcalStripHaloFilter_accept", &trig_Flag_HcalStripHaloFilter_accept, "trig_Flag_HcalStripHaloFilter_accept/I");
    tree_out.Branch("trig_Flag_hcalLaserEventFilter_accept", &trig_Flag_hcalLaserEventFilter_accept, "trig_Flag_hcalLaserEventFilter_accept/I");
    tree_out.Branch("trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept", &trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept, "trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept/I");
    tree_out.Branch("trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept", &trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept, "trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept/I");
    tree_out.Branch("trig_Flag_goodVertices_accept", &trig_Flag_goodVertices_accept, "trig_Flag_goodVertices_accept/I");
    tree_out.Branch("trig_Flag_eeBadScFilter_accept", &trig_Flag_eeBadScFilter_accept, "trig_Flag_eeBadScFilter_accept/I");
    tree_out.Branch("trig_Flag_ecalLaserCorrFilter_accept", &trig_Flag_ecalLaserCorrFilter_accept, "trig_Flag_ecalLaserCorrFilter_accept/I");
    tree_out.Branch("trig_Flag_trkPOGFilters_accept", &trig_Flag_trkPOGFilters_accept, "trig_Flag_trkPOGFilters_accept/I");
    tree_out.Branch("trig_Flag_chargedHadronTrackResolutionFilter_accept", &trig_Flag_chargedHadronTrackResolutionFilter_accept, "trig_Flag_chargedHadronTrackResolutionFilter_accept/I");
    tree_out.Branch("trig_Flag_muonBadTrackFilter_accept", &trig_Flag_muonBadTrackFilter_accept, "trig_Flag_muonBadTrackFilter_accept/I");
    tree_out.Branch("trig_Flag_trkPOG_manystripclus53X_accept", &trig_Flag_trkPOG_manystripclus53X_accept, "trig_Flag_trkPOG_manystripclus53X_accept/I");
    tree_out.Branch("trig_Flag_trkPOG_toomanystripclus53X_accept", &trig_Flag_trkPOG_toomanystripclus53X_accept, "trig_Flag_trkPOG_toomanystripclus53X_accept/I");
    tree_out.Branch("trig_Flag_trkPOG_logErrorTooManyClusters_accept", &trig_Flag_trkPOG_logErrorTooManyClusters_accept, "trig_Flag_trkPOG_logErrorTooManyClusters_accept/I");
    tree_out.Branch("trig_Flag_METFilters_accept", &trig_Flag_METFilters_accept, "trig_Flag_METFilters_accept/I");
   // Setup the trigger for changing data structures.
   
   TRandom3 Tr ;
   Long64_t nbytes = 0, nb = 0;
   int nn=0;
   for (Long64_t jentry=0; jentry<nentries;jentry++){
      displayProgress(jentry, nentries) ;

      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      
      float w_sign = 1.0 ;
      if(!isData)w_sign = mc_w_sign < 0 ? -1 : 1 ;
      if (isData && ev_run < 276271)break;

      Zee_index_out = 0 ;
      heep_index_out = 0 ;
      
      pv_n_out = pv_n ;
      bool triggerMatch = false ;
      bool hasTAndP     = false ;
      if(true==isData){
        //passTrigger = (ev_run<=254914) ? trig_fire_v1 : trig_fire_v2 ;
        
        PU_true_out = -1 ;
        
        // Set weights to 1
        w_PU_golden_out         = 1 ;
        w_PU_silver_out         = 1 ;
        w_PU_silver_down_out    = 1 ;
        w_PU_silver_up_out      = 1 ;
        w_PU_combined_out = 1.0 ;
      }
      else{
        // Set PU weights
        int PU = mc_trueNumInteractions ;
        PU_true_out = PU ;

        w_PU_combined_out       = w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,0,"all");
        w_PU_golden_out         = w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,0,"all");
        w_PU_silver_out         = w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,0,"all");
        w_PU_silver_down_out    = w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,1,"all");
        w_PU_silver_up_out      = w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,2,"all");
      }
      std::vector<muon_candidate*> muons ;
      //cout<<"###########################"<<endl;
      //cout<<" n mu : "<<mu_n<<endl;
      for(unsigned int iMu=0 ; iMu<mu_ibt_pt->size() ; ++iMu){
        //if(!mu_isGlobalMuon->at(iMu))continue;
        float px = mu_ibt_px->at(iMu);
        float py = mu_ibt_py->at(iMu);
        float pz = mu_ibt_pz->at(iMu);
        float pt = mu_ibt_pt->at(iMu) ;
//        std::cout<<"px :"<< px << std::endl;
//        std::cout<<"py :"<< py << std::endl;
//        std::cout<<"pz :"<< pz << std::endl;
//        if(px < -900 || py < -900 || pz < -900)continue;
        float eta    = mu_ibt_eta->at(iMu) ;
        float phi    = mu_ibt_phi->at(iMu) ;
        int   charge = mu_ibt_charge->at(iMu) ;
        if(charge < -900)continue;
        muon_candidate* mu = new muon_candidate(pt, eta, phi, charge) ;
//        mu->muon_isBad = mu_isBad->at(iMu) ;
        mu->muon_isHighPtMuon = mu_isHighPtMuon->at(iMu) ;
        mu->muon_isGlobalMuon = mu_isGlobalMuon->at(iMu) ;
        if(isData){
          mu->pass_Mu50 = Muon50_trig_fire;
          mu->pass_TkMu50 = TkMu50_trig_fire;
          mu->pass_Photon175 = Photon175_trig_fire;
        }
        else{
          mu->pass_Mu50 = Muon50_trig_fire;
          mu->pass_TkMu50 = TkMu50_trig_fire;
          mu->pass_Photon175 = Photon175_trig_fire;
        }
        mu->highPT_MuId(mu_isGlobalMuon->at(iMu),mu_ibt_dz_firstPVtx->at(iMu), mu_ibt_dxy_firstPVtx->at(iMu), mu_ibt_ptError->at(iMu), mu_numberOfMatchedStations->at(iMu),mu_numberOfValidPixelHits->at(iMu), mu_trackerLayersWithMeasurement->at(iMu),mu_numberOfValidMuonHits->at(iMu),mu_isolationR03_sumPt->at(iMu)) ;
//        if(mu->passed)cout<<"passed or not"<<mu->passed<<endl; 
        muons.push_back(mu) ;
      }

      if(muons.size()==0)
      {
        for (std::vector<muon_candidate*>::iterator it = muons.begin(); it != muons.end(); it ++){
          if (NULL != *it)
          { 
            delete *it;
            *it = NULL;
            }
        }
        muons.clear() ;
        muons.swap(muons);
        continue;
      }
      
      std::vector<electron_candidate*> electrons ;
      for(unsigned int iEl=0 ; iEl<gsf_n ; ++iEl){
        float Et     = gsf_caloEnergy->at(iEl)*sin(gsf_theta->at(iEl)) ;
        float gsf_eta_in    = gsf_eta->at(iEl) ;
        float gsf_phi_in    = gsf_phi->at(iEl) ;
        float eta    = gsf_sc_eta->at(iEl) ;
        float phi    = gsf_sc_phi->at(iEl) ;
        int   charge = gsf_charge->at(iEl) ;

        electron_candidate* el = new electron_candidate(Et, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        //cout<<"before corr : "<<el->Et<<"region :"<<el->region<<endl;
        if(isData && el->region==1)*el=electron_candidate(Et*1.0012, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        if(isData && el->region==3)*el=electron_candidate(Et*1.0089, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        //cout<<"after corr : "<<el->Et<<"region :"<<el->region<<endl;
        if(false == isData && el->region==1)*el=electron_candidate(Et*Tr.Gaus(1,0.0123), gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        if(false == isData && el->region==3)*el=electron_candidate(Et*Tr.Gaus(1,0.0229), gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        
        if(isData){
          el->pass_trigger = true;
          el->isHeep = int(gsf_isHeepV7->at(iEl));
          TLorentzVector trigp4_L1_Et_HE_fire ;
          TLorentzVector trigp4_L1_fire ;
          TLorentzVector trigp4_L1_HLT_fire ;
          TLorentzVector trigp4_L1_Et_fire ;
          if (276453 <= ev_run && ev_run <= 278822)
          { 
            for(unsigned int itrig=0 ; itrig<trig_dou33HE_eta->size() ; ++itrig){
              trigp4_L1_Et_HE_fire.SetPtEtaPhiM(100,trig_dou33HE_eta->at(itrig),trig_dou33HE_phi->at(itrig),10) ;
              if(trigp4_L1_Et_HE_fire.DeltaR(el->p4) < 0.1){
                el->L1_Et_HE_fire = true ;
                break ;
              }
            }
            for(unsigned int itrig=0 ; itrig<trig_dou33_L1s_eta->size() ; ++itrig){
              trigp4_L1_fire.SetPtEtaPhiM(100,trig_dou33_L1s_eta->at(itrig),trig_dou33_L1s_phi->at(itrig),10) ;
              if(trigp4_L1_fire.DeltaR(el->p4) < 0.3){
                el->L1_fire = true ;
                break ;
              }
            }
            for(unsigned int itrig=0 ; itrig<trig_dou33_EGL1_eta->size() ; ++itrig){
              trigp4_L1_HLT_fire.SetPtEtaPhiM(100,trig_dou33_EGL1_eta->at(itrig),trig_dou33_EGL1_phi->at(itrig),10) ;
              if(trigp4_L1_HLT_fire.DeltaR(el->p4) < 0.1){
                el->L1_HLT_fire = true ;
                break ;
              }
            }
            for(unsigned int itrig=0 ; itrig<trig_dou33Et_eta->size() ; ++itrig){
              trigp4_L1_Et_fire.SetPtEtaPhiM(100,trig_dou33Et_eta->at(itrig),trig_dou33Et_phi->at(itrig),10) ;
              if(trigp4_L1_Et_fire.DeltaR(el->p4) < 0.1){
                el->L1_Et_fire = true ;
                break ;
              }
            }
          }
          else
          { 
            for(unsigned int itrig=0 ; itrig<trig_dou33MWHE_eta->size() ; ++itrig){
              trigp4_L1_Et_HE_fire.SetPtEtaPhiM(100,trig_dou33MWHE_eta->at(itrig),trig_dou33MWHE_phi->at(itrig),10) ;
              if(trigp4_L1_Et_HE_fire.DeltaR(el->p4) < 0.1){
                el->L1_Et_HE_fire = true ;
                break ;
              }
            }
            for(unsigned int itrig=0 ; itrig<trig_dou33MW_L1s_eta->size() ; ++itrig){
              trigp4_L1_fire.SetPtEtaPhiM(100,trig_dou33MW_L1s_eta->at(itrig),trig_dou33MW_L1s_phi->at(itrig),10) ;
              if(trigp4_L1_fire.DeltaR(el->p4) < 0.3){
                el->L1_fire = true ;
                break ;
              }
            }
            for(unsigned int itrig=0 ; itrig<trig_dou33MW_EGL1_eta->size() ; ++itrig){
              trigp4_L1_HLT_fire.SetPtEtaPhiM(100,trig_dou33MW_EGL1_eta->at(itrig),trig_dou33MW_EGL1_phi->at(itrig),10) ;
              if(trigp4_L1_HLT_fire.DeltaR(el->p4) < 0.1){
                el->L1_HLT_fire = true ;
                break ;
              }
            }
            for(unsigned int itrig=0 ; itrig<trig_dou33MWEt_eta->size() ; ++itrig){
              trigp4_L1_Et_fire.SetPtEtaPhiM(100,trig_dou33MWEt_eta->at(itrig),trig_dou33MWEt_phi->at(itrig),10) ;
              if(trigp4_L1_Et_fire.DeltaR(el->p4) < 0.1){
                el->L1_Et_fire = true ;
                break ;
              }
            }
          }
        }
        else{
          el->pass_trigger = true;
        }
        
        electrons.push_back(el) ;
      }
     
      if(electrons.size()==0)
      {
        for (std::vector<electron_candidate*>::iterator it = electrons.begin(); it != electrons.end(); it ++){
          if (NULL != *it)
          {
            delete *it;
            *it = NULL;
            }
        }
        electrons.clear() ;
        electrons.swap(electrons);
      
        for (std::vector<muon_candidate*>::iterator it = muons.begin(); it != muons.end(); it ++){
          if (NULL != *it)
          { 
            delete *it;
            *it = NULL;
            }
        }
        muons.clear() ;
        muons.swap(muons);
        continue;
      }
      float lastIM=0.;
      int flg_z=-1;
      UInt_t i;
      UInt_t j;
      UInt_t tmp_n = 0;
      std::vector<Z_pair*> Z_pairs ;
//      cout<<"###start####: "<<ev_event<<endl;
      for(i=0;i<electrons.size();i++)
      {
         electron_candidate* heep = electrons.at(i) ;
         if(false==heep->isHeep) continue ;
         for(j=0;j<muons.size();j++)
         {
            muon_candidate* muon = muons.at(j) ;
            if(muon->pt <=5) continue ;
            if(muon->p4.DeltaR(heep->p4_sc) <= 0.1)
            {
              heep->isHeep = false;
            }
         }
      }
      for(i=0;i<electrons.size();i++)
      {
         electron_candidate* heep = electrons.at(i) ;
         if(false==heep->isHeep) continue ;
         for(j=0;j<muons.size();j++)
         {
            muon_candidate* muon = muons.at(j) ;
            if(false==muon->passed) continue ;
            Z_pair* z = new Z_pair(heep, muon);
            Z_pairs.push_back(z);
         }
      }

      for(i=0;i<Z_pairs.size();i++)
      {
         Z_pair* z = Z_pairs.at(i) ;
         if(false==z->Z_accepted) continue ;
         if(z->Invariant_Mass > lastIM)
         {
            lastIM = z->Invariant_Mass ;
            flg_z = i ;
         }
      }
         
//      cout<<"flg z"<<flg_z<<endl;
      if(flg_z < 0)
      {
        for (std::vector<electron_candidate*>::iterator it = electrons.begin(); it != electrons.end(); it ++){
          if (NULL != *it)
          {
            delete *it;
            *it = NULL;
            }
        }
        electrons.clear() ;
        electrons.swap(electrons);

        for (std::vector<muon_candidate*>::iterator it = muons.begin(); it != muons.end(); it ++){
          if (NULL != *it)
          { 
            delete *it;
            *it = NULL;
            }
        }
        muons.clear() ;
        muons.swap(muons);

        for (std::vector<Z_pair*>::iterator it = Z_pairs.begin(); it != Z_pairs.end(); it ++){
          if (NULL != *it)
          {
            delete *it;
            *it = NULL;
            }
        }
        Z_pairs.clear() ;
        Z_pairs.swap(Z_pairs);

        continue;
      }
      Z_pair* z = Z_pairs.at(flg_z) ;

      electron_candidate* heep = z->electron ;

      heep_Et_out             = heep->Et ;
      heep_eta_out            = heep->eta ;
      heep_phi_out            = heep->phi ;
      heep_Et35_out           = heep->Et35 ;
      heep_Et20_out           = heep->Et20 ;
      heep_charge_out         = heep->charge ;
      heep_region_out         = heep->region ;
      heep_ID_heep_out        = heep->accept_heep_ID ;
      heep_ID_noDEtaIn_out    = heep->accept_noDEtaIn_ID ;
      heep_ID_EcalDriven_out  = heep->accept_EcalDriven_ID ;
      heep_ID_noIsolation_out = heep->accept_noIsolation_ID ;
      heep_ID_nominal_out     = heep->accept_nominal_ID ;
      heep_isHeep_out         = heep->isHeep ;
      heep_truthmatched_out   = heep->truthmatched ;
      heep_isHeep              = heep->isHeep ;
      heep_L1_Et_HE_fire       = heep->L1_Et_HE_fire ;
      heep_L1_fire             = heep->L1_fire ;
      heep_L1_HLT_fire         = heep->L1_HLT_fire ;
      heep_L1_Et_fire          = heep->L1_Et_fire ;
        
      triggerMatch = true ;
          
      
      muon_candidate* muon = z->muon;

      muon_eta_out            =muon->eta ;
      muon_phi_out            =muon->phi ;
      muon_charge_out         =muon->charge ;
      muon_region_out         =muon->region ;
      muon_typ_out            =-1 ;
      
      muon_px 	      = muon->p4.Px();
      muon_py 	      = muon->p4.Py();
      muon_pz 	      = muon->p4.Pz();
      muon_pt 	      = muon->pt;
      //muon_isBad = int(muon->muon_isBad) ;
      muon_isHighPtMuon = int(muon->muon_isHighPtMuon) ;
      muon_mu_isGlobalMuon = int(muon->muon_isGlobalMuon) ;

      M_emu = (muon->p4+heep->p4).Mag();
      ev_event_out = ev_event   ;
      ev_run_out = ev_run   ;
      ev_luminosityBlock_out = ev_luminosityBlock ; 


      nn++;
      tree_out.Fill() ;
      
      for (std::vector<electron_candidate*>::iterator it = electrons.begin(); it != electrons.end(); it ++){
        if (NULL != *it)
        {
          delete *it;
          *it = NULL;
          }
      }
      electrons.clear() ;
      electrons.swap(electrons);

      for (std::vector<Z_pair*>::iterator it = Z_pairs.begin(); it != Z_pairs.end(); it ++){
        if (NULL != *it)
        {
          delete *it;
          *it = NULL;
          }
      }
      Z_pairs.clear() ;
      Z_pairs.swap(Z_pairs);

      heep = NULL;
      muon = NULL;
      delete heep;
      delete muon;
 
}
   file_out.cd() ;
   tree_out.Write() ;
   file_out.Close() ;
   std::cout<<"\n"<<nn<<std::endl; 
}
