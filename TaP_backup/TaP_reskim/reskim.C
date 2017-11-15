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
#include "turnon.C"

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
  float L1Et   ;
  
  int truthmatched  ;
  int pass_trigger  ;
  int match_trigger_ele35  ;
  int match_trigger_dou33  ;
  int match_trigger_dou33_unseeded  ;
  int match_trigger_dou33Et  ;
  int match_trigger_dou33Et_unseeded  ;
  int match_trigger_dou33L1  ;
  
  int accept_core_ID        ;
  int accept_isolation      ;
  int accept_tag_ID         ;
  int accept_noDEtaIn_ID    ;
  int accept_EcalDriven_ID  ;
  int accept_noIsolation_ID ;
  int accept_nominal_ID     ;
  int isTag                 ;
  int isProbe               ;
  int isFired               ;
  int isFired_unseeded      ;
  int isEtPassed               ;
  int isEtPassed_unseeded      ;
  int isL1Passed               ;
  
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

    L1Et = 0 ;

    match_trigger_ele35 = 0 ;
    match_trigger_dou33 = 0 ;
    match_trigger_dou33_unseeded = 0 ;
    match_trigger_dou33Et = 0 ;
    match_trigger_dou33Et_unseeded = 0 ;
    match_trigger_dou33L1 = 0 ;
    
    accept_core_ID        = 0 ;
    accept_isolation      = 0 ;
    accept_tag_ID         = 0 ;
    accept_noDEtaIn_ID    = 0 ;
    accept_EcalDriven_ID  = 0 ;
    accept_noIsolation_ID = 0 ;
    accept_nominal_ID     = 0 ;
    isTag                 = 0 ;
    isProbe               = 0 ;
    isFired               = 0 ;
    isFired_unseeded      = 0 ;
    isEtPassed               = 0 ;
    isEtPassed_unseeded      = 0 ;
    isL1Passed               = 0 ;
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
    bool accept_EcalDriven = value_EcalDriven == 1.0 ? 1 : 0 ;
    bool accept_dEtaIn = (fabs(value_dEtaIn) < 0.004 && region==1) || (fabs(value_dEtaIn) < 0.006 && region==3) ? 1 : 0 ;
    bool accept_dPhiIn = (fabs(value_dPhiIn) < 0.06 && region==1) || (fabs(value_dPhiIn) < 0.06 && region==3) ? 1 : 0 ;
