//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun Dec  6 18:36:33 2015 by ROOT version 6.02/05
// from TTree IIHEAnalysis/IIHEAnalysis
// found on file: ../../samples/RunIISpring15DR74/RunIISpring15DR74_ZToEE_50_120_25ns/outfile_1.root
//////////////////////////////////////////////////////////

#ifndef reskim_h
#define reskim_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"

#include <iostream>

//#include "RoccoR.cc"

class reskim {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   ULong_t         ev_event;
   UInt_t          ev_run;
   UInt_t          ev_luminosityBlock;
   UInt_t          ev_time;
   UInt_t          ev_time_unixTime;
   UInt_t          ev_time_microsecondOffset;
   Float_t         ev_fixedGridRhoAll;
   Float_t         ev_fixedGridRhoFastjetAll;
   Float_t         ev_rho_kt6PFJetsForIsolation;
   UInt_t          mc_n;
   Float_t         mc_pdfvariables_weight;
   Float_t         mc_w;
   vector<int>     *mc_index;
   vector<int>     *mc_pdgId;
   vector<int>     *mc_charge;
   vector<int>     *mc_status;
   vector<float>   *mc_mass;
   vector<float>   *mc_px;
   vector<float>   *mc_py;
   vector<float>   *mc_pz;
   vector<float>   *mc_pt;
   vector<float>   *mc_eta;
   vector<float>   *mc_phi;
   vector<float>   *mc_energy;
   vector<unsigned int> *mc_numberOfDaughters;
   vector<unsigned int> *mc_numberOfMothers;
   vector<vector<int> > *mc_mother_index;
   vector<vector<int> > *mc_mother_pdgId;
   vector<vector<float> > *mc_mother_px;
   vector<vector<float> > *mc_mother_py;
   vector<vector<float> > *mc_mother_pz;
   vector<vector<float> > *mc_mother_pt;
   vector<vector<float> > *mc_mother_eta;
   vector<vector<float> > *mc_mother_phi;
   vector<vector<float> > *mc_mother_energy;
   vector<vector<float> > *mc_mother_mass;
   Int_t           mc_trueNumInteractions;
   Int_t           mc_PU_NumInteractions;
   UInt_t          pv_n;
   vector<float>   *pv_x;
   vector<float>   *pv_y;
   vector<float>   *pv_z;
   vector<int>     *pv_isValid;
   vector<float>   *pv_normalizedChi2;
   vector<int>     *pv_ndof;
   vector<int>     *pv_nTracks;
   vector<int>     *pv_totTrackSize;

   vector<float> *LHE_Pt;
   vector<float> *LHE_Eta;
   vector<float> *LHE_Phi;
   vector<float> *LHE_E;
   vector<int> *LHE_pdgid;
   vector<int> *LHE_status;

   vector<float>  *gsf80_energy;
   vector<float>  *gsf80_p;
   vector<float>  *gsf80_pt;
   vector<float>  *gsf80_et;
   vector<float>  *gsf80_caloEnergy;
   vector<float>  *gsf80_hadronicOverEm;
   vector<float>  *gsf80_hcalDepth1OverEcal;
   vector<float>  *gsf80_hcalDepth2OverEcal;
   vector<float>  *gsf80_dr03EcalRecHitSumEt;
   vector<float>  *gsf80_dr03HcalDepth1TowerSumEt;
   vector<float>  *gsf80_ooEmooP;
   vector<float>  *gsf80_eSuperClusterOverP;
   vector<bool>  *gsf80_Loose;
   vector<bool>  *gsf80_Medium;
   vector<bool>  *gsf80_Tight;
   vector<bool>  *gsf80_isHeepV7;
   UInt_t          gsf_n;
   vector<bool>    *gsf_VIDTight;
   vector<int>     *gsf_classification;
   vector<float>   *gsf_energy;
   vector<float>   *gsf_p;
   vector<float>   *gsf_pt;
   vector<float>   *gsf_full5x5_e1x5;
   vector<float>   *gsf_full5x5_e5x5;
   vector<float>   *gsf_full5x5_e2x5Max;
   vector<float>   *gsf_eta;
   vector<float>   *gsf_phi;
   vector<float>   *gsf_theta;
   vector<float>   *gsf_px;
   vector<float>   *gsf_py;
   vector<float>   *gsf_pz;
   vector<float>   *gsf_superClusterEta;
   vector<float>   *gsf_superClusterEnergy;
   vector<float>   *gsf_caloEnergy;
   vector<float>   *gsf_deltaEtaSuperClusterTrackAtVtx;
   vector<float>   *gsf_deltaPhiSuperClusterTrackAtVtx;
   vector<float>   *gsf_hadronicOverEm;
   vector<float>   *gsf_hcalDepth1OverEcal;
   vector<float>   *gsf_hcalDepth2OverEcal;
   vector<float>   *gsf_dr03TkSumPt;
   vector<float>   *gsf_dr03EcalRecHitSumEt;
   vector<float>   *gsf_dr03HcalDepth1TowerSumEt;
   vector<float>   *gsf_dr03HcalDepth2TowerSumEt;
   vector<int>     *gsf_charge;
   vector<float>   *gsf_full5x5_sigmaIetaIeta;
   vector<bool>    *gsf_ecaldrivenSeed;
   vector<int>     *gsf_trackerdrivenSeed;
   vector<int>     *gsf_isEB;
   vector<int>     *gsf_isEE;
   vector<float>   *gsf_deltaEtaSeedClusterTrackAtVtx;
   vector<float>   *gsf_deltaEtaSeedClusterTrackAtCalo;
   vector<float>   *gsf_deltaPhiSeedClusterTrackAtCalo;
   vector<float>   *gsf_ecalEnergy;
   vector<float>   *gsf_eSuperClusterOverP;
   vector<float>   *gsf_dxy;
   vector<float>   *gsf_dxy_beamSpot;
   vector<float>   *gsf_dxy_firstPVtx;
   vector<float>   *gsf_dxyError;
   vector<float>   *gsf_dz;
   vector<float>   *gsf_dz_beamSpot;
   vector<float>   *gsf_dz_firstPVtx;
   vector<float>   *gsf_dzError;
   vector<float>   *gsf_vz;
   vector<int>     *gsf_numberOfValidHits;
   vector<int>     *gsf_nLostInnerHits;
   vector<int>     *gsf_nLostOuterHits;
   vector<int>     *gsf_convFlags;
   vector<float>   *gsf_convDist;
   vector<float>   *gsf_convDcot;
   vector<float>   *gsf_convRadius;
   vector<float>   *gsf_fBrem;
   vector<float>   *gsf_e1x5;
   vector<float>   *gsf_e2x5Max;
   vector<float>   *gsf_e5x5;
   vector<float>   *gsf_r9;
////////////////////////////////////////////
   vector<int>   *gsf_sc_seed_ieta;
   vector<int>   *gsf_sc_seed_iphi;
   vector<int>   *gsf_sc_seed_rawId;
   vector<float> *gsf_sc_energy;
   vector<float> *gsf_sc_rawEnergy;
   vector<float> *gsf_sc_preshowerEnergy;
   vector<float> *gsf_sc_lazyTools_e2x5Right;
   vector<float> *gsf_sc_lazyTools_e2x5Left;
   vector<float> *gsf_sc_lazyTools_e2x5Top;
   vector<float> *gsf_sc_lazyTools_e2x5Bottom;
   vector<float> *gsf_sc_eta;
   vector<float> *gsf_sc_phi;
   vector<float> *gsf_sc_etaWidth;
   vector<float> *gsf_sc_phiWidth;
   vector<float> *gsf_sc_lazyTools_e2x2;
   vector<float> *gsf_sc_lazyTools_e3x3;
   vector<float> *gsf_sc_lazyTools_e4x4;
   vector<float> *gsf_sc_lazyTools_e5x5;
   vector<float> *gsf_sc_lazyTools_e1x3;
   vector<float> *gsf_sc_lazyTools_e3x1;
   vector<float> *gsf_sc_lazyTools_e1x5;
   vector<float> *gsf_sc_lazyTools_e5x1;
   vector<float> *gsf_sc_lazyTools_eMax;
   vector<float> *gsf_sc_lazyTools_e2nd;
   vector<float> *gsf_sc_lazyTools_eLeft;
   vector<float> *gsf_sc_lazyTools_eRight;
   vector<float> *gsf_sc_lazyTools_eTop;
   vector<float> *gsf_sc_lazyTools_eBottom;
////////////////////////////////////////////
   vector<vector<int> > *gsf_hitsinfo;
   vector<float>   *gsf_pixelMatch_dPhi1;
   vector<float>   *gsf_pixelMatch_dPhi2;
   vector<float>   *gsf_pixelMatch_dRz1;
   vector<float>   *gsf_pixelMatch_dRz2;
   vector<int>     *gsf_pixelMatch_subDetector1;
   vector<int>     *gsf_pixelMatch_subDetector2;
   vector<float>   *gsf_mc_bestDR;
   vector<int>     *gsf_mc_index;
   vector<float>   *gsf_mc_ERatio;
   Float_t         MET_caloMet_et;
   Float_t         MET_caloMet_phi;
   Float_t         MET_Et;
   Float_t         MET_phi;
   Float_t         MET_significance;
   Float_t         MET_T1Txy_Pt;
   Float_t         MET_T1Txy_phi;
   Float_t         MET_T1Txy_significance;
   vector<float>   *HEEP_eseffsixix;
   vector<float>   *HEEP_eseffsiyiy;
   vector<float>   *HEEP_eseffsirir;
   vector<float>   *HEEP_preshowerEnergy;
   vector<float>   *HEEP_e1x3;
   vector<float>   *HEEP_eMax;
   vector<float>   *HEEP_e5x5;
   vector<float>   *HEEP_e2x5Right;
   vector<float>   *HEEP_e2x5Left;
   vector<float>   *HEEP_e2x5Top;
   vector<float>   *HEEP_e2x5Bottom;
   vector<float>   *HEEP_eRight;
   vector<float>   *HEEP_eLeft;
   vector<float>   *HEEP_eTop;
   vector<float>   *HEEP_eBottom;
   vector<float>   *HEEP_basicClusterSeedTime;
   vector<int>     *EBHits_rawId;
   vector<int>     *EBHits_iRechit;
   vector<float>   *EBHits_energy;
   vector<int>     *EBHits_ieta;
   vector<int>     *EBHits_iphi;
   vector<int>     *EBHits_RecoFlag;
   vector<int>     *EBHits_kSaturated;
   vector<int>     *EBHits_kLeadingEdgeRecovered;
   vector<int>     *EBHits_kNeighboursRecovered;
   vector<int>     *EBHits_kWeird;
   vector<int>     *EEHits_rawId;
   vector<int>     *EEHits_iRechit;
   vector<float>   *EEHits_energy;
   vector<int>     *EEHits_ieta;
   vector<int>     *EEHits_iphi;
   vector<int>     *EEHits_RecoFlag;
   vector<int>     *EEHits_kSaturated;
   vector<int>     *EEHits_kLeadingEdgeRecovered;
   vector<int>     *EEHits_kNeighboursRecovered;
   vector<int>     *EEHits_kWeird;
   vector<vector<float> > *HEEP_crystal_energy;
   vector<vector<float> > *HEEP_crystal_eta;
   vector<vector<float> > *HEEP_eshitsixix;
   vector<vector<float> > *HEEP_eshitsiyiy;
   vector<vector<int> > *HEEP_crystal_ietaorix;
   vector<vector<int> > *HEEP_crystal_iphioriy;
   vector<int>     *HEEP_cutflow60_Et;
   Int_t           HEEP_cutflow60_Et_n;
   Int_t           HEEP_cutflow60_Et_nCumulative;
   vector<float>   *HEEP_cutflow60_Et_value;
   vector<int>     *HEEP_cutflow60_eta;
   Int_t           HEEP_cutflow60_eta_n;
   Int_t           HEEP_cutflow60_eta_nCumulative;
   vector<float>   *HEEP_cutflow60_eta_value;
   vector<int>     *HEEP_cutflow60_acceptance;
   Int_t           HEEP_cutflow60_acceptance_n;
   vector<int>     *HEEP_cutflow60_EcalDriven;
   Int_t           HEEP_cutflow60_EcalDriven_n;
   Int_t           HEEP_cutflow60_EcalDriven_nCumulative;
   vector<float>   *HEEP_cutflow60_EcalDriven_value;
   vector<int>     *HEEP_cutflow60_dEtaIn;
   Int_t           HEEP_cutflow60_dEtaIn_n;
   Int_t           HEEP_cutflow60_dEtaIn_nCumulative;
   vector<float>   *HEEP_cutflow60_dEtaIn_value;
   vector<int>     *HEEP_cutflow60_dPhiIn;
   Int_t           HEEP_cutflow60_dPhiIn_n;
   Int_t           HEEP_cutflow60_dPhiIn_nCumulative;
   vector<float>   *HEEP_cutflow60_dPhiIn_value;
   vector<int>     *HEEP_cutflow60_HOverE;
   Int_t           HEEP_cutflow60_HOverE_n;
   Int_t           HEEP_cutflow60_HOverE_nCumulative;
   vector<float>   *HEEP_cutflow60_HOverE_value;
   vector<int>     *HEEP_cutflow60_SigmaIetaIeta;
   Int_t           HEEP_cutflow60_SigmaIetaIeta_n;
   Int_t           HEEP_cutflow60_SigmaIetaIeta_nCumulative;
   vector<float>   *HEEP_cutflow60_SigmaIetaIeta_value;
   vector<int>     *HEEP_cutflow60_E1x5OverE5x5;
   Int_t           HEEP_cutflow60_E1x5OverE5x5_n;
   Int_t           HEEP_cutflow60_E1x5OverE5x5_nCumulative;
   vector<float>   *HEEP_cutflow60_E1x5OverE5x5_value;
   vector<int>     *HEEP_cutflow60_E2x5OverE5x5;
   Int_t           HEEP_cutflow60_E2x5OverE5x5_n;
   Int_t           HEEP_cutflow60_E2x5OverE5x5_nCumulative;
   vector<float>   *HEEP_cutflow60_E2x5OverE5x5_value;
   vector<int>     *HEEP_cutflow60_missingHits;
   Int_t           HEEP_cutflow60_missingHits_n;
   Int_t           HEEP_cutflow60_missingHits_nCumulative;
   vector<float>   *HEEP_cutflow60_missingHits_value;
   vector<int>     *HEEP_cutflow60_dxyFirstPV;
   Int_t           HEEP_cutflow60_dxyFirstPV_n;
   Int_t           HEEP_cutflow60_dxyFirstPV_nCumulative;
   vector<float>   *HEEP_cutflow60_dxyFirstPV_value;
   vector<int>     *HEEP_cutflow60_ID;
   Int_t           HEEP_cutflow60_ID_n;
   vector<int>     *HEEP_cutflow60_isolEMHadDepth1;
   Int_t           HEEP_cutflow60_isolEMHadDepth1_n;
   Int_t           HEEP_cutflow60_isolEMHadDepth1_nCumulative;
   vector<float>   *HEEP_cutflow60_isolEMHadDepth1_value;
   vector<int>     *HEEP_cutflow60_IsolPtTrks;
   Int_t           HEEP_cutflow60_IsolPtTrks_n;
   Int_t           HEEP_cutflow60_IsolPtTrks_nCumulative;
   vector<float>   *HEEP_cutflow60_IsolPtTrks_value;
   vector<int>     *HEEP_cutflow60_isolation;
   Int_t           HEEP_cutflow60_isolation_n;
   vector<int>     *HEEP_cutflow60_total;
   Int_t           HEEP_cutflow60_total_n;

