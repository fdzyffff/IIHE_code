void reskim_all(){
  
  bool do_data = true ;
  bool do_MC   = false ;
  
  if(do_data){

    TChain* ch_data_2016G_v6_Sv5_0 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v6_Sv5_1 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v6_Sv5_2 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v6_Sv5_3 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v6_Sv5_4 = new TChain("IIHEAnalysis") ;

    ch_data_2016G_v6_Sv5_0->Add("D_v6_S_v5/0000/*.root") ;
    ch_data_2016G_v6_Sv5_1->Add("D_v6_S_v5/0001/*.root") ;
    ch_data_2016G_v6_Sv5_2->Add("D_v6_S_v5/0002/*.root") ;
    ch_data_2016G_v6_Sv5_3->Add("D_v6_S_v5/0003/*.root") ;
    ch_data_2016G_v6_Sv5_4->Add("D_v6_S_v5/0004/*.root") ;

    reskim reskim_data_2016G_v6_Sv5_0(ch_data_2016G_v6_Sv5_0, true, false, false, 6, 5) ;
    reskim_data_2016G_v6_Sv5_0.Loop("ntuples/reskim/data_2016G_SingleElectron_0_v6_Sv5.root") ;

    reskim reskim_data_2016G_v6_Sv5_1(ch_data_2016G_v6_Sv5_1, true, false, false, 6, 5) ;
    reskim_data_2016G_v6_Sv5_1.Loop("ntuples/reskim/data_2016G_SingleElectron_1_v6_Sv5.root") ;

    reskim reskim_data_2016G_v6_Sv5_2(ch_data_2016G_v6_Sv5_2, true, false, false, 6, 5) ;
    reskim_data_2016G_v6_Sv5_2.Loop("ntuples/reskim/data_2016G_SingleElectron_2_v6_Sv5.root") ;

    reskim reskim_data_2016G_v6_Sv5_3(ch_data_2016G_v6_Sv5_3, true, false, false, 6, 5) ;
    reskim_data_2016G_v6_Sv5_3.Loop("ntuples/reskim/data_2016G_SingleElectron_3_v6_Sv5.root") ;

    reskim reskim_data_2016G_v6_Sv5_4(ch_data_2016G_v6_Sv5_4, true, false, false, 6, 5) ;
    reskim_data_2016G_v6_Sv5_4.Loop("ntuples/reskim/data_2016G_SingleElectron_4_v6_Sv5.root") ;

    TChain* ch_data_2016G_v7_Sv6_0 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v7_Sv6_1 = new TChain("IIHEAnalysis") ;

    ch_data_2016G_v7_Sv6_0->Add("D_v7_S_v6/0000/*.root") ;
    ch_data_2016G_v7_Sv6_1->Add("D_v7_S_v6/0001/*.root") ;

    reskim reskim_data_2016G_v7_Sv6_0(ch_data_2016G_v7_Sv6_0, true, false, false, 7, 6) ;
    reskim_data_2016G_v7_Sv6_0.Loop("ntuples/reskim/data_2016G_SingleElectron_0_v7_Sv6.root") ;

    reskim reskim_data_2016G_v7_Sv6_1(ch_data_2016G_v7_Sv6_1, true, false, false, 7, 6) ;
    reskim_data_2016G_v7_Sv6_1.Loop("ntuples/reskim/data_2016G_SingleElectron_1_v7_Sv6.root") ;

    TChain* ch_data_2016G_v8_Sv7_0 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v8_Sv7_1 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v8_Sv7_2 = new TChain("IIHEAnalysis") ;
    TChain* ch_data_2016G_v8_Sv7_3 = new TChain("IIHEAnalysis") ;

    ch_data_2016G_v8_Sv7_0->Add("D_v8_S_v7/0000/*.root") ;
    ch_data_2016G_v8_Sv7_1->Add("D_v8_S_v7/0001/*.root") ;
    ch_data_2016G_v8_Sv7_2->Add("D_v8_S_v7/0002/*.root") ;
    ch_data_2016G_v8_Sv7_3->Add("D_v8_S_v7/0003/*.root") ;

    reskim reskim_data_2016G_v8_Sv7_0(ch_data_2016G_v8_Sv7_0, true, false, false, 8, 7) ;
    reskim_data_2016G_v8_Sv7_0.Loop("ntuples/reskim/data_2016G_SingleElectron_0_v8_Sv7.root") ;

    reskim reskim_data_2016G_v8_Sv7_1(ch_data_2016G_v8_Sv7_1, true, false, false, 8, 7) ;
    reskim_data_2016G_v8_Sv7_1.Loop("ntuples/reskim/data_2016G_SingleElectron_1_v8_Sv7.root") ;

    reskim reskim_data_2016G_v8_Sv7_2(ch_data_2016G_v8_Sv7_2, true, false, false, 8, 7) ;
    reskim_data_2016G_v8_Sv7_2.Loop("ntuples/reskim/data_2016G_SingleElectron_2_v8_Sv7.root") ;

    reskim reskim_data_2016G_v8_Sv7_3(ch_data_2016G_v8_Sv7_3, true, false, false, 8, 7) ;
    reskim_data_2016G_v8_Sv7_3.Loop("ntuples/reskim/data_2016G_SingleElectron_3_v8_Sv7.root") ;

  }
  
  if(do_MC){
    TChain* ch_ttbar1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar3 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WW    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WZ    		= new TChain("IIHEAnalysis") ;
    TChain* ch_ZZ    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ZToEE 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToEE1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToEE2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToTT1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToTT2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ST_top 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ST_antitop 	= new TChain("IIHEAnalysis") ;
     
    ch_ttbar1	 ->Add("/pnfs/iihe/cms/store/user/wenxing/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-RunIISpring16DR80/160524_115211/0000/*.root") ;
    ch_ttbar2	 ->Add("/pnfs/iihe/cms/store/user/wenxing/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-RunIISpring16DR80/160524_115211/0001/*.root") ;
    ch_ttbar3	 ->Add("/pnfs/iihe/cms/store/user/wenxing/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-RunIISpring16DR80/160524_115211/0002/*.root") ;
    ch_WW   	 ->Add("/pnfs/iihe/cms/store/user/wenxing/WW_TuneCUETP8M1_13TeV-pythia8/crab_WW_TuneCUETP8M1_RunIISpring16DR80/160517_131936/0000/*.root") ;
    ch_WZ   	 ->Add("/pnfs/iihe/cms/store/user/wenxing/WZ_TuneCUETP8M1_13TeV-pythia8/crab_WZ_TuneCUETP8M1_RunIISpring16DR80/160517_132244/0000/*.root") ;
    ch_ZZ   	 ->Add("/pnfs/iihe/cms/store/user/wenxing/ZZ_TuneCUETP8M1_13TeV-pythia8/crab_ZZ_TuneCUETP8M1_RunIISpring16DR80/160524_102134/0000/*.root") ;
    ch_WJets1	 ->Add("/pnfs/iihe/cms/store/user/wenxing/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-RunIISpring16DR80/160525_112135/0000/*.root") ;
    ch_WJets2	 ->Add("/pnfs/iihe/cms/store/user/wenxing/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-RunIISpring16DR80/160525_112135/0001/*.root") ;
    ch_DYToTT1	 ->Add("/pnfs/iihe/cms/store/user/wenxing/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1-amcatnloFXFX-RunIISpring16DR80/160517_131653/0000/*.root"  ) ;
    ch_DYToTT2	 ->Add("/pnfs/iihe/cms/store/user/wenxing/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1-amcatnloFXFX-RunIISpring16DR80/160517_131653/0001/*.root"  ) ;
    ch_DYToEE1	 ->Add("/pnfs/iihe/cms/store/user/wenxing/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1-amcatnloFXFX-RunIISpring16DR80/160517_131653/0000/*.root"  ) ;
    ch_DYToEE2	 ->Add("/pnfs/iihe/cms/store/user/wenxing/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1-amcatnloFXFX-RunIISpring16DR80/160517_131653/0001/*.root"  ) ;
    ch_ST_top	 ->Add("/pnfs/iihe/cms/store/user/wenxing/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_tW_top_5f_inclusiveDecays-powheg-RunIISpring16DR80/160517_133000/0000/*.root"  ) ;
    ch_ST_antitop->Add("/pnfs/iihe/cms/store/user/wenxing/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_tW_antitop_5f_inclusiveDecays-powheg-RunIISpring16DR80/160517_132738/0000/*.root"  ) ;
    ch_ZToEE	 ->Add("/pnfs/iihe/cms/store/user/wenxing/ZToEE_NNPDF30_13TeV-powheg_M_50_120/crab_ZToEE_NNPDF30_13TeV-powheg_M_50_120_RunIISpring16DR80/160517_090136/0000/*.root"  ) ;
         
    reskim reskim_ttbar1(ch_ttbar1, false, false, false) ;
    reskim_ttbar1.Loop("ntuples/reskim/ttbar1.root") ;
    
    reskim reskim_ttbar2(ch_ttbar2, false, false, false) ;
    reskim_ttbar2.Loop("ntuples/reskim/ttbar2.root") ;

    reskim reskim_ttbar3(ch_ttbar3, false, false, false) ;
    reskim_ttbar3.Loop("ntuples/reskim/ttbar3.root") ;

    reskim reskim_WW   (ch_WW   , false, false, false) ;
    reskim_WW   .Loop("ntuples/reskim/WW.root") ;
    
    reskim reskim_WZ   (ch_WZ   , false, false, false) ;
    reskim_WZ   .Loop("ntuples/reskim/WZ.root") ;

    reskim reskim_ZZ   (ch_ZZ   , false, false, false) ;
    reskim_ZZ   .Loop("ntuples/reskim/ZZ.root") ;

    reskim reskim_WJets1(ch_WJets1, false, false, true ) ;
    reskim_WJets1.Loop("ntuples/reskim/WJets1.root") ;

    reskim reskim_WJets2(ch_WJets2, false, false, true ) ;
    reskim_WJets2.Loop("ntuples/reskim/WJets2.root") ;
   
    reskim reskim_DYToTT1(ch_DYToTT1, false, true , false) ;
    reskim_DYToTT1.Loop("ntuples/reskim/DYToTT1.root") ;

    reskim reskim_DYToTT2(ch_DYToTT2, false, true , false) ;
    reskim_DYToTT2.Loop("ntuples/reskim/DYToTT2.root") ;

    reskim reskim_DYToEE1(ch_DYToEE1, false, false , false, 0, true) ;
    reskim_DYToEE1.Loop("ntuples/reskim/DYToEE1.root") ;

    reskim reskim_DYToEE2(ch_DYToEE2, false, false , false, 0, true) ;
    reskim_DYToEE2.Loop("ntuples/reskim/DYToEE2.root") ;

    reskim reskim_ST(ch_ST_top, false, false, false) ;
    reskim_ST.Loop("ntuples/reskim/ST_top.root") ;

    reskim reskim_STa(ch_ST_antitop, false, false, false) ;
    reskim_STa.Loop("ntuples/reskim/ST_antitop.root") ;
  
    reskim reskim_ZToEE(ch_ZToEE, false, false, false) ;
    reskim_ZToEE.Loop("ntuples/reskim/ZToEE.root") ;
  }
  
}

