void reskim_all(){
  
  bool do_data = false ;
  bool do_MC   = true ;
  
  if(do_data){
//    TChain* ch_data_2016B_v2 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v2->Add("M_v2/*.root") ;
//    reskim reskim_data_2016B_v2(ch_data_2016B_v2, true, false, false, false, 0, 2, 0, 999999) ;
//    reskim_data_2016B_v2.Loop("ntuples/reskim/data_2016_SingleMuon_v2.root") ;
//
//    TChain* ch_data_2016B_v3 = new TChain("IIHEAnalysis") ;
//    ch_data_2016B_v3->Add("M_v3/*.root") ;
//    reskim reskim_data_2016B_v3(ch_data_2016B_v3, true, false, false, false, 0, 3, 0, 999999) ;
//    reskim_data_2016B_v3.Loop("ntuples/reskim/data_2016_SingleMuon_v3.root") ;

    TChain* ch_data_2016B_v4 = new TChain("IIHEAnalysis") ;
    ch_data_2016B_v4->Add("M_v4/*.root") ;
    reskim reskim_data_2016B_v4(ch_data_2016B_v4, true, false, false, false, 0, 4, 0, 999999) ;
    reskim_data_2016B_v4.Loop("ntuples/reskim/data_2016G_SingleMuon_v4.root") ;

  
  }
  
  if(do_MC){
    TChain* ch_ttbar0 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar3 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar4 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar5 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ttbar6 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WW1    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WW2    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WW3    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WW4    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WW5    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WZ    		= new TChain("IIHEAnalysis") ;
    TChain* ch_ZZ    		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets0 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets3 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets4 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets5 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets6 		= new TChain("IIHEAnalysis") ;
    TChain* ch_WJets7 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ZToEE 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL0 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL1 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL2 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL3 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL4 		= new TChain("IIHEAnalysis") ;
    TChain* ch_DYToLL5 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ST_top 		= new TChain("IIHEAnalysis") ;
    TChain* ch_ST_antitop 	= new TChain("IIHEAnalysis") ;
     
    ch_WW1   	 ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/WWTo2L2Nu_13TeV-powheg/crab_WWTo2L2Nu_13TeV-powheg/161122_133543/0000/*.root") ;
    ch_WW2   	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WWTo2L2Nu_200To600/161121_151541/0000/*.root") ;
    ch_WW3   	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WWTo2L2Nu_600To1200/161121_151650/0000/*.root") ;
    ch_WW4   	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WWTo2L2Nu_1200To2500/161121_151626/0000/*.root") ;
    ch_WW5   	 ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WWTo2L2Nu_2500ToInf/161121_151715/0000/*.root") ;

    ch_ttbar0    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0000/*.root") ;
    ch_ttbar1    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0001/*.root") ;
    ch_ttbar2    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0002/*.root") ;
    ch_ttbar3    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0003/*.root") ;
    ch_ttbar4    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0004/*.root") ;
    ch_ttbar5    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0005/*.root") ;
    ch_ttbar6    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT/161120_173422/0006/*.root") ;
    ch_WZ        ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WZ/161121_151741/0000/*.root") ;
    ch_ZZ        ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_ZZ/161120_172246/0000/*.root") ;


    ch_WJets0    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0000/*.root") ;
    ch_WJets1    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0001/*.root") ;
    ch_WJets2    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0002/*.root") ;
    ch_WJets3    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0003/*.root") ;
    ch_WJets4    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0004/*.root") ;
    ch_WJets5    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0005/*.root") ;
    ch_WJets6    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/crab_WJetsToLNu/0006/*.root") ;
    ch_DYToLL0   ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0000/*.root") ;
    ch_DYToLL1   ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0001/*.root") ;
    ch_DYToLL2   ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0002/*.root") ;
    ch_DYToLL3   ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0003/*.root") ;
    ch_DYToLL4   ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0004/*.root") ;
    ch_DYToLL5   ->Add("/pnfs/iihe/cms/store/user/wenxing/RunIISpring16DR80_20161120/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1_reHLT_new/161119_213445/0005/*.root") ;
    ch_ST_top    ->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_top/161120_172319/0000/*.root") ;
    ch_ST_antitop->Add("/pnfs/iihe/cms/store/user/xgao/2016MCrereco/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_antitop/161120_172209/0000/*.root") ;
         
//    reskim reskim_DYToLL0(ch_DYToLL0, false, false , false, false) ;
//    reskim_DYToLL0.Loop("ntuples/reskim/fk_DYToLL0.root") ;

//    reskim reskim_DYToLL1(ch_DYToLL1, false, false , false, false) ;
//    reskim_DYToLL1.Loop("ntuples/reskim/fk_DYToLL1.root") ;
//
//    reskim reskim_DYToLL2(ch_DYToLL2, false, false , false, false) ;
//    reskim_DYToLL2.Loop("ntuples/reskim/fk_DYToLL2.root") ;
//
//    reskim reskim_DYToLL3(ch_DYToLL3, false, true , false) ;
//    reskim_DYToLL3.Loop("ntuples/reskim/fk_DYToLL3.root") ;
//
//    reskim reskim_DYToLL4(ch_DYToLL4, false, true , false) ;
//    reskim_DYToLL4.Loop("ntuples/reskim/fk_DYToLL4.root") ;
//
//    reskim reskim_DYToLL5(ch_DYToLL5, false, true , false) ;
//    reskim_DYToLL5.Loop("ntuples/reskim/fk_DYToLL5.root") ;
//
////    reskim reskim_ttbar0(ch_ttbar0, false, false, false) ;
////    reskim_ttbar0.Loop("ntuples/reskim/fk_ttbar0.root") ;
//
//    reskim reskim_ttbar1(ch_ttbar1, false, false, false) ;
//    reskim_ttbar1.Loop("ntuples/reskim/fk_ttbar1.root") ;

    reskim reskim_ttbar2(ch_ttbar2, false, false, false) ;
    reskim_ttbar2.Loop("ntuples/reskim/fk_ttbar2.root") ;

    reskim reskim_ttbar3(ch_ttbar3, false, false, false) ;
    reskim_ttbar3.Loop("ntuples/reskim/fk_ttbar3.root") ;
    
    reskim reskim_ttbar4(ch_ttbar4, false, false, false) ;
    reskim_ttbar4.Loop("ntuples/reskim/fk_ttbar4.root") ;

    reskim reskim_ttbar5(ch_ttbar5, false, false, false) ;
    reskim_ttbar5.Loop("ntuples/reskim/fk_ttbar5.root") ;

    reskim reskim_ttbar6(ch_ttbar6, false, false, false) ;
    reskim_ttbar6.Loop("ntuples/reskim/fk_ttbar6.root") ;

//    reskim reskim_WW1   (ch_WW1   , false, false, false) ;
//    reskim_WW1   .Loop("ntuples/reskim/fk_WW1.root") ;
//   
//    reskim reskim_WW2   (ch_WW2   , false, false, false) ;
//    reskim_WW2   .Loop("ntuples/reskim/fk_WW2.root") ;
//
//    reskim reskim_WW3   (ch_WW3   , false, false, false) ;
//    reskim_WW3   .Loop("ntuples/reskim/fk_WW3.root") ;
//
//    reskim reskim_WW4   (ch_WW4   , false, false, false) ;
//    reskim_WW4   .Loop("ntuples/reskim/fk_WW4.root") ;
//
//    reskim reskim_WW5   (ch_WW5  , false, false, false) ;
//    reskim_WW5   .Loop("ntuples/reskim/fk_WW5.root") ;
//
//    reskim reskim_WZ   (ch_WZ   , false, false, false ) ;
//    reskim_WZ   .Loop("ntuples/reskim/fk_WZ.root") ;
// 
//    reskim reskim_ZZ   (ch_ZZ   , false, false, false) ;
//    reskim_ZZ   .Loop("ntuples/reskim/fk_ZZ.root") ;
//
//    reskim reskim_WJets0(ch_WJets0, false, false, true ) ;
//    reskim_WJets0.Loop("ntuples/reskim/fk_WJets0.root") ;

    reskim reskim_WJets1(ch_WJets1, false, false, true ) ;
    reskim_WJets1.Loop("ntuples/reskim/fk_WJets1.root") ;

    reskim reskim_WJets2(ch_WJets2, false, false, true ) ;
    reskim_WJets2.Loop("ntuples/reskim/fk_WJets2.root") ;

    reskim reskim_WJets3(ch_WJets3, false, false, true ) ;
    reskim_WJets3.Loop("ntuples/reskim/fk_WJets3.root") ;

    reskim reskim_WJets4(ch_WJets4, false, false, true ) ;
    reskim_WJets4.Loop("ntuples/reskim/fk_WJets4.root") ;

    reskim reskim_WJets5(ch_WJets5, false, false, true ) ;
    reskim_WJets5.Loop("ntuples/reskim/fk_WJets5.root") ;

    reskim reskim_WJets6(ch_WJets6, false, false, true ) ;
    reskim_WJets6.Loop("ntuples/reskim/fk_WJets6.root") ;

//    reskim reskim_ST(ch_ST_top, false, false, false) ;
//    reskim_ST.Loop("ntuples/reskim/fk_ST_top.root") ;
//
//    reskim reskim_STa(ch_ST_antitop, false, false, false) ;
//    reskim_STa.Loop("ntuples/reskim/fk_ST_antitop.root") ;
  
  }
  
}