   Int_t trig_Mu50_fire ;
   Int_t trig_TkMu50_fire ;
   Int_t trig_Mu30_TkMu11_fire ;
   Int_t trig_Mu27_fire ;
   Int_t trig_TkMu27_fire ;
   Int_t trig_Mu22_fire ;
   Int_t trig_TkMu22_fire ;
   Int_t trig_DouEle33_MW_fire;
   Int_t trig_DouEle33_fire;
   Int_t trig_Ele23_Ele12_fire; 
   Int_t trig_Ele35_fire;        
   Int_t trig_Ele25_fire;        
   Int_t trig_Mu8_Ele23_fire;
   Int_t trig_Mu23_Ele12_fire;
   Int_t trig_Mu17_TkMu8_fire;
   Int_t trig_Mu17_Mu8_fire; 
   vector<float> *trig_dou33_eta ;
   vector<float> *trig_dou33_phi ;
   vector<float> *trig_dou33Et_eta ;
   vector<float> *trig_dou33Et_phi ;
   vector<float> *trig_dou33_unseeded_eta ;
   vector<float> *trig_dou33_unseeded_phi ;
   vector<float> *trig_dou33Et_unseeded_eta ;
   vector<float> *trig_dou33Et_unseeded_phi ;
   vector<float> *trig_ele27_eta_v1 ;
   vector<float> *trig_ele27_phi_v1 ;
   vector<float> *trig_ele27_eta_v2 ;
   vector<float> *trig_ele27_phi_v2 ;
   
   Float_t mc_w_sign ;
 
   vector<int> *mu_numberOfMatchedStations ;
   vector<int> *mu_trackerLayersWithMeasurement ;
   vector<int> *mu_numberOfValidPixelHits ;
   vector<int> *mu_numberOfValidMuonHits ;

   vector<bool> *mu_isBad ;
   vector<bool> *mu_isHighPtMuon ;
   vector<bool> *mu_isGlobalMuon ;
   vector<bool> *mu_isTightMuon ;
   UInt_t trig_Flag_duplicateMuons_accept ;
   UInt_t trig_Flag_badMuons_accept ;
   UInt_t trig_Flag_noBadMuons_accept ;
   UInt_t trig_Flag_HBHENoiseFilter_accept ;
   UInt_t trig_Flag_BadPFMuonFilter_accept ;
   UInt_t trig_Flag_BadChargedCandidateFilter_accept ;
   UInt_t trig_Flag_HBHENoiseIsoFilter_accept ;
   UInt_t trig_Flag_CSCTightHaloFilter_accept ;
   UInt_t trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept ;
   UInt_t trig_Flag_CSCTightHalo2015Filter_accept ;
   UInt_t trig_Flag_globalTightHalo2016Filter_accept ;
   UInt_t trig_Flag_globalSuperTightHalo2016Filter_accept ;
   UInt_t trig_Flag_HcalStripHaloFilter_accept ;
   UInt_t trig_Flag_hcalLaserEventFilter_accept ;
   UInt_t trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept ;
   UInt_t trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept ;
   UInt_t trig_Flag_goodVertices_accept ;
   UInt_t trig_Flag_eeBadScFilter_accept ;
   UInt_t trig_Flag_ecalLaserCorrFilter_accept ;
   UInt_t trig_Flag_trkPOGFilters_accept ;
   UInt_t trig_Flag_chargedHadronTrackResolutionFilter_accept ;
   UInt_t trig_Flag_muonBadTrackFilter_accept ;
   UInt_t trig_Flag_trkPOG_manystripclus53X_accept ;
   UInt_t trig_Flag_trkPOG_toomanystripclus53X_accept ;
   UInt_t trig_Flag_trkPOG_logErrorTooManyClusters_accept ;
   UInt_t trig_Flag_METFilters_accept ;

 
   vector<float> *mu_it_p;
   vector<float> *mu_it_pt;
   vector<float> *mu_it_px;
   vector<float> *mu_it_py;
   vector<float> *mu_it_pz;
   vector<float> *mu_it_eta;
   vector<float> *mu_it_phi;
   vector<int> *mu_it_charge;
   UInt_t mu_it_n;
   vector<float> *mu_it_dz;
   vector<float> *mu_it_dxy;
   vector<float> *mu_it_ptError;
   vector<float> *mu_it_etaError;
   vector<float> *mu_it_phiError;

   vector<float> *mu_gt_p;
   vector<float> *mu_gt_pt;
   vector<float> *mu_gt_px;
   vector<float> *mu_gt_py;
   vector<float> *mu_gt_pz;
   vector<float> *mu_gt_eta;
   vector<float> *mu_gt_phi;
   vector<int> *mu_gt_charge;
   UInt_t mu_n;
   vector<float> *mu_gt_dz;
   vector<float> *mu_gt_dxy;
   vector<float> *mu_gt_dz_firstPVtx;
   vector<float> *mu_gt_dxy_firstPVtx;
   vector<float> *mu_isolationR03_sumPt;
   vector<float> *mu_pfIsoDbCorrected04;
   vector<float> *mu_gt_ptError;
   vector<float> *mu_gt_etaError;
   vector<float> *mu_gt_phiError;
   vector<float> *mu_rochester_sf;
//Jet
   UInt_t jet_n;

   vector<float> *jet_px ;
   vector<float> *jet_py ;
   vector<float> *jet_pz ;
   vector<float> *jet_pt ;
   vector<float> *jet_eta ;
   vector<float> *jet_theta ;
   vector<float> *jet_phi ;
   vector<float> *jet_energy ;
   vector<float> *jet_CSVv2 ;
   vector<float> *jet_BtagSF_loose ;
   vector<float> *jet_BtagSF_medium ;
   vector<float> *jet_BtagSF_tight ;

   vector<bool> *jet_isJetID ;
   vector<bool> *jet_isJetIDLepVeto ;

   // List of branches
   TBranch        *b_ev_event;   //!
   TBranch        *b_ev_run;   //!
   TBranch        *b_ev_luminosityBlock;   //!
   TBranch        *b_ev_time;   //!
   TBranch        *b_ev_time_unixTime;   //!
   TBranch        *b_ev_time_microsecondOffset;   //!
   TBranch        *b_ev_fixedGridRhoAll;   //!
   TBranch        *b_ev_fixedGridRhoFastjetAll;   //!
//   TBranch        *b_ev_rho_kt6PFJetsForIsolation;   //!
   TBranch        *b_mc_n;   //!
//   TBranch        *b_mc_pdfvariables_weight;   //!
//   TBranch        *b_mc_w;   //!
   TBranch        *b_mc_index;   //!
   TBranch        *b_mc_pdgId;   //!
   TBranch        *b_mc_charge;   //!
   TBranch        *b_mc_status;   //!
   TBranch        *b_mc_mass;   //!
   TBranch        *b_mc_px;   //!
   TBranch        *b_mc_py;   //!
   TBranch        *b_mc_pz;   //!
   TBranch        *b_mc_pt;   //!
   TBranch        *b_mc_eta;   //!
   TBranch        *b_mc_phi;   //!
   TBranch        *b_mc_energy;   //!
   TBranch        *b_mc_numberOfDaughters;   //!
   TBranch        *b_mc_numberOfMothers;   //!
   TBranch        *b_mc_mother_index;   //!
   TBranch        *b_mc_mother_pdgId;   //!
   TBranch        *b_mc_mother_px;   //!
   TBranch        *b_mc_mother_py;   //!
   TBranch        *b_mc_mother_pz;   //!
   TBranch        *b_mc_mother_pt;   //!
   TBranch        *b_mc_mother_eta;   //!
   TBranch        *b_mc_mother_phi;   //!
   TBranch        *b_mc_mother_energy;   //!
   TBranch        *b_mc_mother_mass;   //!
   TBranch        *b_mc_trueNumInteractions;   //!
   TBranch        *b_mc_PU_NumInteractions;   //!
   TBranch        *b_pv_n;   //!
   TBranch        *b_pv_x;   //!
   TBranch        *b_pv_y;   //!
   TBranch        *b_pv_z;   //!
   TBranch        *b_pv_isValid;   //!
   TBranch        *b_pv_normalizedChi2;   //!
   TBranch        *b_pv_ndof;   //!
//   TBranch        *b_pv_nTracks;   //!
//   TBranch        *b_pv_totTrackSize;   //!
   TBranch        *b_LHE_Pt;
   TBranch        *b_LHE_Eta;
   TBranch        *b_LHE_Phi;
   TBranch        *b_LHE_E;
   TBranch        *b_LHE_pdgid;
   TBranch        *b_LHE_status;

