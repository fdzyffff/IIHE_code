#define reskim_cxx
#include "reskim.h"
#include <TH2.h>
#include <TROOT.h>
#include <TSystem.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TLorentzVector.h>

#include <time.h>
#include <iostream>

#include "fkelectron.C"
#include "turnonEle_all.C"
#include "turnonEle33l1.C"
#include "PU_reWeighting.C"
#include "l1PrescaleFuncs.C"

const float m_el = 0.000511 ;
const float m_mu = 0.10566 ;

struct electron_candidate{
  float Et     ;
  float sc_Et  ;
  float eta    ;
  float phi    ;
  float gsf_eta    ;
  float gsf_phi    ;
  float l1_et ;
  int   Et35   ;
  int   Et20   ;
  int   charge ;
  int   region ;
  
  int truthmatched  ;
  int pass_trigger  ;
  int match_trigger_l1_dou33 ;
  int pass_l1_cut  ;
  
  int accept_core_ID        ;
  int accept_isolation      ;
  int accept_heep_ID        ;
  int accept_noDEtaIn_ID    ;
  int accept_EcalDriven_ID  ;
  int accept_noIsolation_ID ;
  int accept_nominal_ID     ;
  int isTag                 ;
  int isHeep_offline        ;
  int isHeep_online        ;
  int isfake                ;
  
  TLorentzVector p4 ;
  TLorentzVector p4_sc ;
  
  electron_candidate(float Et_in, float gsf_eta_in, float gsf_phi_in, float eta_in, float phi_in, int charge_in){
    sc_Et  = 0;
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
    l1_et = 1.0;
    
    truthmatched = 0 ;
    pass_trigger = 0 ;
    match_trigger_l1_dou33 = 0 ;
    pass_l1_cut = 0 ;
    
    accept_core_ID        = 0 ;
    accept_isolation      = 0 ;
    accept_heep_ID        = 0 ;
    accept_noDEtaIn_ID    = 0 ;
    accept_EcalDriven_ID  = 0 ;
    accept_noIsolation_ID = 0 ;
    accept_nominal_ID     = 0 ;
    isTag                 = 0 ;
    isHeep_offline        = 0 ;
    isHeep_online         = 0 ;
    isfake                = 0 ;
  }
 
