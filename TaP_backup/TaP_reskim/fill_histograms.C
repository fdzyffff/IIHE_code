#define fill_histograms_cxx
#include "fill_histograms.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

#include <iostream>

void displayProgress(long current, long max){
  using std::cerr;

  if (current%(max/1000)!=0 && current<max-1) return;

  int width = 52; // Hope the terminal is at least that wide.
  int barWidth = width - 2;
  cerr << "\x1B[2K"; // Clear line
  cerr << "\x1B[2000D"; // Cursor left
  cerr << '[';
  for(int i=0 ; i<barWidth ; ++i){ if(i<barWidth*current/max){ cerr << '=' ; }else{ cerr << ' ' ; } }
  cerr << ']';
  cerr << " " << Form("%8d/%8d (%5.2f%%)", (int)current, (int)max, 100.0*current/max) ;
  cerr.flush();
}

void fill_histograms::Loop(TString sampleName){
   std::cout << sampleName << std::endl ;
   
   time_t time_start = time(0) ;
   char* time_start_text = ctime(&time_start) ;
   std::cout << time_start_text << std::endl ;
   
   if (fChain == 0) return;
   
   int nHistos = 1 ;
   const int NBinnings   =  2 ; nHistos *= NBinnings   ;
   const int NVars       =  4 ; nHistos *= NVars       ;
   const int NRegions    =  3 ; nHistos *= NRegions    ;
   const int NCharges    =  3 ; nHistos *= NCharges    ;
   const int NTagCharges =  3 ; nHistos *= NTagCharges ;
   const int NHEEP       =  3 ; nHistos *= NHEEP       ;
   const int NOSSS       =  3 ; nHistos *= NOSSS       ;
   const int NAltCut     =  4 ; nHistos *= NAltCut     ;
   //const int NJson       =  4 ; nHistos *= NJson       ;
   const int NJson       =  3 ; nHistos *= NJson       ;
   const int NPUW        =  2 ; nHistos *= NPUW        ;
   
   TFile* fBase = new TFile("hBase.root","READ") ;
   
   TFile* file_out = new TFile(Form("ntuples/out/%s_slices.root",sampleName.Data()),"RECREATE") ;
   TH2F* histograms[NBinnings][NVars][NRegions][NCharges][NTagCharges][NOSSS][NAltCut][NJson][NHEEP][NPUW] ;
   
   TString   binningNames[NBinnings  ] = {"cut","fit"} ;
   TString       varNames[NVars      ] = {"Et","eta","phi","nVtx"} ;
   TString    regionNames[NRegions   ] = {"Barrel","Transition","Endcap"} ;
   TString    chargeNames[NCharges   ] = {"em","ep","ea"} ;
   TString tagChargeNames[NTagCharges] = {"tm","tp","ta"} ;
   TString      HEEPNames[NHEEP      ] = {"probes","pass","fail"} ;
   TString      OSSSNames[NOSSS      ] = {"OS","SS","AS"} ;
   TString    altCutNames[NAltCut    ] = {"nominal","gsfIsEcalDriven","noDEtaIn","noIsolation"} ;
   TString      jsonNames[NJson      ] = {"golden","silver","combined"} ;
   TString       PUWNames[NPUW       ] = {"PUW","NoPUW"} ;
   
   //file_in->ls() ;
   std::cout << "Making histograms..." << std::endl ;
   Int_t counter = 0 ;
   for(int iBinning=0 ; iBinning<NBinnings ; ++iBinning){
      for(int iVar=0 ; iVar<NVars ; ++iVar){
        for(int iRegion=0 ; iRegion<NRegions ; ++iRegion){
          TString hBaseName = Form("hBase_2D_%s_%s_%s_mee",
            binningNames[iBinning].Data(),
            varNames[iVar].Data(),
            regionNames[iRegion].Data()) ;
            
          TH2F* hBase = (TH2F*)fBase->Get(hBaseName) ;
	  hBase->Sumw2() ;
          for(int iCharge=0 ; iCharge<NCharges ; ++iCharge){
            for(int iTagCharge=0 ; iTagCharge<NTagCharges ; ++iTagCharge){
              for(int iOSSS=0 ; iOSSS<NOSSS ; ++iOSSS){
                for(int iAltCut=0 ; iAltCut<NAltCut ; ++iAltCut){
                  for(int iJson=0 ; iJson<NJson ; ++iJson){
                    for(int iHEEP=0 ; iHEEP<NHEEP ; ++iHEEP){
                      for(int iPUW=0 ; iPUW<NPUW ; ++iPUW){
                        counter++ ;
                        displayProgress(counter,nHistos) ;
                        TString hName = Form("h_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s",
                              binningNames[iBinning].Data(),
                              sampleName.Data(),
                              varNames[iVar].Data(),
                              regionNames[iRegion].Data(),
                              chargeNames[iCharge].Data(),
                              tagChargeNames[iTagCharge].Data(),
                              OSSSNames[iOSSS].Data(),
                              altCutNames[iAltCut].Data(),
                              jsonNames[iJson].Data(),
                              HEEPNames[iHEEP].Data(),
                              PUWNames[iPUW].Data()) ;
                        TH2F* h2D = (TH2F*) hBase->Clone(hName) ;
                        h2D->Scale(0.0) ;
                        if(!h2D){
                          std::cout << hName << std::endl ;
                        }
                        else{
                          histograms[iBinning][iVar][iRegion][iCharge][iTagCharge][iOSSS][iAltCut][iJson][iHEEP][iPUW] = h2D ;
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
   std::cout << "Done!" << std::endl ;
   time_t time_mid = time(0) ;
   char* time_mid_text = ctime(&time_mid) ;
   std::cout << time_mid_text << std::endl ;
   
   Long64_t nentries = fChain->GetEntries();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      displayProgress(jentry, nentries) ;
      
      int iRegion = p_region-1 ;
      if(iRegion<0 || iRegion>2) continue ;
      int iCharge    = (p_charge<0) ? 0 : 1 ;
      int iTagCharge = (t_charge<0) ? 0 : 1 ;
      int iOSSS      = (OS        ) ? 0 : 1 ;
      
      float var_values[NVars] = {p_Et, p_eta, p_phi, (float)1.0*pv_n} ;
      for(int iB=0 ; iB<NBinnings ; ++iB){
        for(int iVar=0 ; iVar<NVars ; ++iVar){
          float v = var_values[iVar] ;
          float Et_threshold = (iVar==0) ? 20.0 : 35.0 ;
          if(p_Et < Et_threshold) continue ;
          for(int iA=0 ; iA<NAltCut ; ++iA){
            bool fill_1HEEP = true ;
            int pass_or_fail = 0 ; // 1 for pass, 2 for fail
            switch(iA){
              case 0: pass_or_fail = (p_ID_nominal    ) ? 1 : 2 ; break ;
              case 1:
                if(p_ID_EcalDriven==false){
                  fill_1HEEP = false ;
                break ;
                }
                pass_or_fail = (p_ID_nominal) ? 1 : 2 ;
                break ;
              case 2: pass_or_fail = (p_ID_noDEtaIn   ) ? 1 : 2 ; break ;
              case 3: pass_or_fail = (p_ID_noIsolation) ? 1 : 2 ; break ;
            }
            int iCharges   [2] = {iCharge   ,2} ;
            int iOSSSS     [2] = {iOSSS     ,2} ;
            int iTagCharges[2] = {iTagCharge,2} ;
            
            for(int iC=0 ; iC<2 ; ++iC){
              for(int iO=0 ; iO<2 ; ++iO){
                for(int iJson=0 ; iJson<NJson ; ++iJson){
                  float w = w_PU[iJson] ;
                  if(w<0 || isnan(w)) continue ;
                  for(int iT=0 ; iT<2 ; ++iT){
                    if(fill_1HEEP){
                      histograms[iB][iVar][iRegion][iCharges[iC]][iTagCharges[iT]][iOSSSS[iO]][iA][iJson][0][0]->Fill(v, mee, w) ;
                      histograms[iB][iVar][iRegion][iCharges[iC]][iTagCharges[iT]][iOSSSS[iO]][iA][iJson][0][1]->Fill(v, mee) ;
                      if(pass_or_fail==1){
                        histograms[iB][iVar][iRegion][iCharges[iC]][iTagCharges[iT]][iOSSSS[iO]][iA][iJson][1][0]->Fill(v, mee, w) ;
                        histograms[iB][iVar][iRegion][iCharges[iC]][iTagCharges[iT]][iOSSSS[iO]][iA][iJson][1][1]->Fill(v, mee) ;
                      }
                      else{
                        histograms[iB][iVar][iRegion][iCharges[iC]][iTagCharges[iT]][iOSSSS[iO]][iA][iJson][2][0]->Fill(v, mee, w) ;
                        histograms[iB][iVar][iRegion][iCharges[iC]][iTagCharges[iT]][iOSSSS[iO]][iA][iJson][2][1]->Fill(v, mee, 1) ;
                      }
                    }
                  }
                }
              }  
            }
          }
        }
      }
   }
   
   std::cout << "Writing histograms..." << std::endl ;
   int nEmpty = 0 ;
   for(int iBinning=0 ; iBinning<NBinnings ; ++iBinning){
      for(int iVar=0 ; iVar<NVars ; ++iVar){
        for(int iRegion=0 ; iRegion<NRegions ; ++iRegion){
          for(int iCharge=0 ; iCharge<NCharges ; ++iCharge){
            for(int iTagCharge=0 ; iTagCharge<NTagCharges ; ++iTagCharge){
              for(int iOSSS=0 ; iOSSS<NOSSS ; ++iOSSS){
                for(int iAltCut=0 ; iAltCut<NAltCut ; ++iAltCut){
                  for(int iJson=0 ; iJson<NJson ; ++iJson){
                    for(int iHEEP=0 ; iHEEP<NHEEP ; ++iHEEP){
                      for(int iPUW=0 ; iPUW<NPUW ; ++iPUW){
                        TH2F* h = histograms[iBinning][iVar][iRegion][iCharge][iTagCharge][iOSSS][iAltCut][iJson][iHEEP][iPUW] ;
                        if(h->GetSumOfWeights()<1e-3){
                          nEmpty++ ;
                        }
                        h->Write() ;
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
   }
   std::cout << nEmpty << " empty histograms of " << nHistos << std::endl ;
   file_out->Close() ;
   
   time_t time_end = time(0) ;
   char* time_end_text = ctime(&time_end) ;
   std::cout << time_end_text << std::endl ;
}
