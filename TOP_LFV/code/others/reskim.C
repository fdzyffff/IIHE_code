#define reskim_cxx
#include "reskim.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TLorentzVector.h>

#include <time.h>
#include <iostream>

//#include "MC_pileup_weight.C"
#include "PU_reWeighting.C"
#include "XYMETCorrection.h"
#include "RoccoR.cc"
#include "BTagCalibrationStandalone.h"

const float m_el = 0.000511 ;
const float m_mu = 0.10566 ;

struct electron_candidate{
  float Et     ;
  float pt     ;
  float sc_eta    ;
  float sc_phi    ;
  float gsf_eta    ;
  float gsf_phi    ;
  float dxy_firstPVtx    ;
  float dz_firstPVtx    ;
  int   charge ;
  int   region ;
  
  int truthmatched  ;
  int pass_trigger  ;
  int match_trigger_l1_dou33 ;
  
  int isLoose;
  int isMedium;
  int isTight;
  int passed;
  int isLeading;

  int accept_core_ID        ;
  int accept_isolation      ;
  int accept_heep_ID         ;
  int accept_noDEtaIn_ID    ;
  int accept_EcalDriven_ID  ;
  int accept_noIsolation_ID ;
  int accept_nominal_ID     ;
  int isTag                 ;
  
  TLorentzVector p4 ;
  TLorentzVector p4_2nd ;
  TLorentzVector p4_sc ;
  
  electron_candidate(float Pt_in, float gsf_eta_in, float gsf_phi_in, float sc_eta_in, float sc_phi_in, int charge_in){
    pt     = Pt_in     ;
    sc_eta    = sc_eta_in    ;
    sc_phi    = sc_phi_in    ;
    gsf_eta    = gsf_eta_in    ;
    gsf_phi    = gsf_phi_in    ;

    dxy_firstPVtx = 0;
    dz_firstPVtx = 0;
    charge = charge_in ;
    
    region = 0 ;
    if     (fabs(sc_eta)<1.4442){ region = 1 ; }
    else if(fabs(sc_eta)<1.566 ){ region = 2 ; }
    else if(fabs(sc_eta)<2.5   ){ region = 3 ; }
    else{ region = 4 ; }
    
    p4.SetPtEtaPhiM(pt, gsf_eta, gsf_phi, m_el) ;
    p4_sc.SetPtEtaPhiM(pt, sc_eta, sc_phi, m_el) ;

    Et = p4.Et();

    truthmatched = 0 ;
    pass_trigger = 0 ;
    match_trigger_l1_dou33 = 0 ;
    
    isLoose = 0;
    isMedium = 0;
    isTight = 0;
    passed = 0;
    accept_core_ID        = 0 ;
    accept_isolation      = 0 ;
    accept_heep_ID        = 0 ;
    accept_noDEtaIn_ID    = 0 ;
    accept_EcalDriven_ID  = 0 ;
    accept_noIsolation_ID = 0 ;
    accept_nominal_ID     = 0 ;
    isTag                 = 0 ;
    isLeading = 0;
    isTight = 0;
  }
  void check_pass()
  {
  	if(fabs(gsf_eta) < 2.4 && (fabs(sc_eta)<=1.4442 || fabs(sc_eta)>=1.566) && pt>20 && isTight)
  	{
		  passed = 1;
    }
  }
};

struct muon_candidate{
  float Et     ;
  float pt     ;
  float pt_old ;
  float px     ;
  float py     ;
  float pz     ;
  float eta    ;
  float phi    ;
  float pfiso04;
  int   charge ;
  int   region ;
  int   typ ;

  
  int isLoose;
  int isMedium;
  int isTight;
  int isLeading;

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
  int isTag                 ;
  int passed  ; 

  bool highPT_MuID  ; 
  bool muon_isBad ;
  bool muon_isHighPtMuon ;
  bool muon_isGlobalMuon ;
 
  TLorentzVector p4 ;
  TLorentzVector p4_2nd ;
  
  muon_candidate(float pt_in, float pt_old_in, float eta_in, float phi_in, int charge_in){
    pt     = pt_in     ;
    pt_old = pt_old_in ;
    eta    = eta_in    ;
    phi    = phi_in    ;
    charge = charge_in ;
    p4.SetPtEtaPhiM(pt, eta, phi, m_mu) ;
    p4_2nd.SetPtEtaPhiM(pt_old, eta, phi, m_mu) ;
    px = p4.Px();
    py = p4.Py();
    pz = p4.Pz();
   
    Et=p4.Et();
 
    region = 0 ;
    if     (fabs(eta)<1.2){ region = 1 ; }
    else if(fabs(eta)<2.4 ){ region = 3 ; }
    else{ region = 4 ; }
    

    highPT_MuID = false ;
    passed = 0 ;
    pass_trigger = false ;
    typ = 0 ;
    pass_Mu50 = false ;
    pass_TkMu50 = false ;
    pass_Photon175 = false ;
    muon_isBad = false ;
    muon_isHighPtMuon = false ;
    muon_isGlobalMuon = false ;
    isLeading = 0;
    isTight = 0;
  }
  void highPT_MuId(bool isGlobalMuon, float dz_in, float dxy_in, float ptError_in,int numberOfMatchedStations,int numberOfValidPixelHits,int trackerLayersWithMeasurement,int numberOfValidMuonHits , float isoR03sumpt ){
     pass_trigger = pass_Mu50 || pass_TkMu50 || pass_Photon175 ;
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
  void meidum()
  {
  }
  void check_pass()
  {
  	if(fabs(eta)<2.4 && pt>20 && isTight && pfiso04 < 0.15)
  	{
  		passed = 1;
  	}
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
  float jet_DeepCSV;
  float BtagSF_loose;
  float BtagSF_medium;
  float BtagSF_tight;
  int   typ ;
  int partonFlavour;

  
  int JetIDLepVeto;
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
    JetIDLepVeto = 0;
  	passed = 0;
  	isbjet = 0;
    jet_DeepCSV = 0;
    BtagSF_loose = 0;
    BtagSF_medium = 0;
    BtagSF_tight = 0;
    p4.SetPtEtaPhiM(pt, eta, phi, 0.0f);
    partonFlavour = -1;
  }
  void check_pass()
  {
  	if (pt>30 && fabs(eta)<2.4 && JetIDLepVeto)
  	{
  		passed = 1;
  		if (jet_DeepCSV > 0.6321) // 2016: 0.6321; 2017: 0.4941; 2018: 0.4184
  		{
  			isbjet = 1;
  		}
  	}
  }
};

struct  Lep_candidate
{
  float pt     ;
  float px     ;
  float py     ;
  float pz     ;
  float eta    ;
  float phi    ;

  int region ;
  int charge ;

  int isE;
  int isMu;
  int isLeading;
  int passed;

  TLorentzVector p4 ;
  TLorentzVector p4_2nd ;
  Lep_candidate()
  {
  	isE = 0;
  	isMu = 0;
  	isLeading = 0;
  	charge = 0;
  	region = 0;
  	passed = 0;
  }
};

void event_fill_ele(Lep_candidate *Lep_in,electron_candidate *ele_in)
{
	Lep_candidate *Lep = Lep_in;
	electron_candidate *ele = ele_in;
	Lep->isE = 1;
	Lep->pt = ele->pt;
	Lep->p4 = ele->p4;
	Lep->eta = ele->sc_eta;
	Lep->phi = ele->sc_phi;
	Lep->charge = ele->charge;
	Lep->region = ele->region;
	Lep->isLeading = ele->isLeading;
	Lep->p4_2nd = ele->p4_2nd;
}

void event_fill_muon(Lep_candidate *Lep_in,muon_candidate *muon_in)
{
	Lep_candidate *Lep = Lep_in;
	muon_candidate *muon = muon_in;
	Lep->isMu = 1;
	Lep->pt = muon->pt;
	Lep->p4 = muon->p4;
	Lep->eta = muon->eta;
	Lep->phi = muon->phi;
	Lep->charge = muon->charge;
	Lep->region = muon->region;
	Lep->isLeading = muon->isLeading;
	Lep->p4_2nd = muon->p4_2nd;
}

float scale_factor( TH2F* h, float X, float Y , TString uncert){
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
  if(x_min < X && X < x_max) binx = Xaxis->FindBin(X);
  else binx= (X<=x_min) ? 1 : NbinsX ;
  if(y_min < Y && Y < y_max) biny = Yaxis->FindBin(Y);
  else biny= (Y<=y_min) ? 1 : NbinsY ;
  if(uncert=="up") return (h->GetBinContent(binx, biny)+h->GetBinError(binx, biny));
  else if(uncert=="down") return (h->GetBinContent(binx, biny)-h->GetBinError(binx, biny));
  else return  h->GetBinContent(binx, biny);
}

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