   TBranch        *b_gsf80_energy;
   TBranch        *b_gsf80_p;
   TBranch        *b_gsf80_pt;
   TBranch        *b_gsf80_et;
   TBranch        *b_gsf80_caloEnergy;
   TBranch        *b_gsf80_hadronicOverEm;
   TBranch        *b_gsf80_hcalDepth1OverEcal;
   TBranch        *b_gsf80_hcalDepth2OverEcal;
   TBranch        *b_gsf80_dr03EcalRecHitSumEt;
   TBranch        *b_gsf80_dr03HcalDepth1TowerSumEt;
   TBranch        *b_gsf80_ooEmooP;
   TBranch        *b_gsf80_eSuperClusterOverP;
   TBranch        *b_gsf80_Loose;
   TBranch        *b_gsf80_Medium;
   TBranch        *b_gsf80_Tight;
   TBranch        *b_gsf80_isHeepV7;
   TBranch        *b_gsf_n;   //!
   TBranch        *b_gsf_VIDTight;
   TBranch        *b_gsf_classification;   //!
   TBranch        *b_gsf_energy;   //!
   TBranch        *b_gsf_p;   //!
   TBranch        *b_gsf_pt;   //!
   TBranch        *b_gsf_full5x5_e1x5;   //!
   TBranch        *b_gsf_full5x5_e5x5;   //!
   TBranch        *b_gsf_full5x5_e2x5Max;   //!
   TBranch        *b_gsf_eta;   //!
   TBranch        *b_gsf_phi;   //!
   TBranch        *b_gsf_theta;   //!
   TBranch        *b_gsf_px;   //!
   TBranch        *b_gsf_py;   //!
   TBranch        *b_gsf_pz;   //!
   TBranch        *b_gsf_superClusterEta;   //!
   TBranch        *b_gsf_superClusterEnergy;   //!
   TBranch        *b_gsf_caloEnergy;   //!
   TBranch        *b_gsf_deltaEtaSuperClusterTrackAtVtx;   //!
   TBranch        *b_gsf_deltaPhiSuperClusterTrackAtVtx;   //!
   TBranch        *b_gsf_hadronicOverEm;   //!
   TBranch        *b_gsf_hcalDepth1OverEcal;   //!
   TBranch        *b_gsf_hcalDepth2OverEcal;   //!
   TBranch        *b_gsf_dr03TkSumPt;   //!
   TBranch        *b_gsf_dr03EcalRecHitSumEt;   //!
   TBranch        *b_gsf_dr03HcalDepth1TowerSumEt;   //!
   TBranch        *b_gsf_dr03HcalDepth2TowerSumEt;   //!
   TBranch        *b_gsf_charge;   //!
   TBranch        *b_gsf_full5x5_sigmaIetaIeta;   //!
   TBranch        *b_gsf_ecaldrivenSeed;   //!
   TBranch        *b_gsf_trackerdrivenSeed;   //!
   TBranch        *b_gsf_isEB;   //!
   TBranch        *b_gsf_isEE;   //!
   TBranch        *b_gsf_deltaEtaSeedClusterTrackAtVtx;
   TBranch        *b_gsf_deltaEtaSeedClusterTrackAtCalo;   //!
   TBranch        *b_gsf_deltaPhiSeedClusterTrackAtCalo;   //!
   TBranch        *b_gsf_ecalEnergy;   //!
   TBranch        *b_gsf_eSuperClusterOverP;   //!
   TBranch        *b_gsf_dxy;   //!
   TBranch        *b_gsf_dxy_beamSpot;   //!
   TBranch        *b_gsf_dxy_firstPVtx;   //!
   TBranch        *b_gsf_dxyError;   //!
   TBranch        *b_gsf_dz;   //!
   TBranch        *b_gsf_dz_beamSpot;   //!
   TBranch        *b_gsf_dz_firstPVtx;   //!
   TBranch        *b_gsf_dzError;   //!
   TBranch        *b_gsf_vz;   //!
   TBranch        *b_gsf_numberOfValidHits;   //!
   TBranch        *b_gsf_nLostInnerHits;   //!
   TBranch        *b_gsf_nLostOuterHits;   //!
   TBranch        *b_gsf_convFlags;   //!
   TBranch        *b_gsf_convDist;   //!
   TBranch        *b_gsf_convDcot;   //!
   TBranch        *b_gsf_convRadius;   //!
   TBranch        *b_gsf_fBrem;   //!
   TBranch        *b_gsf_e1x5;   //!
   TBranch        *b_gsf_e2x5Max;   //!
   TBranch        *b_gsf_e5x5;   //!
   TBranch        *b_gsf_r9;   //!
//////////////////////////////////////////////
   TBranch *b_gsf_sc_seed_ieta;
   TBranch *b_gsf_sc_seed_iphi;
   TBranch *b_gsf_sc_seed_rawId;
   TBranch *b_gsf_sc_energy;
   TBranch *b_gsf_sc_rawEnergy;
   TBranch *b_gsf_sc_preshowerEnergy;
   TBranch *b_gsf_sc_lazyTools_e2x5Right;
   TBranch *b_gsf_sc_lazyTools_e2x5Left;
   TBranch *b_gsf_sc_lazyTools_e2x5Top;
   TBranch *b_gsf_sc_lazyTools_e2x5Bottom;
   TBranch *b_gsf_sc_eta;
   TBranch *b_gsf_sc_phi;
   TBranch *b_gsf_sc_etaWidth;
   TBranch *b_gsf_sc_phiWidth;
   TBranch *b_gsf_sc_lazyTools_e2x2;
   TBranch *b_gsf_sc_lazyTools_e3x3;
   TBranch *b_gsf_sc_lazyTools_e4x4;
   TBranch *b_gsf_sc_lazyTools_e5x5;
   TBranch *b_gsf_sc_lazyTools_e1x3;
   TBranch *b_gsf_sc_lazyTools_e3x1;
   TBranch *b_gsf_sc_lazyTools_e1x5;
   TBranch *b_gsf_sc_lazyTools_e5x1;
   TBranch *b_gsf_sc_lazyTools_eMax;
   TBranch *b_gsf_sc_lazyTools_e2nd;
   TBranch *b_gsf_sc_lazyTools_eLeft;
   TBranch *b_gsf_sc_lazyTools_eRight;
   TBranch *b_gsf_sc_lazyTools_eTop;
   TBranch *b_gsf_sc_lazyTools_eBottom;
///////////////////////////////////////
   TBranch        *b_gsf_hitsinfo;   //!
   TBranch        *b_gsf_pixelMatch_dPhi1;   //!
   TBranch        *b_gsf_pixelMatch_dPhi2;   //!
   TBranch        *b_gsf_pixelMatch_dRz1;   //!
   TBranch        *b_gsf_pixelMatch_dRz2;   //!
   TBranch        *b_gsf_pixelMatch_subDetector1;   //!
   TBranch        *b_gsf_pixelMatch_subDetector2;   //!
   TBranch        *b_gsf_mc_bestDR;   //!
   TBranch        *b_gsf_mc_index;   //!
   TBranch        *b_gsf_mc_ERatio;   //!
//   TBranch        *b_MET_caloMet_et;   //!
//   TBranch        *b_MET_caloMet_phi;   //!
   TBranch        *b_MET_T1Smear_Pt;   //!
   TBranch        *b_MET_T1Smear_phi;   //!
   TBranch        *b_MET_T1Smear_significance;   //!
   TBranch        *b_MET_pfMetMuEGClean_et;   //!
   TBranch        *b_MET_pfMetMuEGClean_phi;   //!
   TBranch        *b_MET_nominal_significance;   //!
   TBranch        *b_MET_T1Txy_Pt;   //!
   TBranch        *b_MET_T1Txy_phi;   //!
   TBranch        *b_MET_T1Txy_significance;   //!
   TBranch        *b_HEEP_eseffsixix;   //!
   TBranch        *b_HEEP_eseffsiyiy;   //!
   TBranch        *b_HEEP_eseffsirir;   //!
   TBranch        *b_HEEP_preshowerEnergy;   //!
   TBranch        *b_HEEP_e1x3;   //!
   TBranch        *b_HEEP_eMax;   //!
   TBranch        *b_HEEP_e5x5;   //!
   TBranch        *b_HEEP_e2x5Right;   //!
   TBranch        *b_HEEP_e2x5Left;   //!
   TBranch        *b_HEEP_e2x5Top;   //!
   TBranch        *b_HEEP_e2x5Bottom;   //!
   TBranch        *b_HEEP_eRight;   //!
   TBranch        *b_HEEP_eLeft;   //!
   TBranch        *b_HEEP_eTop;   //!
   TBranch        *b_HEEP_eBottom;   //!
   TBranch        *b_HEEP_basicClusterSeedTime;   //!
   TBranch        *b_EBHits_rawId;   //!
   TBranch        *b_EBHits_iRechit;   //!
   TBranch        *b_EBHits_energy;   //!
   TBranch        *b_EBHits_ieta;   //!
   TBranch        *b_EBHits_iphi;   //!
   TBranch        *b_EBHits_RecoFlag;   //!
   TBranch        *b_EBHits_kSaturated;   //!
   TBranch        *b_EBHits_kLeadingEdgeRecovered;   //!
   TBranch        *b_EBHits_kNeighboursRecovered;   //!
   TBranch        *b_EBHits_kWeird;   //!
   TBranch        *b_EEHits_rawId;   //!
   TBranch        *b_EEHits_iRechit;   //!
   TBranch        *b_EEHits_energy;   //!
   TBranch        *b_EEHits_ieta;   //!
   TBranch        *b_EEHits_iphi;   //!
   TBranch        *b_EEHits_RecoFlag;   //!
   TBranch        *b_EEHits_kSaturated;   //!
   TBranch        *b_EEHits_kLeadingEdgeRecovered;   //!
   TBranch        *b_EEHits_kNeighboursRecovered;   //!
   TBranch        *b_EEHits_kWeird;   //!
   TBranch        *b_HEEP_crystal_energy;   //!
   TBranch        *b_HEEP_crystal_eta;   //!
   TBranch        *b_HEEP_eshitsixix;   //!
   TBranch        *b_HEEP_eshitsiyiy;   //!
   TBranch        *b_HEEP_crystal_ietaorix;   //!
   TBranch        *b_HEEP_crystal_iphioriy;   //!
   TBranch        *b_HEEP_cutflow60_Et;   //!
   TBranch        *b_HEEP_cutflow60_Et_n;   //!
   TBranch        *b_HEEP_cutflow60_Et_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_Et_value;   //!
   TBranch        *b_HEEP_cutflow60_eta;   //!
   TBranch        *b_HEEP_cutflow60_eta_n;   //!
   TBranch        *b_HEEP_cutflow60_eta_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_eta_value;   //!
   TBranch        *b_HEEP_cutflow60_acceptance;   //!
   TBranch        *b_HEEP_cutflow60_acceptance_n;   //!
   TBranch        *b_HEEP_cutflow60_EcalDriven;   //!
   TBranch        *b_HEEP_cutflow60_EcalDriven_n;   //!
   TBranch        *b_HEEP_cutflow60_EcalDriven_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_EcalDriven_value;   //!
   TBranch        *b_HEEP_cutflow60_dEtaIn;   //!
   TBranch        *b_HEEP_cutflow60_dEtaIn_n;   //!
   TBranch        *b_HEEP_cutflow60_dEtaIn_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_dEtaIn_value;   //!
   TBranch        *b_HEEP_cutflow60_dPhiIn;   //!
   TBranch        *b_HEEP_cutflow60_dPhiIn_n;   //!
   TBranch        *b_HEEP_cutflow60_dPhiIn_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_dPhiIn_value;   //!
   TBranch        *b_HEEP_cutflow60_HOverE;   //!
   TBranch        *b_HEEP_cutflow60_HOverE_n;   //!
   TBranch        *b_HEEP_cutflow60_HOverE_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_HOverE_value;   //!
   TBranch        *b_HEEP_cutflow60_SigmaIetaIeta;   //!
   TBranch        *b_HEEP_cutflow60_SigmaIetaIeta_n;   //!
   TBranch        *b_HEEP_cutflow60_SigmaIetaIeta_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_SigmaIetaIeta_value;   //!
   TBranch        *b_HEEP_cutflow60_E1x5OverE5x5;   //!
   TBranch        *b_HEEP_cutflow60_E1x5OverE5x5_n;   //!
   TBranch        *b_HEEP_cutflow60_E1x5OverE5x5_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_E1x5OverE5x5_value;   //!
   TBranch        *b_HEEP_cutflow60_E2x5OverE5x5;   //!
   TBranch        *b_HEEP_cutflow60_E2x5OverE5x5_n;   //!
   TBranch        *b_HEEP_cutflow60_E2x5OverE5x5_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_E2x5OverE5x5_value;   //!
   TBranch        *b_HEEP_cutflow60_missingHits;   //!
   TBranch        *b_HEEP_cutflow60_missingHits_n;   //!
   TBranch        *b_HEEP_cutflow60_missingHits_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_missingHits_value;   //!
   TBranch        *b_HEEP_cutflow60_dxyFirstPV;   //!
   TBranch        *b_HEEP_cutflow60_dxyFirstPV_n;   //!
   TBranch        *b_HEEP_cutflow60_dxyFirstPV_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_dxyFirstPV_value;   //!
   TBranch        *b_HEEP_cutflow60_ID;   //!
   TBranch        *b_HEEP_cutflow60_ID_n;   //!
   TBranch        *b_HEEP_cutflow60_isolEMHadDepth1;   //!
   TBranch        *b_HEEP_cutflow60_isolEMHadDepth1_n;   //!
   TBranch        *b_HEEP_cutflow60_isolEMHadDepth1_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_isolEMHadDepth1_value;   //!
   TBranch        *b_HEEP_cutflow60_IsolPtTrks;   //!
   TBranch        *b_HEEP_cutflow60_IsolPtTrks_n;   //!
   TBranch        *b_HEEP_cutflow60_IsolPtTrks_nCumulative;   //!
   TBranch        *b_HEEP_cutflow60_IsolPtTrks_value;   //!
   TBranch        *b_HEEP_cutflow60_isolation;   //!
   TBranch        *b_HEEP_cutflow60_isolation_n;   //!
   TBranch        *b_HEEP_cutflow60_total;   //!
   TBranch        *b_HEEP_cutflow60_total_n;   //!
   
