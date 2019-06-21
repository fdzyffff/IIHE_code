
#include "TMath.h"
#include "TRandom3.h"

namespace trig_Photon175{


  TRandom3 randNrGen;
  float turnOnfunction(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
    float eff = 0.0;
    eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
    return eff;
  }
  
  float turnOn(float scEt,float scEta){
    if (0.0<=fabs(scEta) && fabs(scEta)<0.79)
      return turnOnfunction(scEt,0.082, 32.859, 1.778, 0.905, 32.956, 0.532);
    else if (0.79<=fabs(scEta) && fabs(scEta)<1.1)
      return turnOnfunction(scEt,0.122, 33.091, 1.665, 0.866, 33.138, 0.634);
    else if (1.1<=fabs(scEta) && fabs(scEta)<1.4442)
      return turnOnfunction(scEt,0.175, 33.299, 1.596, 0.818, 33.252, 0.687);
    else if (1.566<=fabs(scEta) && fabs(scEta)<1.70)
      return turnOnfunction(scEt,0.130, 32.930, 2.451, 0.865, 33.323, 0.794);
    else if (1.70<=fabs(scEta) && fabs(scEta)<2.1)
      return turnOnfunction(scEt,0.264, 33.985, 1.736, 0.734, 33.749, 0.859);
    else if (2.1<=fabs(scEta) && fabs(scEta)<2.5)
      return turnOnfunction(scEt,0.602, 35.483, 1.796, 0.397, 34.603, 0.989);
    else
      return -1.0;
  }
  
  bool passTrig(float scEt,float scEta){return 1.0>randNrGen.Uniform(0,1);}

}
  