   std::string rochesterFile;
   std::string btagFile;

  if(year == "2016")    rochesterFile = "input/RoccoR2016.txt";
  if(year == "2017")    rochesterFile = "input/RoccoR2017.txt";
  if(year == "2018")    rochesterFile = "input/RoccoR2018.txt";
  RoccoR  rc(rochesterFile);

  if(year == "2016")    btagFile = "input/DeepCSV_2016LegacySF_V1.csv";
  if(year == "2017")    btagFile = "input/DeepCSV_94XSF_V4_B_F.csv";
  if(year == "2018")    btagFile = "input/DeepCSV_102XSF_V1.csv";

  BTagCalibrationReader reader(BTagEntry::OP_MEDIUM, "central", {"up", "down"});
  if (!isData) {
  	std::cout<<"Loading BTagEntry"<<std::endl;     
  	BTagCalibration calib("DeepCSV",btagFile); 
  	reader.load(calib,BTagEntry::FLAV_B,"comb"); 
  	reader.load(calib,BTagEntry::FLAV_C,"comb");
  	reader.load(calib,BTagEntry::FLAV_UDSG,"comb");
  }

  Double_t ptBins[11] = {30., 40., 60., 80., 100., 150., 200., 300., 400., 500., 1000.};
  Double_t etaBins [4]= {0., 0.6, 1.2, 2.4};
  TH2D *h2_BTaggingEff_Denom_b    = new TH2D("h2_BTaggingEff_Denom_b"   , ";p_{T} [GeV];#eta", 10 , ptBins, 3 , etaBins);
  TH2D *h2_BTaggingEff_Denom_c    = new TH2D("h2_BTaggingEff_Denom_c"   , ";p_{T} [GeV];#eta", 10 , ptBins, 3 , etaBins);
  TH2D *h2_BTaggingEff_Denom_udsg = new TH2D("h2_BTaggingEff_Denom_udsg", ";p_{T} [GeV];#eta", 10 , ptBins, 3 , etaBins);
  TH2D *h2_BTaggingEff_Num_b      = new TH2D("h2_BTaggingEff_Num_b"     , ";p_{T} [GeV];#eta", 10 , ptBins, 3 , etaBins);
  TH2D *h2_BTaggingEff_Num_c      = new TH2D("h2_BTaggingEff_Num_c"     , ";p_{T} [GeV];#eta", 10 , ptBins, 3 , etaBins);
  TH2D *h2_BTaggingEff_Num_udsg   = new TH2D("h2_BTaggingEff_Num_udsg"  , ";p_{T} [GeV];#eta", 10 , ptBins, 3 , etaBins); 

  TH2F  btagEff_b_H;
  TH2F  btagEff_c_H;
  TH2F  btagEff_udsg_H;

  if(!isData){
    TFile *f_btagEff_Map = new TFile("input/btagEff.root");
    if(year == "2016"){
      btagEff_b_H = *(TH2F*)f_btagEff_Map->Get("2016_h2_BTaggingEff_b");
      btagEff_c_H = *(TH2F*)f_btagEff_Map->Get("2016_h2_BTaggingEff_c");
      btagEff_udsg_H = *(TH2F*)f_btagEff_Map->Get("2016_h2_BTaggingEff_udsg");
    }
    if(year == "2017"){
      btagEff_b_H = *(TH2F*)f_btagEff_Map->Get("2017_h2_BTaggingEff_b");
      btagEff_c_H = *(TH2F*)f_btagEff_Map->Get("2017_h2_BTaggingEff_c");
      btagEff_udsg_H = *(TH2F*)f_btagEff_Map->Get("2017_h2_BTaggingEff_udsg");
    }
    if(year == "2018"){
      btagEff_b_H = *(TH2F*)f_btagEff_Map->Get("2018_h2_BTaggingEff_b");
      btagEff_c_H = *(TH2F*)f_btagEff_Map->Get("2018_h2_BTaggingEff_c");
      btagEff_udsg_H = *(TH2F*)f_btagEff_Map->Get("2018_h2_BTaggingEff_udsg");
    }
  }

   if (isTTbar)
   {
      std::cout<<"MC top weight applied"<<std::endl ;
   }
   
   TFile file_out(fname,"RECREATE") ;
   TTree tree_out("tap","Streamlined heep and probe") ;
   

   Int_t final_trig_Mu8_Ele23_fire = 0;
   Int_t final_trig_Mu23_Ele12_fire = 0;
   float PU_true_out = 0;
   float w_PU_down_out = 0;
   float w_PU_up_out = 0;
   float w_PU_out = 0;
   float w_top = 0;
   float w_Btag_loose = 0;
   float w_Btag_medium = 0;
   float w_Btag_tight = 0;
   float w_Btag_offline = 0;

   float P_bjet_data =1;
   float P_bjet_mc =1;
   
   int isPrint = 0;
   float M_ll = 0;
   float Pt_ll = 0;
   float MET_OfflineCorrect_Pt = 0.0;
   float MET_OfflineCorrect_phi = 0.0;
   int n_lep = 0;
   int isEE = 0;
   int isEMu = 0;
   int isMuMu = 0;
   int n_jet = 0;
   int n_bjet = 0;
   int trig_DE33_fire = 0;
   int pass_trigger_EE = 0;
   int pass_trigger_EMu = 0;
   int pass_trigger_MuMu = 0;
   int pass_trigger_EE_step2 = 0;
   int pass_trigger_EMu_step2 = 0;
   int pass_trigger_MuMu_step2 = 0;
   int pass_global = 0;
   int pass_MET_filters = 0;
   int pass_step0=0;
   int pass_step1=0;
   int pass_step2=0;
   int pass_step3=0;
   int pass_step411=0;
   int pass_step412=0;
   int pass_step421=0;
   int pass_step422=0;
   int pass_step43=0;
   int pass_step5=0;

   float leading_pt;
   float leading_px;
   float leading_py;
   float leading_pz;
   float leading_eta;
   float leading_phi;
   float leading_mass;

   float leading_2nd_pt;
   float leading_2nd_px;
   float leading_2nd_py;
   float leading_2nd_pz;
   float leading_2nd_eta;
   float leading_2nd_phi;
   float leading_2nd_mass;

   int leading_charge;
   int leading_region;
   int leading_isE;
   int leading_isMu;
   int leading_isLeading;

   float sub_leading_pt;
   float sub_leading_px;
   float sub_leading_py;
   float sub_leading_pz;
   float sub_leading_eta;
   float sub_leading_phi;
   float sub_leading_mass;

   float sub_leading_2nd_pt;
   float sub_leading_2nd_px;
   float sub_leading_2nd_py;
   float sub_leading_2nd_pz;
   float sub_leading_2nd_eta;
   float sub_leading_2nd_phi;
   float sub_leading_2nd_mass;

   int sub_leading_charge;
   int sub_leading_region;
   int sub_leading_isE;
   int sub_leading_isMu;
   int sub_leading_isLeading;

   vector <float> jet_pt_out ;
   vector <float> jet_energy_out ;
   vector <float> jet_px_out ;
   vector <float> jet_py_out ;
   vector <float> jet_pz_out ;
   vector <float> jet_eta_out ;
   vector <float> jet_phi_out ;
   vector <float> jet_DeepCSV_out ;
   vector <int> jet_IDLoose_out ;

   vector <float> LHE_top_pt;

   tree_out.Branch("ev_event"    , &ev_event    , "ev_event/l"  ) ;
   tree_out.Branch("ev_run"      , &ev_run      , "ev_run/i"    ) ;
   tree_out.Branch("ev_luminosityBlock"    , &ev_luminosityBlock    , "ev_luminosityBlock/i"    ) ;
   tree_out.Branch("ev_fixedGridRhoAll"	,	&ev_fixedGridRhoAll	, "ev_fixedGridRhoAll/F"	) ;

   tree_out.Branch("pv_n"   , &pv_n, "pv_n/I") ;
   tree_out.Branch("PU_true", &PU_true_out , "PU_true/I"  ) ;
   
