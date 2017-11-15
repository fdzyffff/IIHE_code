#ifndef DIELESCALEFACTORS_ELE27WPLOOSETRIGTURN_C
#define DIELESCALEFACTORS_ELE27WPLOOSETRIGTURN_C

#include "TMath.h"
#include "TRandom3.h"

namespace trigEle33{


  TRandom3 randNrGen;
  float turnOnfunction(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
    float eff = 0.0;
    eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
    return eff;
  }
  
  float turnOn(float scEt,float scEta){
    if (0.0<=fabs(scEta) && fabs(scEta)<0.79)
      return turnOnfunction(scEt,0.286,35.3,1.87,0.711,33.6,0.443);
    else if (0.79<=fabs(scEta) && fabs(scEta)<1.1)
      return turnOnfunction(scEt,0.548,34,0.563,0.45,36.1,1.85);
    else if (1.1<=fabs(scEta) && fabs(scEta)<1.4442)
      return turnOnfunction(scEt,0.444,35.4,0.974,0.552,37.7,2.06);
    else if (1.566<=fabs(scEta) && fabs(scEta)<1.70)
      return turnOnfunction(scEt,0.576,35,1.09,0.423,36.5,2.41);
    else if (1.70<=fabs(scEta) && fabs(scEta)<2.1)
      return turnOnfunction(scEt,0.788,34.3,0.904,0.212,34.3,1.87);
    else if (2.1<=fabs(scEta) && fabs(scEta)<2.5)
      return turnOnfunction(scEt,0.978,34.8,1.31,0.0272,36.3,4.56);
    else
      return -1.0;
  }
  
  bool passTrig(float scEt,float scEta){return turnOn(scEt,scEta)>randNrGen.Uniform(0,1);}

}
  


#endif
