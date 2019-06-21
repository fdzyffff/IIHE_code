#include <TFile.h>
#include <TH1.h>

#include <iostream>

void test_PU(){
  TFile f_PU_golden     ("~/public/HEEP/data2015/PUHistograms/dataPUBin_25ns_complete_golden.root"          ,"READ") ;
  TFile f_PU_silver_down("~/public/HEEP/data2015/PUHistograms/dataPUBin_25ns_complete_silver_minus1Sig.root","READ") ;
  TFile f_PU_silver_up  ("~/public/HEEP/data2015/PUHistograms/dataPUBin_25ns_complete_silver_plus1Sig.root" ,"READ") ;
  TFile f_PU_silver     ("~/public/HEEP/data2015/PUHistograms/dataPUBin_25ns_complete_silver.root"          ,"READ") ;
  TFile f_PU_MC("~/public/HEEP/data2015/PUHistograms/mcPUDist25ns.root", "READ") ;
  TH1F* h_PU_MC = (TH1F*) f_PU_MC.Get("mcPUDist") ;
  
  TH1F* h_PU_golden      = (TH1F*) f_PU_golden     .Get("pileup") ;
  TH1F* h_PU_silver_down = (TH1F*) f_PU_silver_down.Get("pileup") ;
  TH1F* h_PU_silver_up   = (TH1F*) f_PU_silver_up  .Get("pileup") ;
  TH1F* h_PU_silver      = (TH1F*) f_PU_silver     .Get("pileup") ;
  
  h_PU_golden     ->Scale(1.0/h_PU_golden     ->GetSumOfWeights()) ;
  h_PU_silver_down->Scale(1.0/h_PU_silver_down->GetSumOfWeights()) ;
  h_PU_silver_up  ->Scale(1.0/h_PU_silver_up  ->GetSumOfWeights()) ;
  h_PU_silver     ->Scale(1.0/h_PU_silver     ->GetSumOfWeights()) ;
  
  float n_golden_raw = 0 ;
  float n_golden_w   = 0 ;
  
  for(int bin=1 ; bin<=h_PU_MC->GetNbinsX() ; ++bin){
    n_golden_w   += h_PU_golden->GetBinContent(bin)/h_PU_MC->GetBinContent(bin) ;
    n_golden_raw += h_PU_golden->GetBinContent(bin) ;
  }
  std::cout << n_golden_w << " " << n_golden_raw << std::endl ;
}
  