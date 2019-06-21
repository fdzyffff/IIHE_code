#include "TMath.h"
#include "TRandom3.h"

namespace fkmuon{
  
//float FRweight(float eta, float pt){
//  float FR = 0.0;
//  float FR_Ptcut = 53.0;
//  if(fabs(eta)<1.2 && pt>FR_Ptcut)
//    {
//      FR = 2.67532e+00*TMath::Landau(pt,1.02643e+03,4.36449e+02,0);
//    }
//  else if(fabs(eta)>1.2  && fabs(eta)<2.4 && pt>FR_Ptcut)
//    {
//      FR = 2.52245e+00*TMath::Landau(pt,4.93427e+02,2.56237e+02,0);
//    }
//  else {
//    cout<<"out of FR range"<<endl;
//  }
//  return (FR/(1-FR));
//}

//FR for 2018 data 
float FRweight(float eta, float pt){
  float FR = 0.0;
  float FR_Ptcut = 53.0;
  if(fabs(eta)<1.2 && pt>FR_Ptcut)
    {
      FR = 2.65491e+00*TMath::Landau(pt,1.40077e+03,6.82333e+02,0);
    }
  else if(fabs(eta)>1.2  && fabs(eta)<2.4 && pt>FR_Ptcut)
    {
      FR = 2.47728e+00*TMath::Landau(pt,5.20390e+02,2.28904e+02,0);
    }
  else {
    cout<<"out of FR range"<<endl;
  }
  return (FR/(1-FR));
}
}