   tree_out.Branch("w_PU_up"  , &w_PU_up_out    , "w_PU_up/F"   ) ;
   tree_out.Branch("w_PU_down", &w_PU_down_out  , "w_PU_down/F" ) ;
   tree_out.Branch("w_PU"     , &w_PU_out       , "w_PU/F"      ) ;
   tree_out.Branch("w_top"    , &w_top          , "w_top/F"     ) ;

   tree_out.Branch("w_Btag_loose"	  , &w_Btag_loose			, "w_Btag_loose/F"    ) ;
   tree_out.Branch("w_Btag_medium"	  , &w_Btag_medium			, "w_Btag_medium/F"    ) ;
   tree_out.Branch("w_Btag_tight"	  , &w_Btag_tight			, "w_Btag_tight/F"    ) ;
   tree_out.Branch("w_Btag_offline"   , &w_Btag_offline     , "w_Btag_offline/F"    ) ;

   tree_out.Branch("M_ll"		,&M_ll			,"M_ll/F"		);
   tree_out.Branch("Pt_ll"		,&Pt_ll			,"Pt_ll/F"		);
   tree_out.Branch("MET_OfflineCorrect_Pt"   ,&MET_OfflineCorrect_Pt    ,"MET_OfflineCorrect_Pt/F"   );
   tree_out.Branch("MET_OfflineCorrect_phi"    ,&MET_OfflineCorrect_phi   ,"MET_OfflineCorrect_phi/F"    );
   tree_out.Branch("MET_FinalCollection_Pt"		,&MET_FinalCollection_Pt		,"MET_FinalCollection_Pt/F"		);
//   tree_out.Branch("MET_FinalCollection_Px"   ,&MET_FinalCollection_Px    ,"MET_FinalCollection_Px/F"   );
//   tree_out.Branch("MET_FinalCollection_Py"   ,&MET_FinalCollection_Py    ,"MET_FinalCollection_Py/F"   );
   tree_out.Branch("MET_FinalCollection_phi"		,&MET_FinalCollection_phi		,"MET_FinalCollection_phi/F"		);
   tree_out.Branch("MET_FinalCollection_significance"	,&MET_FinalCollection_significance	,"MET_FinalCollection_significance/F"	);
   tree_out.Branch("MET_T1Txy_Pt"		,&MET_T1Txy_Pt			,"MET_T1Txy_Pt/F"		);
   tree_out.Branch("MET_T1Txy_phi"		,&MET_T1Txy_phi			,"MET_T1Txy_phi/F"		);
   tree_out.Branch("MET_T1Txy_significance"	,&MET_T1Txy_significance	,"MET_T1Txy_significance/F"	);
   tree_out.Branch("isEE"		,&isEE			,"isEE/I"		);
   tree_out.Branch("isEMu"		,&isEMu			,"isEMu/I"		);
   tree_out.Branch("isMuMu"		,&isMuMu		,"isMuMu/I"		);
   tree_out.Branch("n_jet"		,&n_jet			,"n_jet/I"		);
   tree_out.Branch("n_bjet"		,&n_bjet		,"n_bjet/I"		);
   tree_out.Branch("n_lep"		,&n_lep			,"n_lep/I"		);

   tree_out.Branch("leading_pt"		,&leading_pt		,"leading_pt/F"		);
   tree_out.Branch("leading_px"		,&leading_px		,"leading_px/F"		);
   tree_out.Branch("leading_py"		,&leading_py		,"leading_py/F"		);
   tree_out.Branch("leading_pz"		,&leading_pz		,"leading_pz/F"		);
   tree_out.Branch("leading_eta"	,&leading_eta		,"leading_eta/F"		);
   tree_out.Branch("leading_phi"	,&leading_phi		,"leading_phi/F"		);
   tree_out.Branch("leading_mass"	,&leading_mass		,"leading_mass/F"		);

   tree_out.Branch("leading_2nd_pt"	,&leading_2nd_pt	,"leading_2nd_pt/F"		);
   tree_out.Branch("leading_2nd_px"	,&leading_2nd_px	,"leading_2nd_px/F"		);
   tree_out.Branch("leading_2nd_py"	,&leading_2nd_py	,"leading_2nd_py/F"		);
   tree_out.Branch("leading_2nd_pz"	,&leading_2nd_pz	,"leading_2nd_pz/F"		);
   tree_out.Branch("leading_2nd_eta"	,&leading_2nd_eta	,"leading_2nd_eta/F"		);
   tree_out.Branch("leading_2nd_phi"	,&leading_2nd_phi	,"leading_2nd_phi/F"		);
   tree_out.Branch("leading_2nd_mass"	,&leading_2nd_mass	,"leading_2nd_mass/F"		);


   tree_out.Branch("leading_charge"	,&leading_charge	,"leading_charge/I"		);
   tree_out.Branch("leading_region"	,&leading_region	,"leading_region/I"		);
   tree_out.Branch("leading_isE"	,&leading_isE		,"leading_isE/I"		);
   tree_out.Branch("leading_isMu"	,&leading_isMu		,"leading_isMu/I"		);
   tree_out.Branch("leading_isLeading"	,&leading_isLeading		,"leading_isLeading/I"		);

   tree_out.Branch("sub_leading_pt"	,&sub_leading_pt	,"sub_leading_pt/F"		);
   tree_out.Branch("sub_leading_px"	,&sub_leading_px	,"sub_leading_px/F"		);
   tree_out.Branch("sub_leading_py"	,&sub_leading_py	,"sub_leading_py/F"		);
   tree_out.Branch("sub_leading_pz"	,&sub_leading_pz	,"sub_leading_pz/F"		);
   tree_out.Branch("sub_leading_eta"	,&sub_leading_eta	,"sub_leading_eta/F"		);
   tree_out.Branch("sub_leading_phi"	,&sub_leading_phi	,"sub_leading_phi/F"		);
   tree_out.Branch("sub_leading_mass"	,&sub_leading_mass	,"sub_leading_mass/F"		);

   tree_out.Branch("sub_leading_2nd_pt"		,&sub_leading_2nd_pt	,"sub_leading_2nd_pt/F"		);
   tree_out.Branch("sub_leading_2nd_px"		,&sub_leading_2nd_px	,"sub_leading_2nd_px/F"		);
   tree_out.Branch("sub_leading_2nd_py"		,&sub_leading_2nd_py	,"sub_leading_2nd_py/F"		);
   tree_out.Branch("sub_leading_2nd_pz"		,&sub_leading_2nd_pz	,"sub_leading_2nd_pz/F"		);
   tree_out.Branch("sub_leading_2nd_eta"	,&sub_leading_2nd_eta	,"sub_leading_2nd_eta/F"		);
   tree_out.Branch("sub_leading_2nd_phi"	,&sub_leading_2nd_phi	,"sub_leading_2nd_phi/F"		);
   tree_out.Branch("sub_leading_2nd_mass"	,&sub_leading_2nd_mass	,"sub_leading_2nd_mass/F"		);

   tree_out.Branch("sub_leading_charge"	,&sub_leading_charge	,"sub_leading_charge/I"		);
   tree_out.Branch("sub_leading_region"	,&sub_leading_region	,"sub_leading_region/I"		);
   tree_out.Branch("sub_leading_isE"	,&sub_leading_isE		,"sub_leading_isE/I"		);
   tree_out.Branch("sub_leading_isMu"	,&sub_leading_isMu		,"sub_leading_isMu/I"		);
   tree_out.Branch("sub_leading_isLeading"	,&sub_leading_isLeading		,"sub_leading_isLeading/I"		);

   tree_out.Branch("jet_pt"	,&jet_pt_out) ;
   tree_out.Branch("jet_energy"	,&jet_energy_out) ;
   tree_out.Branch("jet_px"	,&jet_px_out) ;
   tree_out.Branch("jet_py"	,&jet_py_out) ;
   tree_out.Branch("jet_pz"	,&jet_pz_out) ;
   tree_out.Branch("jet_eta"	,&jet_eta_out) ;
   tree_out.Branch("jet_phi"	,&jet_phi_out) ;
   tree_out.Branch("jet_IDLoose",&jet_IDLoose_out) ;
   tree_out.Branch("jet_DeepCSV"	,&jet_DeepCSV_out) ;

   tree_out.Branch("LHE_top_pt", &LHE_top_pt);