  void apply_ID_value(float value_dPhiIn, float value_Sieie, float value_missingHits, float value_dxyFirstPV, float value_HOverE, float value_caloEnergy, float value_E1x5OverE5x5, float value_E2x5OverE5x5, float value_isolEMHadDepth1, float value_IsolPtTrks, float value_EcalDriven, float value_dEtaIn, float rho, bool isFake){
//    bool accept_HOverE = true ;
//    if     (region==1){ accept_HOverE = value_HOverE < 0.05 + 1.0/value_caloEnergy ; }
//    else if(region==3){ accept_HOverE = value_HOverE < 0.05 + (-0.4 + 0.4*fabs(eta)) * rho /value_caloEnergy ; }
//    bool accept_E1x5OverE5x5  = value_E1x5OverE5x5 > 0.83 ;
//    bool accept_E2x5OverE5x5  = value_E2x5OverE5x5 > 0.94 ;
//    bool accept_showershape   = (accept_E1x5OverE5x5 || accept_E2x5OverE5x5) ;
//    if(region!=1) accept_showershape = true ;
//    bool accept_Sieie = value_Sieie < 0.03;
//    if(region!=3) accept_Sieie = true;
////    bool accept_EcalDriven = 1 ;
//    bool accept_EcalDriven = value_EcalDriven >= 0.99 ? 1 : 0 ;
//    bool accept_dEtaIn = (fabs(value_dEtaIn) < 0.004 && region==1) || (fabs(value_dEtaIn) < 0.006 && region==3) ? 1 : 0 ;
//    bool accept_dPhiIn = (fabs(value_dPhiIn) < 0.06 && region==1) || (fabs(value_dPhiIn) < 0.06 && region==3) ? 1 : 0 ;
////    bool accept_dPhiIn = true;
//    bool accept_isolEMHadDepth1 = true;
//    if     (region==1) accept_isolEMHadDepth1 = value_isolEMHadDepth1 < 2+ 0.03*Et + 0.28*rho;
//    else if(region==3) accept_isolEMHadDepth1 = ( ((value_isolEMHadDepth1 < 2.5 + 0.28*rho) && Et<50) || ((value_isolEMHadDepth1 < 2.5 + 0.03*(Et-50) + (0.15 + 0.07 * fabs(eta))*rho) && Et>50) ) ? 1 : 0 ;
//    bool accept_IsolPtTrks = value_IsolPtTrks < 5 ;
//    bool accept_missingHits = value_missingHits < 2 ;
////    bool accept_missingHits = true ;
//    bool accept_dxyFirstPV = (fabs(value_dxyFirstPV) < 0.02 && region==1) || (fabs(value_dxyFirstPV) < 0.05 && region==3) ;//check
//
//    accept_core_ID = (accept_dPhiIn && accept_Sieie && accept_missingHits && accept_dxyFirstPV && accept_HOverE && accept_showershape) ? 1 : 0 ;
//    accept_isolation = (accept_isolEMHadDepth1 && accept_IsolPtTrks) ? 1 : 0 ;
//    accept_heep_ID          = (accept_core_ID && accept_isolation && accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
//    accept_noDEtaIn_ID     = (accept_core_ID && accept_isolation && accept_EcalDriven                 ) ? 1 : 0 ;
//    accept_noIsolation_ID  = (accept_core_ID &&                     accept_EcalDriven && accept_dEtaIn) ? 1 : 0 ;
//    accept_nominal_ID      = (accept_heep_ID                                                           ) ? 1 : 0 ;
//    if(region!=3) accept_noDEtaIn_ID = accept_nominal_ID ;
//    accept_EcalDriven_ID = accept_EcalDriven ;

    isHeep_offline = ((region==1||region==3) && Et>35 && accept_heep_ID && pass_trigger) ? 1 : 0 ;
    if (((region==1||region==3) && Et>35 && !accept_heep_ID && pass_trigger ))
    {
        if((region ==1) && (value_Sieie < 0.013) && (value_HOverE < 0.15) && (value_missingHits <=1) && (value_dxyFirstPV < 0.02) )
        {
            isfake = 1;
        }
        if((region ==3) && (value_Sieie < 0.034) && (value_HOverE < 0.10) && (value_missingHits <=1) && (value_dxyFirstPV < 0.05) )
        {
            isfake = 1;
        }
    }
    isTag = isFake? isfake : isHeep_offline ;
    if ((region == 1 && p4_sc.Et() >= 43) || (region == 3 && p4_sc.Et() >= 48))
    {
        pass_l1_cut = true;
    }
//    if(isTag)
//    {
//      cout<<" # Heep got "<<endl;
//      cout<<" # isFake :  "<<isFake<<endl;
//    }
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
        if (electron_1_in->Et > electron_2_in->Et) {
          electron_1 = electron_1_in ;
          electron_2 = electron_2_in ;
        } else {
          electron_1 = electron_2_in ;
          electron_2 = electron_1_in ;
        }
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


struct jet_candidate{
  float pt     ;
  float px     ;
  float py     ;
  float pz     ;
  float E      ;
  float eta    ;
  float phi    ;
  float jet_CSVv2;
  int   typ ;

  
  int isLoose;
  int isMedium;
  int isTight;
  int isLeading;

  int isbjet;
  int passed; 
 
  TLorentzVector p4 ;
  
  jet_candidate(float pt_in, float eta_in, float phi_in, float energy_in){
  	pt = pt_in;
  	eta = eta_in;
  	phi = phi_in;
        E = energy_in;
        isLoose = 0;
  	passed = 0;
  	isbjet = 0;
        jet_CSVv2 = 0;
        p4.SetPtEtaPhiE(pt, eta, phi, E);
  }
  void check_pass()
  {
  	if (pt>30 & fabs(eta)<2.4 & isLoose)
  	{
  		passed = 1;
  		if (jet_CSVv2 > 0.8484)
  		{
  			isbjet = 1;
  		}
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
   
   int ttbar_reweight = false;
   int isFake_e = false;
   int isFake_mu = false;
   int ele_pass_l1_cut = false;
   int ele_pass_l1_turnOn = false;
   if (strstr(fname,"fke_")!=NULL)
   {
      isFake_e = true;
      isFake_mu = false;
      cout<<"select fake electron"<<endl;
   }
   if (strstr(fname,"fkm_")!=NULL)
   {
      isFake_e = false;
      isFake_mu = true;
      cout<<"select fake muon"<<endl;
   }
   float Mass_treshold=9999.0;
//   if (isWW)
//   {
//      Mass_treshold = 200;
//      cout<<"WW mass bin applied, will select only M_ll < "<<Mass_treshold<<"GeV"<<endl;
//   }
//   if (isTTbar)
//   {
//      Mass_treshold = 500;
//      cout<<"TTbar mass bin applied, will select only M_ll < "<<Mass_treshold<<"GeV"<<endl;
//   }
//   if (isDY)
//   {
//      Mass_treshold = 400;
//      cout<<"DY mass bin applied, will select only M_ll < "<<Mass_treshold<<"GeV"<<endl;
//   }
   if (strstr(fname,"ttbar")!=NULL)
   {
      ttbar_reweight = true;
      cout<<"ttbar top reweight applied"<<endl;
   }

   time_t time_start = time(0) ;
   char* time_start_text = ctime(&time_start) ;
   std::cout << time_start_text << std::endl ;

   Long64_t nentries = fChain->GetEntries();
   std::cout << "In:  " << nentries << std::endl ;
   
   //fChain->SetBranchStatus("*",1) ;
   
   TFile file_out(fname,"RECREATE") ;
   TTree tree_out("tap","Streamlined heep and probe") ;
   TTree tree_out_2("info","Streamlined tag and probe") ;
   
   float mee_out ;
   int   OS_out ;

   float w_sign ;
   
   int   pv_n_out ;
   int   PU_true_out ;
   float w_PU_down_out ;
   float w_PU_up_out ;
   float w_PU_out ;
   float w_fake ;
   float w_other ;
   float w_l1 ;
   
   float ele1_px ;
   float ele1_py ;
   float ele1_pz ;
   float ele1_Et_out ;
   float ele1_sc_Et_out ;
   float ele1_gsfeta_out ;
   float ele1_eta_out ;
   float ele1_phi_out ;
   int   ele1_Et35_out ;
   int   ele1_Et20_out ;
   int   ele1_charge_out ;
   int   ele1_region_out ;
   int   ele1_ID_heep_out ;
   int   ele1_ID_noDEtaIn_out ;
   int   ele1_ID_EcalDriven_out ;
   int   ele1_ID_noIsolation_out ;
   int   ele1_ID_nominal_out ;
   int   ele1_isFake_out ;
   int   ele1_isHeep_online_out ;
   int   ele1_isHeep_offline_out ;
   int   ele1_truthmatched_out ;

   float ele2_px ;
   float ele2_py ;
   float ele2_pz ;
   float ele2_Et_out ;
   float ele2_sc_Et_out ;
   float ele2_gsfeta_out ;
   float ele2_eta_out ;
   float ele2_phi_out ;
   int   ele2_Et35_out ;
   int   ele2_Et20_out ;
   int   ele2_charge_out ;
   int   ele2_region_out ;
   int   ele2_ID_heep_out ;
   int   ele2_ID_noDEtaIn_out ;
   int   ele2_ID_EcalDriven_out ;
   int   ele2_ID_noIsolation_out ;
   int   ele2_ID_nominal_out ;
   int   ele2_isFake_out ;
   int   ele2_isHeep_online_out ;
   int   ele2_isHeep_offline_out ;
   int   ele2_truthmatched_out ;

   // These variables keep track of how many Z->ee candidates we have in the event.
   int Zee_index_out ;
   int heep_index_out ;
   int probe_index_out ;

   int isEE = 0;
   int isEE_acc_inBB = 0;
   int isEE_acc_inBE = 0;
   int isEE_acc = 0;
   int isMuMu = 0;
   float M_ll_mc = 0.0;

   int n_jet ;
   int n_bjet ;

   float l1_LowestSingleL1EG ;

   vector <float> jet_pt_out ;
   vector <float> jet_energy_out ;
   vector <float> jet_px_out ;
   vector <float> jet_py_out ;
   vector <float> jet_pz_out ;
   vector <float> jet_eta_out ;
   vector <float> jet_phi_out ;
   vector <int> jet_passed_out ;
   vector <int> jet_isbjet_out ;

   
   tree_out.Branch("Z_index", &Zee_index_out  , "Z_index/I") ;
   tree_out.Branch("t_index", &heep_index_out  , "t_index/I") ;
   tree_out.Branch("p_index", &probe_index_out, "p_index/I") ;
   
   tree_out.Branch("mee"      , &mee_out      , "mee/F"      ) ;
   tree_out.Branch("OS"       , &OS_out       , "OS/I"       ) ;

   tree_out.Branch("ev_event_out"    , &ev_event    , "ev_event_out/l"    ) ;
   tree_out.Branch("ev_run_out"      , &ev_run      , "ev_run_out/i"    ) ;
   tree_out.Branch("ev_luminosityBlock_out"    , &ev_luminosityBlock    , "ev_luminosityBlock_out/i"    ) ;

   tree_out.Branch("isFake_e"	, &isFake_e	, "isFake_e/i"	) ;

   tree_out.Branch("pv_n"   , &pv_n_out, "pv_n/I") ;
   tree_out.Branch("PU_true", &PU_true_out , "PU_true/I"  ) ;
   
   tree_out.Branch("w_PU_up"  , &w_PU_up_out    , "w_PU_up/F"     ) ;
   tree_out.Branch("w_PU_down", &w_PU_down_out  , "w_PU_down/F"       ) ;
   tree_out.Branch("w_PU"     , &w_PU_out       , "w_PU/F"        ) ;
   tree_out.Branch("w_other"  , &w_other        , "w_other/F"        ) ;
   tree_out.Branch("w_fake"   , &w_fake         , "w_fake/F"          ) ;
   tree_out.Branch("w_l1"     , &w_l1           , "w_l1/F"        ) ;

   tree_out.Branch("ev_prefiringweight", &ev_prefiringweight, "ev_prefiringweight/F");
   tree_out.Branch("ev_prefiringweightup", &ev_prefiringweightup, "ev_prefiringweightup/F");
   tree_out.Branch("ev_prefiringweightdown", &ev_prefiringweightdown, "ev_prefiringweightdown/F");

   tree_out.Branch("l1_LowestSingleL1EG"   , &l1_LowestSingleL1EG  ,  "l1_LowestSingleL1EG/F") ;   
   tree_out.Branch("ele_pass_l1_cut" ,&ele_pass_l1_cut, "ele_pass_l1_cut/i");
   tree_out.Branch("ele_pass_l1_turnOn" ,&ele_pass_l1_turnOn, "ele_pass_l1_turnOn/i");

   tree_out.Branch("ele1_px", &ele1_px, "ele1_px/F") ;
   tree_out.Branch("ele1_py", &ele1_py, "ele1_py/F") ;
   tree_out.Branch("ele1_pz", &ele1_pz, "ele1_pz/F") ;
   tree_out.Branch("ele1_Et"    , &ele1_Et_out    , "ele1_Et/F"    ) ;
   tree_out.Branch("ele1_sc_Et" , &ele1_sc_Et_out , "ele1_sc_Et/F" ) ;
   tree_out.Branch("ele1_eta"   , &ele1_eta_out   , "ele1_eta/F"   ) ;
   tree_out.Branch("ele1_phi"   , &ele1_phi_out   , "ele1_phi/F"   ) ;
   tree_out.Branch("ele1_Et35"  , &ele1_Et35_out  , "ele1_Et35/I"  ) ;
   tree_out.Branch("ele1_Et20"  , &ele1_Et20_out  , "ele1_Et20/I"  ) ;
   tree_out.Branch("ele1_charge", &ele1_charge_out, "ele1_charge/I") ;
   tree_out.Branch("ele1_region", &ele1_region_out, "ele1_region/I") ;
   
   tree_out.Branch("ele1_isHeep_offline", &ele1_isHeep_offline_out, "ele1_isHeep_offline/I"   ) ;
   tree_out.Branch("ele1_isHeep_online" , &ele1_isHeep_online_out , "ele1_isHeep_online/I"   ) ;
   tree_out.Branch("ele1_isFake"        , &ele1_isFake_out        , "ele1_isFake/I"        ) ;
   tree_out.Branch("ele1_ID_heep"       , &ele1_ID_heep_out       , "ele1_ID_heep/I"        ) ;
   tree_out.Branch("ele1_ID_noDEtaIn"   , &ele1_ID_noDEtaIn_out   , "ele1_ID_noDEtaIn/I"   ) ;
   tree_out.Branch("ele1_ID_EcalDriven" , &ele1_ID_EcalDriven_out , "ele1_ID_EcalDriven/I" ) ;
   tree_out.Branch("ele1_ID_noIsolation", &ele1_ID_noIsolation_out, "ele1_ID_noIsolation/I") ;
   tree_out.Branch("ele1_ID_nominal"    , &ele1_ID_nominal_out    , "ele1_ID_nominal/I"    ) ;
   tree_out.Branch("ele1_truthmatched"  , &ele1_truthmatched_out  , "ele1_truthmatched/I"  ) ;
   
   tree_out.Branch("ele2_px", &ele2_px, "ele2_px/F") ;
   tree_out.Branch("ele2_py", &ele2_py, "ele2_py/F") ;
   tree_out.Branch("ele2_pz", &ele2_pz, "ele2_pz/F") ;
   tree_out.Branch("ele2_Et"    , &ele2_Et_out    , "ele2_Et/F"    ) ;
   tree_out.Branch("ele2_sc_Et" , &ele2_sc_Et_out , "ele2_sc_Et/F" ) ;
   tree_out.Branch("ele2_eta"   , &ele2_eta_out   , "ele2_eta/F"   ) ;
   tree_out.Branch("ele2_phi"   , &ele2_phi_out   , "ele2_phi/F"   ) ;
   tree_out.Branch("ele2_Et35"  , &ele2_Et35_out  , "ele2_Et35/I"  ) ;
   tree_out.Branch("ele2_Et20"  , &ele2_Et20_out  , "ele2_Et20/I"  ) ;
   tree_out.Branch("ele2_charge", &ele2_charge_out, "ele2_charge/I") ;
   tree_out.Branch("ele2_region", &ele2_region_out, "ele2_region/I") ;
   
   tree_out.Branch("ele2_isHeep_offline", &ele2_isHeep_offline_out, "ele2_isHeep_offline/I"   ) ;
   tree_out.Branch("ele2_isHeep_online" , &ele2_isHeep_online_out , "ele2_isHeep_online/I"   ) ;
   tree_out.Branch("ele2_isFake"        , &ele2_isFake_out        , "ele2_isFake/I"        ) ;
   tree_out.Branch("ele2_ID_heep"       , &ele2_ID_heep_out       , "ele2_ID_heep/I"        ) ;
   tree_out.Branch("ele2_ID_noDEtaIn"   , &ele2_ID_noDEtaIn_out   , "ele2_ID_noDEtaIn/I"   ) ;
   tree_out.Branch("ele2_ID_EcalDriven" , &ele2_ID_EcalDriven_out , "ele2_ID_EcalDriven/I" ) ;
   tree_out.Branch("ele2_ID_noIsolation", &ele2_ID_noIsolation_out, "ele2_ID_noIsolation/I") ;
   tree_out.Branch("ele2_ID_nominal"    , &ele2_ID_nominal_out    , "ele2_ID_nominal/I"    ) ;
   tree_out.Branch("ele2_truthmatched"  , &ele2_truthmatched_out  , "ele2_truthmatched/I"  ) ;

   tree_out.Branch("M_ee"   , &mee_out , "M_ee/F"  ) ;
   tree_out.Branch("M_ll_mc"       , &M_ll_mc       , "M_ll_mc/F"       ) ;

   tree_out.Branch("MET_Et"		,&MET_Et		,"MET_Et/F"		);
   tree_out.Branch("MET_phi"		,&MET_phi		,"MET_phi/F"		);
   tree_out.Branch("MET_significance"	,&MET_significance	,"MET_significance/F"	);
   tree_out.Branch("MET_T1Txy_Pt"		,&MET_T1Txy_Pt			,"MET_T1Txy_Pt/F"		);
   tree_out.Branch("MET_T1Txy_phi"		,&MET_T1Txy_phi			,"MET_T1Txy_phi/F"		);
   tree_out.Branch("MET_T1Txy_significance"	,&MET_T1Txy_significance	,"MET_T1Txy_significance/F"	);

   tree_out_2.Branch("isEE_acc_inBB"       , &isEE_acc_inBB       , "isEE_acc_inBB/I"       ) ;
   tree_out_2.Branch("isEE_acc_inBE"       , &isEE_acc_inBE       , "isEE_acc_inBE/I"       ) ;
   tree_out_2.Branch("isEE"       , &isEE       , "isEE/I"       ) ;
   tree_out_2.Branch("isEE_acc"       , &isEE_acc       , "isEE_acc/I"       ) ;
   tree_out_2.Branch("isMuMu"       , &isMuMu       , "isMuMu/I"       ) ;
   tree_out_2.Branch("M_ll_mc"       , &M_ll_mc       , "M_ll_mc/F"       ) ;
   tree_out_2.Branch("w_sign"         , &w_sign          , "w_sign/F"          ) ;

   tree_out.Branch("n_jet"	,&n_jet		,"n_jet/I"		);
   tree_out.Branch("n_bjet"	,&n_bjet	,"n_bjet/I"		);
   tree_out.Branch("jet_pt"	,&jet_pt_out) ;
   tree_out.Branch("jet_energy"	,&jet_energy_out) ;
   tree_out.Branch("jet_px"	,&jet_px_out) ;
   tree_out.Branch("jet_py"	,&jet_py_out) ;
   tree_out.Branch("jet_pz"	,&jet_pz_out) ;
   tree_out.Branch("jet_eta"	,&jet_eta_out) ;
   tree_out.Branch("jet_phi"	,&jet_phi_out) ;
   tree_out.Branch("jet_passed"	,&jet_passed_out) ;
   tree_out.Branch("jet_isbjet"	,&jet_isbjet_out) ;

//   tree_out.Branch("trig_Flag_duplicateMuons_accept", &trig_Flag_duplicateMuons_accept, "trig_Flag_duplicateMuons_accept/I");
//   tree_out.Branch("trig_Flag_badMuons_accept", &trig_Flag_badMuons_accept, "trig_Flag_badMuons_accept/I");
//   tree_out.Branch("trig_Flag_noBadMuons_accept", &trig_Flag_noBadMuons_accept, "trig_Flag_noBadMuons_accept/I");
//   tree_out.Branch("trig_Flag_HBHENoiseFilter_accept", &trig_Flag_HBHENoiseFilter_accept, "trig_Flag_HBHENoiseFilter_accept/I");
//   tree_out.Branch("trig_Flag_HBHENoiseIsoFilter_accept", &trig_Flag_HBHENoiseIsoFilter_accept, "trig_Flag_HBHENoiseIsoFilter_accept/I");
//   tree_out.Branch("trig_Flag_CSCTightHaloFilter_accept", &trig_Flag_CSCTightHaloFilter_accept, "trig_Flag_CSCTightHaloFilter_accept/I");
//   tree_out.Branch("trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept", &trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept, "trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept/I");
//   tree_out.Branch("trig_Flag_CSCTightHalo2015Filter_accept", &trig_Flag_CSCTightHalo2015Filter_accept, "trig_Flag_CSCTightHalo2015Filter_accept/I");
//   tree_out.Branch("trig_Flag_globalTightHalo2016Filter_accept", &trig_Flag_globalTightHalo2016Filter_accept, "trig_Flag_globalTightHalo2016Filter_accept/I");
//   tree_out.Branch("trig_Flag_globalSuperTightHalo2016Filter_accept", &trig_Flag_globalSuperTightHalo2016Filter_accept, "trig_Flag_globalSuperTightHalo2016Filter_accept/I");
//   tree_out.Branch("trig_Flag_HcalStripHaloFilter_accept", &trig_Flag_HcalStripHaloFilter_accept, "trig_Flag_HcalStripHaloFilter_accept/I");
//   tree_out.Branch("trig_Flag_hcalLaserEventFilter_accept", &trig_Flag_hcalLaserEventFilter_accept, "trig_Flag_hcalLaserEventFilter_accept/I");
//   tree_out.Branch("trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept", &trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept, "trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept/I");
//   tree_out.Branch("trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept", &trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept, "trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept/I");
//   tree_out.Branch("trig_Flag_goodVertices_accept", &trig_Flag_goodVertices_accept, "trig_Flag_goodVertices_accept/I");
//   tree_out.Branch("trig_Flag_eeBadScFilter_accept", &trig_Flag_eeBadScFilter_accept, "trig_Flag_eeBadScFilter_accept/I");
//   tree_out.Branch("trig_Flag_ecalLaserCorrFilter_accept", &trig_Flag_ecalLaserCorrFilter_accept, "trig_Flag_ecalLaserCorrFilter_accept/I");
//   tree_out.Branch("trig_Flag_trkPOGFilters_accept", &trig_Flag_trkPOGFilters_accept, "trig_Flag_trkPOGFilters_accept/I");
//   tree_out.Branch("trig_Flag_chargedHadronTrackResolutionFilter_accept", &trig_Flag_chargedHadronTrackResolutionFilter_accept, "trig_Flag_chargedHadronTrackResolutionFilter_accept/I");
//   tree_out.Branch("trig_Flag_muonBadTrackFilter_accept", &trig_Flag_muonBadTrackFilter_accept, "trig_Flag_muonBadTrackFilter_accept/I");
//   tree_out.Branch("trig_Flag_trkPOG_manystripclus53X_accept", &trig_Flag_trkPOG_manystripclus53X_accept, "trig_Flag_trkPOG_manystripclus53X_accept/I");
//   tree_out.Branch("trig_Flag_trkPOG_toomanystripclus53X_accept", &trig_Flag_trkPOG_toomanystripclus53X_accept, "trig_Flag_trkPOG_toomanystripclus53X_accept/I");
//   tree_out.Branch("trig_Flag_trkPOG_logErrorTooManyClusters_accept", &trig_Flag_trkPOG_logErrorTooManyClusters_accept, "trig_Flag_trkPOG_logErrorTooManyClusters_accept/I");
//   tree_out.Branch("trig_Flag_METFilters_accept", &trig_Flag_METFilters_accept, "trig_Flag_METFilters_accept/I");
   tree_out.Branch("trig_DouEle33MW_fire", &trig_DouEle33MW_fire, "trig_DouEle33MW_fire/I");

   // Setup the trigger for changing data structures.
   
//   std::vector<runCounter> runs ;
   
   TRandom3 Tr ;
   Long64_t nbytes = 0, nb = 0;
   int nn=0;
   for (Long64_t jentry=0; jentry<nentries;jentry++){
      displayProgress(jentry, nentries) ;

      w_sign = 1.0 ;
      n_jet = 0;
      n_bjet = 0;
      isEE = false ;
      isEE_acc = false ;
      isEE_acc_inBB = false ;
      isEE_acc_inBE = false ;
      isMuMu = false ;
      M_ll_mc = 0.0 ;

      vector <float>().swap(jet_pt_out) ;
      vector <float>().swap(jet_energy_out) ;
      vector <float>().swap(jet_px_out) ;
      vector <float>().swap(jet_py_out) ;
      vector <float>().swap(jet_pz_out) ;
      vector <float>().swap(jet_eta_out) ;
      vector <float>().swap(jet_phi_out) ;
      vector <int>().swap(jet_passed_out) ;
      vector <int>().swap(jet_isbjet_out) ;
    
      //fChain->SetBranchStatus("*",0) ;

      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   
      nbytes += nb;

      if(isData)
      {
        int ev_run_tmp = int(ev_run) ;
        l1_LowestSingleL1EG = getLowestSingleL1EG(ev_run_tmp, ev_luminosityBlock);
      }
      else
      {
        l1_LowestSingleL1EG = 0 ;
      }
      //std::cout<<"LowestSingleL1EG : "<<l1_LowestSingleL1EG<<std::endl;

      w_l1 = 1.0 ;
      w_other = 1.0 ;
      w_fake = 1.0 ;
      if(ttbar_reweight)
      {
        for(unsigned iMC=0 ; iMC<LHE_Pt->size() ; ++iMC)
        {
          if( (abs(LHE_pdgid->at(iMC)) == 6) )w_other = w_other*exp(0.0615-0.0005*LHE_Pt->at(iMC));
        }
        w_other = sqrt(w_other);
      }

      if(!isData)w_sign = mc_w_sign < 0 ? -1 : 1 ;

/*      if((!isData) && (Mass_treshold < 9999.0)){
      TLorentzVector MC_p4_1(1,0,0,0);
      TLorentzVector MC_p4_2(1,0,0,0);
      bool accept=true;

      for(unsigned iMC=0 ; iMC<LHE_Pt->size() ; ++iMC){
      if( (abs(LHE_pdgid->at(iMC)) != 15) ) continue;
      MC_p4_1.SetPtEtaPhiE(LHE_Pt->at(iMC),LHE_Eta->at(iMC),LHE_Phi->at(iMC),LHE_E->at(iMC)) ;
      for(unsigned jMC=iMC+1 ; jMC<LHE_Pt->size() ; ++jMC){
      if( (abs(LHE_pdgid->at(jMC)) != 15) ) continue;
      MC_p4_2.SetPtEtaPhiE(LHE_Pt->at(jMC),LHE_Eta->at(jMC),LHE_Phi->at(jMC),LHE_E->at(jMC)) ;
      if(MC_p4_1.DeltaR(MC_p4_2)<0.001) continue;
      if((MC_p4_1+MC_p4_2).M()>Mass_treshold){accept=false; break;}
      }
      if(accept==false) break;
      }
      if(accept==false) continue;
      }
*/

      if(true==isDYToTT){
        bool reject_event = false ;
        bool has_ep = false ;
        bool has_em = false ;
        for(unsigned iMC=0 ; iMC<mc_n ; ++iMC){
          if(mc_pdgId->at(iMC)== 11) has_em = true ;
          if(mc_pdgId->at(iMC)==-11) has_ep = true ;
          if(has_ep && has_em){
            reject_event = true ;
            break ;
          }
        }
        if(reject_event==true) continue ;
      }

//      if(true==isDYToEE){
//        bool accept_event = false ;
//        bool has_ep = false ;
//        bool has_em = false ;
//        for(unsigned iMC=0 ; iMC<mc_n ; ++iMC){
//          if(mc_pdgId->at(iMC)== 11) has_em = true ;
//          if(mc_pdgId->at(iMC)==-11) has_ep = true ;
//          if(has_ep && has_em){
//            accept_event = true ;
//            break ;
//          }
//        }
//        if(accept_event==false) continue ;
//      }

      if(true==isDYToEE){
        bool accept_event = false ;
        bool has_ep = false ;
        bool has_em = false ;
        for(unsigned iMC=0 ; iMC<LHE_pdgid->size() ; ++iMC){
          if(LHE_pdgid->at(iMC)== 11) has_em = true ;
          if(LHE_pdgid->at(iMC)==-11) has_ep = true ;
          if(has_ep && has_em){
            accept_event = true ;
            break ;
          }
        }
        if(accept_event==false) continue ;
      }

      Zee_index_out = 0 ;
      Zee_index_out = 0 ;
      heep_index_out = 0 ;
      
      pv_n_out = pv_n ;
      bool triggerMatch = false ;
      bool hasTAndP     = false ;
      if(true==isData){
        PU_true_out = 1.0 ;
        // Set weights to 1
        w_PU_up_out 	= 1.0 ;
        w_PU_down_out 	= 1.0 ;
        w_PU_out 	= 1.0 ;
      }
      else{
        // Set PU weights
        int PU = mc_trueNumInteractions ;
        PU_true_out = PU ;

        w_PU_out       = w_sign*PU_2017_Rereco::MC_pileup_weight(PU, mc_str, "Rereco_all");
        //w_PU_up_out    = w_sign*PU_2017_Rereco::MC_pileup_weight(PU,1,"all");
        //w_PU_down_out  = w_sign*PU_2017_Rereco::MC_pileup_weight(PU,2,"all");
      }

      if (!isData) {
        int tmp_n_ele = 0 ;
        int acc_tmp_n_ele = 0 ;
        int tmp_n_muon = 0 ;
        int find_barrel = 0 ;
        int find_endcap = 0 ;
        TLorentzVector p4_ele ;
        TLorentzVector p4_muon ;
        p4_ele.SetXYZM(0,0,0,0) ;
        p4_muon.SetXYZM(0,0,0,0) ;
        //for(unsigned iMC=0 ; iMC<mc_pdgId->size() ; ++iMC)
        //{
        //  if(abs(mc_pdgId->at(iMC)) == 11 && mc_status->at(iMC) == 23)
        //  {
        //    TLorentzVector tmp_p4_ele ;
        //    tmp_p4_ele.SetXYZM(mc_px->at(iMC), mc_py->at(iMC), mc_pz->at(iMC), mc_mass->at(iMC)) ;
        //    p4_ele = p4_ele + tmp_p4_ele ;
        //    tmp_n_ele += 1 ;
        //  }
        //  if(abs(mc_pdgId->at(iMC)) == 13 && mc_status->at(iMC) == 23)
        //  {
        //    TLorentzVector tmp_p4_muon ;
        //    tmp_p4_muon.SetXYZM(mc_px->at(iMC), mc_py->at(iMC), mc_pz->at(iMC), mc_mass->at(iMC)) ;
        //    p4_muon = p4_muon + tmp_p4_muon ;
        //    tmp_n_muon += 1 ;
        //  }
        //}
        if (LHE_pdgid->size() > 0) {
          for(unsigned iMC=0 ; iMC<LHE_pdgid->size() ; ++iMC)
          {
            if(abs(LHE_pdgid->at(iMC)) == 11)// && mc_status->at(iMC) == 23)
            {
              TLorentzVector tmp_p4_ele ;
              tmp_p4_ele.SetPtEtaPhiE(LHE_Pt->at(iMC), LHE_Eta->at(iMC), LHE_Phi->at(iMC), LHE_E->at(iMC)) ;
              p4_ele = p4_ele + tmp_p4_ele ;
              tmp_n_ele += 1 ;
              if(tmp_p4_ele.Et() > 35)
              { 
                if(fabs(tmp_p4_ele.Eta()) < 1.4442)
                { 
                  find_barrel = true ;
                  acc_tmp_n_ele += 1;
                }
                else if(1.566 < fabs(tmp_p4_ele.Eta()) && fabs(tmp_p4_ele.Eta()) < 2.5)
                { 
                  find_endcap = true ;
                  acc_tmp_n_ele += 1;
                }
              }
            }
            if(abs(LHE_pdgid->at(iMC)) == 13)// && mc_status->at(iMC) == 23)
            {
              TLorentzVector tmp_p4_muon ;
              tmp_p4_muon.SetPtEtaPhiE(LHE_Pt->at(iMC), LHE_Eta->at(iMC), LHE_Phi->at(iMC), LHE_E->at(iMC)) ;
              p4_muon = p4_muon + tmp_p4_muon ;
              tmp_n_muon += 1 ;
            }
          }
        }
        //cout<<"tmp_n_ele : "<<tmp_n_ele<<endl;
        //cout<<"tmp_n_muon : "<<tmp_n_muon<<endl;
        if(tmp_n_ele==2)
        {
          isEE = true ;
          M_ll_mc = p4_ele.Mag() ;
          if(acc_tmp_n_ele == 2)
          {
            isEE_acc = true ;
            if (find_barrel && !find_endcap)
            {
              isEE_acc_inBB = true ;
            }
            if (find_barrel && find_endcap)
            {
              isEE_acc_inBE = true ;
            }
          }
        }
/*        if(tmp_n_muon==2)
        {
          isMuMu = true ;
          M_ll_mc = p4_muon.Mag() ;
        }*/
        if(isEE)
        {
          tree_out_2.Fill() ;
        }
      }


      std::vector<electron_candidate*> electrons ;
      for(unsigned int iEl=0 ; iEl<gsf_eta->size() ; ++iEl){
        float Et     = gsf_ecalEnergy->at(iEl)*sin(gsf_theta->at(iEl)) ;
        float gsf_eta_in    = gsf_eta->at(iEl) ;
        float gsf_phi_in    = gsf_phi->at(iEl) ;
        float eta    = gsf_sc_eta->at(iEl) ;
        float phi    = gsf_sc_phi->at(iEl) ;
        int   charge = gsf_charge->at(iEl) ;

        electron_candidate* el = new electron_candidate(Et, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        el->sc_Et = gsf_sc_energy->at(iEl)*sin(gsf_theta->at(iEl)) ;
        el->p4_sc.SetPtEtaPhiM(el->sc_Et, eta, phi, m_el) ;


        if(isData)
        {

          TLorentzVector trigp4_dou33 ;

          for(unsigned int itrig=0 ; itrig<trig_dou33MW_EGL1_eta->size() ; ++itrig)
          {
            trigp4_dou33.SetPtEtaPhiM(100,trig_dou33MW_EGL1_eta->at(itrig),trig_dou33MW_EGL1_phi->at(itrig),10) ;
            if(trigp4_dou33.DeltaR(el->p4_sc) < 0.3)
            {
              el->l1_et = trig_dou33MW_EGL1_et->at(itrig);
              if (el->l1_et >= l1_LowestSingleL1EG)
              {
                el->match_trigger_l1_dou33 = true;
                break ;
              }
            } 
          }

          for(unsigned int itrig=0 ; itrig<trig_dou33MW_unseeded_eta->size() ; ++itrig)
          { 
            trigp4_dou33.SetPtEtaPhiM(100,trig_dou33MW_unseeded_eta->at(itrig),trig_dou33MW_unseeded_phi->at(itrig),10) ;
            if(trigp4_dou33.DeltaR(el->p4_sc) < 0.1)
            { 
              el->pass_trigger = true;
              break ;
            }
          }
        }
        else
        {
          el->pass_trigger = trigEle33_2017::passTrig(el->Et, eta) ;
          el->match_trigger_l1_dou33 = trigEle33l1::passTrig(el->sc_Et, eta);
        }
        
        el->accept_heep_ID = gsf_VID_heepElectronID_HEEPV70->at(iEl);
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
                           ev_fixedGridRhoFastjetAll,
                           isFake_e) ;


        //el->isHeep_online = gsf_isHeepV7->at(iEl);
        el->isHeep_online = 0;
        if(el->isTag)
        {
          electrons.push_back(el) ;
        }
      }
     
      if(electrons.size()<2)
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
         electron_candidate* tag1 = electrons.at(i) ;
         if(false==tag1->isTag) continue ;
         for(j=i+1;j<electrons.size();j++)
         {
            electron_candidate* tag2 = electrons.at(j) ;
            if(false==tag2->isTag) continue ;
            Z_pair* z = new Z_pair(tag1, tag2);
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
      // fill jet
//      std::vector<jet_candidate*> jets ;
//      for(unsigned int ijet=0 ; ijet<jet_pt->size() ; ++ijet){
//        float pt     = jet_pt->at(ijet) ;
//        float eta    = jet_eta->at(ijet) ;
//        float phi    = jet_phi->at(ijet) ;
//        float energy = jet_energy->at(ijet) ;
//
//        jet_candidate* jet = new jet_candidate(pt, eta, phi, energy) ;
//        jet->isLoose = int(jet_isJetIDLoose->at(ijet));
//        jet->jet_CSVv2 = jet_CSVv2->at(ijet);
//        jet->check_pass();
//
//     	jets.push_back(jet);
//      }

      Z_pair* z = Z_pairs.at(flg_z) ;

      electron_candidate* ele1 = z->electron_1 ;

      ele1_px                 = ele1->p4.Px();
      ele1_py                 = ele1->p4.Py();
      ele1_pz                 = ele1->p4.Pz();
      ele1_Et_out             = ele1->Et ;
      ele1_eta_out            = ele1->eta ;
      ele1_gsfeta_out         = ele1->p4.Eta() ;
      ele1_phi_out            = ele1->phi ;
      ele1_Et35_out           = ele1->Et35 ;
      ele1_Et20_out           = ele1->Et20 ;
      ele1_charge_out         = ele1->charge ;
      ele1_region_out         = ele1->region ;
      ele1_ID_heep_out        = ele1->accept_heep_ID ;
      ele1_ID_noDEtaIn_out    = ele1->accept_noDEtaIn_ID ;
      ele1_ID_EcalDriven_out  = ele1->accept_EcalDriven_ID ;
      ele1_ID_noIsolation_out = ele1->accept_noIsolation_ID ;
      ele1_ID_nominal_out     = ele1->accept_nominal_ID ;
      ele1_isFake_out         = ele1->isfake ;
      ele1_isHeep_online_out  = ele1->isHeep_online ;
      ele1_isHeep_offline_out = ele1->isHeep_offline ;
      ele1_truthmatched_out   = ele1->truthmatched ;
        
      triggerMatch = true ;

      electron_candidate* ele2 = z->electron_2 ;

      ele2_px                 = ele2->p4.Px();
      ele2_py                 = ele2->p4.Py();
      ele2_pz                 = ele2->p4.Pz();
      ele2_Et_out             = ele2->Et ;
      ele2_gsfeta_out         = ele2->p4.Eta();
      ele2_eta_out            = ele2->eta ;
      ele2_phi_out            = ele2->phi ;
      ele2_Et35_out           = ele2->Et35 ;
      ele2_Et20_out           = ele2->Et20 ;
      ele2_charge_out         = ele2->charge ;
      ele2_region_out         = ele2->region ;
      ele2_ID_heep_out        = ele2->accept_heep_ID ;
      ele2_ID_noDEtaIn_out    = ele2->accept_noDEtaIn_ID ;
      ele2_ID_EcalDriven_out  = ele2->accept_EcalDriven_ID ;
      ele2_ID_noIsolation_out = ele2->accept_noIsolation_ID ;
      ele2_ID_nominal_out     = ele2->accept_nominal_ID ;
      ele2_isFake_out         = ele2->isfake ;
      ele2_isHeep_online_out  = ele2->isHeep_online ;
      ele2_isHeep_offline_out = ele2->isHeep_offline ;
      ele2_truthmatched_out   = ele2->truthmatched ;

	  mee_out = (ele1->p4+ele2->p4).Mag();

//      electron_candidate* leading_ele = ele1->p4.Pt() > ele2->p4.Pt()? ele1: ele2 ;
//      if (isData)
//      {
        w_l1 = 1.0;
//      }
//      else
//      {
//        w_l1 = trigEle33l1::turnOn_MW(ele1->Et, ele1->eta) + trigEle33l1::turnOn_MW(ele2->Et, ele2->eta) - (trigEle33l1::turnOn_MW(ele1->Et, ele1->eta)*trigEle33l1::turnOn_MW(ele2->Et, ele2->eta));
//      }


      ele_pass_l1_turnOn =  (ele1->match_trigger_l1_dou33 || ele2->match_trigger_l1_dou33);
      ele_pass_l1_cut = ((ele1->match_trigger_l1_dou33 && ele1->pass_l1_cut) || (ele2->match_trigger_l1_dou33 && ele2->pass_l1_cut));
//      if(isFake_e)
//     {
//        float fr = 0;
//        fr = fkelectron::frFuncData(ele->Et, ele->eta) ;
//        w_fake = fr/(1 - fr) ;
//      }

      n_jet = 0;
      n_bjet = 0;
//      for (unsigned ijet = 0; ijet<jets.size(); ijet++)
//      { 
//        jet_candidate *jet = jets.at(ijet);
//        if (jet->passed && jet->p4.DeltaR(ele->p4) > 0.4 && jet->p4.DeltaR(muon->p4) > 0.4)
//        {       
//                n_jet++;
//        }
//        if (jet->isbjet && jet->p4.DeltaR(ele->p4) > 0.4 && jet->p4.DeltaR(muon->p4) > 0.4)
//        {       
//                n_bjet++;
//        }
//      }
//
//      for (unsigned ijet = 0; ijet<jets.size(); ijet++)
//      { 
//        jet_candidate *jet = jets.at(ijet);
//        if (jet->p4.DeltaR(ele->p4) > 0.4 && jet->p4.DeltaR(muon->p4) > 0.4)
//        {       
//          jet_pt_out.push_back(jet->p4.Pt()) ;
//          jet_energy_out.push_back(jet->p4.E()) ;
//          jet_px_out.push_back(jet->p4.Px()) ;
//          jet_py_out.push_back(jet->p4.Py()) ;
//          jet_pz_out.push_back(jet->p4.Pz()) ;
//          jet_eta_out.push_back(jet->p4.Eta()) ;
//          jet_phi_out.push_back(jet->p4.Phi()) ;
//          jet_passed_out.push_back(jet->passed) ;
//          jet_isbjet_out.push_back(jet->isbjet) ;
//        }
//      }


      //ele_pass_l1_turnOn = true;
        nn++ ;
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

      ele1 = NULL;
      ele2 = NULL;
      delete ele1;
      delete ele2;
 
//      for (std::vector<jet_candidate*>::iterator it = jets.begin(); it != jets.end(); it ++){
//        if (NULL != *it)
//        { 
//          delete *it;
//          *it = NULL;
//          }
//      }
//      jets.clear() ;
//      jets.swap(jets);
}
   file_out.cd() ;
   tree_out.Write() ;
   tree_out_2.Write() ;
   file_out.Close() ;
   std::cout<<"\n"<<nn<<std::endl; 
}
