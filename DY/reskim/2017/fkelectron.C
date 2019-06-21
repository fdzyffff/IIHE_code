#include "TMath.h"
#include "TRandom3.h"

namespace fkelectron{

float frFuncData(float et,float eta)
{
   if(std::abs(eta)<1.5){
     if(et<131.424) return 
0.105781+-0.00251823*et+2.28326e-05*et*et+-7.21185e-08*et*et*et;
     else if(et>=131.424 && et<355.514) return 
0.0137969+-0.000103437*et+3.61974e-07*et*et+-4.25465e-10*et*et*et;
     else return 0.00279259+2.42827e-06*et;
   }else if(std::abs(eta)<2.0){
     if(et<121.849) return 0.11723+-0.00129615*et+4.67464e-06*et*et;
     else if(et>=121.849 && et<226.175) return 0.034505+-4.76287e-05*et;
     else return 0.0257885+-9.08954e-06*et;
   }else if(std::abs(eta)<2.5){
     if(et<112.517) return 0.0807503+-0.000341528*et;
     else return 0.0423239;
   }else return 0.;
}

}
  