   TBranch        *b_mc_w_sign;   //!
   
   TBranch *b_trig_Mu27_fire ;
   TBranch *b_trig_TkMu27_fire ;
   TBranch *b_trig_Mu22_fire ;
   TBranch *b_trig_TkMu22_fire ;
   TBranch *b_trig_Mu30_TkMu11_fire ;
   TBranch *b_trig_Mu50_fire ;
   TBranch *b_trig_TkMu50_fire ;
   TBranch *b_trig_DouEle33_MW_fire ;
   TBranch *b_trig_DouEle33_fire ;
   TBranch *b_trig_Ele23_Ele12_fire;        
   TBranch *b_trig_Ele35_fire;        
   TBranch *b_trig_Ele25_fire;        
   TBranch *b_trig_Mu8_Ele23_fire; 
   TBranch *b_trig_Mu23_Ele12_fire;
   TBranch *b_trig_Mu17_TkMu8_fire;
   TBranch *b_trig_Mu17_Mu8_fire; 

   TBranch *b_mu_numberOfMatchedStations;
   TBranch *b_mu_trackerLayersWithMeasurement;
   TBranch *b_mu_numberOfValidPixelHits;
   TBranch *b_mu_numberOfValidMuonHits;

   TBranch *b_mu_isBad ;
   TBranch *b_mu_isHighPtMuon ;
   TBranch *b_mu_isGlobalMuon ;
   TBranch *b_mu_isTightMuon ;
   TBranch *b_trig_Flag_duplicateMuons_accept ;
   TBranch *b_trig_Flag_badMuons_accept ;
   TBranch *b_trig_Flag_noBadMuons_accept ;
   TBranch *b_trig_Flag_HBHENoiseFilter_accept ;
   TBranch *b_trig_Flag_BadPFMuonFilter_accept ;
   TBranch *b_trig_Flag_BadChargedCandidateFilter_accept ;
   TBranch *b_trig_Flag_HBHENoiseIsoFilter_accept ;
   TBranch *b_trig_Flag_CSCTightHaloFilter_accept ;
   TBranch *b_trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept ;
   TBranch *b_trig_Flag_CSCTightHalo2015Filter_accept ;
   TBranch *b_trig_Flag_globalTightHalo2016Filter_accept ;
   TBranch *b_trig_Flag_globalSuperTightHalo2016Filter_accept ;
   TBranch *b_trig_Flag_HcalStripHaloFilter_accept ;
   TBranch *b_trig_Flag_hcalLaserEventFilter_accept ;
   TBranch *b_trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept ;
   TBranch *b_trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept ;
   TBranch *b_trig_Flag_goodVertices_accept ;
   TBranch *b_trig_Flag_eeBadScFilter_accept ;
   TBranch *b_trig_Flag_ecalLaserCorrFilter_accept ;
   TBranch *b_trig_Flag_trkPOGFilters_accept ;
   TBranch *b_trig_Flag_chargedHadronTrackResolutionFilter_accept ;
   TBranch *b_trig_Flag_muonBadTrackFilter_accept ;
   TBranch *b_trig_Flag_trkPOG_manystripclus53X_accept ;
   TBranch *b_trig_Flag_trkPOG_toomanystripclus53X_accept ;
   TBranch *b_trig_Flag_trkPOG_logErrorTooManyClusters_accept ;
   TBranch *b_trig_Flag_METFilters_accept ;

   TBranch *b_mu_it_p;
   TBranch *b_mu_it_pt;
   TBranch *b_mu_it_px;
   TBranch *b_mu_it_py;
   TBranch *b_mu_it_pz;
   TBranch *b_mu_it_eta;
   TBranch *b_mu_it_phi;
   TBranch *b_mu_it_charge;
   TBranch *b_mu_it_n;
   TBranch *b_mu_it_dz;
   TBranch *b_mu_it_dxy;
   TBranch *b_mu_it_ptError;
   TBranch *b_mu_it_etaError;
   TBranch *b_mu_it_phiError;

   TBranch *b_mu_gt_p;
   TBranch *b_mu_gt_pt;
   TBranch *b_mu_gt_px;
   TBranch *b_mu_gt_py;
   TBranch *b_mu_gt_pz;
   TBranch *b_mu_gt_eta;
   TBranch *b_mu_gt_phi;
   TBranch *b_mu_gt_charge;
   TBranch *b_mu_n;
   TBranch *b_mu_gt_dz;
   TBranch *b_mu_gt_dxy;
   TBranch *b_mu_gt_dz_firstPVtx;
   TBranch *b_mu_gt_dxy_firstPVtx;
   TBranch *b_mu_isolationR03_sumPt;
   TBranch *b_mu_pfIsoDbCorrected04;
   TBranch *b_mu_gt_ptError;
   TBranch *b_mu_gt_etaError;
   TBranch *b_mu_gt_phiError;
   TBranch *b_mu_rochester_sf;

   TBranch *b_jet_n;
   TBranch *b_jet_px;
   TBranch *b_jet_py;
   TBranch *b_jet_pz;
   TBranch *b_jet_pt;
   TBranch *b_jet_energy;
   TBranch *b_jet_Smeared_px;
   TBranch *b_jet_Smeared_py;
   TBranch *b_jet_Smeared_pz;
   TBranch *b_jet_Smeared_pt;
   TBranch *b_jet_Smeared_energy;
   TBranch *b_jet_eta;
   TBranch *b_jet_theta;
   TBranch *b_jet_phi;
   TBranch *b_jet_CSVv2;
   TBranch *b_jet_isJetID ;
   TBranch *b_jet_isJetIDLepVeto ;
   TBranch *b_jet_BtagSF_loose ;
   TBranch *b_jet_BtagSF_medium ;
   TBranch *b_jet_BtagSF_tight ;

   bool isData  ;
   bool isDY ;
   bool isZToEE ;
   bool isTTbar ;
   bool isWW ;
   ULong_t No_print ;
   TString mc_str_in;
   TString sys_str_in;
   int triggerVersion ;
   int triggerVersion_singleMuon ;

   float goldenLumi ;
   float silverLumi ;
   float combinedLumi ;

   //RoccoR *rc_;

   reskim(TTree *tree=0, bool isData_in=false, bool isDY_in=false, bool isTTbar_in=false, bool isWW_in=false, ULong_t No_print_in = 0, TString mc_str_in = "", TString sys_str_in = "norminal");
   virtual ~reskim();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TString);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
   virtual bool     Find_branch(TTree *tree, TString branch_name);
};

#endif

#ifdef reskim_cxx
reskim::reskim(TTree *tree, bool isData_in, bool isDY_in, bool isTTbar_in, bool isWW_in, ULong_t No_print_in, TString mc_str_in, TString sys_str_in)
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.

   isData  = isData_in  ;
   isDY = isDY_in ;
   isTTbar = isTTbar_in ;
   isWW = isWW_in ;
   No_print = No_print_in ;
//   rc_  = new RoccoR("rcdata.2016.v3");
   Init(tree);
}

reskim::~reskim()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t reskim::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t reskim::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

bool reskim::Find_branch(TTree *tree, TString branch_name) {
	int i = 0;
	TObjArray *tmp_array = fChain->GetListOfBranches();
	for(i = 0; i<tmp_array->GetEntries(); i++)
	{ 
		if(strstr(tmp_array->At(i)->GetName(), branch_name))
			return true;
	}
	cout<<"Branch : "<<branch_name<<" set failed"<<endl;
	return false;
}

