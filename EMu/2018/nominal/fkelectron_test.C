#include "fkelectron_2018.C"


void fkelectron_test() {
  float i;

  TGraph *gr_1 = new TGraph()
  for (i = 1.0; i < 300; i += 1.0) {
    fr = fkelectron_2018::frFuncData(1, i, 1, 1, 1);
    gr_1.SetPoint(i, fr);
  }
  //std::cout<<"Et : "<<i<<"  fake rate : "<<fr<<std::endl ;
  gr_1.Draw("APC");
  c1.Update();
 
    
  }
}
//#fkelectron_2018.frFuncData(ev_run, ele->p4.Et(), ele->p4_sc.Eta(), ele->p4.Eta(), ele->p4.Phi()) ;
