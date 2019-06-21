#include "turnonEle33.C"

void ttt()
{
  float x[200];
  float y[200];
  for (Int_t i=0;i<200;i++) {
    x[i] = 30+i*0.1;
    y[i] = trigEle33::turnOn(x[i],1);
    printf(" i %i %f %f \n",i,x[i],y[i]);
  }
   TGraph *gr = new TGraph(200,x,y);
   gr->SetLineColor(2);
   gr->SetLineWidth(4);
   gr->SetMarkerColor(4);
   gr->SetMarkerStyle(21);
   gr->SetTitle("a simple graph");
   gr->GetXaxis()->SetTitle("X title");
   gr->GetYaxis()->SetTitle("Y title");
   gr->Draw("ACP");

//   TH1F *h1 = new TH1F("h1","xxxxx",20,30,50);
//   for (Int_t i=0; i<20000; i++) {
//   float a;
//   a = 30+i*0.001;
//     if (trigEle33::passTrig(a,1)==1)
//     {
//       h1->Fill(a);
//     }
//   }
//   h1->Draw("");
}
