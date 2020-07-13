#include "TMath.h"
#include "TRandom3.h"
#include <iostream>

namespace fkmuon_2016{
  
float FRweight(float eta, float pt){
/* without Giovanni filter
  float FR = 0.0;
  parEB1 = 1.11018e-01;
  parEB2 = -1.21961e-03;
  parEB3 = 5.27578e-06;
  parEB4 = 2.40160e+00;
  parEB5 = -5.90161e+03;
  parEB6 = 2.28745e+03;
  parEB7 = 4.04533e-01;
  parEE1 = 1.37269e-01;
  parEE2 =-1.08720e-03; 
  parEE3 =  5.62699e-06;
  parEE4 = 2.33319e-01;*/

   /* with Giovanni filter*/
   float FR = 0.0;
   float parEB1 = 1.11040e-01;
   float parEB2 = -1.21997e-03;
   float parEB3 = 5.27748e-06;
   float parEB4 = 2.38002e+00;
   float parEB5 = -5.72651e+03;
   float parEB6 = 2.23475e+03;
   float parEB7 = 4.12519e-01;
   float parEE1 = 1.37352e-01;
   float parEE2 = -1.08994e-03;
   float parEE3 = 5.64918e-06;
   float parEE4 = 2.38683e-01;
  if(fabs(eta)<1.2 && pt>53.0 && pt<=200.0)
     {
       FR = parEB1 + parEB2*pow(pt,1) + parEB3*pow(pt,2);
     }
   else if(fabs(eta)<1.2 && pt>200 && pt<=800.0)
     {
       FR = parEB4 + parEB5 / (parEB6 + pt );
     }
   else if(fabs(eta)<1.2 && pt>800.0)
     {
       FR = parEB7;
     }
   else if(fabs(eta)>1.2  && fabs(eta)<2.4 && pt>53.0 && pt<=250.0)
     {
       FR = parEE1 + parEE2*pow(pt,1) + parEE3*pow(pt,2);
     }
   else if(fabs(eta)>1.2 && fabs(eta)<2.4 && pt>250.0)
     {
       FR = parEE4;
     }
   else {
     std::cout<<"out of FR range"<<std::endl;
   }
   return (FR/(1-FR));
 }

}

namespace fkmuon_2017{

float FRweight(float eta, float pt){
  float FR = 0.0;
  float FR_Ptcut = 53.0;
  if(fabs(eta)<1.2 && pt>FR_Ptcut)
    {
      FR = 2.67532e+00*TMath::Landau(pt,1.02643e+03,4.36449e+02,0);
    }
  else if(fabs(eta)>1.2  && fabs(eta)<2.4 && pt>FR_Ptcut)
    {
      FR = 2.52245e+00*TMath::Landau(pt,4.93427e+02,2.56237e+02,0);
    }
  else {
    std::cout<<"out of FR range"<<std::endl;
  }
  return (FR/(1-FR));
}
}


namespace fkmuon_2018{

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
    std::cout<<"out of FR range"<<std::endl;
  }
  return (FR/(1-FR));
}
}