void reskim::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   if (No_print > 0)cout<<"print info of event number : "<<No_print<<endl;
   mc_index = 0;
   mc_pdgId = 0;
   mc_charge = 0;
   mc_status = 0;
   mc_mass = 0;
   mc_px = 0;
   mc_py = 0;
   mc_pz = 0;
   mc_pt = 0;
   mc_eta = 0;
   mc_phi = 0;
   mc_energy = 0;
   mc_numberOfDaughters = 0;
   mc_numberOfMothers = 0;
   mc_mother_index = 0;
   mc_mother_pdgId = 0;
   mc_mother_px = 0;
   mc_mother_py = 0;
   mc_mother_pz = 0;
   mc_mother_pt = 0;
   mc_mother_eta = 0;
   mc_mother_phi = 0;
   mc_mother_energy = 0;
   mc_mother_mass = 0;
   pv_x = 0;
   pv_y = 0;
   pv_z = 0;
   pv_isValid = 0;
   pv_normalizedChi2 = 0;
   pv_ndof = 0;
   pv_nTracks = 0;
   pv_totTrackSize = 0;

   LHE_Pt = 0;
   LHE_Eta = 0;
   LHE_Phi = 0;
   LHE_E = 0;
   LHE_pdgid = 0;
   LHE_status = 0;

   gsf80_energy = 0;
   gsf80_p = 0;
   gsf80_pt = 0;
   gsf80_et = 0;
   gsf80_caloEnergy = 0;
   gsf80_hadronicOverEm = 0;
   gsf80_hcalDepth1OverEcal = 0;
   gsf80_hcalDepth2OverEcal = 0;
   gsf80_dr03EcalRecHitSumEt = 0;
   gsf80_dr03HcalDepth1TowerSumEt = 0;
   gsf80_ooEmooP = 0;
   gsf80_eSuperClusterOverP = 0;
   gsf80_Loose = 0;
   gsf80_Medium = 0;
   gsf80_Tight = 0;
   gsf80_isHeepV7 = 0;
   gsf_VIDTight = 0;
   gsf_classification = 0;
   gsf_energy = 0;
   gsf_p = 0;
   gsf_pt = 0;
   gsf_full5x5_e1x5 = 0;
   gsf_full5x5_e5x5 = 0;
   gsf_full5x5_e2x5Max = 0;
   gsf_eta = 0;
   gsf_phi = 0;
   gsf_theta = 0;
   gsf_px = 0;
   gsf_py = 0;
   gsf_pz = 0;
   gsf_superClusterEta = 0;
   gsf_superClusterEnergy = 0;
   gsf_caloEnergy = 0;
   gsf_deltaEtaSuperClusterTrackAtVtx = 0;
   gsf_deltaPhiSuperClusterTrackAtVtx = 0;
   gsf_hadronicOverEm = 0;
   gsf_hcalDepth1OverEcal = 0;
   gsf_hcalDepth2OverEcal = 0;
   gsf_dr03TkSumPt = 0;
   gsf_dr03EcalRecHitSumEt = 0;
   gsf_dr03HcalDepth1TowerSumEt = 0;
   gsf_dr03HcalDepth2TowerSumEt = 0;
   gsf_charge = 0;
   gsf_full5x5_sigmaIetaIeta = 0;
   gsf_ecaldrivenSeed = 0;
   gsf_trackerdrivenSeed = 0;
   gsf_isEB = 0;
   gsf_isEE = 0;
   gsf_deltaEtaSeedClusterTrackAtVtx  = 0;
   gsf_deltaEtaSeedClusterTrackAtCalo = 0;
   gsf_deltaPhiSeedClusterTrackAtCalo = 0;
   gsf_ecalEnergy = 0;
   gsf_eSuperClusterOverP = 0;
   gsf_dxy = 0;
   gsf_dxy_beamSpot = 0;
   gsf_dxy_firstPVtx = 0;
   gsf_dxyError = 0;
   gsf_dz = 0;
   gsf_dz_beamSpot = 0;
   gsf_dz_firstPVtx = 0;
   gsf_dzError = 0;
   gsf_vz = 0;
   gsf_numberOfValidHits = 0;
   gsf_nLostInnerHits = 0;
   gsf_nLostOuterHits = 0;
   gsf_convFlags = 0;
   gsf_convDist = 0;
   gsf_convDcot = 0;
   gsf_convRadius = 0;
   gsf_fBrem = 0;
   gsf_e1x5 = 0;
   gsf_e2x5Max = 0;
   gsf_e5x5 = 0;
   gsf_r9 = 0;
   gsf_sc_seed_ieta = 0;
   gsf_sc_seed_iphi = 0;
   gsf_sc_seed_rawId = 0;
   gsf_sc_energy = 0;
   gsf_sc_rawEnergy = 0;
   gsf_sc_preshowerEnergy = 0;
   gsf_sc_lazyTools_e2x5Right = 0;
   gsf_sc_lazyTools_e2x5Left = 0;
   gsf_sc_lazyTools_e2x5Top = 0;
   gsf_sc_lazyTools_e2x5Bottom = 0;
   gsf_sc_eta = 0;
   gsf_sc_phi = 0;
   gsf_sc_etaWidth = 0;
   gsf_sc_phiWidth = 0;
   gsf_sc_lazyTools_e2x2 = 0;
   gsf_sc_lazyTools_e3x3 = 0;
   gsf_sc_lazyTools_e4x4 = 0;
   gsf_sc_lazyTools_e5x5 = 0;
   gsf_sc_lazyTools_e1x3 = 0;
   gsf_sc_lazyTools_e3x1 = 0;
   gsf_sc_lazyTools_e1x5 = 0;
   gsf_sc_lazyTools_e5x1 = 0;
   gsf_sc_lazyTools_eMax = 0;
   gsf_sc_lazyTools_e2nd = 0;
   gsf_sc_lazyTools_eLeft = 0;
   gsf_sc_lazyTools_eRight = 0;
   gsf_sc_lazyTools_eTop = 0;
   gsf_sc_lazyTools_eBottom = 0;
   gsf_hitsinfo = 0;
   gsf_pixelMatch_dPhi1 = 0;
   gsf_pixelMatch_dPhi2 = 0;
   gsf_pixelMatch_dRz1 = 0;
   gsf_pixelMatch_dRz2 = 0;
   gsf_pixelMatch_subDetector1 = 0;
   gsf_pixelMatch_subDetector2 = 0;
   gsf_mc_bestDR = 0;
   gsf_mc_index = 0;
   gsf_mc_ERatio = 0;
   MET_Et = 0;
   MET_phi = 0;
   MET_significance = 0;
   MET_T1Txy_Pt = 0;
   MET_T1Txy_phi = 0;
   MET_T1Txy_significance = 0;
   HEEP_eseffsixix = 0;
   HEEP_eseffsiyiy = 0;
   HEEP_eseffsirir = 0;
   HEEP_preshowerEnergy = 0;
   HEEP_e1x3 = 0;
   HEEP_eMax = 0;
   HEEP_e5x5 = 0;
   HEEP_e2x5Right = 0;
   HEEP_e2x5Left = 0;
   HEEP_e2x5Top = 0;
   HEEP_e2x5Bottom = 0;
   HEEP_eRight = 0;
   HEEP_eLeft = 0;
   HEEP_eTop = 0;
   HEEP_eBottom = 0;
   HEEP_basicClusterSeedTime = 0;
   EBHits_rawId = 0;
   EBHits_iRechit = 0;
   EBHits_energy = 0;
   EBHits_ieta = 0;
   EBHits_iphi = 0;
   EBHits_RecoFlag = 0;
   EBHits_kSaturated = 0;
   EBHits_kLeadingEdgeRecovered = 0;
   EBHits_kNeighboursRecovered = 0;
   EBHits_kWeird = 0;
   EEHits_rawId = 0;
   EEHits_iRechit = 0;
   EEHits_energy = 0;
   EEHits_ieta = 0;
   EEHits_iphi = 0;
   EEHits_RecoFlag = 0;
   EEHits_kSaturated = 0;
   EEHits_kLeadingEdgeRecovered = 0;
   EEHits_kNeighboursRecovered = 0;
   EEHits_kWeird = 0;
   HEEP_crystal_energy = 0;
   HEEP_crystal_eta = 0;
   HEEP_eshitsixix = 0;
   HEEP_eshitsiyiy = 0;
   HEEP_crystal_ietaorix = 0;
   HEEP_crystal_iphioriy = 0;
   HEEP_cutflow60_Et = 0;
   HEEP_cutflow60_Et_value = 0;
   HEEP_cutflow60_eta = 0;
   HEEP_cutflow60_eta_value = 0;
   HEEP_cutflow60_acceptance = 0;
   HEEP_cutflow60_EcalDriven = 0;
   HEEP_cutflow60_EcalDriven_value = 0;
   HEEP_cutflow60_dEtaIn = 0;
   HEEP_cutflow60_dEtaIn_value = 0;
   HEEP_cutflow60_dPhiIn = 0;
   HEEP_cutflow60_dPhiIn_value = 0;
   HEEP_cutflow60_HOverE = 0;
   HEEP_cutflow60_HOverE_value = 0;
   HEEP_cutflow60_SigmaIetaIeta = 0;
   HEEP_cutflow60_SigmaIetaIeta_value = 0;
   HEEP_cutflow60_E1x5OverE5x5 = 0;
   HEEP_cutflow60_E1x5OverE5x5_value = 0;
   HEEP_cutflow60_E2x5OverE5x5 = 0;
   HEEP_cutflow60_E2x5OverE5x5_value = 0;
   HEEP_cutflow60_missingHits = 0;
   HEEP_cutflow60_missingHits_value = 0;
   HEEP_cutflow60_dxyFirstPV = 0;
   HEEP_cutflow60_dxyFirstPV_value = 0;
   HEEP_cutflow60_ID = 0;
   HEEP_cutflow60_isolEMHadDepth1 = 0;
   HEEP_cutflow60_isolEMHadDepth1_value = 0;
   HEEP_cutflow60_IsolPtTrks = 0;
   HEEP_cutflow60_IsolPtTrks_value = 0;
   HEEP_cutflow60_isolation = 0;
   HEEP_cutflow60_total = 0;
   
   trig_Mu27_fire = 0;
   trig_TkMu27_fire = 0;
   trig_Mu22_fire = 0;
   trig_TkMu22_fire = 0;
   trig_Mu30_TkMu11_fire = 0;
   trig_Mu50_fire = 0;
   trig_TkMu50_fire = 0;
   trig_DouEle33_MW_fire = 0 ;
   trig_DouEle33_fire = 0 ;
   trig_Ele23_Ele12_fire =0 ;   
   trig_Ele35_fire =0 ;
   trig_Ele25_fire =0 ;
   trig_Mu8_Ele23_fire =0 ;
   trig_Mu23_Ele12_fire =0 ;
   trig_Mu17_TkMu8_fire =0 ;
   trig_Mu17_Mu8_fire =0 ;

   mu_numberOfMatchedStations = 0;
   mu_trackerLayersWithMeasurement= 0;
   mu_numberOfValidPixelHits = 0 ;
   mu_numberOfValidMuonHits = 0;

   mu_isBad  = 0 ;
   mu_isHighPtMuon  = 0 ;
   mu_isGlobalMuon  = 0 ;
   mu_isTightMuon = 0 ;
   trig_Flag_duplicateMuons_accept  = 0 ;
   trig_Flag_badMuons_accept  = 0 ;
   
   trig_Flag_BadPFMuonFilter_accept  = 0 ;
   trig_Flag_BadChargedCandidateFilter_accept  = 0 ;
   trig_Flag_HBHENoiseFilter_accept  = 0 ;
   trig_Flag_HBHENoiseIsoFilter_accept  = 0 ;
   trig_Flag_CSCTightHaloFilter_accept  = 0 ;
   trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept  = 0 ;
   trig_Flag_CSCTightHalo2015Filter_accept  = 0 ;
   trig_Flag_globalTightHalo2016Filter_accept  = 0 ;
   trig_Flag_globalSuperTightHalo2016Filter_accept  = 0 ;
   trig_Flag_HcalStripHaloFilter_accept  = 0 ;
   trig_Flag_hcalLaserEventFilter_accept  = 0 ;
   trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept  = 0 ;
   trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept  = 0 ;
   trig_Flag_goodVertices_accept  = 0 ;
   trig_Flag_eeBadScFilter_accept  = 0 ;
   trig_Flag_ecalLaserCorrFilter_accept  = 0 ;
   trig_Flag_trkPOGFilters_accept  = 0 ;
   trig_Flag_chargedHadronTrackResolutionFilter_accept  = 0 ;
   trig_Flag_muonBadTrackFilter_accept  = 0 ;
   trig_Flag_trkPOG_manystripclus53X_accept  = 0 ;
   trig_Flag_trkPOG_toomanystripclus53X_accept  = 0 ;
   trig_Flag_trkPOG_logErrorTooManyClusters_accept  = 0 ;
   trig_Flag_METFilters_accept  = 0 ;

   mu_it_p = 0;
   mu_it_pt = 0;
   mu_it_px = 0;
   mu_it_py = 0;
   mu_it_pz = 0;
   mu_it_eta = 0;
   mu_it_phi = 0;
   mu_it_charge = 0;
   mu_it_n = 0;
   mu_it_dz = 0;
   mu_it_dxy = 0;
   mu_it_ptError = 0;
   mu_it_etaError = 0;
   mu_it_phiError = 0;

   mu_gt_p = 0;
   mu_gt_pt = 0;
   mu_gt_px = 0;
   mu_gt_py = 0;
   mu_gt_pz = 0;
   mu_gt_eta = 0;
   mu_gt_phi = 0;
   mu_gt_charge = 0;
   mu_n = 0;
   mu_gt_dz = 0;
   mu_gt_dxy = 0;
   mu_gt_dz_firstPVtx = 0;
   mu_gt_dxy_firstPVtx = 0;
   mu_isolationR03_sumPt = 0;
   mu_pfIsoDbCorrected04 = 0;
   mu_gt_ptError = 0;
   mu_gt_etaError = 0;
   mu_gt_phiError = 0;
   mu_rochester_sf = 0;

   jet_n = 0 ;
   jet_px = 0 ;
   jet_py = 0 ;
   jet_pz = 0 ;
   jet_pt = 0 ;
   jet_eta = 0 ;
   jet_theta = 0 ;
   jet_phi = 0 ;
   jet_energy = 0 ;

   jet_CSVv2 = 0 ;
   jet_isJetIDLepVeto = 0 ;
   jet_isJetID = 0 ;

   jet_BtagSF_loose = 0 ;
   jet_BtagSF_medium = 0 ;
   jet_BtagSF_tight = 0 ;
 
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);
   
   fChain->SetBranchAddress("ev_event", &ev_event, &b_ev_event);
   fChain->SetBranchAddress("ev_run", &ev_run, &b_ev_run);
   fChain->SetBranchAddress("ev_luminosityBlock", &ev_luminosityBlock, &b_ev_luminosityBlock);
   fChain->SetBranchAddress("ev_time", &ev_time, &b_ev_time);
   fChain->SetBranchAddress("ev_time_unixTime", &ev_time_unixTime, &b_ev_time_unixTime);
   fChain->SetBranchAddress("ev_time_microsecondOffset", &ev_time_microsecondOffset, &b_ev_time_microsecondOffset);
   fChain->SetBranchAddress("ev_fixedGridRhoAll", &ev_fixedGridRhoAll, &b_ev_fixedGridRhoAll);
   fChain->SetBranchAddress("ev_fixedGridRhoFastjetAll", &ev_fixedGridRhoFastjetAll, &b_ev_fixedGridRhoFastjetAll);
