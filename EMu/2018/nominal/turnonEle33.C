#include "TMath.h"
#include "TRandom3.h"

namespace trigEle33{


  TRandom3 randNrGen;
  float turnOnfunction(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
    float eff = 0.0;
    eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
    return eff;
  }
  
  float turnOn_MW(float scEt,float scEta){
    if (0.0<=fabs(scEta) && fabs(scEta)<0.79)
      return turnOnfunction(scEt,0.8466, 33.83, 0.485, 0.1243, 34.91, 2.036);
    else if (0.79<=fabs(scEta) && fabs(scEta)<1.1)
      return turnOnfunction(scEt,0.8814, 34.03, 0.6074, 0.09289, 34.81, 2.541);
    else if (1.1<=fabs(scEta) && fabs(scEta)<1.4442)
      return turnOnfunction(scEt,0.8956, 34.36, 0.8005, 0.07847, 34.06, 2.666);
    else if (1.566<=fabs(scEta) && fabs(scEta)<1.70)
      return turnOnfunction(scEt,0.5002, 34.35, 0.7048, 0.469, 35.49, 2.034);
    else if (1.70<=fabs(scEta) && fabs(scEta)<2.1)
      return turnOnfunction(scEt,0.5482, 34.62, 0.7567, 0.4285, 35.82, 1.907);
    else if (2.1<=fabs(scEta) && fabs(scEta)<2.5)
      return turnOnfunction(scEt,0.5252, 34.39, 0.9929, 0.4466, 36.41, 2.296);
    else
      return -1.0;
  }
  
  bool passTrig(float scEt,float scEta){return turnOn_MW(scEt,scEta)>randNrGen.Uniform(0,1);}
  //bool passTrig(float scEt,float scEta){return turnOn_MW(scEt,scEta)>randNrGen.Uniform(0,1);}

}
  
