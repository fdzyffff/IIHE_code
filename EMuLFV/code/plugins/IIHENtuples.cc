#define IIHENtuples_cxx
#include "IIHENtuples.h"
//#include <TH2.h>
//#include <TStyle.h>
#include <TLorentzVector.h>

#include <time.h>
#include <iostream>
#include <TRandom3.h>

#include "fkelectron_2016_2017_2018.h"
#include "fkmuon_2016_2017_2018.h"
#include "PU_reWeighting.h"
//#include "turnonEle_all.C"

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
    isTag                 = 0 ;
    isHeep_offline        = 0 ;
    isHeep_online         = 0 ;
    isfake                = 0 ;
  }
 
  void apply_ID_value(float value_dPhiIn, float value_Sieie, float value_missingHits, float value_dxyFirstPV, float value_HOverE, float value_caloEnergy, float value_E1x5OverE5x5, float value_E2x5OverE5x5, float value_isolEMHadDepth1, float value_IsolPtTrks, float value_EcalDriven, float value_dEtaIn, float rho, bool isFake){
//    bool accept_HOverE = true ;
//    if     (region==1){ accept_HOverE = value_HOverE < 0.05 + 1.0/value_caloEnergy ; }
//    else if(region==3){ accept_HOverE = value_HOverE < 0.05 + 5.0/value_caloEnergy ; }
//    bool accept_E1x5OverE5x5  = value_E1x5OverE5x5 > 0.83 ;
//    bool accept_E2x5OverE5x5  = value_E2x5OverE5x5 > 0.94 ;
//    bool accept_showershape   = (accept_E1x5OverE5x5 || accept_E2x5OverE5x5) ;
//    if(region!=1) accept_showershape = true ;
//    bool accept_Sieie = value_Sieie < 0.03;
//    if(region!=3) accept_Sieie = true;
////    bool accept_EcalDriven = 1 ;
//    bool accept_EcalDriven = value_EcalDriven == 1.0 ? 1 : 0 ;
//    bool accept_dEtaIn = (fabs(value_dEtaIn) < 0.004 && region==1) || (fabs(value_dEtaIn) < 0.006 && region==3) ? 1 : 0 ;
//    bool accept_dPhiIn = (fabs(value_dPhiIn) < 0.06 && region==1) || (fabs(value_dPhiIn) < 0.06 && region==3) ? 1 : 0 ;
////    bool accept_dPhiIn = true;
//    bool accept_isolEMHadDepth1 = true;
//    if     (region==1) accept_isolEMHadDepth1 = value_isolEMHadDepth1 < 2+ 0.03*Et + 0.28*rho;
//    else if(region==3) accept_isolEMHadDepth1 = ( ((value_isolEMHadDepth1 < 2.5 + 0.28*rho) && Et<50) || ((value_isolEMHadDepth1 < 2.5 + 0.03*(Et-50) + 0.28*rho) && Et>50) ) ? 1 : 0 ;
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

    accept_heep_ID = isHeep_online;
    isHeep_offline = ((region==1||region==3) && Et>35 && accept_heep_ID && pass_trigger ) ? 1 : 0 ;
    if (((region==1||region==3) && Et>35 && !accept_heep_ID && pass_trigger ))
    {
        if((region ==1) && (value_Sieie < 0.013) && (value_HOverE < 0.15) && (value_missingHits < 2) && (value_dxyFirstPV < 0.02) )
        {
            isfake = 1;
        }
        if((region ==3) && (value_Sieie < 0.034) && (value_HOverE < 0.10) && (value_missingHits < 2) && (value_dxyFirstPV < 0.05) )
        {
            isfake = 1;
        }
    }
    isTag = isFake? isfake : isHeep_offline ;
    //if(isTag)
    //{
    //  cout<<" # Heep got "<<endl;
    //  cout<<" # isFake :  "<<isFake<<endl;
    //}
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
  int pass_TkMu100 ;
  int pass_Photon175 ;
  int pass_Ele115 ;

  
  int accept_core_ID        ;
  int accept_isolation      ;
  int accept_heep_ID         ;
  int accept_noDEtaIn_ID    ;
  int accept_EcalDriven_ID  ;
  int accept_noIsolation_ID ;
  int accept_nominal_ID     ;
  int isTag                 ;


  bool passed  ; 
  bool passed_muon  ; 
  bool passed_fake  ; 
  bool highPT_MuID  ; 
  bool fake_MuID  ; 
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
    fake_MuID = false ;
    passed = false ;
    passed_muon = false ;
    passed_fake = false ;
    pass_trigger = false ;
    typ = 0 ;
    pass_Mu50 = false ;
    pass_TkMu100 = false ;
    pass_Photon175 = false ;
    pass_Ele115 = false ;
    muon_isBad = false ;
    muon_isHighPtMuon = false ;
    muon_isGlobalMuon = false ;
  }
  void highPT_MuId(bool isTrackerMuon, bool isGlobalMuon, float dz_in, float dxy_in, float ptError_in,int numberOfMatchedStations,int numberOfValidPixelHits,int trackerLayersWithMeasurement,int numberOfValidMuonHits , float isoR03sumpt , bool Fake){
//    printf("typ : %d ,  dz : %f , dxy : %f , ptratio : %f , Pt : %f\n", typ_in,fabs(dz_in),fabs(dxy_in),ptError_in/pt,pt);
//     if (isGlobalMuon && (numberOfMatchedStations>1) && (numberOfValidPixelHits>0) && (trackerLayersWithMeasurement>5) && (numberOfValidMuonHits>0))
//     {
//        if ((fabs(dz_in) < 0.5) && (fabs(dxy_in)<0.2) &&(ptError_in/pt < 0.3))
//        {
//            highPT_MuID = true ;
//        }
//     }
     highPT_MuID = muon_isHighPtMuon;
     if (highPT_MuID && (pt >= 53.0) && (fabs(eta)<2.4) && (isoR03sumpt/pt < 0.1) )
     {
        passed_muon = true ;
     }
     if (Fake && !passed_muon)
     {
        //pass_trigger = pass_Mu50 == 1;// || pass_TkMu100 == 1;
        if (isGlobalMuon && isTrackerMuon && (trackerLayersWithMeasurement>5) && (numberOfValidMuonHits>0))
        {
           if ((fabs(dz_in) < 1.0) && (fabs(dxy_in)<0.2))
           {
               fake_MuID = true ;
           }
        }
        if (fake_MuID && (pt >= 53.0) && (fabs(eta)<2.4) && pass_trigger)
        {
           passed_fake = true ;
        }
     }
     passed = Fake?passed_fake:passed_muon;
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
        Z_accepted = 1 ;
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
  	if (pt>30 && fabs(eta)<2.4 && isLoose)
  	{
  		passed = 1;
  		if (jet_CSVv2 > 0.8484)
  		{
  			isbjet = 1;
  		}
  	}
  }
};