   tree_out.Branch("jet_BtagSF_loose"	,&jet_BtagSF_loose, "jet_BtagSF_loose/f") ;
   tree_out.Branch("jet_BtagSF_medium"	,&jet_BtagSF_medium, "jet_BtagSF_medium/f") ;
   tree_out.Branch("jet_BtagSF_tight"	,&jet_BtagSF_tight, "jet_BtagSF_tight/f") ;

   tree_out.Branch("pass_global"	,&pass_global	,"pass_global/I") ;
   tree_out.Branch("pass_MET_filters"	,&pass_MET_filters	,"pass_MET_filters/I") ;
   tree_out.Branch("pass_step0"		,&pass_step0	,"pass_step0/I") ;
   tree_out.Branch("pass_step1"		,&pass_step1	,"pass_step1/I") ;

   tree_out.Branch("pass_trigger_EE"		,&pass_trigger_EE	,"pass_trigger_EE/I") ;
   tree_out.Branch("pass_trigger_EMu"		,&pass_trigger_EMu	,"pass_trigger_EMu/I") ;
   tree_out.Branch("pass_trigger_MuMu"		,&pass_trigger_MuMu	,"pass_trigger_MuMu/I") ;
   tree_out.Branch("pass_trigger_EE_step2"	,&pass_trigger_EE_step2		,"pass_trigger_EE_step2/I") ;
   tree_out.Branch("pass_trigger_EMu_step2"	,&pass_trigger_EMu_step2	,"pass_trigger_EMu_step2/I") ;
   tree_out.Branch("pass_trigger_MuMu_step2"	,&pass_trigger_MuMu_step2	,"pass_trigger_MuMu_step2/I") ;

   tree_out.Branch("trig_Mu24_fire"   ,&trig_Mu24_fire  ,"trig_Mu24_fire/I");
   tree_out.Branch("trig_TkMu24_fire"		,&trig_TkMu24_fire	,"trig_TkMu24_fire/I");
   tree_out.Branch("trig_Mu27_fire"   ,&trig_Mu27_fire  ,"trig_Mu27_fire/I");
   tree_out.Branch("trig_Ele27_fire"		,&trig_Ele27_fire	,"trig_Ele27_fire/I");
   tree_out.Branch("trig_Ele32_fire"    ,&trig_Ele32_fire ,"trig_Ele32_fire/I");
   tree_out.Branch("trig_Ele35_fire"    ,&trig_Ele35_fire ,"trig_Ele35_fire/I");
   tree_out.Branch("trig_Mu8_Ele23_fire"	,&final_trig_Mu8_Ele23_fire	,"trig_Mu8_Ele23_fire/I");
   tree_out.Branch("trig_Mu23_Ele12_fire"	,&final_trig_Mu23_Ele12_fire	,"trig_Mu23_Ele12_fire/I");

   tree_out.Branch("trig_Flag_goodVertices_accept", &trig_Flag_goodVertices_accept, "trig_Flag_goodVertices_accept/I");
   tree_out.Branch("trig_Flag_globalSuperTightHalo2016Filter_accept", &trig_Flag_globalSuperTightHalo2016Filter_accept, "trig_Flag_globalSuperTightHalo2016Filter_accept/I");
   tree_out.Branch("trig_Flag_HBHENoiseFilter_accept", &trig_Flag_HBHENoiseFilter_accept, "trig_Flag_HBHENoiseFilter_accept/I");
   tree_out.Branch("trig_Flag_HBHENoiseIsoFilter_accept", &trig_Flag_HBHENoiseIsoFilter_accept, "trig_Flag_HBHENoiseIsoFilter_accept/I");
   tree_out.Branch("trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept", &trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept, "trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept/I");
   tree_out.Branch("trig_Flag_BadPFMuonFilter_accept", &trig_Flag_BadPFMuonFilter_accept, "trig_Flag_BadPFMuonFilter_accept/I");
   tree_out.Branch("trig_Flag_eeBadScFilter_accept", &trig_Flag_eeBadScFilter_accept, "trig_Flag_eeBadScFilter_accept/I");
   tree_out.Branch("trig_Flag_ecalBadCalibReduced", &trig_Flag_ecalBadCalibReduced, "trig_Flag_ecalBadCalibReduced/I");
   tree_out.Branch("trig_Flag_METFilters_accept", &trig_Flag_METFilters_accept, "trig_Flag_METFilters_accept/I");
   // Setup the trigger for changing data structures.
   

//   std::vector<runCounter> runs ;
   
