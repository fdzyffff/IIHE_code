#include "TMath.h"
#include "TRandom3.h"

namespace trigEle35{


  TRandom3 randNrGen;
  float turnOnfunction(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
    float eff = 0.0;
    eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
    return eff;
  }
  
  float turnOn_MW(float scEt,float scEta){
    if (scEt <= 40)
    {
      if (0.0<=fabs(scEta) && fabs(scEta)<=1.4442)
        return turnOnfunction(scEt,0.6843, 36.1, 0.5742, 35.5, 60.82, 7.506);
      else if (1.566<=fabs(scEta) && fabs(scEta)<=2.5)
        return turnOnfunction(scEt,0.6018, 36.57, 1.114, 0.07188, 39.11, 0.469);
      else
        return -1.0;
     }
     else
     {
      if (0.0<=fabs(scEta) && fabs(scEta)<=1.4442)
        return turnOnfunction(scEt,0.6343, 25.65, 9.226, 0.2579, 21.61, 37.93);
      else if (1.566<=fabs(scEta) && fabs(scEta)<=2.5)
        return turnOnfunction(scEt,0.6539, 35.51, 4.037, 0.2153, 37.33, 38.0);
      else
        return -1.0;
     }
  }
  
  bool passTrig(float scEt,float scEta){return turnOn_MW(scEt,scEta)>randNrGen.Uniform(0,1);}
  //bool passTrig(float scEt,float scEta){return turnOn_MW(scEt,scEta)>randNrGen.Uniform(0,1);}

}
  
