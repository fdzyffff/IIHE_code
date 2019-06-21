#include "TCanvas.h"
#include "TF1.h"

#include "turnonEle33.C"
#include "turnonEle35.C"
#include "turnonEle33l1.C"
void turnonTest()
{
   TCanvas *c1 = new TCanvas("c1", "test_hc" , 200,10,700,500);
   c1->SetGrid();
   TH1F *h1 = new TH1F("h1", "turn on test hist", 500, 30, 80);

   Double_t eta = 2.150;
   Double_t Et = 30;
   for(Et = 25; Et<80; Et+=0.01)
   {
      for(int i = 0; i<10000; i++)
      {
          if(trigEle35::passTrig(Et, eta))
          {
             h1->Fill(Et);
          }
      }
   }
   h1->Draw("");
   c1->Update();
   
}