//   fChain->SetBranchAddress("ev_rho_kt6PFJetsForIsolation", &ev_rho_kt6PFJetsForIsolation, &b_ev_rho_kt6PFJetsForIsolation);
   if(isData==false){
       fChain->SetBranchAddress("mc_n", &mc_n, &b_mc_n);
//       fChain->SetBranchAddress("mc_pdfvariables_weight", &mc_pdfvariables_weight, &b_mc_pdfvariables_weight);
//       fChain->SetBranchAddress("mc_w", &mc_w, &b_mc_w);
       fChain->SetBranchAddress("mc_index", &mc_index, &b_mc_index);
       fChain->SetBranchAddress("mc_pdgId", &mc_pdgId, &b_mc_pdgId);
       fChain->SetBranchAddress("mc_charge", &mc_charge, &b_mc_charge);
       fChain->SetBranchAddress("mc_status", &mc_status, &b_mc_status);
       fChain->SetBranchAddress("mc_mass", &mc_mass, &b_mc_mass);
       fChain->SetBranchAddress("mc_px", &mc_px, &b_mc_px);
       fChain->SetBranchAddress("mc_py", &mc_py, &b_mc_py);
       fChain->SetBranchAddress("mc_pz", &mc_pz, &b_mc_pz);
       fChain->SetBranchAddress("mc_pt", &mc_pt, &b_mc_pt);
       fChain->SetBranchAddress("mc_eta", &mc_eta, &b_mc_eta);
       fChain->SetBranchAddress("mc_phi", &mc_phi, &b_mc_phi);
       fChain->SetBranchAddress("mc_energy", &mc_energy, &b_mc_energy);
       fChain->SetBranchAddress("mc_numberOfDaughters", &mc_numberOfDaughters, &b_mc_numberOfDaughters);
       fChain->SetBranchAddress("mc_numberOfMothers", &mc_numberOfMothers, &b_mc_numberOfMothers);
       fChain->SetBranchAddress("mc_mother_index", &mc_mother_index, &b_mc_mother_index);
       fChain->SetBranchAddress("mc_mother_pdgId", &mc_mother_pdgId, &b_mc_mother_pdgId);
       fChain->SetBranchAddress("mc_mother_px", &mc_mother_px, &b_mc_mother_px);
       fChain->SetBranchAddress("mc_mother_py", &mc_mother_py, &b_mc_mother_py);
       fChain->SetBranchAddress("mc_mother_pz", &mc_mother_pz, &b_mc_mother_pz);
       fChain->SetBranchAddress("mc_mother_pt", &mc_mother_pt, &b_mc_mother_pt);
       fChain->SetBranchAddress("mc_mother_eta", &mc_mother_eta, &b_mc_mother_eta);
       fChain->SetBranchAddress("mc_mother_phi", &mc_mother_phi, &b_mc_mother_phi);
       fChain->SetBranchAddress("mc_mother_energy", &mc_mother_energy, &b_mc_mother_energy);
       fChain->SetBranchAddress("mc_mother_mass", &mc_mother_mass, &b_mc_mother_mass);
       fChain->SetBranchAddress("mc_trueNumInteractions", &mc_trueNumInteractions, &b_mc_trueNumInteractions);
       fChain->SetBranchAddress("mc_PU_NumInteractions", &mc_PU_NumInteractions, &b_mc_PU_NumInteractions);
       fChain->SetBranchAddress("LHE_Pt", &LHE_Pt,      &b_LHE_Pt);
       fChain->SetBranchAddress("LHE_Eta", &LHE_Eta,    &b_LHE_Eta);
       fChain->SetBranchAddress("LHE_Phi", &LHE_Phi,    &b_LHE_Phi);
       fChain->SetBranchAddress("LHE_E", &LHE_E,        &b_LHE_E);
       fChain->SetBranchAddress("LHE_pdgid", &LHE_pdgid,        &b_LHE_pdgid);
       fChain->SetBranchAddress("LHE_status", &LHE_status,      &b_LHE_status);
   }
   fChain->SetBranchAddress("pv_n", &pv_n, &b_pv_n);
   fChain->SetBranchAddress("pv_x", &pv_x, &b_pv_x);
   fChain->SetBranchAddress("pv_y", &pv_y, &b_pv_y);
   fChain->SetBranchAddress("pv_z", &pv_z, &b_pv_z);
   fChain->SetBranchAddress("pv_isValid", &pv_isValid, &b_pv_isValid);
   fChain->SetBranchAddress("pv_normalizedChi2", &pv_normalizedChi2, &b_pv_normalizedChi2);
   fChain->SetBranchAddress("pv_ndof", &pv_ndof, &b_pv_ndof);