float top_reweighting_uncertainty(float top_pt_in){
  float weight = 0.0;
  if (top_pt_in < 0.0) {
    weight = 0.0;
  } else if (top_pt_in < 150.0) {
    weight = 0.045;
  } else if (top_pt_in < 1000.0) {
    weight = 0.04 * top_pt_in/1000.0 + 0.045;
  } else if (top_pt_in < 1100.0) {
    weight = 0.09;
  } else if (top_pt_in < 1200.0) {
    weight = 0.1;
  } else if (top_pt_in < 1400.0) {
    weight = 0.12;
  } else if (top_pt_in < 1600.0) {
    weight = 0.14;
  } else if (top_pt_in < 1800.0) {
    weight = 0.155;
  } else if (top_pt_in < 2000.0) {
    weight = 0.18;
  } else if (top_pt_in < 2200.0) {
    weight = 0.2;
  } else if (top_pt_in < 2600.0) {
    weight = 0.243;
  } else if (top_pt_in < 3000.0) {
    weight = 0.34;
  } else if (top_pt_in > 2999.9) {
    weight = 0.34;
  }
  return weight;
}


bool IIHENtuples::Loop(){
   if (fChain == 0) return false;

   vector <float> jet_pt_out ;
   vector <float> jet_energy_out ;
   vector <float> jet_px_out ;
   vector <float> jet_py_out ;
   vector <float> jet_pz_out ;
   vector <float> jet_eta_out ;
   vector <float> jet_phi_out ;
   vector <int> jet_passed_out ;
   vector <int> jet_isbjet_out ;

   // Setup the trigger for changing data structures.

    n_jet = 0;
    n_bjet = 0;
    pass_lepton_veto = 0;

    vector <float>().swap(jet_pt_out) ;
    vector <float>().swap(jet_energy_out) ;
    vector <float>().swap(jet_px_out) ;
    vector <float>().swap(jet_py_out) ;
    vector <float>().swap(jet_pz_out) ;
    vector <float>().swap(jet_eta_out) ;
    vector <float>().swap(jet_phi_out) ;
    vector <int>().swap(jet_passed_out) ;
    vector <int>().swap(jet_isbjet_out) ;
      
    w_top = 1.0 ;
    w_ts1_up = 1.0 ;
    w_ts1_down = 1.0 ;
    w_top_PDF_up = 1.0 ;
    w_top_PDF_down = 1.0 ;
    w_top_Qscale_up = 1.0 ;
    w_top_Qscale_down = 1.0 ;
    w_other = 1.0 ;
    w_fake = 1.0 ;
    w_WW_up = 1.0 ; 
    w_WW_down = 1.0 ;

    gen_mass = -1.0 ;
    gen_leading_pt = -1.0 ;
    gen_subleading_pt = -1.0 ;

    ele_MC_matched = false ;
    muon_MC_matched = false ;

    TRandom3 Tr;

    bool find_t1 = false;
    bool find_t2 = false;
    TLorentzVector MC_p4_1(1,0,0,0);
    TLorentzVector MC_p4_2(1,0,0,0);
    if(ttbar_reweight)
    {
      if (LHE_pdgid->size() > 1) {
        for(unsigned iMC=0 ; iMC<LHE_Pt->size() ; ++iMC)
        {
          if( (abs(LHE_pdgid->at(iMC)) == 6) )
          {
            if (!find_t1)
            {
              MC_p4_1.SetPtEtaPhiE(LHE_Pt->at(iMC),LHE_Eta->at(iMC),LHE_Phi->at(iMC),LHE_E->at(iMC)) ;
              find_t1 = true;
            }
            else if (!find_t2)
            {
              MC_p4_2.SetPtEtaPhiE(LHE_Pt->at(iMC),LHE_Eta->at(iMC),LHE_Phi->at(iMC),LHE_E->at(iMC)) ;
              find_t2 = true;
            }
          }
        }
      } else if (mc_pdgId->size() > 1) {
        for(unsigned iMC=0 ; iMC<mc_pt->size() ; ++iMC)
        {
          if( (abs(mc_pdgId->at(iMC)) == 6) )
          {
            if (!find_t1)
            {
              MC_p4_1.SetPtEtaPhiE(mc_pt->at(iMC),mc_eta->at(iMC),mc_phi->at(iMC),mc_energy->at(iMC)) ;
              find_t1 = true;
            }
            else if (!find_t2)
            {
              MC_p4_2.SetPtEtaPhiE(mc_pt->at(iMC),mc_eta->at(iMC),mc_phi->at(iMC),mc_energy->at(iMC)) ;
              find_t2 = true;
            }
          }
        }
      }
      if(find_t1 && find_t2)
      {
        //float tmp_t1 = exp(0.0615-0.0005*MC_p4_1.Pt());
        //float tmp_t2 = exp(0.0615-0.0005*MC_p4_2.Pt());
        float tmp_t1 = exp(-1.08872e+00-(1.19998e-02)*MC_p4_1.Pt())+8.95139e-01;
        float tmp_t2 = exp(-1.08872e+00-(1.19998e-02)*MC_p4_2.Pt())+8.95139e-01;
        float tmp_t1_uncer = top_reweighting_uncertainty(MC_p4_1.Pt());
        float tmp_t2_uncer = top_reweighting_uncertainty(MC_p4_2.Pt());
        w_ts1_up = sqrt(tmp_t1*(1.0 + tmp_t1_uncer)*tmp_t2*(1.0 + tmp_t2_uncer) );
        w_ts1_down = sqrt(tmp_t1*(1.0 - tmp_t1_uncer)*tmp_t2*(1.0 - tmp_t2_uncer) );
        w_top = sqrt(tmp_t1 * tmp_t2);
      }
      // TODO:top shape
    }

    float w_sign = 1.0 ;
    if(!isData) {w_sign = mc_w_sign < 0 ? -1 : 1 ;}

    if(true==isDY){
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
      if(accept==false) return false;
    }


    if(true==isTTbar){
      TLorentzVector MC_p4_1(1,0,0,0);
      TLorentzVector MC_p4_2(1,0,0,0);
      bool accept=true;
      for(unsigned iMC=0 ; iMC<mc_n ; ++iMC){
      if( (abs(mc_pdgId->at(iMC)) != 11 && abs(mc_pdgId->at(iMC)) != 13 && abs(mc_pdgId->at(iMC)) != 15) ) continue;
      MC_p4_1.SetPtEtaPhiM(mc_pt->at(iMC),mc_eta->at(iMC),mc_phi->at(iMC),mc_mass->at(iMC)) ;
      for(unsigned jMC=iMC+1 ; jMC<mc_n ; ++jMC){
      if( (abs(mc_pdgId->at(jMC)) != 11 && abs(mc_pdgId->at(jMC)) != 13 && abs(mc_pdgId->at(jMC)) != 15) ) continue;
      MC_p4_2.SetPtEtaPhiM(mc_pt->at(jMC),mc_eta->at(jMC),mc_phi->at(jMC),mc_mass->at(jMC)) ;
      if(MC_p4_1.DeltaR(MC_p4_2)<0.001) continue;
      if((MC_p4_1+MC_p4_2).M()>Mass_treshold){accept=false; break;}
      }
      if(accept==false) break;
      }
      if(accept==false) return false;
      }

      if(true==isWW){
      TLorentzVector MC_p4_1(1,0,0,0);
      TLorentzVector MC_p4_2(1,0,0,0);
      bool accept=true;

      for(unsigned iMC=0 ; iMC<mc_n ; ++iMC){
      if( (abs(mc_pdgId->at(iMC)) != 11 && abs(mc_pdgId->at(iMC)) != 13 && abs(mc_pdgId->at(iMC)) != 15) ) continue;
      MC_p4_1.SetPtEtaPhiM(mc_pt->at(iMC),mc_eta->at(iMC),mc_phi->at(iMC),mc_mass->at(iMC)) ;
      for(unsigned jMC=iMC+1 ; jMC<mc_n ; ++jMC){
      if( (abs(mc_pdgId->at(jMC)) != 11 && abs(mc_pdgId->at(jMC)) != 13 && abs(mc_pdgId->at(jMC)) != 15) ) continue;
      MC_p4_2.SetPtEtaPhiM(mc_pt->at(jMC),mc_eta->at(jMC),mc_phi->at(jMC),mc_mass->at(jMC)) ;
      if(MC_p4_1.DeltaR(MC_p4_2)<0.001) continue;
      if((MC_p4_1+MC_p4_2).M()>Mass_treshold){accept=false; break;}
      }
      if(accept==false) break;
      }
      if(accept==false) return false;
    }

    Zee_index_out = 0 ;
    heep_index_out = 0 ;
      
    pv_n_out = pv_n ;

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

      w_PU_out       = w_sign*PU_2016::MC_pileup_weight_2016(PU, "nominal");
      w_PU_up_out    = w_sign*PU_2016::MC_pileup_weight_2016(PU, "up");
      w_PU_down_out  = w_sign*PU_2016::MC_pileup_weight_2016(PU, "down");
    }
    std::vector<muon_candidate*> muons ;
    for(unsigned int iMu=0 ; iMu<mu_ibt_pt->size() ; ++iMu){
      //float px = mu_ibt_px->at(iMu);
      //float py = mu_ibt_py->at(iMu);
      //float pz = mu_ibt_pz->at(iMu);
      float pt = mu_ibt_pt->at(iMu) ;
      float eta    = mu_ibt_eta->at(iMu) ;
      float phi    = mu_ibt_phi->at(iMu) ;
      int   charge = mu_ibt_charge->at(iMu) ;
      if(charge < -900)continue;
      muon_candidate* mu = new muon_candidate(pt, eta, phi, charge) ;
      if( (sys_mu_pt_scale_up || sys_mu_pt_scale_down) && !isData)
      {
        //float pt_scale = 0.0;
        float pt_mean = 0.0;
        float pt_err = 0.0;
        if (eta < -2.1){
          if (phi < -2.4){
            pt_mean = -0.39;
            pt_err = 0.046;
          } else if (phi > 2.4){
            pt_mean = 0.15;
            pt_err = 0.063;
          } else {
            pt_mean = -0.38;
            pt_err = 0.09;
          }
        } else if (eta < -1.2){
          if (phi < -2.4){
            pt_mean = -0.039;
            pt_err = 0.032;
          } else if (phi > 2.4){
            pt_mean = -0.11;
            pt_err = 0.029;
          } else {
            pt_mean = -0.041;
            pt_err = 0.03;
          }
        } else if (eta < 0){
             if (phi < -2.4){
                pt_mean = -0.004;
                pt_err = 0.025;
             } else if (phi > 2.4){
                pt_mean = -0.035;
                pt_err = 0.023;
             } else {
                pt_mean = -0.0023;
                pt_err = 0.023;
             }
          } else if (eta < 1.2){
             if (phi < -2.4){
                pt_mean = -0.012;
                pt_err = 0.022;
             } else if (phi > 2.4){
                pt_mean = 0.004;
                pt_err = 0.024;
             } else {
                pt_mean = -0.017;
                pt_err = 0.022;
             }
          } else if (eta < 2.1){
             if (phi < -2.4){
                pt_mean = 0.005;
                pt_err = 0.033;
             } else if (phi > 2.4){
                pt_mean = 0.07;
                pt_err = 0.035;
             } else {
                pt_mean = 0.0036;
                pt_err = 0.039;
             }
          } else {
             if (phi < -2.4){
                pt_mean = -0.24;
                pt_err = 0.078;
             } else if (phi > 2.4){
                pt_mean = -0.092;
                pt_err = 0.075;
             } else {
                pt_mean = -0.12;
                pt_err = 0.061;
             }
          }
//          float rnd = pt_mean;
          float rnd = Tr.Gaus(pt_mean, pt_err);
          int step_n = 5;
          while (fabs(pt_mean-rnd) > pt_err && step_n > 0) {
            rnd = Tr.Gaus(pt_mean, pt_err);
            step_n--;
          }

          float pt_TeV = pt / 1000.0;
          float new_pt = 1000.0 * ( pt_TeV / (1.0 + rnd * pt_TeV / charge) );
          //https://indico.cern.ch/event/750046/contributions/3150921/attachments/1727369/2790733/TrackerAlignment.pdf
          *mu = muon_candidate(new_pt, eta, phi, charge) ;
        }
        else if(sys_mu_pt_res_up && !isData)
        {
          if (fabs(eta) < 1.2) {
            if (pt < 200 ) {
              *mu = muon_candidate(pt*Tr.Gaus(1,0.003), eta, phi, charge) ;
            } else if (pt < 500) {
              *mu = muon_candidate(pt*Tr.Gaus(1,0.005), eta, phi, charge) ;
            } else {
              *mu = muon_candidate(pt*Tr.Gaus(1,0.01), eta, phi, charge) ;
            }
          } else {
            if (pt < 200 ) {
              *mu = muon_candidate(pt*Tr.Gaus(1,0.006), eta, phi, charge) ;
            } else if (pt < 500) {
              *mu = muon_candidate(pt*Tr.Gaus(1,0.01), eta, phi, charge) ;
            } else {
              *mu = muon_candidate(pt*Tr.Gaus(1,0.02), eta, phi, charge) ;
            }
          }
        }

        mu->muon_isHighPtMuon = mu_isHighPtMuon->at(iMu) ;
        mu->muon_isGlobalMuon = mu_isGlobalMuon->at(iMu) ;
        mu->pass_trigger = Muon50_trig_fire || TkMu50_trig_fire;
        //mu->pass_TkMu100 = TkMu100_trig_fire;
        //mu->pass_Photon175 = Photon175_trig_fire;
        //mu->pass_Ele115 = Ele115_trig_fire;
        mu->highPT_MuId(mu_isTrackerMuon->at(iMu),mu_isGlobalMuon->at(iMu),mu_ibt_dz_firstPVtx->at(iMu), mu_ibt_dxy_firstPVtx->at(iMu), mu_ibt_ptError->at(iMu), mu_numberOfMatchedStations->at(iMu),mu_numberOfValidPixelHits->at(iMu), mu_trackerLayersWithMeasurement->at(iMu),mu_numberOfValidMuonHits->at(iMu),mu_isolationR03_sumPt->at(iMu),isFake_mu) ;
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
        return false;
      }
      
      std::vector<electron_candidate*> electrons ;
      for(unsigned int iEl=0 ; iEl<gsf_n ; ++iEl){
        float Et     = gsf_ecalEnergy->at(iEl)*sin(gsf_theta->at(iEl)) ;
        float gsf_eta_in    = gsf_eta->at(iEl) ;
        float gsf_phi_in    = gsf_phi->at(iEl) ;
        float eta    = gsf_sc_eta->at(iEl) ;
        float phi    = gsf_sc_phi->at(iEl) ;
        int   charge = gsf_charge->at(iEl) ;

//        electron_candidate* el = new electron_candidate(Et * egamma::eCorr(ev_run, Et, eta, gsf_r9->at(iEl), 12, !isData), gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        electron_candidate* el = new electron_candidate(Et, gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        float tmp_sc = 0.02;
        if (el->region == 1) {
            tmp_sc = 0.02;
        } else if (el->region == 3) {
            tmp_sc = 0.02;
        }

        if (sys_ele_et_scale_up && !isData)
        {
           *el = electron_candidate(Et * (1.0 + tmp_sc), gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        }  
	      if (sys_ele_et_scale_down && !isData)
        {
           *el = electron_candidate(Et * (1.0 - tmp_sc), gsf_eta_in, gsf_phi_in, eta, phi, charge) ;
        }

        el->pass_trigger = true ;
        el->match_trigger_l1_dou33 = true ;
    
        el->isHeep_online = gsf_isHeepV7->at(iEl);
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
        return false;;
      }
      
      pass_lepton_veto = (electrons.size() == 1 && muons.size() == 1);
      
      float lastIM=0.;
      int flg_z=-1;
      UInt_t i;
      UInt_t j;
      std::vector<Z_pair*> Z_pairs ;
      for(i=0;i<electrons.size();i++)
      {
         electron_candidate* ele = electrons.at(i) ;
         if(false==ele->isTag) continue ;
         for(j=0;j<muons.size();j++)
         {
            muon_candidate* muon = muons.at(j) ;
            if(muon->pt <=5) continue ;
            if(muon->p4.DeltaR(ele->p4) <= 0.1)
            {
              ele->isTag = false;
            }
         }
      }
      for(i=0;i<electrons.size();i++)
      {
         electron_candidate* ele = electrons.at(i) ;
         if(false==ele->isTag) continue ;
         for(j=0;j<muons.size();j++)
         {
            muon_candidate* muon = muons.at(j) ;
            if(false==muon->passed) continue ;
            Z_pair* z = new Z_pair(ele, muon);
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

        return false;
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

      electron_candidate* ele = z->electron ;

      ele_px 	      = ele->p4.Px();
      ele_py 	      = ele->p4.Py();
      ele_pz 	      = ele->p4.Pz();
      ele_Et_out             = ele->Et ;
      ele_eta_out            = ele->eta ;
      ele_phi_out            = ele->phi ;
      ele_Et35_out           = ele->Et35 ;
      ele_Et20_out           = ele->Et20 ;
      ele_charge_out         = ele->charge ;
      ele_region_out         = ele->region ;
      ele_ID_heep_out        = ele->accept_heep_ID ;
      ele_ID_noDEtaIn_out    = ele->accept_noDEtaIn_ID ;
      ele_ID_EcalDriven_out  = ele->accept_EcalDriven_ID ;
      ele_ID_noIsolation_out = ele->accept_noIsolation_ID ;
      ele_ID_nominal_out     = ele->accept_nominal_ID ;
      ele_isFake_out         = ele->isfake ;
      ele_isHeep_online_out  = ele->isHeep_online ;
      ele_isHeep_offline_out = ele->isHeep_offline ;
      ele_truthmatched_out   = ele->truthmatched ;
        

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
      muon_isHighPtMuon = int(muon->muon_isHighPtMuon) ;
      muon_mu_isGlobalMuon = int(muon->muon_isGlobalMuon) ;

      M_emu = (muon->p4+ele->p4).Mag();

      if (year == "2016") {
        if(isFake_e)
        {
          float fr = 0;
          fr = FRE_2016::frFuncData(ele->Et, ele->eta) ;
          w_fake = fr/(1 - fr) ;
        }
        if(isFake_mu)
        {
          w_fake = fkmuon_2016::FRweight(muon->eta, muon->pt) ;
        }
      }
      if (year == "2017") {
        if(isFake_e)
        {
          float fr = 0;
          fr = FRE_2017::frFuncData(ele->Et, ele->eta) ;
          w_fake = fr/(1 - fr) ;
        }
        if(isFake_mu)
        {
          w_fake = fkmuon_2017::FRweight(muon->eta, muon->pt) ;
        }
      }
      if (year == "2018") {
        if(isFake_e)
        {
          float fr = 0;
          fr = FRE_2018::frFuncData(ele->Et, ele->eta, ele->phi, ev_run, isData) ;
          w_fake = fr/(1 - fr) ;
        }
        if(isFake_mu)
        {
          w_fake = fkmuon_2018::FRweight(muon->eta, muon->pt) ;
        }
      }

      n_jet = 0;
      n_bjet = 0;

//MC matching

      if(!isData) {

        TLorentzVector mc_ele_p4(1,0,0,1);
        TLorentzVector mc_muon_p4(1,0,0,1);
        for(unsigned iMC = 0; iMC<mc_n ; ++iMC) {
          if ( (abs(mc_pdgId->at(iMC)) == 11) && ( (abs(mc_status->at(iMC)) == 23) || (abs(mc_status->at(iMC)) == 1) ) ) {
            mc_ele_p4.SetPtEtaPhiM(mc_pt->at(iMC), mc_eta->at(iMC), mc_phi->at(iMC), 0.000511);
            if (mc_ele_p4.DeltaR(ele->p4) < 0.3) {
              ele_MC_matched = true;
              break;
            }
          }
        }
        for(unsigned iMC = 0; iMC<mc_n ; ++iMC) {
          if ( (abs(mc_pdgId->at(iMC)) == 13) && ( (abs(mc_status->at(iMC)) == 23) || (abs(mc_status->at(iMC)) == 1) ) ) {
            mc_muon_p4.SetPtEtaPhiM(mc_pt->at(iMC), mc_eta->at(iMC), mc_phi->at(iMC), 0.10566);
            if (mc_muon_p4.DeltaR(muon->p4) < 0.3) {
              muon_MC_matched = true;
              break;
            }
          }
        }
        if (ele_MC_matched && muon_MC_matched) {
          gen_mass = (mc_ele_p4 + mc_muon_p4).Mag();
          if (mc_ele_p4.Pt()>mc_muon_p4.Pt()) {
            gen_leading_pt = mc_ele_p4.Pt();
            gen_subleading_pt = mc_muon_p4.Pt();
          } else {            
            gen_leading_pt = mc_muon_p4.Pt();
            gen_subleading_pt = mc_ele_p4.Pt();
          }
        }
      } else {
        ele_MC_matched = true;  
        muon_MC_matched = true;
      }
      
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

      ele = NULL;
      muon = NULL;
      delete ele;
      delete muon;
 
//      for (std::vector<jet_candidate*>::iterator it = jets.begin(); it != jets.end(); it ++){
//        if (NULL != *it)
//        { 
//          delete *it;
//          *it = NULL;
//          }
//      }
//      jets.clear() ;
//      jets.swap(jets);


    if(ttbar_reweight)
    {
      w_top_PDF_up = 1.0 ;
      w_top_PDF_down = 1.0 ;
      w_top_Qscale_up = 1.0 ;
      w_top_Qscale_down = 1.0 ;
      float x = M_emu;
      float w_top_PDF = 1.007 + -1.739e-4 * x + 1.383e-7 * x*x;
      w_top_PDF -= 1.0;

      w_top_PDF_up = 1.0 + w_top_PDF;
      w_top_PDF_down = 1.0 - w_top_PDF;

      float w_top_Qscale = 1.007 + -1.238e-5 * x + 9.69e-9 * x*x;
      w_top_Qscale -= 1.0;

      w_top_Qscale_up = 1.0 + w_top_Qscale;
      w_top_Qscale_down = 1.0 - w_top_Qscale;
    }

    w_other *= ev_prefiringweight;
    return (ele_MC_matched && muon_MC_matched);
}