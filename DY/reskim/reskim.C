#define reskim_cxx
#include "reskim.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TLorentzVector.h>

#include <time.h>
#include <iostream>

#include "turnonEle33.C"
#include "turnonEle33L1seeded.C"
#include "turnon.C"
#include "MC_pileup_weight.C"

const float m_el = 0.000511 ;
const float m_mu = 0.10566 ;

//struct runCounter{
//  unsigned int runNumber ;
//  int nRaw ;
//  int nTriggerMatch ;
//  int nHasTAndP ;
//  runCounter(int number){
//    runNumber = number ;
//    nRaw = 0 ;
//    nTriggerMatch = 0 ;
//    nHasTAndP = 0 ;
//  }
//  void increment(bool triggerMatch, bool hasTAndP){
//    nRaw++ ;
//    if(triggerMatch) nTriggerMatch++ ;
//    if(hasTAndP    ) nHasTAndP++     ;
//  }
//  void print(){
//    std::cout << Form("%6d   %6d  %6d  %6d  %5.2f%%", runNumber, nRaw, nTriggerMatch, nHasTAndP, 100.0*nHasTAndP/nRaw) << std::endl ;
//  }
//};

struct electron_candidate{
  float Et     ;
  float gsf_eta    ;
  float gsf_phi    ;
  float eta    ;
  float phi    ;
  int   Et35   ;
  int   Et20   ;
  int   charge ;
  int   region ;
  
  int truthmatched  ;
  int pass_trigger  ;
  int match_trigger_l1_dou33 ;
  
  int accept_core_ID        ;
  int accept_isolation      ;
  int accept_tag_ID         ;
  int accept_noDEtaIn_ID    ;
  int accept_EcalDriven_ID  ;
  int accept_noIsolation_ID ;
  int accept_nominal_ID     ;
  int isTag                 ;
  
  TLorentzVector p4 ;
  TLorentzVector p4_sc ;
  
  electron_candidate(float Et_in, float gsf_eta_in, float gsf_phi_in, float sc_eta_in, float sc_phi_in, int charge_in){
    Et         = Et_in     ;
    gsf_eta    = gsf_eta_in    ;
    gsf_phi    = gsf_phi_in    ;
    eta        = sc_eta_in    ;
    phi        = sc_phi_in    ;
    charge     = charge_in ;
    
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
    accept_tag_ID         = 0 ;
    accept_noDEtaIn_ID    = 0 ;
    accept_EcalDriven_ID  = 0 ;
    accept_noIsolation_ID = 0 ;
    accept_nominal_ID     = 0 ;
    isTag                 = 0 ;
  }
 
//  void apply_EnergyScale(float value){
//
//}

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
  
