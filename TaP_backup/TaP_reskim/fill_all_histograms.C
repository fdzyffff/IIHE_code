void fill_all_histograms(){
  fill_histograms fh ;
  
  bool do_data = true ;
  bool do_MC   = true ;
  
  if(do_data){
    TFile f_data_golden2015BC50ns("ntuples/reskim/data_golden2015BC50ns.root") ;
    TTree* t_data_golden2015BC50ns = (TTree*) f_data_golden2015BC50ns.Get("tap") ;
    fh.Init(t_data_golden2015BC50ns) ;
    fh.Loop("data_golden2015BC50ns") ;
    
    TFile f_data_golden2015C25ns("ntuples/reskim/data_golden2015C25ns.root") ;
    TTree* t_data_golden2015C25ns = (TTree*) f_data_golden2015C25ns.Get("tap") ;
    fh.Init(t_data_golden2015C25ns) ;
    fh.Loop("data_golden2015C25ns") ;
    
    TFile f_data_golden2015D("ntuples/reskim/data_golden2015D.root") ;
    TTree* t_data_golden2015D = (TTree*) f_data_golden2015D.Get("tap") ;
    fh.Init(t_data_golden2015D) ;
    fh.Loop("data_golden2015D") ;
    
    TFile f_data_golden0T25ns("ntuples/reskim/data_golden0T25ns.root") ;
    TTree* t_data_golden0T25ns = (TTree*) f_data_golden0T25ns.Get("tap") ;
    fh.Init(t_data_golden0T25ns) ;
    fh.Loop("data_golden0T25ns") ;
    
    TFile f_data_silverNotGolden("ntuples/reskim/data_silverNotGolden.root") ;
    TTree* t_data_silverNotGolden = (TTree*) f_data_silverNotGolden.Get("tap") ;
    fh.Init(t_data_silverNotGolden) ;
    fh.Loop("data_silverNotGolden") ;
    
    TChain* ch_silver = new TChain("tap") ;
    ch_silver->Add("ntuples/reskim/data_golden2015D.root") ;
    ch_silver->Add("ntuples/reskim/data_silverNotGolden.root") ;
    fh.Init(ch_silver) ;
    fh.Loop("data_silver") ;
  }
  
  if(do_MC){
    TFile f_ttbar("ntuples/reskim/ttbar.root") ;
    TFile f_WW   ("ntuples/reskim/WW.root"   ) ;
    TFile f_WJets("ntuples/reskim/WJets.root") ;
    TFile f_ZToEE("ntuples/reskim/ZToEE.root") ;
    TFile f_ZToTT("ntuples/reskim/ZToTT.root") ;
    
    TTree* t_ttbar = (TTree*) f_ttbar.Get("tap") ;
    TTree* t_WW    = (TTree*) f_WW   .Get("tap") ;
    TTree* t_WJets = (TTree*) f_WJets.Get("tap") ;
    TTree* t_ZToEE = (TTree*) f_ZToEE.Get("tap") ;
    TTree* t_ZToTT = (TTree*) f_ZToTT.Get("tap") ;
    
    fh.Init(t_ttbar) ; fh.Loop("ttbar") ;
    fh.Init(t_WW   ) ; fh.Loop("WW"   ) ;
    fh.Init(t_WJets) ; fh.Loop("WJets") ;
    fh.Init(t_ZToEE) ; fh.Loop("ZToEE") ;
    fh.Init(t_ZToTT) ; fh.Loop("ZToTT") ;
  }
}

