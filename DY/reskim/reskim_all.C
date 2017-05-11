void reskim_all(){
  
  bool do_data = true ;
  bool do_MC   = false ;
  
  if(do_data){
//    TChain* ch_data_2016B_v3 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v3->Add("D_v3/*.root") ;
//    reskim reskim_data_2016B_v3(ch_data_2016B_v3, true, false, false, false, 3, 0, 274442) ;
//    reskim_data_2016B_v3.Loop("ntuples/reskim/data_2016B_DoubleEG_v3.root") ;
//
//    TChain* ch_data_2016B_v4 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v4->Add("D_v4/*.root") ;
//    reskim reskim_data_2016B_v4(ch_data_2016B_v4, true, false, false, false, 4, 274954, 275066) ;
//    reskim_data_2016B_v4.Loop("ntuples/reskim/data_2016B_DoubleEG_v4.root") ;
//
//    TChain* ch_data_2016B_v5 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v5->Add("D_v5/*.root") ;
//    reskim reskim_data_2016B_v5(ch_data_2016B_v5, true, false, false, false, 5, 275067, 275318) ;
//    reskim_data_2016B_v5.Loop("ntuples/reskim/data_2016B_DoubleEG_v5.root") ;
//
//    TChain* ch_data_2016B_v6 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v6->Add("D_v6/*.root") ;
//    reskim reskim_data_2016B_v6(ch_data_2016B_v6, true, false, false, false, 6, 275319, 276834) ;
//    reskim_data_2016B_v6.Loop("ntuples/reskim/data_2016E_DoubleEG_v6.root") ;
//
//    TChain* ch_data_2016B_v7 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v7->Add("D_v7/*.root") ;
//    reskim reskim_data_2016B_v7(ch_data_2016B_v7, true, false, false, false, 7, 0, 278240) ;
//    reskim_data_2016B_v7.Loop("ntuples/reskim/data_2016F_DoubleEG_v7.root") ;
//
//    TChain* ch_data_2016B_v8 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v8->Add("D_v8/*.root") ;
//    reskim reskim_data_2016B_v8(ch_data_2016B_v8, true, false, false, false, 8, 278270, 999999) ;
//    reskim_data_2016B_v8.Loop("ntuples/reskim/data_2016F_DoubleEG_v8.root") ;
//
    TChain* ch_data_2016G_v9 = new TChain("IIHEAnalysis") ;
    ch_data_2016G_v9->Add("rB/00111/*.root") ;
    reskim reskim_data_2016G_v9(ch_data_2016G_v9, true, false, false, false, 51, 0, 999999) ;
    reskim_data_2016G_v9.Loop("ntuples/reskim/data_2016G_SingleElectron_0011_rB.root") ;


  
  }
  
  if(do_MC){
    TChain* ch_ttbar0 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar3 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar4 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar5 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar6 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WW    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WZ    		= new TChain("IIHEAnalysis") ;
    TChain* ch_ZZ    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets0 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets3 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets4 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets5 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets6 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ZToEE 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToEE0 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToEE1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToEE2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL0 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL3 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL4 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL5 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ST_top 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ST_antitop 	= new TChain("IIHEAnalysis") ;
     
    ch_ttbar0	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0000/*.root") ;
    ch_ttbar1	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0001/*.root") ;
    ch_ttbar2	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0002/*.root") ;
    ch_ttbar3	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0003/*.root") ;
    ch_ttbar4	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0004/*.root") ;
    ch_ttbar5	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0005/*.root") ;
    ch_ttbar6	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0006/*.root") ;
    ch_WW   	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WW/161121_151603/0000/*.root") ;
    ch_WZ   	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WZ/161121_151741/0000/*.root") ;
    ch_ZZ   	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_ZZ/161120_172246/0000/*.root") ;
    ch_WJets0	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0000/*.root") ;
    ch_WJets1	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0001/*.root") ;
    ch_WJets2	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0002/*.root") ;
    ch_WJets3	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0003/*.root") ;
    ch_WJets4	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0004/*.root") ;
    ch_WJets5	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0005/*.root") ;
    ch_WJets6	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0006/*.root") ;
    ch_DYToLL0	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0000/*.root") ;
    ch_DYToLL1	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0001/*.root") ;
    ch_DYToLL2	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0002/*.root") ;
    ch_DYToLL3	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0003/*.root") ;
    ch_DYToLL4	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0004/*.root") ;
    ch_DYToLL5	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0005/*.root") ;
    ch_DYToEE0	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYToEE_NNPDF30_13TeV-powheg-pythia8/crab_DYToEE_NNPDF30_13TeV-powheg-pythia8/161119_212555/0000/*.root") ;
    ch_DYToEE1	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYToEE_NNPDF30_13TeV-powheg-pythia8/crab_DYToEE_NNPDF30_13TeV-powheg-pythia8/161119_212555/0001/*.root") ;
    ch_DYToEE2	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYToEE_NNPDF30_13TeV-powheg-pythia8/crab_DYToEE_NNPDF30_13TeV-powheg-pythia8/161119_212555/0002/*.root") ;
    ch_ST_top	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_top/161120_172319/0000/*.root") ;
    ch_ST_antitop->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_antitop/161120_172209/0000/*.root") ;
         
//    reskim reskim_DYToEE0(ch_DYToEE0, false, false , false, false) ;
//    reskim_DYToEE0.Loop("ntuples/reskim/DYToEE0.root") ;

//    reskim reskim_DYToEE1(ch_DYToEE1, false, false , false, false) ;
//    reskim_DYToEE1.Loop("ntuples/reskim/DYToEE1.root") ;
//
//    reskim reskim_DYToEE2(ch_DYToEE2, false, false , false, false) ;
//    reskim_DYToEE2.Loop("ntuples/reskim/DYToEE2.root") ;


//    reskim reskim_WZ   (ch_WZ   , false, false, false ) ;
//    reskim_WZ   .Loop("ntuples/reskim/WZ.root") ;
//
//    reskim reskim_ttbar0(ch_ttbar1, false, false, false) ;
//    reskim_ttbar0.Loop("ntuples/reskim/ttbar0.root") ;

//    reskim reskim_ttbar1(ch_ttbar1, false, false, false) ;
//    reskim_ttbar1.Loop("ntuples/reskim/ttbar1.root") ;
//
//    reskim reskim_ttbar2(ch_ttbar2, false, false, false) ;
//    reskim_ttbar2.Loop("ntuples/reskim/ttbar2.root") ;
//
//    reskim reskim_ttbar3(ch_ttbar3, false, false, false) ;
//    reskim_ttbar3.Loop("ntuples/reskim/ttbar3.root") ;
//
//    reskim reskim_ttbar4(ch_ttbar4, false, false, false) ;
//    reskim_ttbar4.Loop("ntuples/reskim/ttbar4.root") ;
    
//    reskim reskim_WW   (ch_WW   , false, false, false) ;
//    reskim_WW   .Loop("ntuples/reskim/WW.root") ;
//    
//    reskim reskim_ZZ   (ch_ZZ   , false, false, false) ;
//    reskim_ZZ   .Loop("ntuples/reskim/ZZ.root") ;
//
//    reskim reskim_WJets0(ch_WJets0, false, false, true ) ;
//    reskim_WJets0.Loop("ntuples/reskim/WJets0.root") ;

//    reskim reskim_WJets1(ch_WJets1, false, false, true ) ;
//    reskim_WJets1.Loop("ntuples/reskim/WJets1.root") ;
//
//    reskim reskim_WJets2(ch_WJets2, false, false, true ) ;
//    reskim_WJets2.Loop("ntuples/reskim/WJets2.root") ;

    reskim reskim_WJets3(ch_WJets3, false, false, true ) ;
    reskim_WJets3.Loop("ntuples/reskim/WJets3.root") ;

    reskim reskim_WJets4(ch_WJets4, false, false, true ) ;
    reskim_WJets4.Loop("ntuples/reskim/WJets4.root") ;

    reskim reskim_WJets5(ch_WJets5, false, false, true ) ;
    reskim_WJets5.Loop("ntuples/reskim/WJets5.root") ;

    reskim reskim_WJets6(ch_WJets6, false, false, true ) ;
    reskim_WJets6.Loop("ntuples/reskim/WJets6.root") ;

//    reskim reskim_DYToLL0(ch_DYToLL0, false, true , false) ;
//    reskim_DYToLL0.Loop("ntuples/reskim/DYToLL0.root") ;

    reskim reskim_DYToLL1(ch_DYToLL1, false, true , false) ;
    reskim_DYToLL1.Loop("ntuples/reskim/DYToLL1.root") ;

    reskim reskim_DYToLL2(ch_DYToLL2, false, true , false) ;
    reskim_DYToLL2.Loop("ntuples/reskim/DYToLL2.root") ;

    reskim reskim_DYToLL3(ch_DYToLL3, false, true , false) ;
    reskim_DYToLL3.Loop("ntuples/reskim/DYToLL3.root") ;

    reskim reskim_DYToLL4(ch_DYToLL4, false, true , false) ;
    reskim_DYToLL4.Loop("ntuples/reskim/DYToLL4.root") ;

    reskim reskim_DYToLL5(ch_DYToLL5, false, true , false) ;
    reskim_DYToLL5.Loop("ntuples/reskim/DYToLL5.root") ;

//    reskim reskim_ST(ch_ST_top, false, false, false) ;
//    reskim_ST.Loop("ntuples/reskim/ST_top.root") ;
//
//    reskim reskim_STa(ch_ST_antitop, false, false, false) ;
//    reskim_STa.Loop("ntuples/reskim/ST_antitop.root") ;
  
  }
  
}

