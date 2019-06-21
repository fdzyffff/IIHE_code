#include "TMath.h"
#include "TRandom3.h"

namespace trigEle27{


  TRandom3 randNrGen;
  float turnOnfunction(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
    float eff = 0.0;
    eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
    return eff;
  }
  
  float turnOn(float scEt,float scEta){
    if (0.0<=fabs(scEta) && fabs(scEta)<1.4442)
      return turnOnfunction(scEt,0.218,36.9,5.15,0.725,-15.7,42);
    else if (1.566<=fabs(scEta) && fabs(scEta)<2.5)
      return turnOnfunction(scEt,0.142,30.4,0.332,0.716,20.5,15.8);
    else
      return -1.0;
  }
  
  bool passTrig(float scEt,float scEta){return turnOn(scEt,scEta)>randNrGen.Uniform(0,1);}

}
  