  TRandom3 Tr ;
  Long64_t nbytes = 0, nb = 0;
  int nn=0;
  for (Long64_t jentry=0; jentry<nentries;jentry++)
  {
    M_ll = 0;
    Pt_ll = 0;
    isEE = 0;
    isEMu = 0;
    isMuMu = 0;
    n_jet = 0;
    n_bjet = 0;
    isPrint = false;
    MET_OfflineCorrect_Pt = 0.0;
    MET_OfflineCorrect_phi = 0.0;

    w_Btag_offline = 1.0;

    P_bjet_data =1;
    P_bjet_mc =1;

    trig_DE33_fire = false;
    pass_trigger_EE = 0;
    pass_trigger_EMu = 0;
    pass_trigger_MuMu = 0;
    pass_trigger_EE_step2 = 0;
    pass_trigger_EMu_step2 = 0;
    pass_trigger_MuMu_step2 = 0;
    pass_global = 1;
    pass_MET_filters = 0;
    pass_step0=0;
    pass_step1=0;
    pass_step2=0;
    pass_step3=0;
    pass_step411=0;
    pass_step412=0;
    pass_step421=0;
    pass_step422=0;
    pass_step43=0;
    pass_step5=0;
    
    leading_pt = 0;
    leading_px = 0;
    leading_py = 0;
    leading_pz = 0;
    leading_eta = 0;
    leading_phi = 0;
    leading_mass = 0;
    
    leading_2nd_pt = 0;
    leading_2nd_px = 0;
    leading_2nd_py = 0;
    leading_2nd_pz = 0;
    leading_2nd_eta = 0;
    leading_2nd_phi = 0;
    leading_2nd_mass = 0;
    
    leading_charge = 0;
    leading_region = 0;
    leading_isE = 0;
    leading_isMu = 0;
    leading_isLeading = 0;
    
    sub_leading_pt = 0;
    sub_leading_px = 0;
    sub_leading_py = 0;
    sub_leading_pz = 0;
    sub_leading_eta = 0;
    sub_leading_phi = 0;
    sub_leading_mass = 0;
    
    sub_leading_2nd_pt = 0;
    sub_leading_2nd_px = 0;
    sub_leading_2nd_py = 0;
    sub_leading_2nd_pz = 0;
    sub_leading_2nd_eta = 0;
    sub_leading_2nd_phi = 0;
    sub_leading_2nd_mass = 0;
    
    sub_leading_charge = 0;
    sub_leading_region = 0;
    sub_leading_isE = 0;
    sub_leading_isMu = 0;
    sub_leading_isLeading = 0;
    
    vector <float>().swap(jet_pt_out) ;
    vector <float>().swap(jet_energy_out) ;
    vector <float>().swap(jet_px_out) ;
    vector <float>().swap(jet_py_out) ;
    vector <float>().swap(jet_pz_out) ;
    vector <float>().swap(jet_eta_out) ;
    vector <float>().swap(jet_phi_out) ;
    vector <float>().swap(jet_DeepCSV_out) ;
    vector <int>().swap(jet_IDLoose_out) ;
    vector <float>().swap(LHE_top_pt) ;

    
    displayProgress(jentry, nentries) ;
      
//      if (jentry>2000000)break;

      //Long64_t ientry = LoadTree(jentry);
      //if (ientry < 0) break;
      //nb = fChain->GetEntry(jentry);   nbytes += nb;
    fChain->GetEntry(jentry);
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if (No_print > 0)
    {
      if (ev_event == No_print)
      {
        isPrint = true;
      }
      else
      {
        isPrint = false;
        continue;
      }
    }
    else
    {
      isPrint = false;
    }
    if (isPrint)
    {
      cout<<"start print "<<endl;
      if (!isData)
      {
        cout<<"#############  event : "<<ev_event<<"##############"<<endl;
      }
    }
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // check MET filters
    if (year == "2016") {
    	if (isData) {
      		pass_MET_filters = trig_Flag_goodVertices_accept
                        && trig_Flag_globalSuperTightHalo2016Filter_accept
                        && trig_Flag_HBHENoiseFilter_accept
                        && trig_Flag_HBHENoiseIsoFilter_accept
                        && trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept
                        && trig_Flag_BadPFMuonFilter_accept
                        && trig_Flag_eeBadScFilter_accept;
    	} else {
      		pass_MET_filters = trig_Flag_goodVertices_accept
                        && trig_Flag_globalSuperTightHalo2016Filter_accept
                        && trig_Flag_HBHENoiseFilter_accept
                        && trig_Flag_HBHENoiseIsoFilter_accept
                        && trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept
                        && trig_Flag_BadPFMuonFilter_accept;
    	}
    }
    if (year == "2017") {
    	if (isData) {
      		pass_MET_filters = trig_Flag_goodVertices_accept
                       	&& trig_Flag_globalSuperTightHalo2016Filter_accept
                       	&& trig_Flag_HBHENoiseFilter_accept
                       	&& trig_Flag_HBHENoiseIsoFilter_accept
                       	&& trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept
                       	&& trig_Flag_BadPFMuonFilter_accept
                       	&& trig_Flag_eeBadScFilter_accept
                       	&& trig_Flag_ecalBadCalibReduced;
    	} else {
      		pass_MET_filters = trig_Flag_goodVertices_accept
                       	&& trig_Flag_globalSuperTightHalo2016Filter_accept
                       	&& trig_Flag_HBHENoiseFilter_accept
                       	&& trig_Flag_HBHENoiseIsoFilter_accept
                       	&& trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept
                       	&& trig_Flag_BadPFMuonFilter_accept
                       	//&& trig_Flag_eeBadScFilter_accept
                       	&& trig_Flag_ecalBadCalibReduced;
    	}
    }
    if (year == "2018") {
      if (isData) {
          pass_MET_filters = trig_Flag_goodVertices_accept
                        && trig_Flag_globalSuperTightHalo2016Filter_accept
                        && trig_Flag_HBHENoiseFilter_accept
                        && trig_Flag_HBHENoiseIsoFilter_accept
                        && trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept
                        && trig_Flag_BadPFMuonFilter_accept
                        && trig_Flag_eeBadScFilter_accept;
      } else {
          pass_MET_filters = trig_Flag_goodVertices_accept
                        && trig_Flag_globalSuperTightHalo2016Filter_accept
                        && trig_Flag_HBHENoiseFilter_accept
                        && trig_Flag_HBHENoiseIsoFilter_accept
                        && trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept
                        && trig_Flag_BadPFMuonFilter_accept;
                        //&& trig_Flag_eeBadScFilter_accept
      }
	}
    if (isPrint)
    {
      cout<<"################ MET #################"<<endl;
      cout<<"trig_Flag_goodVertices_accept : "<<trig_Flag_goodVertices_accept<<endl;
      cout<<"trig_Flag_globalSuperTightHalo2016Filter_accept : "<<trig_Flag_globalSuperTightHalo2016Filter_accept<<endl;
      cout<<"trig_Flag_HBHENoiseFilter_accept : "<<trig_Flag_HBHENoiseFilter_accept<<endl;
      cout<<"trig_Flag_HBHENoiseIsoFilter_accept : "<<trig_Flag_HBHENoiseIsoFilter_accept<<endl;
      cout<<"trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept : "<<trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept<<endl;
      cout<<"trig_Flag_BadPFMuonFilter_accept : "<<trig_Flag_BadPFMuonFilter_accept<<endl;
      //cout<<"trig_Flag_BadChargedCandidateFilter_accept : "<<trig_Flag_BadChargedCandidateFilter_accept<<endl;
      cout<<"(only use for data)trig_Flag_eeBadScFilter_accept : "<<trig_Flag_eeBadScFilter_accept<<endl;
      cout<<"trig_Flag_ecalBadCalibReduced (been rerun locally, 2017) : "<<trig_Flag_ecalBadCalibReduced<<endl;
      cout<<"pass MET filters : "<<pass_MET_filters<<endl;
    }

    float w_sign = 1.0 ;
    if(!isData)
    {
    w_sign = mc_w_sign < 0 ? -1 : 1 ;
    }

    w_top = 1.0 ;
    if(isTTbar)
    {
      for(unsigned iMC=0 ; iMC<LHE_Pt->size() ; ++iMC)
      {
        if( (abs(LHE_pdgid->at(iMC)) == 6) ) {
          w_top = w_top*(exp(-1.08872e+00-(1.19998e-02)*LHE_Pt->at(iMC))+8.95139e-01);
          LHE_top_pt.push_back(LHE_Pt->at(iMC));
        }
      }
      w_top = sqrt(w_top);
    }

    if(true==isData){
        
      PU_true_out = -1 ;
        
        // Set weights to 1
      w_PU_up_out    = 1.0 ;
      w_PU_down_out  = 1.0 ;
      w_PU_out       = 1.0 ;
    }
    else{
      // Set PU weights
      int PU = mc_trueNumInteractions ;
      PU_true_out = PU ;
      if (year == "2016") {
        w_PU_out       = w_sign*PU_2016::MC_pileup_weight_2016(PU, "nominal");
        w_PU_up_out    = w_sign*PU_2016::MC_pileup_weight_2016(PU, "up");
        w_PU_down_out  = w_sign*PU_2016::MC_pileup_weight_2016(PU, "down");
      } 
      if (year == "2017") {
        w_PU_out       = w_sign*PU_2017::MC_pileup_weight_2017(PU, "nominal");
        w_PU_up_out    = w_sign*PU_2017::MC_pileup_weight_2017(PU, "up");
        w_PU_down_out  = w_sign*PU_2017::MC_pileup_weight_2017(PU, "down");
      } 
      if (year == "2018") {
        w_PU_out       = w_sign*PU_2018::MC_pileup_weight_2018(PU, "nominal");
        w_PU_up_out    = w_sign*PU_2018::MC_pileup_weight_2018(PU, "up");
        w_PU_down_out  = w_sign*PU_2018::MC_pileup_weight_2018(PU, "down");
      }
    }
    //MET offline correction https://lathomas.web.cern.ch/lathomas/METStuff/XYCorrections/
    std::pair<float,float>  TheXYCorr_Met_MetPhi(-99.0,-99.0);
    if (year == "2016") {
      TheXYCorr_Met_MetPhi = METXYCorr_Met_MetPhi(MET_FinalCollection_Pt, MET_FinalCollection_phi, ev_run, 2016, !isData, pv_n);
    }
    if (year == "2017") {
      TheXYCorr_Met_MetPhi = METXYCorr_Met_MetPhi(MET_FinalCollection_Pt, MET_FinalCollection_phi, ev_run, 2017, !isData, pv_n);
    }
    if (year == "2018") {
      TheXYCorr_Met_MetPhi = METXYCorr_Met_MetPhi(MET_FinalCollection_Pt, MET_FinalCollection_phi, ev_run, 2018, !isData, pv_n);
    }
    MET_OfflineCorrect_Pt = TheXYCorr_Met_MetPhi.first;
    MET_OfflineCorrect_phi = TheXYCorr_Met_MetPhi.second;

    std::vector<muon_candidate*> muons ;
    for(unsigned int iMu=0 ; iMu<mu_gt_pt->size() ; ++iMu){
      if(!int(mu_isGlobalMuon->at(iMu)))continue;
      float pt     = mu_gt_pt->at(iMu) ;
      float eta    = mu_gt_eta->at(iMu) ;
      float phi    = mu_gt_phi->at(iMu) ;
      int   charge = mu_gt_charge->at(iMu) ;

      float muPtSFRochester = 1.0;
      if(isData){
        muPtSFRochester = rc.kScaleDT(charge, pt, eta, phi, 0, 0);
      } else {
        if (mu_mc_index->at(iMu)!=-1 && abs(mc_pdgId->at(mu_mc_index->at(iMu)) == 13)) {
          muPtSFRochester = rc.kSpreadMC(charge, pt, eta, phi, mc_pt->at(mu_mc_index->at(iMu)),0, 0);
        }
        if (mu_mc_index->at(iMu)<0) {
          muPtSFRochester = rc.kSmearMC(charge, pt, eta, phi, mu_trackerLayersWithMeasurement->at(iMu) , Tr.Rndm(),0, 0);
        }
      }

      muon_candidate* mu = new muon_candidate(pt * muPtSFRochester, pt, eta, phi, charge) ;
      mu->p4_2nd.SetPtEtaPhiM(pt, eta, phi, m_mu); 
      mu->muon_isHighPtMuon = mu_isHighPtMuon->at(iMu) ;
      mu->muon_isGlobalMuon = mu_isGlobalMuon->at(iMu) ;

      mu->isTight = int(mu_isTightMuon->at(iMu));
      mu->pfiso04 = mu_pfIsoDbCorrected04->at(iMu);
      mu->check_pass();
      if(mu->passed)
      {
        muons.push_back(mu) ;
    	}
      if(isPrint)
      {
        cout<<"################ Muon #################"<<endl;
        cout<<"mu pt :"<<mu->pt<<endl;
        cout<<"mu pt (without rochester correction):"<<mu->pt_old<<endl;
        cout<<"mu eta :"<<mu->eta<<endl;
        cout<<"mu phi :"<<mu->phi<<endl;
        cout<<"mu E :"<<mu->p4.E()<<endl;
        cout<<"mu charge :"<<mu->charge<<endl;
        cout<<"mu iso :"<<mu->pfiso04<<endl;
        cout<<"mu isTight :"<<mu->isTight<<endl;
        cout<<"mu passed :"<<mu->passed<<endl;
      }
    }
   
    std::vector<electron_candidate*> electrons ;
    for(unsigned int iEl=0 ; iEl<gsf_n ; ++iEl){
      float pt_in     = gsf_ecalTrkEnergyPostCorr->at(iEl)*sin(2.*atan(exp(-1.*gsf_eta->at(iEl)))) ; ;
      float gsf_eta_in    = gsf_eta->at(iEl) ;
      float gsf_phi_in    = gsf_phi->at(iEl) ;
      float sc_eta    = gsf_sc_eta->at(iEl) ;
      float sc_phi    = gsf_sc_phi->at(iEl) ;
      int   charge = gsf_charge->at(iEl) ;

      electron_candidate* el = new electron_candidate(pt_in, gsf_eta_in, gsf_phi_in, sc_eta, sc_phi, charge) ;
      el->p4_2nd.SetPtEtaPhiM(gsf_pt->at(iEl), gsf_eta_in, gsf_phi_in, m_el); 

      el->pass_trigger = true;

      el->isTight = gsf_Tight->at(iEl);
      el->dxy_firstPVtx = gsf_dxy_firstPVtx->at(iEl);
      el->dz_firstPVtx = gsf_dz_firstPVtx->at(iEl);
      el->check_pass();

      if(el->passed)
      {
      	 electrons.push_back(el) ;
      }
      if(isPrint)
      {
        cout<<"################ Electron #################"<<endl;
        cout<<"el Et :"<<el->Et<<endl;
        cout<<"el pt :"<<el->p4.Pt()<<endl;
        cout<<"el gsf eta :"<<el->gsf_eta<<endl;
        cout<<"el gsf phi :"<<el->gsf_phi<<endl;
        cout<<"el sc eta :"<<el->sc_eta<<endl;
        cout<<"el sc phi :"<<el->sc_phi<<endl;
        cout<<"el E :"<<el->p4.E()<<endl;
        cout<<"el dxy(firstPV) :"<<el->dxy_firstPVtx<<endl;
        cout<<"el dz(firstPV) :"<<el->dz_firstPVtx<<endl;
        cout<<"el charge :"<<el->charge<<endl;
        cout<<"el isTight :"<<el->isTight<<endl;
        cout<<"el passed :"<<el->passed<<endl;
      }
    }



    isEMu = 0;
    isEE = 0;
    isMuMu = 0;
    M_ll = 0;
    Pt_ll = 0;
    //start check pass1
    std::vector<Lep_candidate*> leptons;
    for (unsigned int iEl = 0; iEl < electrons.size(); ++iEl)
    {
      Lep_candidate* lep = new Lep_candidate();
      event_fill_ele(lep, electrons.at(iEl));
      leptons.push_back(lep);
    }
    for (unsigned int iMu = 0; iMu < muons.size(); ++iMu)
    {
      Lep_candidate* lep = new Lep_candidate();
      event_fill_muon(lep, muons.at(iMu));
      leptons.push_back(lep);
    }
    n_lep = leptons.size();

    int flag_lep1 = -1;
    int flag_lep2 = -1;
    if (leptons.size()==2)
    {
      for (unsigned int iLep = 0; iLep < leptons.size(); ++iLep)
      {
      	Lep_candidate* lep = leptons.at(iLep);
      	if (flag_lep1<0)
      	{
      		flag_lep2 = flag_lep1;
      		flag_lep1 = iLep;
      	}
      	else if (lep->pt > leptons.at(flag_lep1)->pt)
      	{
      		flag_lep2 = flag_lep1;
      		flag_lep1 = iLep;
      	}      			
      	else if (flag_lep2<0)
      	{
      		flag_lep2 = iLep;
      	}
      	else if (lep->pt > leptons.at(flag_lep2)->pt)
      	{
      		flag_lep2 = iLep;
      	}
      }
    }

    Lep_candidate *leading_lep 	= new Lep_candidate();
    Lep_candidate *sub_leading_lep 	= new Lep_candidate();
    if (flag_lep1!=-1 && flag_lep2!=-1)
    {
      leading_lep = leptons.at(flag_lep1);
      sub_leading_lep = leptons.at(flag_lep2);
      M_ll = (leading_lep->p4+sub_leading_lep->p4).Mag();
      Pt_ll = (leading_lep->p4+sub_leading_lep->p4).Pt();
      if (isPrint)
      {
        cout<<"################ Lepton #################"<<endl;
        cout<<"leading_lep pt : "<<leading_lep->pt<<endl;
        cout<<"sub_leading_lep pt : "<<sub_leading_lep->pt<<endl;
        cout<<"Mass(lepton pair) : "<<M_ll<<endl;
      }
      if (leading_lep->pt >25 && M_ll>20)
      {
      	leading_lep->isLeading = true;
        pass_step1 = true;
      }
    }
    if (pass_step1)
    {
      if (leading_lep->isE != sub_leading_lep->isE)
      {
      	isEMu = 1;
      }
      if (leading_lep->isE && sub_leading_lep->isE)
      {
      	isEE = 1;
      }
      if (leading_lep->isMu && sub_leading_lep->isMu)
      {
      	isMuMu = 1;
      }    
    }
    pass_global = pass_global && pass_step1;
    //end check pass1
    //start check pass2
    if (pass_step1)
    {
    	if ((isEE || isMuMu)&&(M_ll < 76 || M_ll > 106))
    	{
    	pass_step2 = true;
    	}
    	else if(isEMu)
    	{
    	pass_step2 = true;
    	}
    }
    pass_global = pass_global && pass_step2;
    //end check pass2
    //start check pass3
    if(pass_step1)
    {
      if (((isEE || isMuMu) && MET_FinalCollection_Pt > 40) || isEMu)
      {
      	pass_step3 = true;
      }
    }
    pass_global = pass_global && pass_step3;
    //end check pass3
    n_jet = 0;
    n_bjet = 0;
    w_Btag_loose = 1.0;
    w_Btag_medium = 1.0;
    w_Btag_tight = 1.0;

    //fill jet
    std::vector<jet_candidate*> jets ;
    for(unsigned int ijet=0 ; ijet<jet_pt->size() ; ++ijet){
      float pt     = jet_pt->at(ijet) ;
      float eta    = jet_eta->at(ijet) ;
      float phi    = jet_phi->at(ijet) ;
      float energy = jet_energy->at(ijet) ;

      jet_candidate* jet = new jet_candidate(pt, eta, phi, energy) ;
      jet->JetIDLepVeto = jet_isJetIDLepVeto->at(ijet);
      jet->jet_DeepCSV = jet_DeepCSV->at(ijet);
      jet->partonFlavour = jet_partonFlavour->at(ijet);
      jet->check_pass();

      if (jet->p4.DeltaR(leading_lep->p4) > 0.4 && jet->p4.DeltaR(sub_leading_lep->p4) > 0.4) {
        jets.push_back(jet);
        if (jet->passed) { n_jet++;  }
        if (jet->isbjet) { n_bjet++; }
      }

      
    }
    //end jet fill
    for (unsigned ijet = 0; ijet<jets.size(); ijet++)
    { 
      if (isData) break;
      jet_candidate *jet = jets.at(ijet);
      if (!jet->passed) continue; 
      if( abs(jet->partonFlavour) == 5){
        h2_BTaggingEff_Denom_b->Fill(jet->pt, abs(jet->eta));
        if( jet->isbjet ) {
          h2_BTaggingEff_Num_b->Fill(jet->pt, abs(jet->eta));
          P_bjet_mc = P_bjet_mc * scale_factor(&btagEff_b_H, jet->pt, abs(jet->eta),"");
          P_bjet_data = P_bjet_data * scale_factor(&btagEff_b_H, jet->pt, abs(jet->eta),"") * reader.eval_auto_bounds("central", BTagEntry::FLAV_B,  abs(jet->eta), jet->pt);
        }
        if( !jet->isbjet ) {
          P_bjet_mc = P_bjet_mc * (1 - scale_factor(&btagEff_b_H, jet->pt, abs(jet->eta),""));
          P_bjet_data = P_bjet_data * (1- (scale_factor(&btagEff_b_H, jet->pt, abs(jet->eta),"") * reader.eval_auto_bounds("central", BTagEntry::FLAV_B,  abs(jet->eta), jet->pt)));
        }  
      }
      if( abs(jet->partonFlavour) == 4){
        h2_BTaggingEff_Denom_c->Fill(jet->pt, abs(jet->eta));
        if( jet->isbjet) {
          h2_BTaggingEff_Num_c->Fill(jet->pt, abs(jet->eta));
          P_bjet_mc = P_bjet_mc * scale_factor(&btagEff_c_H, jet->pt, abs(jet->eta),"");
          P_bjet_data = P_bjet_data * scale_factor(&btagEff_c_H, jet->pt, abs(jet->eta),"") * reader.eval_auto_bounds("central", BTagEntry::FLAV_C,  abs(jet->eta), jet->pt);
        }
        if( !jet->isbjet ) {
          P_bjet_mc = P_bjet_mc * (1 - scale_factor(&btagEff_c_H, jet->pt, abs(jet->eta),""));
          P_bjet_data = P_bjet_data * (1- (scale_factor(&btagEff_c_H, jet->pt, abs(jet->eta),"") * reader.eval_auto_bounds("central", BTagEntry::FLAV_C,  abs(jet->eta), jet->pt)));
        }
      }
      if( abs(jet->partonFlavour) != 4 && abs(jet->partonFlavour) != 5){
        h2_BTaggingEff_Denom_udsg->Fill(jet->pt, abs(jet->eta));
        if( jet->isbjet) {
          h2_BTaggingEff_Num_udsg->Fill(jet->pt, abs(jet->eta));
          P_bjet_mc = P_bjet_mc * scale_factor(&btagEff_udsg_H, jet->pt, abs(jet->eta),"");
          P_bjet_data = P_bjet_data * scale_factor(&btagEff_udsg_H, jet->pt, abs(jet->eta),"") * reader.eval_auto_bounds("central", BTagEntry::FLAV_UDSG,  abs(jet->eta), jet->pt);
        }
        if( !jet->isbjet ) {
          P_bjet_mc = P_bjet_mc * (1 - scale_factor(&btagEff_udsg_H, jet->pt, abs(jet->eta),""));
          P_bjet_data = P_bjet_data * (1- (scale_factor(&btagEff_udsg_H, jet->pt, abs(jet->eta),"") * reader.eval_auto_bounds("central", BTagEntry::FLAV_UDSG,  abs(jet->eta), jet->pt)));
        }
      }
    }


    if (isData) {
      w_Btag_loose = 1.0;
      w_Btag_medium = 1.0;
      w_Btag_tight = 1.0;
      w_Btag_offline = 1.0;
    } else {
      w_Btag_loose = jet_BtagSF_loose;
      w_Btag_medium = jet_BtagSF_medium;
      w_Btag_tight = jet_BtagSF_tight;
      if (P_bjet_mc!= 0.0){w_Btag_offline = (P_bjet_data/P_bjet_mc);}
    }


    //start check pass411
    if (n_jet >= 3)
    {
      pass_step411 = true;
    }
    //start check pass412
    //pass_global = pass_global && pass_step411;
    if (n_bjet >=1)
    {
      pass_step412 = true;
    }

    pass_global = pass_global && (pass_step411 && pass_step412);
    //end check pass4
    //start check pass5
    pass_step5 = true;
    for (unsigned ijet = 0; ijet<jets.size(); ijet++)
    {
      jet_candidate *jet = jets.at(ijet);
      if (isPrint)
      {
        cout<<"################ Jet #################"<<endl;
        cout<<"jet : pt "<<jet->pt<<" ;  |eta|"<<fabs(jet->eta)<<endl;
        cout<<"jet : DeltaR(leading_lep) "<<jet->p4.DeltaR(leading_lep->p4)<<endl;
        cout<<"jet : DeltaR(sub_leading_lep) "<<jet->p4.DeltaR(sub_leading_lep->p4)<<endl;
      }
      if (jet->pt > 40 && (fabs(jet->eta)>2.4 && fabs(jet->eta)<5.2) && jet->JetIDLepVeto && jet->p4.DeltaR(leading_lep->p4) > 0.4 && jet->p4.DeltaR(sub_leading_lep->p4) > 0.4)
      {
        pass_step5 = false;
        break;
      }
    }

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if (year == "2016") {
    	final_trig_Mu8_Ele23_fire = trig_Mu8_Ele23_fire;
    	final_trig_Mu23_Ele12_fire = trig_Mu23_Ele12_fire;
    	if ( isData && (ev_run > 280385) ) {
      	final_trig_Mu8_Ele23_fire = trig_Mu8_Ele23_DZ_fire;
      	final_trig_Mu23_Ele12_fire = trig_Mu23_Ele12_DZ_fire;
    	}
    	if (isEE && (trig_Ele23_Ele12_fire) ) {pass_trigger_EE = true;}
    	if (isEMu && (final_trig_Mu8_Ele23_fire || final_trig_Mu23_Ele12_fire) ) {pass_trigger_EMu = true;}
    	if (isMuMu && (trig_Mu17_Mu8_fire) ) {pass_trigger_MuMu = true;}
    	if(isEE && (pass_trigger_EE || trig_Ele27_fire) ) {pass_trigger_EE_step2 = true;}
    	if(isEMu && (pass_trigger_EMu || trig_Ele27_fire || trig_Mu24_fire || trig_TkMu24_fire) ) {pass_trigger_EMu_step2 = true;}
    	if(isMuMu && (pass_trigger_MuMu || trig_Mu24_fire || trig_TkMu24_fire) ) {pass_trigger_MuMu_step2 = true;}
	
    	if (isPrint) {
      		if (isEMu) {
        		cout<<"################ Trig EMu #################"<<endl;
        		if (isData && (ev_run > 280385)) {cout<<"Use DZ trigger"<<endl;}
        		cout<<"pass trig_Mu8_Ele23_fire : "<<trig_Mu8_Ele23_fire<<endl;
        		cout<<"pass trig_Mu23_Ele12_fire : "<<trig_Mu23_Ele12_fire<<endl;
        		cout<<"pass trig_Mu8_Ele23_DZ_fire : "<<trig_Mu8_Ele23_DZ_fire<<endl;
        		cout<<"pass trig_Mu23_Ele12_DZ_fire : "<<trig_Mu23_Ele12_DZ_fire<<endl;
        		cout<<"pass trig_Ele27_fire : "<<trig_Ele27_fire<<endl;
        		cout<<"pass trig_Mu24_fire : "<<trig_Mu24_fire<<endl;
        		cout<<"pass trig_TkMu24_fire : "<<trig_TkMu24_fire<<endl;
        		cout<<"pass pass_trigger_EMu : "<<pass_trigger_EMu<<endl;
        		cout<<"pass pass_trigger_EMu_step2 : "<<pass_trigger_EMu_step2<<endl;
      		}
    	}
    }
    if (year == "2017") {
    	final_trig_Mu8_Ele23_fire = trig_Mu8_Ele23_DZ_fire;
    	final_trig_Mu23_Ele12_fire = trig_Mu23_Ele12_fire;
    	if (isData && (ev_run < 299368) ) {final_trig_Mu23_Ele12_fire = trig_Mu23_Ele12_DZ_fire;}
    	if (isEE && (trig_Ele23_Ele12_fire) ) {pass_trigger_EE = true;}
    	if (isEMu && (final_trig_Mu8_Ele23_fire || final_trig_Mu23_Ele12_fire) ) {pass_trigger_EMu = true;}
    	if (isMuMu && (trig_Mu17_Mu8_fire) ) {pass_trigger_MuMu = true;}
    	if (isEE && (pass_trigger_EE || trig_Ele35_fire) ) {pass_trigger_EE_step2 = true;}
    	if (isEMu && (pass_trigger_EMu || trig_Ele35_fire || trig_Mu27_fire) ) {pass_trigger_EMu_step2 = true;}
    	if (isMuMu && (pass_trigger_MuMu || trig_Mu27_fire) ) {pass_trigger_MuMu_step2 = true;}

    	if (isPrint){
      		if (isEMu) {
        		cout<<"################ Trig EMu #################"<<endl;
        		if (isData && (ev_run < 299368)) {cout<<"Use DZ trigger"<<endl;}
        		cout<<"pass trig_Mu8_Ele23_DZ_fire : "<<trig_Mu8_Ele23_DZ_fire<<endl;
        		cout<<"pass trig_Mu23_Ele12_fire : "<<final_trig_Mu23_Ele12_fire<<endl;
        		cout<<"pass trig_Mu23_Ele12_DZ_fire : "<<trig_Mu23_Ele12_DZ_fire<<endl;
        		cout<<"pass trig_Ele35_fire : "<<trig_Ele35_fire<<endl;
        		cout<<"pass trig_Mu27_fire : "<<trig_Mu27_fire<<endl;
        		cout<<"pass pass_trigger_EMu : "<<pass_trigger_EMu<<endl;
        		cout<<"pass pass_trigger_EMu_step2 : "<<pass_trigger_EMu_step2<<endl;
      		}
    	}
    }
    if (year == "2018") {
    	final_trig_Mu8_Ele23_fire = trig_Mu8_Ele23_DZ_fire;
    	final_trig_Mu23_Ele12_fire = trig_Mu23_Ele12_fire;
    	if (isEE && (trig_Ele23_Ele12_fire) ) {pass_trigger_EE = true;}
    	if (isEMu && (final_trig_Mu8_Ele23_fire || final_trig_Mu23_Ele12_fire) ) {pass_trigger_EMu = true;}
    	if (isMuMu && (trig_Mu17_Mu8_fire) ) {pass_trigger_MuMu = true;}
    	if (isEE && (pass_trigger_EE || trig_Ele32_fire) ) {pass_trigger_EE_step2 = true;}
    	if (isEMu && (pass_trigger_EMu || trig_Ele32_fire || trig_Mu24_fire) ) {pass_trigger_EMu_step2 = true;}
    	if (isMuMu && (pass_trigger_MuMu || trig_Mu24_fire) ) {pass_trigger_MuMu_step2 = true;}

    	if (isPrint){
      		if (isEMu) {
        		cout<<"################ Trig EMu #################"<<endl;
        		cout<<"pass trig_Mu8_Ele23_DZ_fire : "<<trig_Mu8_Ele23_DZ_fire<<endl;
        		cout<<"pass trig_Mu23_Ele12_fire : "<<final_trig_Mu23_Ele12_fire<<endl;
        		cout<<"pass trig_Ele32_fire : "<<trig_Ele32_fire<<endl;
        		cout<<"pass trig_Mu24_fire : "<<trig_Mu24_fire<<endl;
        		cout<<"pass pass_trigger_EMu : "<<pass_trigger_EMu<<endl;
        		cout<<"pass pass_trigger_EMu_step2 : "<<pass_trigger_EMu_step2<<endl;
      		}
    	}
    }


    if (isPrint)
    {
      cout<<"################ Ret #################"<<endl;
      cout<<"pass step1 : "<<pass_step1<<endl;
    }
    if (pass_step1)
    {
      leading_pt = leading_lep->pt;
      leading_px = leading_lep->p4.Px();
      leading_py = leading_lep->p4.Py();
      leading_pz = leading_lep->p4.Pz();
      leading_eta = leading_lep->eta;
      leading_phi = leading_lep->phi;
      leading_2nd_pt = leading_lep->p4_2nd.Pt();
      leading_2nd_px = leading_lep->p4_2nd.Px();
      leading_2nd_py = leading_lep->p4_2nd.Py();
      leading_2nd_pz = leading_lep->p4_2nd.Pz();
      leading_2nd_eta = leading_lep->p4_2nd.Eta();
      leading_2nd_phi = leading_lep->p4_2nd.Phi();
      leading_charge = leading_lep->charge;
      leading_region = leading_lep->region;
      leading_isLeading = leading_lep->isLeading;
      leading_isE = leading_lep->isE;
      leading_isMu = leading_lep->isMu;
      leading_mass = leading_lep->p4.Mag();
	
      sub_leading_pt = sub_leading_lep->pt;
      sub_leading_px = sub_leading_lep->p4.Px();
      sub_leading_py = sub_leading_lep->p4.Py();
      sub_leading_pz = sub_leading_lep->p4.Pz();
      sub_leading_eta = sub_leading_lep->eta;
      sub_leading_phi = sub_leading_lep->phi;
      sub_leading_2nd_pt = sub_leading_lep->p4_2nd.Pt();
      sub_leading_2nd_px = sub_leading_lep->p4_2nd.Px();
      sub_leading_2nd_py = sub_leading_lep->p4_2nd.Py();
      sub_leading_2nd_pz = sub_leading_lep->p4_2nd.Pz();
      sub_leading_2nd_eta = sub_leading_lep->p4_2nd.Eta();
      sub_leading_2nd_phi = sub_leading_lep->p4_2nd.Phi();
      sub_leading_charge = sub_leading_lep->charge;
      sub_leading_region = sub_leading_lep->region;
      sub_leading_isLeading = sub_leading_lep->isLeading;
      sub_leading_isE = sub_leading_lep->isE;
      sub_leading_isMu = sub_leading_lep->isMu;
      sub_leading_mass = sub_leading_lep->p4.Mag();

      for (unsigned ijet = 0; ijet<jets.size(); ijet++)
      { 
        jet_candidate *jet = jets.at(ijet);
        if (jet->p4.DeltaR(leading_lep->p4) > 0.4 && jet->p4.DeltaR(sub_leading_lep->p4) > 0.4)
        {       
          jet_pt_out.push_back(jet->p4.Pt()) ;
          jet_energy_out.push_back(jet->p4.E()) ;
          jet_px_out.push_back(jet->p4.Px()) ;
          jet_py_out.push_back(jet->p4.Py()) ;
          jet_pz_out.push_back(jet->p4.Pz()) ;
          jet_eta_out.push_back(jet->p4.Eta()) ;
          jet_phi_out.push_back(jet->p4.Phi()) ;
          jet_IDLoose_out.push_back(jet->JetIDLepVeto) ;
          jet_DeepCSV_out.push_back(jet->jet_DeepCSV) ;
        }
      }
    }
/*
    if (pass_global)
    {
      nn++;
    }*/
    if (pass_step1)
    {
      tree_out.Fill() ;
      nn++;
    }
    //clean up swap
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

    for (std::vector<jet_candidate*>::iterator it = jets.begin(); it != jets.end(); it ++){
      if (NULL != *it)
      { 
        delete *it;
        *it = NULL;
      }
    }
    jets.clear() ;
    jets.swap(jets);
    for (std::vector<Lep_candidate*>::iterator it = leptons.begin(); it != leptons.end(); it ++){
      if (NULL != *it)
      { 
        delete *it;
        *it = NULL;
      }
    }
    leptons.clear() ;
    leptons.swap(leptons);

    leading_lep = NULL;
    sub_leading_lep = NULL;
    delete leading_lep;
    delete sub_leading_lep;
      
  }
  file_out.cd() ;
  tree_out.Write() ;
   h2_BTaggingEff_Denom_b   ->Write("",TObject::kOverwrite); 
   h2_BTaggingEff_Denom_c   ->Write("",TObject::kOverwrite); 
   h2_BTaggingEff_Denom_udsg->Write("",TObject::kOverwrite); 
   h2_BTaggingEff_Num_b     ->Write("",TObject::kOverwrite); 
   h2_BTaggingEff_Num_c     ->Write("",TObject::kOverwrite); 
   h2_BTaggingEff_Num_udsg  ->Write("",TObject::kOverwrite); 
  file_out.Close() ;
  std::cout<<"\n"<<nn<<std::endl; 
}