//    bool accept_dPhiIn = true;
    bool accept_isolEMHadDepth1 = true;
    if     (region==1) accept_isolEMHadDepth1 = value_isolEMHadDepth1 < 2+ 0.03*Et + 0.28*rho;
    else if(region==3) accept_isolEMHadDepth1 = ( ((value_isolEMHadDepth1 < 2.5 + 0.28*rho) && Et<50) || ((value_isolEMHadDepth1 < 2.5 + 0.03*(Et-50) + 0.28*rho) && Et>50) ) ? 1 : 0 ;
    bool accept_IsolPtTrks = value_IsolPtTrks < 5 ;
    bool accept_missingHits = value_missingHits < 2 ;
    bool accept_dxyFirstPV = (fabs(value_dxyFirstPV) < 0.02 && region==1) || (fabs(value_dxyFirstPV) < 0.05 && region==3) ;//check

    accept_core_ID = (accept_dPhiIn && accept_Sieie && accept_missingHits && accept_dxyFirstPV && accept_HOverE && accept_showershape) ? 1 : 0 ;
    accept_isolation = (accept_isolEMHadDepth1 && accept_IsolPtTrks) ? 1 : 0 ;
    accept_tag_ID          = (accept_core_ID && accept_isolation &&  accept_dEtaIn) ? 1 : 0 ;
    accept_noDEtaIn_ID     = (accept_core_ID && accept_isolation                  ) ? 1 : 0 ;
    accept_noIsolation_ID  = (accept_core_ID &&                      accept_dEtaIn) ? 1 : 0 ;
    accept_nominal_ID      = (accept_tag_ID                                       ) ? 1 : 0 ;
    if(region!=3) accept_noDEtaIn_ID = accept_nominal_ID ;
    accept_EcalDriven_ID = accept_EcalDriven ;

    isTag = (Et>35 && region==1 && accept_tag_ID) ? 1 : 0 ;
    isProbe = (accept_tag_ID ) ? 1 : 0 ;

}
};
void displayProgress(long current, long max){
  using std::cerr;

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
   
   TFile file_out(fname,"RECREATE") ;
   fChain->SetBranchStatus("*"           ,0) ;
   fChain->SetBranchStatus("trig*"           ,1) ;
   fChain->SetBranchStatus("pv*"           ,1) ;
   fChain->SetBranchStatus("ev_*"           ,1) ;
   TTree* tree_out = fChain->CloneTree(0) ; 
   fChain->SetBranchStatus("*"           ,1) ;
   tree_out->SetName("tap") ;
   
   float mee_out ;
   int   OS_out ;
   int   HLT_Ele27_out ;
   
   int   pv_n_out ;
   int   heep_n_out ;
   int   PU_true_out ;
   float w_PU_golden_out ;
   float w_PU_silver_out ;
   float w_PU_silver_up_out ;
   float w_PU_silver_down_out ;
   float w_PU_combined_out ;
   
   float tag_Et_out ;
   float tag_sc_eta_out ;
   float tag_eta_out ;
   float tag_phi_out ;
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
   int   probe_Et35_out ;
   int   probe_Et20_out ;
   int   probe_ID_tag_out ;
   int   probe_ID_noDEtaIn_out ;
   int   probe_ID_EcalDriven_out ;
   int   probe_ID_noIsolation_out ;
   int   probe_ID_nominal_out ;
   int   probe_isProbe_out ;
   int   probe_truthmatched_out ;

   int   Pass_DoubleEle33 ;
  
 
   float M_ee ;
   float M_ee_sc ;
   float probe_sc_eta_out ;
   float probe_eta_out ;
   float probe_phi_out ;
   int   probe_typ_out ;
   int   probe_charge_out ;
   int   probe_region_out ;
   float probe_px ;
   float probe_py ;
   float probe_pz ;
   float probe_pt ;
   int  probe_fired ;
   int  probe_fired_unseeded ;
   int  probe_Et_fired ;
   int  probe_Et_fired_unseeded ;
   int  probe_L1_fired ;
   // These variables keep track of how many Z->ee candidates we have in the event.
   
   tree_out->Branch("mee"      , &mee_out      , "mee/F"      ) ;
   tree_out->Branch("OS"       , &OS_out       , "OS/I"       ) ;
   tree_out->Branch("HLT_Ele27", &HLT_Ele27_out, "HLT_Ele27/I") ;
   
   tree_out->Branch("heep_n"   , &heep_n_out, "heep_n/I") ;
   tree_out->Branch("PU_true", &PU_true_out , "PU_true/I"  ) ;
   tree_out->Branch("Pass_DoubleEle33", &Pass_DoubleEle33 , "Pass_DoubleEle33/I"  ) ;
   tree_out->Branch("probe_fired", &probe_fired , "probe_fired/I"  ) ;
   tree_out->Branch("probe_fired_unseeded", &probe_fired_unseeded , "probe_fired_unseeded/I"  ) ;
   tree_out->Branch("probe_Et_fired", &probe_Et_fired , "probe_Et_fired/I"  ) ;
   tree_out->Branch("probe_Et_fired_unseeded", &probe_Et_fired_unseeded , "probe_Et_fired_unseeded/I"  ) ;
   tree_out->Branch("probe_L1_fired", &probe_L1_fired , "probe_L1_fired/I"  ) ;
   
   tree_out->Branch("w_PU_golden"         , &w_PU_golden_out          , "w_PU_golden/F"          ) ;
   tree_out->Branch("w_PU_silver"         , &w_PU_silver_out          , "w_PU_silver/F"          ) ;
   tree_out->Branch("w_PU_silver_down"    , &w_PU_silver_down_out     , "w_PU_silver_down/F"     ) ;
   tree_out->Branch("w_PU_silver_up"      , &w_PU_silver_up_out       , "w_PU_silver_up/F"       ) ;
   tree_out->Branch("w_PU_combined"       , &w_PU_combined_out        , "w_PU_combined/F"        ) ;
   
   tree_out->Branch("t_Et"    , &tag_Et_out    , "t_Et/F"    ) ;
   tree_out->Branch("t_sc_eta", &tag_sc_eta_out, "t_sc_eta/F"   ) ;
   tree_out->Branch("t_eta"   , &tag_eta_out   , "t_eta/F"   ) ;
   tree_out->Branch("t_phi"   , &tag_phi_out   , "t_phi/F"   ) ;
   tree_out->Branch("t_Et35"  , &tag_Et35_out  , "t_Et35/I"  ) ;
   tree_out->Branch("t_Et20"  , &tag_Et20_out  , "t_Et20/I"  ) ;
   tree_out->Branch("t_charge", &tag_charge_out, "t_charge/I") ;
   tree_out->Branch("t_region", &tag_region_out, "t_region/I") ;
   tree_out->Branch("t_isTag" , &tag_isTag_out , "t_isTag/I" ) ;
   
   tree_out->Branch("t_ID_tag"        , &tag_ID_tag_out        , "t_ID_tag/I"        ) ;
   tree_out->Branch("t_ID_noDEtaIn"   , &tag_ID_noDEtaIn_out   , "t_ID_noDEtaIn/I"   ) ;
   tree_out->Branch("t_ID_EcalDriven" , &tag_ID_EcalDriven_out , "t_ID_EcalDriven/I" ) ;
   tree_out->Branch("t_ID_noIsolation", &tag_ID_noIsolation_out, "t_ID_noIsolation/I") ;
   tree_out->Branch("t_ID_nominal"    , &tag_ID_nominal_out    , "t_ID_nominal/I"    ) ;
   tree_out->Branch("t_truthmatched"  , &tag_truthmatched_out  , "t_truthmatched/I"  ) ;
   
   tree_out->Branch("p_Et"    , &probe_Et_out    , "p_Et/F"    ) ;
   tree_out->Branch("p_Et35"  , &probe_Et35_out  , "p_Et35/I"  ) ;
   tree_out->Branch("p_Et20"  , &probe_Et20_out  , "p_Et20/I"  ) ;
   tree_out->Branch("p_charge", &probe_charge_out, "p_charge/I") ;
   tree_out->Branch("p_region", &probe_region_out, "p_region/I") ;
   tree_out->Branch("p_isProbe", &probe_isProbe_out , "p_isProbe/I" ) ;
   
   tree_out->Branch("p_ID_tag"        , &probe_ID_tag_out        , "p_ID_tag/I"        ) ;
   tree_out->Branch("p_ID_noDEtaIn"   , &probe_ID_noDEtaIn_out   , "p_ID_noDEtaIn/I"   ) ;
   tree_out->Branch("p_ID_EcalDriven" , &probe_ID_EcalDriven_out , "p_ID_EcalDriven/I" ) ;
   tree_out->Branch("p_ID_noIsolation", &probe_ID_noIsolation_out, "p_ID_noIsolation/I") ;
   tree_out->Branch("p_ID_nominal"    , &probe_ID_nominal_out    , "p_ID_nominal/I"    ) ;
   tree_out->Branch("p_truthmatched"  , &probe_truthmatched_out  , "p_truthmatched/I"  ) ;
   
   tree_out->Branch("probe_sc_eta", &probe_sc_eta_out, "probe_sc_eta/F"   ) ;
   tree_out->Branch("probe_eta"   , &probe_eta_out   , "probe_eta/F"   ) ;
   tree_out->Branch("probe_phi"   , &probe_phi_out   , "probe_phi/F"   ) ;
   tree_out->Branch("probe_charge", &probe_charge_out, "probe_charge/I") ;
   tree_out->Branch("probe_region", &probe_region_out, "probe_region/I") ;
   tree_out->Branch("probe_type"  , &probe_typ_out   , "probe_typ/I") ;
   
   tree_out->Branch("probe_px", &probe_px, "probe_px/F") ;
   tree_out->Branch("probe_py", &probe_py, "probe_py/F") ;
   tree_out->Branch("probe_pz", &probe_pz, "probe_pz/F") ;
   tree_out->Branch("probe_pt", &probe_pt, "probe_pt/F") ;
   tree_out->Branch("M_ee"  , &M_ee  , "M_ee/F"  ) ;
   tree_out->Branch("M_ee_sc"  , &M_ee_sc  , "M_ee_sc/F"  ) ;
   // Setup the trigger for changing data structures.
   
   Ele33_trig_fire = -1;
   
   TRandom3 rand ;
   Long64_t nbytes = 0, nb = 0;
   int nn=0;
   for (Long64_t jentry=0; jentry<nentries;jentry++){
      displayProgress(jentry, nentries) ;
      
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

      bool triggerMatch = false ;
      bool hasTAndP     = false ;
      if(true==isData){
        
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

        w_PU_combined_out = w_sign;
        w_PU_golden_out   = w_sign;
        w_PU_silver_out   = w_sign;
        w_PU_silver_down_out   = w_sign;
        w_PU_silver_up_out     = w_sign;
      }
      
      std::vector<electron_candidate*> electrons ;
      //cout<<"gsf_n : "<<gsf_n<<endl;
      for(unsigned int iEl=0 ; iEl<gsf_n ; ++iEl){
        float Et     = gsf_caloEnergy->at(iEl)*sin(2.*atan(exp(-1.*gsf_sc_eta->at(iEl)))) ;
        int   charge = gsf_charge->at(iEl) ;
        float gsf_eta_in    = gsf_eta->at(iEl) ;
        float gsf_phi_in    = gsf_phi->at(iEl) ;
        float eta    = gsf_sc_eta->at(iEl) ;
        float phi    = gsf_sc_phi->at(iEl) ;

        electron_candidate* el = new electron_candidate(Et, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;

        //cout<<"before corr : "<<el->Et<<"region :"<<el->region<<endl;
        //cout<<"after corr : "<<el->Et<<"region :"<<el->region<<endl;
        //cout<<"*************************"<<endl;
        
        el->apply_ID_value(gsf_deltaPhiSuperClusterTrackAtVtx->at(iEl),
                           gsf_full5x5_sigmaIetaIeta->at(iEl),
                     float(gsf_nLostInnerHits->at(iEl) ),
                      fabs(gsf_dxy_firstPVtx->at(iEl)),
                           gsf_hadronicOverEm->at(iEl),
                           gsf_sc_energy->at(iEl),
                          (gsf_full5x5_e1x5->at(iEl)/gsf_full5x5_e5x5->at(iEl) ),
                          (gsf_full5x5_e2x5Max->at(iEl)/gsf_full5x5_e5x5->at(iEl) ),
                          (gsf_dr03EcalRecHitSumEt->at(iEl) + gsf_dr03HcalDepth1TowerSumEt->at(iEl) ),
                           gsf_dr03TkSumPt->at(iEl),
                     float(gsf_ecaldrivenSeed->at(iEl) ),
                           gsf_deltaEtaSeedClusterTrackAtVtx->at(iEl),
                           ev_fixedGridRhoFastjetAll) ;

        if(el->isProbe)
        {
          electrons.push_back(el) ;
        }
      }
     
      if(electrons.size()!=2)
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

      int n_tag = 0;
      int n_probe = 0;
      int flg_tag = -1;
      int flg_probe = -1;
      UInt_t i;
      for(i=0;i<electrons.size();i++)
      {
         electron_candidate* tag = electrons.at(i) ;
         if(tag->isTag)
         {
            n_tag += 1;
            flg_tag = i;
         }
         if(tag->isProbe)
         {
            n_probe += 1;
         }
      }
      if(n_tag == 0 && n_probe == 2)
      {
         flg_tag = 0;
         flg_probe = 1;
      }
      else
      {
         flg_probe = 1 - flg_tag ;
      }

      if(flg_probe<0 || flg_tag<0 || electrons.size()<2 || (flg_probe == flg_tag))
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
      electron_candidate* tag = electrons.at(flg_tag) ;

      tag_Et_out             = tag->Et ;
      tag_sc_eta_out         = tag->eta ;
      tag_eta_out            = tag->p4.Eta() ;
      tag_phi_out            = tag->p4.Phi() ;
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
          
      
      electron_candidate* probe = electrons.at(flg_probe);

      probe_Et_out             =probe->Et ;
      probe_sc_eta_out         =probe->eta ;
      probe_eta_out            =probe->p4.Eta() ;
      probe_phi_out            =probe->p4.Phi() ;
      probe_charge_out         =probe->charge ;
      probe_region_out         =probe->region ;
      probe_isProbe_out        =probe->isProbe ;
      probe_typ_out            =-1 ;
      
      probe_px 	      = probe->p4.Px();
      probe_py 	      = probe->p4.Py();
      probe_pz 	      = probe->p4.Pz();
      probe_pt 	      = probe->Et;

      probe_ID_tag_out         = probe->accept_tag_ID ;
      probe_ID_noDEtaIn_out    = probe->accept_noDEtaIn_ID ;
      probe_ID_EcalDriven_out  = probe->accept_EcalDriven_ID ;
      probe_ID_noIsolation_out = probe->accept_noIsolation_ID ;
      probe_ID_nominal_out     = probe->accept_nominal_ID ;

      heep_n_out = electrons.size() ;

      M_ee = (probe->p4+tag->p4).Mag();
      M_ee_sc = (probe->p4_sc+tag->p4_sc).Mag();
      probe_fired = probe->isFired;
      probe_fired_unseeded = probe->isFired_unseeded;
      probe_Et_fired = probe->isEtPassed;
      probe_Et_fired_unseeded = probe->isEtPassed_unseeded;
      probe_L1_fired = probe->isL1Passed;

      nn++;
      tree_out->Fill() ;
      
      for (std::vector<electron_candidate*>::iterator it = electrons.begin(); it != electrons.end(); it ++){
        if (NULL != *it)
        {
          delete *it;
          *it = NULL;
          }
      }
      electrons.clear() ;
      electrons.swap(electrons);
      tag = NULL;
      probe = NULL;
      delete tag;
      delete probe;
 
}
   tree_out->Write() ;
   file_out.Close() ;
      std::cout<<"\n"<<nn<<std::endl; 
}