    accept_tag_ID          = (accept_core_ID && accept_isolation && accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_noDEtaIn_ID     = (accept_core_ID && accept_isolation && accept_EcalDriven                 ) ? 1 : 0 ;
    accept_noIsolation_ID  = (accept_core_ID &&                     accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_nominal_ID      = (accept_tag_ID                                                           ) ? 1 : 0 ;
    if(region!=3) accept_noDEtaIn_ID = accept_nominal_ID ;
    accept_EcalDriven_ID = accept_EcalDriven ;
    
//    isTag = (Et>35 && region==1 && accept_tag_ID && pass_trigger) ? 1 : 0 ;
    isTag = (Et>35 && accept_tag_ID && pass_trigger) ? 1 : 0 ;
//    isTag = (Et>35 && accept_tag_ID ) ? 1 : 0 ;
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
    accept_tag_ID          = (accept_core_ID && accept_isolation && accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_noDEtaIn_ID     = (accept_core_ID && accept_isolation && accept_EcalDriven                 ) ? 1 : 0 ;
    accept_noIsolation_ID  = (accept_core_ID &&                     accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
    accept_nominal_ID      = (accept_tag_ID                                                           ) ? 1 : 0 ;
    if(region!=3) accept_noDEtaIn_ID = accept_nominal_ID ;
    accept_EcalDriven_ID = accept_EcalDriven ;

    isTag = ((region==1||region==3) && Et>35 && accept_tag_ID && pass_trigger && match_trigger_l1_dou33) ? 1 : 0 ;
    //isTag = ((region==1||region==3) && Et>35 && accept_tag_ID) ? 1 : 0 ;
    
}
};

struct Z_pair{
    int Z_accepted ;
    int region_1 ;
    int region_2 ;
    float Invariant_Mass ;
    float SumEt ;
    electron_candidate* electron_1 ;
    electron_candidate* electron_2 ; 

    Z_pair(electron_candidate* electron_1_in, electron_candidate* electron_2_in)
    {
        electron_1 = electron_1_in ;
        electron_2 = electron_2_in ;
        Z_accepted = 1;
        Invariant_Mass = (electron_1->p4 + electron_2->p4).Mag() ;
        region_1 = electron_1->region ;
        region_2 = electron_2->region ;
        SumEt = electron_1->Et + electron_2->Et ;
//        if ((region_1 ==1 && region_2 == 1) || (region_1 ==1 && region_2 == 1) || (region_1 ==1 && region_2 == 1))
//        {
//            Z_accepted = 1 ;
//        }
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
   
   time_t time_start = time(0) ;
   char* time_start_text = ctime(&time_start) ;
   std::cout << time_start_text << std::endl ;

   Long64_t nentries = fChain->GetEntries();
   std::cout << "In:  " << nentries << std::endl ;
   
   fChain->SetBranchStatus("*",0) ;
   if(isData){
     fChain->SetBranchStatus("trig_HLT_*",1) ;
   }
   else{
     fChain->SetBranchStatus("mc_*",1) ;
   }
   fChain->SetBranchStatus("ev_*"           ,1) ;
   fChain->SetBranchStatus("Zee_*"          ,1) ;
   fChain->SetBranchStatus("pv_n"           ,1) ;
   fChain->SetBranchStatus("gsf_*"          ,1) ;
   
   TFile file_out(fname,"RECREATE") ;
   TTree tree_out("tap","Streamlined tag and probe") ;
   
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
   
   float tag_Et_out ;
   float tag_eta_out ;
   float tag_phi_out ;
   float tag_gsf_eta_out ;
   float tag_gsf_phi_out ;
   int   tag_Et35_out ;
   int   tag_Et20_out ;
   int   tag_charge_out ;
   int   tag_region_out ;
   int   tag_ID_tag_out ;
   int   tag_ID_noDEtaIn_out ;
   int   tag_ID_EcalDriven_out ;
   int   tag_ID_noIsolation_out ;
   int   tag_ID_nominal_out ;
   int   tag_isTag_out ;
   int   tag_truthmatched_out ;
   
   float probe_Et_out ;
   float probe_eta_out ;
   float probe_phi_out ;
   int   probe_Et35_out ;
   int   probe_Et20_out ;
   int   probe_charge_out ;
   int   probe_region_out ;
   int   probe_ID_tag_out ;
   int   probe_ID_noDEtaIn_out ;
   int   probe_ID_EcalDriven_out ;
   int   probe_ID_noIsolation_out ;
   int   probe_ID_nominal_out ;
   int   probe_isTag_out ;
   int   probe_truthmatched_out ;
  
 
   float tag2_eta_out ;
   float tag2_phi_out ;
   float M_ee ;
   float M_ee_sc ;
   int   tag2_typ_out ;
   int   tag2_charge_out ;
   int   tag2_region_out ;
   float tag2_px ;
   float tag2_py ;
   float tag2_pz ;
   float tag2_Et ;
   // These variables keep track of how many Z->ee candidates we have in the event.
   int Zee_index_out ;
   int tag_index_out ;
   int probe_index_out ;

   UInt_t ev_event_out = 0 ;
   UInt_t ev_run_out = 0 ;
   UInt_t ev_luminosityBlock_out = 0 ;

   
   tree_out.Branch("Z_index", &Zee_index_out  , "Z_index/I") ;
   tree_out.Branch("t_index", &tag_index_out  , "t_index/I") ;
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
   
   tree_out.Branch("heep1_Et"    , &tag_Et_out    , "heep1_Et/F"    ) ;
   tree_out.Branch("heep1_eta"   , &tag_eta_out   , "heep1_eta/F"   ) ;
   tree_out.Branch("heep1_phi"   , &tag_phi_out   , "heep1_phi/F"   ) ;
   tree_out.Branch("heep1_Et35"  , &tag_Et35_out  , "heep1_Et35/I"  ) ;
   tree_out.Branch("heep1_Et20"  , &tag_Et20_out  , "heep1_Et20/I"  ) ;
   tree_out.Branch("heep1_charge", &tag_charge_out, "heep1_charge/I") ;
   tree_out.Branch("heep1_region", &tag_region_out, "heep1_region/I") ;
   
   tree_out.Branch("heep1_ID_tag"        , &tag_ID_tag_out        , "heep1_ID_tag/I"        ) ;
   tree_out.Branch("heep1_ID_noDEtaIn"   , &tag_ID_noDEtaIn_out   , "heep1_ID_noDEtaIn/I"   ) ;
   tree_out.Branch("heep1_ID_EcalDriven" , &tag_ID_EcalDriven_out , "heep1_ID_EcalDriven/I" ) ;
   tree_out.Branch("heep1_ID_noIsolation", &tag_ID_noIsolation_out, "heep1_ID_noIsolation/I") ;
   tree_out.Branch("heep1_ID_nominal"    , &tag_ID_nominal_out    , "heep1_ID_nominal/I"    ) ;
   tree_out.Branch("heep1_truthmatched"  , &tag_truthmatched_out  , "heep1_truthmatched/I"  ) ;
   
   tree_out.Branch("p_Et"    , &probe_Et_out    , "p_Et/F"    ) ;
   tree_out.Branch("p_eta"   , &probe_eta_out   , "p_eta/F"   ) ;
   tree_out.Branch("p_phi"   , &probe_phi_out   , "p_phi/F"   ) ;
   tree_out.Branch("p_Et35"  , &probe_Et35_out  , "p_Et35/I"  ) ;
   tree_out.Branch("p_Et20"  , &probe_Et20_out  , "p_Et20/I"  ) ;
   tree_out.Branch("p_charge", &probe_charge_out, "p_charge/I") ;
   tree_out.Branch("p_region", &probe_region_out, "p_region/I") ;
   
   tree_out.Branch("p_ID_tag"        , &probe_ID_tag_out        , "p_ID_tag/I"        ) ;
   tree_out.Branch("p_ID_noDEtaIn"   , &probe_ID_noDEtaIn_out   , "p_ID_noDEtaIn/I"   ) ;
   tree_out.Branch("p_ID_EcalDriven" , &probe_ID_EcalDriven_out , "p_ID_EcalDriven/I" ) ;
   tree_out.Branch("p_ID_noIsolation", &probe_ID_noIsolation_out, "p_ID_noIsolation/I") ;
   tree_out.Branch("p_ID_nominal"    , &probe_ID_nominal_out    , "p_ID_nominal/I"    ) ;
   tree_out.Branch("p_truthmatched"  , &probe_truthmatched_out  , "p_truthmatched/I"  ) ;
   
   tree_out.Branch("heep2_eta"   , &tag2_eta_out   , "heep2_eta/F"   ) ;
   tree_out.Branch("heep2_phi"   , &tag2_phi_out   , "heep2_phi/F"   ) ;
   tree_out.Branch("heep2_charge", &tag2_charge_out, "heep2_charge/I") ;
   tree_out.Branch("heep2_region", &tag2_region_out, "heep2_region/I") ;
   tree_out.Branch("heep2_type"  , &tag2_typ_out   , "heep2_typ/I") ;
   
   tree_out.Branch("heep2_px", &tag2_px, "heep2_px/F") ;
   tree_out.Branch("heep2_py", &tag2_py, "heep2_py/F") ;
   tree_out.Branch("heep2_pz", &tag2_pz, "heep2_pz/F") ;
   tree_out.Branch("heep2_Et", &tag2_Et, "heep2_Et/F") ;
   tree_out.Branch("M_ee"  , &M_ee  , "M_ee/F"  ) ;
   tree_out.Branch("M_ee_sc"  , &M_ee_sc  , "M_ee_sc/F"  ) ;
   // Setup the trigger for changing data structures.
   
   // upto run 254914 ['trig_HLT_Ele27_eta2p1_WPLoose_Gsf_v1_accept']
   // from run 256630 ['trig_HLT_Ele27_eta2p1_WPLoose_Gsf_v2_accept']
   
   Ele33_trig_fire = -1;
   trig_fire_v1 = -1 ;
   trig_fire_v2 = -1 ;
   
//   std::vector<runCounter> runs ;
   
   TRandom3 Tr ;
   Long64_t nbytes = 0, nb = 0;
   int nn=0;
//   if(false==isData){
      TFile* f_L1Map= new TFile("l1EGJet200EffMapAllMC.root");
//   }
   for (Long64_t jentry=0; jentry<nentries;jentry++){
      displayProgress(jentry, nentries) ;
      
//      if (jentry>2000000)break;

      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      
      float w_sign = 1.0 ;
      if(true==isWJets){
      w_sign = mc_w_sign < 0 ? -1 : 1 ;
      }
      if(true==isZToTT){
      w_sign = mc_w_sign < 0 ? -1 : 1 ;
      }
      if(true==isZToEE){
      w_sign = mc_w_sign < 0 ? -1 : 1 ;
      }

      if(true==isZToTT){
        bool accept_event = false ;
        bool has_taup = false ;
        bool has_taum = false ;
        for(unsigned iMC=0 ; iMC<mc_n ; ++iMC){
          if(mc_pdgId->at(iMC)== 15) has_taum = true ;
          if(mc_pdgId->at(iMC)==-15) has_taup = true ;
          if(has_taup && has_taum){
            accept_event = true ;
            break ;
          }
        }
        if(accept_event==false) continue ;
      }

      if(true==isZToEE){
        bool accept_event = false ;
        bool has_ep = false ;
        bool has_em = false ;
        for(unsigned iMC=0 ; iMC<mc_n ; ++iMC){
          if(mc_pdgId->at(iMC)== 11) has_em = true ;
          if(mc_pdgId->at(iMC)==-11) has_ep = true ;
          if(has_ep && has_em){
            accept_event = true ;
            break ;
          }
        }
        if(accept_event==false) continue ;
      }      
 
      if(true==isData){
        if(ev_run<runNo1) continue;
        if(ev_run>runNo2) continue;
      }

      Zee_index_out = 0 ;
      tag_index_out = 0 ;
      
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

        w_PU_combined_out 	= w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,0,"all");
        w_PU_golden_out 	= w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,0,"all");
        w_PU_silver_out  	= w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,0,"all");
        w_PU_silver_down_out   	= w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,1,"all");
        w_PU_silver_up_out     	= w_sign*PU_reReco_Morind17::MC_pileup_weight(PU,2,"all");
      }
//      std::vector<tag2_candidate*> muons ;
//      for(unsigned int iMu=0 ; iMu<mu_gt_n ; ++iMu){
//        float px = mu_gt_px->at(iMu);
//        float py = mu_gt_py->at(iMu);
//        float pz = mu_gt_pz->at(iMu);
//        float pt     = mu_gt_pt->at(iMu) ;
//        if(px < -900 || py < -900 || pz < -900)continue;
////        std::cout<<"px :"<< px << std::endl;
////        std::cout<<"py :"<< py << std::endl;
////        std::cout<<"pz :"<< pz << std::endl;
//        float eta    = mu_gt_eta->at(iMu) ;
//        float phi    = mu_gt_phi->at(iMu) ;
//        int   charge = mu_gt_charge->at(iMu) ;
//        tag2_candidate* mu = new tag2_candidate(pt, eta, phi, charge) ;
//        mu->highPT_MuId(mu_isGlobalMuon->at(iMu),mu_it_dz->at(iMu), mu_it_dxy->at(iMu), mu_it_ptError->at(iMu), mu_numberOfMatchedStations->at(iMu),mu_numberOfValidPixelHits->at(iMu), mu_trackerLayersWithMeasurement->at(iMu),mu_numberOfValidMuonHits->at(iMu)) ;
////        if(mu->passed)cout<<"passed or not"<<mu->passed<<endl; 
//        muons.push_back(mu) ;
//      }
//
//      if(muons.size()==0)continue;
      
