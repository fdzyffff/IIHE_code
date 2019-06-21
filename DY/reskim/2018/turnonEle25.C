#include "TMath.h"
#include "TRandom3.h"

namespace trigEle25{


  TRandom3 randNrGen;
  float turnOnfunction(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
    float eff = 0.0;
    eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
    return eff;
  }
  
  float turnOn_MW(float scEt,float scEta){
    if (0.0<=fabs(scEta) && fabs(scEta)<0.79)
      return turnOnfunction(scEt, 0.912, 33.79, 0.4654, 0.06635, 34.51, 2.517);
    else if (0.79<=fabs(scEta) && fabs(scEta)<1.1)
      return turnOnfunction(scEt, 0.8773, 33.85, 0.541, 0.1008, 34.42, 2.383);
    else if (1.1<=fabs(scEta) && fabs(scEta)<1.4442)
      return turnOnfunction(scEt, 0.8864, 34.23, 0.7141, 0.08538, 34.00, 2.671);
    else if (1.566<=fabs(scEta) && fabs(scEta)<1.70)
      return turnOnfunction(scEt, 0.8303, 34.08, 0.7835, 0.1395, 34.29, 2.818);
    else if (1.70<=fabs(scEta) && fabs(scEta)<2.1)
      return turnOnfunction(scEt, 0.7842, 34.25, 0.7481, 0.201, 34.47, 1.889);
    else if (2.1<=fabs(scEta) && fabs(scEta)<2.5)
      return turnOnfunction(scEt, 0.5522, 34.5, 0.8883, 0.42588, 35.34, 1.851);
    else
      return -1.0;
  }
  
  bool passTrig(float scEt,float scEta){return turnOn_MW(scEt,scEta)>randNrGen.Uniform(0,1);}
  //bool passTrig(float scEt,float scEta){return turnOn_MW(scEt,scEta)>randNrGen.Uniform(0,1);}

}
  