//   fChain->SetBranchAddress("pv_nTracks", &pv_nTracks, &b_pv_nTracks);
//   fChain->SetBranchAddress("pv_totTrackSize", &pv_totTrackSize, &b_pv_totTrackSize);

   fChain->SetBranchAddress("gsf80_energy",  &gsf80_energy,  &b_gsf80_energy);
   fChain->SetBranchAddress("gsf80_p",  &gsf80_p,  &b_gsf80_p);
   fChain->SetBranchAddress("gsf80_pt",  &gsf80_pt,  &b_gsf80_pt);
   fChain->SetBranchAddress("gsf80_et",  &gsf80_et,  &b_gsf80_et);
   fChain->SetBranchAddress("gsf80_caloEnergy",  &gsf80_caloEnergy,  &b_gsf80_caloEnergy);
   fChain->SetBranchAddress("gsf80_hadronicOverEm",  &gsf80_hadronicOverEm,  &b_gsf80_hadronicOverEm);
   fChain->SetBranchAddress("gsf80_hcalDepth1OverEcal",  &gsf80_hcalDepth1OverEcal,  &b_gsf80_hcalDepth1OverEcal);
   fChain->SetBranchAddress("gsf80_hcalDepth2OverEcal",  &gsf80_hcalDepth2OverEcal,  &b_gsf80_hcalDepth2OverEcal);
   fChain->SetBranchAddress("gsf80_dr03EcalRecHitSumEt",  &gsf80_dr03EcalRecHitSumEt,  &b_gsf80_dr03EcalRecHitSumEt);
   fChain->SetBranchAddress("gsf80_dr03HcalDepth1TowerSumEt",  &gsf80_dr03HcalDepth1TowerSumEt,  &b_gsf80_dr03HcalDepth1TowerSumEt);
   fChain->SetBranchAddress("gsf80_ooEmooP",  &gsf80_ooEmooP,  &b_gsf80_ooEmooP);
   fChain->SetBranchAddress("gsf80_eSuperClusterOverP",  &gsf80_eSuperClusterOverP,  &b_gsf80_eSuperClusterOverP);
   fChain->SetBranchAddress("gsf80_Loose",  &gsf80_Loose,  &b_gsf80_Loose);
   fChain->SetBranchAddress("gsf80_Medium",  &gsf80_Medium,  &b_gsf80_Medium);
   fChain->SetBranchAddress("gsf80_Tight",  &gsf80_Tight,  &b_gsf80_Tight);
   fChain->SetBranchAddress("gsf80_isHeepV7",  &gsf80_isHeepV7,  &b_gsf80_isHeepV7);
   fChain->SetBranchAddress("gsf_n", &gsf_n, &b_gsf_n);
   fChain->SetBranchAddress("gsf_VIDTight", &gsf_VIDTight, &b_gsf_VIDTight);
   fChain->SetBranchAddress("gsf_classification", &gsf_classification, &b_gsf_classification);
   fChain->SetBranchAddress("gsf_energy", &gsf_energy, &b_gsf_energy);
   fChain->SetBranchAddress("gsf_p", &gsf_p, &b_gsf_p);
   fChain->SetBranchAddress("gsf_pt", &gsf_pt, &b_gsf_pt);
   fChain->SetBranchAddress("gsf_full5x5_e1x5", &gsf_full5x5_e1x5, &b_gsf_full5x5_e1x5);
   fChain->SetBranchAddress("gsf_full5x5_e5x5", &gsf_full5x5_e5x5, &b_gsf_full5x5_e5x5);
   fChain->SetBranchAddress("gsf_full5x5_e2x5Max", &gsf_full5x5_e2x5Max, &b_gsf_full5x5_e2x5Max);
   fChain->SetBranchAddress("gsf_eta", &gsf_eta, &b_gsf_eta);
   fChain->SetBranchAddress("gsf_phi", &gsf_phi, &b_gsf_phi);
   fChain->SetBranchAddress("gsf_theta", &gsf_theta, &b_gsf_theta);
   fChain->SetBranchAddress("gsf_px", &gsf_px, &b_gsf_px);
   fChain->SetBranchAddress("gsf_py", &gsf_py, &b_gsf_py);
   fChain->SetBranchAddress("gsf_pz", &gsf_pz, &b_gsf_pz);
   fChain->SetBranchAddress("gsf_caloEnergy", &gsf_caloEnergy, &b_gsf_caloEnergy);
   fChain->SetBranchAddress("gsf_deltaEtaSuperClusterTrackAtVtx", &gsf_deltaEtaSuperClusterTrackAtVtx, &b_gsf_deltaEtaSuperClusterTrackAtVtx);
   fChain->SetBranchAddress("gsf_deltaPhiSuperClusterTrackAtVtx", &gsf_deltaPhiSuperClusterTrackAtVtx, &b_gsf_deltaPhiSuperClusterTrackAtVtx);
   fChain->SetBranchAddress("gsf_hadronicOverEm", &gsf_hadronicOverEm, &b_gsf_hadronicOverEm);
   fChain->SetBranchAddress("gsf_hcalDepth1OverEcal", &gsf_hcalDepth1OverEcal, &b_gsf_hcalDepth1OverEcal);
   fChain->SetBranchAddress("gsf_hcalDepth2OverEcal", &gsf_hcalDepth2OverEcal, &b_gsf_hcalDepth2OverEcal);
   fChain->SetBranchAddress("gsf_dr03TkSumPtHEEP7", &gsf_dr03TkSumPt, &b_gsf_dr03TkSumPt);
   fChain->SetBranchAddress("gsf_dr03EcalRecHitSumEt", &gsf_dr03EcalRecHitSumEt, &b_gsf_dr03EcalRecHitSumEt);
   fChain->SetBranchAddress("gsf_dr03HcalDepth1TowerSumEt", &gsf_dr03HcalDepth1TowerSumEt, &b_gsf_dr03HcalDepth1TowerSumEt);
   fChain->SetBranchAddress("gsf_dr03HcalDepth2TowerSumEt", &gsf_dr03HcalDepth2TowerSumEt, &b_gsf_dr03HcalDepth2TowerSumEt);
   fChain->SetBranchAddress("gsf_charge", &gsf_charge, &b_gsf_charge);
   fChain->SetBranchAddress("gsf_full5x5_sigmaIetaIeta", &gsf_full5x5_sigmaIetaIeta, &b_gsf_full5x5_sigmaIetaIeta);
   fChain->SetBranchAddress("gsf_ecaldrivenSeed", &gsf_ecaldrivenSeed, &b_gsf_ecaldrivenSeed);
   fChain->SetBranchAddress("gsf_trackerdrivenSeed", &gsf_trackerdrivenSeed, &b_gsf_trackerdrivenSeed);
   fChain->SetBranchAddress("gsf_isEB", &gsf_isEB, &b_gsf_isEB);
   fChain->SetBranchAddress("gsf_isEE", &gsf_isEE, &b_gsf_isEE);
   fChain->SetBranchAddress("gsf_deltaEtaSeedClusterTrackAtVtx",  &gsf_deltaEtaSeedClusterTrackAtVtx,  &b_gsf_deltaEtaSeedClusterTrackAtVtx);
   fChain->SetBranchAddress("gsf_deltaEtaSeedClusterTrackAtCalo", &gsf_deltaEtaSeedClusterTrackAtCalo, &b_gsf_deltaEtaSeedClusterTrackAtCalo);
   fChain->SetBranchAddress("gsf_deltaPhiSeedClusterTrackAtCalo", &gsf_deltaPhiSeedClusterTrackAtCalo, &b_gsf_deltaPhiSeedClusterTrackAtCalo);
   fChain->SetBranchAddress("gsf_ecalEnergy", &gsf_ecalEnergy, &b_gsf_ecalEnergy);
   fChain->SetBranchAddress("gsf_eSuperClusterOverP", &gsf_eSuperClusterOverP, &b_gsf_eSuperClusterOverP);
   fChain->SetBranchAddress("gsf_dxy", &gsf_dxy, &b_gsf_dxy);
   fChain->SetBranchAddress("gsf_dxy_beamSpot", &gsf_dxy_beamSpot, &b_gsf_dxy_beamSpot);
   fChain->SetBranchAddress("gsf_dxy_firstPVtx", &gsf_dxy_firstPVtx, &b_gsf_dxy_firstPVtx);
   fChain->SetBranchAddress("gsf_dxyError", &gsf_dxyError, &b_gsf_dxyError);
   fChain->SetBranchAddress("gsf_dz", &gsf_dz, &b_gsf_dz);
   fChain->SetBranchAddress("gsf_dz_beamSpot", &gsf_dz_beamSpot, &b_gsf_dz_beamSpot);
   fChain->SetBranchAddress("gsf_dz_firstPVtx", &gsf_dz_firstPVtx, &b_gsf_dz_firstPVtx);
   fChain->SetBranchAddress("gsf_dzError", &gsf_dzError, &b_gsf_dzError);
   fChain->SetBranchAddress("gsf_vz", &gsf_vz, &b_gsf_vz);
   fChain->SetBranchAddress("gsf_numberOfValidHits", &gsf_numberOfValidHits, &b_gsf_numberOfValidHits);
   fChain->SetBranchAddress("gsf_nLostInnerHits", &gsf_nLostInnerHits, &b_gsf_nLostInnerHits);
   fChain->SetBranchAddress("gsf_nLostOuterHits", &gsf_nLostOuterHits, &b_gsf_nLostOuterHits);
   fChain->SetBranchAddress("gsf_convFlags", &gsf_convFlags, &b_gsf_convFlags);
   fChain->SetBranchAddress("gsf_convDist", &gsf_convDist, &b_gsf_convDist);
   fChain->SetBranchAddress("gsf_convDcot", &gsf_convDcot, &b_gsf_convDcot);
   fChain->SetBranchAddress("gsf_convRadius", &gsf_convRadius, &b_gsf_convRadius);
   fChain->SetBranchAddress("gsf_fBrem", &gsf_fBrem, &b_gsf_fBrem);
   fChain->SetBranchAddress("gsf_e1x5", &gsf_e1x5, &b_gsf_e1x5);
   fChain->SetBranchAddress("gsf_e2x5Max", &gsf_e2x5Max, &b_gsf_e2x5Max);
   fChain->SetBranchAddress("gsf_e5x5", &gsf_e5x5, &b_gsf_e5x5);
   fChain->SetBranchAddress("gsf_r9", &gsf_r9, &b_gsf_r9);
   fChain->SetBranchAddress("gsf_sc_energy",               &gsf_sc_energy, &b_gsf_sc_energy);
   fChain->SetBranchAddress("gsf_sc_seed_rawId",           &gsf_sc_seed_rawId, &b_gsf_sc_seed_rawId);
   fChain->SetBranchAddress("gsf_sc_seed_ieta",           &gsf_sc_seed_ieta, &b_gsf_sc_seed_ieta);
   fChain->SetBranchAddress("gsf_sc_seed_iphi",           &gsf_sc_seed_iphi, &b_gsf_sc_seed_iphi);
   fChain->SetBranchAddress("gsf_sc_rawEnergy",            &gsf_sc_rawEnergy, &b_gsf_sc_rawEnergy);
   fChain->SetBranchAddress("gsf_sc_preshowerEnergy",      &gsf_sc_preshowerEnergy, &b_gsf_sc_preshowerEnergy);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e2x5Right",  &gsf_sc_lazyTools_e2x5Right, &b_gsf_sc_lazyTools_e2x5Right);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e2x5Left",   &gsf_sc_lazyTools_e2x5Left, &b_gsf_sc_lazyTools_e2x5Left);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e2x5Top",    &gsf_sc_lazyTools_e2x5Top, &b_gsf_sc_lazyTools_e2x5Top);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e2x5Bottom", &gsf_sc_lazyTools_e2x5Bottom, &b_gsf_sc_lazyTools_e2x5Bottom);
   fChain->SetBranchAddress("gsf_fBrem", &gsf_fBrem, &b_gsf_fBrem);
   fChain->SetBranchAddress("gsf_sc_eta",                  &gsf_sc_eta, &b_gsf_sc_eta);
   fChain->SetBranchAddress("gsf_sc_phi",                  &gsf_sc_phi, &b_gsf_sc_phi);
   fChain->SetBranchAddress("gsf_sc_etaWidth",             &gsf_sc_etaWidth, &b_gsf_sc_etaWidth);
   fChain->SetBranchAddress("gsf_sc_phiWidth",             &gsf_sc_phiWidth, &b_gsf_sc_phiWidth);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e2x2",       &gsf_sc_lazyTools_e2x2, &b_gsf_sc_lazyTools_e2x2);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e3x3",       &gsf_sc_lazyTools_e3x3, &b_gsf_sc_lazyTools_e3x3);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e4x4",       &gsf_sc_lazyTools_e4x4, &b_gsf_sc_lazyTools_e4x4);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e5x5",       &gsf_sc_lazyTools_e5x5, &b_gsf_sc_lazyTools_e5x5);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e1x3",       &gsf_sc_lazyTools_e1x3, &b_gsf_sc_lazyTools_e1x3);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e3x1",       &gsf_sc_lazyTools_e3x1, &b_gsf_sc_lazyTools_e3x1);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e1x5",       &gsf_sc_lazyTools_e1x5, &b_gsf_sc_lazyTools_e1x5);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e5x1",       &gsf_sc_lazyTools_e5x1, &b_gsf_sc_lazyTools_e5x1);
   fChain->SetBranchAddress("gsf_sc_lazyTools_eMax",       &gsf_sc_lazyTools_eMax, &b_gsf_sc_lazyTools_eMax);
   fChain->SetBranchAddress("gsf_sc_lazyTools_e2nd",       &gsf_sc_lazyTools_e2nd, &b_gsf_sc_lazyTools_e2nd);
   fChain->SetBranchAddress("gsf_sc_lazyTools_eLeft",      &gsf_sc_lazyTools_eLeft, &b_gsf_sc_lazyTools_eLeft);
   fChain->SetBranchAddress("gsf_sc_lazyTools_eRight",     &gsf_sc_lazyTools_eRight, &b_gsf_sc_lazyTools_eRight);
   fChain->SetBranchAddress("gsf_sc_lazyTools_eTop",       &gsf_sc_lazyTools_eTop, &b_gsf_sc_lazyTools_eTop);
   fChain->SetBranchAddress("gsf_sc_lazyTools_eBottom",    &gsf_sc_lazyTools_eBottom, &b_gsf_sc_lazyTools_eBottom);

   fChain->SetBranchAddress("gsf_hitsinfo", &gsf_hitsinfo, &b_gsf_hitsinfo);
   fChain->SetBranchAddress("gsf_pixelMatch_dPhi1", &gsf_pixelMatch_dPhi1, &b_gsf_pixelMatch_dPhi1);
   fChain->SetBranchAddress("gsf_pixelMatch_dPhi2", &gsf_pixelMatch_dPhi2, &b_gsf_pixelMatch_dPhi2);
   fChain->SetBranchAddress("gsf_pixelMatch_dRz1", &gsf_pixelMatch_dRz1, &b_gsf_pixelMatch_dRz1);
   fChain->SetBranchAddress("gsf_pixelMatch_dRz2", &gsf_pixelMatch_dRz2, &b_gsf_pixelMatch_dRz2);
   fChain->SetBranchAddress("gsf_pixelMatch_subDetector1", &gsf_pixelMatch_subDetector1, &b_gsf_pixelMatch_subDetector1);
   fChain->SetBranchAddress("gsf_pixelMatch_subDetector2", &gsf_pixelMatch_subDetector2, &b_gsf_pixelMatch_subDetector2);
   fChain->SetBranchAddress("gsf_mc_bestDR", &gsf_mc_bestDR, &b_gsf_mc_bestDR);
   fChain->SetBranchAddress("gsf_mc_index", &gsf_mc_index, &b_gsf_mc_index);
   fChain->SetBranchAddress("gsf_mc_ERatio", &gsf_mc_ERatio, &b_gsf_mc_ERatio);

   if (isData)
   {
      fChain->SetBranchAddress("MET_pfMetMuEGClean_et", &MET_Et, &b_MET_pfMetMuEGClean_et);
      fChain->SetBranchAddress("MET_pfMetMuEGClean_phi", &MET_phi, &b_MET_pfMetMuEGClean_phi);
      fChain->SetBranchAddress("MET_nominal_significance", &MET_significance, &b_MET_nominal_significance);      
   }
   else
   {
      cout<<"use MET MC"<<endl;
      fChain->SetBranchAddress("MET_T1Smear_Pt", &MET_Et, &b_MET_T1Smear_Pt);
      fChain->SetBranchAddress("MET_T1Smear_phi", &MET_phi, &b_MET_T1Smear_phi);      
      fChain->SetBranchAddress("MET_T1Smear_significance", &MET_significance, &b_MET_T1Smear_significance);      
   }
   fChain->SetBranchAddress("MET_T1Txy_Pt", &MET_T1Txy_Pt, &b_MET_T1Txy_Pt);      
   fChain->SetBranchAddress("MET_T1Txy_phi", &MET_T1Txy_phi, &b_MET_T1Txy_phi);      
   fChain->SetBranchAddress("MET_T1Txy_significance", &MET_T1Txy_significance, &b_MET_T1Txy_significance);      


//for muon:
   fChain->SetBranchAddress("mu_it_p", &mu_it_p, &b_mu_it_p);
   fChain->SetBranchAddress("mu_it_px", &mu_it_px, &b_mu_it_px);
   fChain->SetBranchAddress("mu_it_py", &mu_it_py, &b_mu_it_py);
   fChain->SetBranchAddress("mu_it_pz", &mu_it_pz, &b_mu_it_pz);

   fChain->SetBranchAddress("mu_numberOfMatchedStations", &mu_numberOfMatchedStations, &b_mu_numberOfMatchedStations);
   fChain->SetBranchAddress("mu_trackerLayersWithMeasurement", &mu_trackerLayersWithMeasurement, &b_mu_trackerLayersWithMeasurement);
   fChain->SetBranchAddress("mu_numberOfValidPixelHits", &mu_numberOfValidPixelHits, &b_mu_numberOfValidPixelHits);
   fChain->SetBranchAddress("mu_numberOfValidMuonHits", &mu_numberOfValidMuonHits, &b_mu_numberOfValidMuonHits);

   fChain->SetBranchAddress("mu_isHighPtMuon", &mu_isHighPtMuon, &b_mu_isHighPtMuon);
   fChain->SetBranchAddress("mu_isGlobalMuon", &mu_isGlobalMuon, &b_mu_isGlobalMuon);
   fChain->SetBranchAddress("mu_isTightMuon", &mu_isTightMuon, &b_mu_isTightMuon);

   fChain->SetBranchAddress("mu_it_pt", &mu_it_pt, &b_mu_it_pt);
   fChain->SetBranchAddress("mu_it_eta", &mu_it_eta, &b_mu_it_eta);
   fChain->SetBranchAddress("mu_it_phi", &mu_it_phi, &b_mu_it_phi);
   fChain->SetBranchAddress("mu_it_charge", &mu_it_charge, &b_mu_it_charge);
   fChain->SetBranchAddress("mu_it_dz", &mu_it_dz, &b_mu_it_dz);
   fChain->SetBranchAddress("mu_it_dxy", &mu_it_dxy, &b_mu_it_dxy);
   fChain->SetBranchAddress("mu_it_ptError", &mu_it_ptError, &b_mu_it_ptError);
   fChain->SetBranchAddress("mu_it_etaError", &mu_it_etaError, &b_mu_it_etaError);
   fChain->SetBranchAddress("mu_it_phiError", &mu_it_phiError, &b_mu_it_phiError);

   fChain->SetBranchAddress("mu_gt_p", &mu_gt_p, &b_mu_gt_p);
   fChain->SetBranchAddress("mu_gt_px", &mu_gt_px, &b_mu_gt_px);
   fChain->SetBranchAddress("mu_gt_py", &mu_gt_py, &b_mu_gt_py);
   fChain->SetBranchAddress("mu_gt_pz", &mu_gt_pz, &b_mu_gt_pz);

   fChain->SetBranchAddress("mu_gt_pt", &mu_gt_pt, &b_mu_gt_pt);
   fChain->SetBranchAddress("mu_gt_eta", &mu_gt_eta, &b_mu_gt_eta);
   fChain->SetBranchAddress("mu_gt_phi", &mu_gt_phi, &b_mu_gt_phi);
   fChain->SetBranchAddress("mu_gt_charge", &mu_gt_charge, &b_mu_gt_p);
   fChain->SetBranchAddress("mu_n", &mu_n, &b_mu_n);
   fChain->SetBranchAddress("mu_gt_dz", &mu_gt_dz, &b_mu_gt_dz);
   fChain->SetBranchAddress("mu_gt_dxy", &mu_gt_dxy, &b_mu_gt_dxy);
   fChain->SetBranchAddress("mu_gt_dz_firstPVtx", &mu_gt_dz_firstPVtx, &b_mu_gt_dz_firstPVtx);
   fChain->SetBranchAddress("mu_gt_dxy_firstPVtx", &mu_gt_dxy_firstPVtx, &b_mu_gt_dxy_firstPVtx);
   fChain->SetBranchAddress("mu_isolationR03_sumPt", &mu_isolationR03_sumPt, &b_mu_isolationR03_sumPt);
   fChain->SetBranchAddress("mu_pfIsoDbCorrected04", &mu_pfIsoDbCorrected04, &b_mu_pfIsoDbCorrected04);
   fChain->SetBranchAddress("mu_gt_ptError", &mu_gt_ptError, &b_mu_gt_ptError);
   fChain->SetBranchAddress("mu_gt_etaError", &mu_gt_etaError, &b_mu_gt_etaError);
   fChain->SetBranchAddress("mu_gt_phiError", &mu_gt_phiError, &b_mu_gt_phiError);