      std::vector<electron_candidate*> electrons ;
      for(unsigned int iEl=0 ; iEl<gsf_n ; ++iEl){
        float Et     = gsf_caloEnergy->at(iEl)*sin(gsf_theta->at(iEl)) ;
        //float Et     = gsf_caloEnergy->at(iEl)*sin(2.*atan(exp(-1.*gsf_sc_eta->at(iEl)))) ; 
        int   charge = gsf_charge->at(iEl) ;
        float gsf_eta_in    = gsf_eta->at(iEl) ;
        float gsf_phi_in    = gsf_phi->at(iEl) ;
        float eta    = gsf_sc_eta->at(iEl) ;
        float phi    = gsf_sc_phi->at(iEl) ;

        electron_candidate* el = new electron_candidate(Et, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        //cout<<"before corr : "<<el->Et<<"region :"<<el->region<<endl;
        if(isData && el->region==1)*el=electron_candidate(Et*1.0012, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        if(isData && el->region==3)*el=electron_candidate(Et*1.0089, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        //cout<<"after corr : "<<el->Et<<"region :"<<el->region<<endl;
        if(false == isData && el->region==1)*el=electron_candidate(Et*Tr.Gaus(1,0.0123), gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        if(false == isData && el->region==3)*el=electron_candidate(Et*Tr.Gaus(1,0.0229), gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        //cout<<"*************************"<<endl;
        

        if(isData){
          bool tmp_trigger_pass = 0;

          TLorentzVector trigp4_dou33 ;

             for(unsigned int itrig=0 ; itrig<trig_dou33_unseeded_eta->size() ; ++itrig){
               trigp4_dou33.SetPtEtaPhiM(100,trig_dou33_unseeded_eta->at(itrig),trig_dou33_unseeded_phi->at(itrig),10) ;
               if(trigp4_dou33.DeltaR(el->p4) < 0.1){
                 tmp_trigger_pass = true ;
                 break ;
               }
             }
             el->pass_trigger = (Ele33_trig_fire && tmp_trigger_pass);

//          TLorentzVector trigp4_L1_1 ;
//          bool match_trigger_L1_1 = false ;
//
//          for(unsigned int itrig=0 ; itrig<trig_L1_eta_1->size() ; ++itrig){
//            trigp4_L1_1.SetPtEtaPhiM(100,trig_L1_eta_1->at(itrig),trig_L1_phi_1->at(itrig),10) ;
//            if(trigp4_L1_1.DeltaR(el->p4) < 0.1){
//              match_trigger_L1_1 = true ;
//              break ;
//            }
//          }
//
//          TLorentzVector trigp4_L1_2 ;
//          bool match_trigger_L1_2 = false ;
//
//          for(unsigned int itrig=0 ; itrig<trig_L1_eta_2->size() ; ++itrig){
//            trigp4_L1_2.SetPtEtaPhiM(100,trig_L1_eta_2->at(itrig),trig_L1_phi_2->at(itrig),10) ;
//            if(trigp4_L1_2.DeltaR(el->p4) < 0.1){
//              match_trigger_L1_2 = true ;
//              break ;
//            }
//          }
   
//          el->match_trigger_l1_dou33 = match_trigger_L1_1 || match_trigger_L1_2 ;
          el->match_trigger_l1_dou33 = true ;


        }
        else{
          el->pass_trigger = trigEle33::passTrig(Et, eta) ;
          el->match_trigger_l1_dou33 = true;
        }
        
/*        el->apply_ID_value(HEEP_cutflow60_dPhiIn_value->at(iEl),
                    HEEP_cutflow60_SigmaIetaIeta_value->at(iEl),
                    HEEP_cutflow60_missingHits_value->at(iEl),
                    HEEP_cutflow60_dxyFirstPV_value->at(iEl),
                    HEEP_cutflow60_HOverE_value->at(iEl),
                    gsf_caloEnergy->at(iEl),
                    HEEP_cutflow60_E1x5OverE5x5_value->at(iEl),
                    HEEP_cutflow60_E2x5OverE5x5_value->at(iEl),
                    HEEP_cutflow60_isolEMHadDepth1_value->at(iEl),
                    HEEP_cutflow60_IsolPtTrks_value->at(iEl),
                    HEEP_cutflow60_EcalDriven_value->at(iEl),
                    HEEP_cutflow60_dEtaIn_value->at(iEl),
                    ev_fixedGridRhoFastjetAll) ;
*/
        el->apply_ID_value(gsf_deltaPhiSuperClusterTrackAtVtx->at(iEl),
                           gsf_full5x5_sigmaIetaIeta->at(iEl),
                     float(gsf_nLostInnerHits->at(iEl) ),
                      fabs(gsf_dxy_firstPVtx->at(iEl)),
                           gsf_hadronicOverEm->at(iEl),
                           gsf_superClusterEnergy->at(iEl),
                          (gsf_full5x5_e1x5->at(iEl)/gsf_full5x5_e5x5->at(iEl) ),
                          (gsf_full5x5_e2x5Max->at(iEl)/gsf_full5x5_e5x5->at(iEl) ),
                          (gsf_dr03EcalRecHitSumEt->at(iEl) + gsf_dr03HcalDepth1TowerSumEt->at(iEl) ),
                           gsf_dr03TkSumPt->at(iEl),
                     float(gsf_ecaldrivenSeed->at(iEl) ),
                           gsf_deltaEtaSeedClusterTrackAtVtx->at(iEl),
                           ev_fixedGridRhoFastjetAll) ;


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
        continue;
      }
      float lastEt=0.;
      int flg_e=-1;
      int flg_e2=-1;
      int flg_z=-1;
      UInt_t i;
      UInt_t j;
      UInt_t tmp_n = 0;
      std::vector<Z_pair*> Z_pairs ;
//      cout<<"###start####: "<<ev_event<<endl;
      for(i=0;i<electrons.size();i++)
      {
         electron_candidate* tag = electrons.at(i) ;
         if(false==tag->isTag) continue ;
         for(j=i+1;j<electrons.size();j++)
         {
            electron_candidate* tag2 = electrons.at(j) ;
            if(false==tag2->isTag) continue ;
            Z_pair* z = new Z_pair(tag, tag2);
            Z_pairs.push_back(z);
         }
      }

      for(i=0;i<Z_pairs.size();i++)
      {
         Z_pair* z = Z_pairs.at(i) ;
         if(false==z->Z_accepted) continue ;
         if(z->SumEt > lastEt)
         {
            lastEt = z->SumEt ;
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

      electron_candidate* tag = z->electron_1 ;

      tag_Et_out             = tag->Et ;
      tag_eta_out            = tag->eta ;
      tag_phi_out            = tag->phi ;
      tag_Et35_out           = tag->Et35 ;
      tag_Et20_out           = tag->Et20 ;
      tag_charge_out         = tag->charge ;
      tag_region_out         = tag->region ;
      tag_ID_tag_out         = tag->accept_tag_ID ;
      tag_ID_noDEtaIn_out    = tag->accept_noDEtaIn_ID ;
      tag_ID_EcalDriven_out  = tag->accept_EcalDriven_ID ;
      tag_ID_noIsolation_out = tag->accept_noIsolation_ID ;
      tag_ID_nominal_out     = tag->accept_nominal_ID ;
      tag_isTag_out          = tag->isTag ;
      tag_truthmatched_out   = tag->truthmatched ;
        
      triggerMatch = true ;
          
      
      electron_candidate* tag2 = z->electron_2;

      tag2_eta_out            =tag2->eta ;
      tag2_phi_out            =tag2->phi ;
      tag2_charge_out         =tag2->charge ;
      tag2_region_out         =tag2->region ;
      tag2_typ_out            =-1 ;
      
      tag2_px 	      = tag2->p4.Px();
      tag2_py 	      = tag2->p4.Py();
      tag2_pz 	      = tag2->p4.Pz();
      tag2_Et 	      = tag2->Et;

      if(tag->pass_trigger==1 && tag2->pass_trigger==1)HLT_Ele33_out = 1;
      else HLT_Ele33_out = 0;

      M_ee = (tag2->p4+tag->p4).Mag();
      M_ee_sc = (tag2->p4_sc+tag->p4_sc).Mag();
//      std::cout<<"m_ee : "<< M_ee<< std::endl;
//        std::cout<<"m_ee : "<< z->Invariant_Mass<< std::endl;
      ev_event_out = ev_event   ;
      ev_run_out = ev_run   ;
      ev_luminosityBlock_out = ev_luminosityBlock ; 

//      std::cout<<ev_run_out<<" "<<ev_luminosityBlock_out<<" "<<ev_event_out<<std::endl;

//      if(false == isData){
//        w_PU_combined_out *= ((trigEle33L1seeded::L1reweight(f_L1Map, tag->Et, tag->eta)*trigEle33L1seeded::L1reweight(f_L1Map, tag2->Et, tag2->eta)*3.512/7.12) + (3.608/7.12) ) ;
//      }

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

      tag = NULL;
      tag2 = NULL;
      delete tag;
      delete tag2;
 
}
   f_L1Map->Close() ;
   file_out.cd() ;
   tree_out.Write() ;
   file_out.Close() ;
      std::cout<<"\n"<<nn<<std::endl; 
}
