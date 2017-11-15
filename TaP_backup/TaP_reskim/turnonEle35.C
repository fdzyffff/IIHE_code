#ifndef DIELESCALEFACTORS_ELE27WPLOOSETRIGTURN_C
#define DIELESCALEFACTORS_ELE27WPLOOSETRIGTURN_C

#include "TMath.h"
#include "TRandom3.h"

namespace trigEle27{


  TRandom3 randNrGen;
  float turnOnfunction_Et(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
    float eff = 0.0;
    eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
    return eff;
  }
  
  float turnOnfunction_ID(float Et, float p0, float p1, float p2){
    if(Et>120)
    {
      Et = 120;
    }
    float eff = 0.0;
    eff = p0 + p1*Et + p2*Et*Et;
    return eff;
  }
  
  float turnOn(float scEt,float scEta){
    if (0.0<=fabs(scEta) && fabs(scEta)<1.4442)
      return turnOnfunction_Et(scEt,0.6052,12.96,19.85,0.3783,37.36,0.4359) * turnOnfunction_Et(scEt,0.7588,0.003095,-0.00001509);
    else if (1.566<=fabs(scEta) && fabs(scEta)<2.5)
      return turnOnfunction_Et(scEt,-0.648,166.4,8.226,0.9682,36,2.09) * turnOnfunction_Et(scEt,0.6985,0.003587,-0.00001692);
    else
      return -1.0;
  }
  
  bool passTrig(float scEt,float scEta){return turnOn(scEt,scEta)>randNrGen.Uniform(0,1);}

}
  


#endif