//   if(!isData)
//   {
//      fChain->SetBranchAddress("mu_rochester_sf", &mu_rochester_sf, &b_mu_rochester_sf);
//   }
  
   if(!isData)
   {
      fChain->SetBranchAddress("mc_w_sign", &mc_w_sign, &b_mc_w_sign);
   }

    if(Find_branch(fChain, "trig_Flag_duplicateMuons_accept"))
    {
       fChain->SetBranchAddress("trig_Flag_duplicateMuons_accept", &trig_Flag_duplicateMuons_accept, &b_trig_Flag_duplicateMuons_accept);
    }
    if(Find_branch(fChain, "trig_Flag_badMuons_accept"))
    {  
       fChain->SetBranchAddress("trig_Flag_badMuons_accept", &trig_Flag_badMuons_accept, &b_trig_Flag_badMuons_accept);
    }
    if(Find_branch(fChain, "trig_Flag_noBadMuons_accept"))
    {  
       fChain->SetBranchAddress("trig_Flag_noBadMuons_accept", &trig_Flag_noBadMuons_accept, &b_trig_Flag_noBadMuons_accept);
    }


   fChain->SetBranchAddress("trig_Flag_BadPFMuonFilter_accept", &trig_Flag_BadPFMuonFilter_accept, &b_trig_Flag_BadPFMuonFilter_accept);
   fChain->SetBranchAddress("trig_Flag_BadChargedCandidateFilter_accept", &trig_Flag_BadChargedCandidateFilter_accept, &b_trig_Flag_BadChargedCandidateFilter_accept);
   fChain->SetBranchAddress("trig_Flag_HBHENoiseFilter_accept", &trig_Flag_HBHENoiseFilter_accept, &b_trig_Flag_HBHENoiseFilter_accept);
   fChain->SetBranchAddress("trig_Flag_HBHENoiseIsoFilter_accept", &trig_Flag_HBHENoiseIsoFilter_accept, &b_trig_Flag_HBHENoiseIsoFilter_accept);
   fChain->SetBranchAddress("trig_Flag_CSCTightHaloFilter_accept", &trig_Flag_CSCTightHaloFilter_accept, &b_trig_Flag_CSCTightHaloFilter_accept);
   fChain->SetBranchAddress("trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept", &trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept, &b_trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept);
   fChain->SetBranchAddress("trig_Flag_CSCTightHalo2015Filter_accept", &trig_Flag_CSCTightHalo2015Filter_accept, &b_trig_Flag_CSCTightHalo2015Filter_accept);
   fChain->SetBranchAddress("trig_Flag_globalTightHalo2016Filter_accept", &trig_Flag_globalTightHalo2016Filter_accept, &b_trig_Flag_globalTightHalo2016Filter_accept);
   fChain->SetBranchAddress("trig_Flag_globalSuperTightHalo2016Filter_accept", &trig_Flag_globalSuperTightHalo2016Filter_accept, &b_trig_Flag_globalSuperTightHalo2016Filter_accept);
   fChain->SetBranchAddress("trig_Flag_HcalStripHaloFilter_accept", &trig_Flag_HcalStripHaloFilter_accept, &b_trig_Flag_HcalStripHaloFilter_accept);
   fChain->SetBranchAddress("trig_Flag_hcalLaserEventFilter_accept", &trig_Flag_hcalLaserEventFilter_accept, &b_trig_Flag_hcalLaserEventFilter_accept);
   fChain->SetBranchAddress("trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept", &trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept, &b_trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept);
   fChain->SetBranchAddress("trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept", &trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept, &b_trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept);
   fChain->SetBranchAddress("trig_Flag_goodVertices_accept", &trig_Flag_goodVertices_accept, &b_trig_Flag_goodVertices_accept);
   fChain->SetBranchAddress("trig_Flag_eeBadScFilter_accept", &trig_Flag_eeBadScFilter_accept, &b_trig_Flag_eeBadScFilter_accept);
   fChain->SetBranchAddress("trig_Flag_ecalLaserCorrFilter_accept", &trig_Flag_ecalLaserCorrFilter_accept, &b_trig_Flag_ecalLaserCorrFilter_accept);
   fChain->SetBranchAddress("trig_Flag_trkPOGFilters_accept", &trig_Flag_trkPOGFilters_accept, &b_trig_Flag_trkPOGFilters_accept);
   fChain->SetBranchAddress("trig_Flag_chargedHadronTrackResolutionFilter_accept", &trig_Flag_chargedHadronTrackResolutionFilter_accept, &b_trig_Flag_chargedHadronTrackResolutionFilter_accept);
   fChain->SetBranchAddress("trig_Flag_muonBadTrackFilter_accept", &trig_Flag_muonBadTrackFilter_accept, &b_trig_Flag_muonBadTrackFilter_accept);
   fChain->SetBranchAddress("trig_Flag_trkPOG_manystripclus53X_accept", &trig_Flag_trkPOG_manystripclus53X_accept, &b_trig_Flag_trkPOG_manystripclus53X_accept);
   fChain->SetBranchAddress("trig_Flag_trkPOG_toomanystripclus53X_accept", &trig_Flag_trkPOG_toomanystripclus53X_accept, &b_trig_Flag_trkPOG_toomanystripclus53X_accept);
   fChain->SetBranchAddress("trig_Flag_trkPOG_logErrorTooManyClusters_accept", &trig_Flag_trkPOG_logErrorTooManyClusters_accept, &b_trig_Flag_trkPOG_logErrorTooManyClusters_accept);
   fChain->SetBranchAddress("trig_Flag_METFilters_accept", &trig_Flag_METFilters_accept, &b_trig_Flag_METFilters_accept);

   if(false==isData){
       cout<<"is MC, use triggers"<<endl ;
   }

	if(Find_branch(fChain, "trig_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_accept"))
	{  
		fChain->SetBranchAddress("trig_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_accept" , &trig_Mu8_Ele23_fire ,  &b_trig_Mu8_Ele23_fire ) ;
	}
	if(Find_branch(fChain, "trig_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_accept"))
	{
		fChain->SetBranchAddress("trig_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_accept", &trig_Mu23_Ele12_fire,  &b_trig_Mu23_Ele12_fire) ;
	} 
	if(Find_branch(fChain, "trig_HLT_Ele35_WPTight_Gsf_accept")) 
	{
		fChain->SetBranchAddress("trig_HLT_Ele35_WPTight_Gsf_accept"    , &trig_Ele35_fire         , &b_trig_Ele35_fire        ) ;
	}  
	if(Find_branch(fChain, "trig_HLT_IsoMu27_accept")) 
	{ 
		fChain->SetBranchAddress("trig_HLT_IsoMu27_accept"    , &trig_Mu27_fire, &b_trig_Mu27_fire) ;
	}
	if(Find_branch(fChain, "trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_accept")) 
	{
		fChain->SetBranchAddress("trig_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_accept"      , &trig_Ele23_Ele12_fire         , &b_trig_Ele23_Ele12_fire        ) ;
	}
	if(Find_branch(fChain, "trig_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_accept"))
	{
		fChain->SetBranchAddress("trig_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_accept"             , &trig_Mu17_TkMu8_fire,  &b_trig_Mu17_TkMu8_fire) ;
	} 




/*
     if(Find_branch(fChain, "trig_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_accept"))
     {
        fChain->SetBranchAddress("trig_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_accept"          , &trig_DouEle33_MW_fire, &b_trig_DouEle33_MW_fire) ;
     } 
     if(Find_branch(fChain, "trig_HLT_Mu30_TkMu11_accept"))
     {
        fChain->SetBranchAddress("trig_HLT_Mu30_TkMu11_accept"    , &trig_Mu30_TkMu11_fire, &b_trig_Mu30_TkMu11_fire) ;
     } 
     if(Find_branch(fChain, "trig_HLT_Mu50_accept"))
     {
        fChain->SetBranchAddress("trig_HLT_Mu50_accept"    , &trig_Mu50_fire, &b_trig_Mu50_fire) ;
     } 
     if(Find_branch(fChain, "trig_HLT_TkMu50_accept"))
     {
        fChain->SetBranchAddress("trig_HLT_TkMu50_accept"    , &trig_TkMu50_fire, &b_trig_TkMu50_fire) ;
     } 
     if(Find_branch(fChain, "trig_HLT_IsoMu22_eta2p1_accept"))
     {
        fChain->SetBranchAddress("trig_HLT_IsoMu22_eta2p1_accept"    , &trig_Mu22_fire, &b_trig_Mu22_fire) ;
     } 
     if(Find_branch(fChain, "trig_HLT_IsoTkMu22_eta2p1_accept"))
     {
        fChain->SetBranchAddress("trig_HLT_IsoTkMu22_eta2p1_accept"    , &trig_TkMu22_fire, &b_trig_TkMu22_fire) ;
     } 
     if(Find_branch(fChain, "trig_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_accept"))
     {
        fChain->SetBranchAddress("trig_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_accept"               , &trig_Mu17_Mu8_fire  ,  &b_trig_Mu17_Mu8_fire  ) ;
     } */


   fChain->SetBranchAddress("jet_n", &jet_n, &b_jet_n)  ;
   if (isData)
   {
      fChain->SetBranchAddress("jet_pt", &jet_pt, &b_jet_pt)  ;
      //fChain->SetBranchAddress("jet_px", &jet_px, &b_jet_px)  ;
      //fChain->SetBranchAddress("jet_py", &jet_py, &b_jet_py)  ;
      //fChain->SetBranchAddress("jet_pz", &jet_pz, &b_jet_pz)  ;
      fChain->SetBranchAddress("jet_energy", &jet_energy, &b_jet_energy)  ;
   }
   else{
      fChain->SetBranchAddress("jet_Smeared_pt", &jet_pt, &b_jet_Smeared_pt)  ;
      //fChain->SetBranchAddress("jet_Smeared_px", &jet_px, &b_jet_Smeared_px)  ;
      //fChain->SetBranchAddress("jet_Smeared_py", &jet_py, &b_jet_Smeared_py)  ;
      //fChain->SetBranchAddress("jet_Smeared_pz", &jet_pz, &b_jet_Smeared_pz)  ;
      fChain->SetBranchAddress("jet_Smeared_energy", &jet_energy, &b_jet_Smeared_energy)  ;
   }
   fChain->SetBranchAddress("jet_eta", &jet_eta, &b_jet_eta)  ;
   fChain->SetBranchAddress("jet_theta", &jet_theta, &b_jet_theta)  ;
   fChain->SetBranchAddress("jet_phi", &jet_phi, &b_jet_phi)  ;
   fChain->SetBranchAddress("jet_DeepCSV", &jet_CSVv2, &b_jet_CSVv2) ;
   fChain->SetBranchAddress("jet_isJetID_2017", &jet_isJetID, &b_jet_isJetID) ;
   fChain->SetBranchAddress("jet_isJetIDLepVeto", &jet_isJetIDLepVeto, &b_jet_isJetIDLepVeto) ;
   
   Notify();
}

Bool_t reskim::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void reskim::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t reskim::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef reskim_cxx
