
#include "TMath.h"
#include "TRandom3.h"

namespace trig_Mu50{


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
  
  float muonTriggerWeight(const float mu_pt, const float mu_eta){
//      [0.918826,0.799085,0.926197,0.885586,0.854526,0.816214,0.736484]
//      [0.921847,0.813589,0.921885,0.86827,0.789756,0.815474,0.734284]
//      [0.952756,0.642857,0.907787,0.84153,0.807882,0.753247,0.635135]
  
      unsigned int etaBINS = 7;
      double SF_trigger[etaBINS];
      if (fabs(mu_pt) < 100.){
          SF_trigger[0] = 0.918826; SF_trigger[1] = 0.799085; SF_trigger[2] = 0.926197; SF_trigger[3] = 0.885586; SF_trigger[4] = 0.854526; SF_trigger[5] = 0.816214; SF_trigger[6] = 0.736484;
      }else if(fabs(mu_pt) < 200.){
          SF_trigger[0] = 0.921847; SF_trigger[1] = 0.813589; SF_trigger[2] = 0.921885; SF_trigger[3] = 0.86827; SF_trigger[4] = 0.789756; SF_trigger[5] = 0.815474; SF_trigger[6] = 0.734284;
      }else{
          SF_trigger[0] = 0.952756; SF_trigger[1] = 0.642857; SF_trigger[2] = 0.907787; SF_trigger[3] = 0.84153; SF_trigger[4] = 0.807882; SF_trigger[5] = 0.753247; SF_trigger[6] = 0.635135;
      }
      
  //    Eta bins definition.
      double etabin[etaBINS+1];
      etabin[0]=0.; etabin[1]=0.2; etabin[2]=0.3; etabin[3]=0.9; etabin[4]=1.2; etabin[5]=1.6; etabin[6]=2.1; etabin[7]=2.4;
      
      unsigned int ibin = etaBINS;
      for (unsigned int kbin=0; kbin<=etaBINS; ++kbin) {
          if (fabs(mu_eta)<etabin[kbin+1]) {
              ibin = kbin;
              break;
          }
      }
      
      float sf = SF_trigger[ibin];
      return sf;
      
  }
  bool passTrig(float scEt,float scEta){return 0.97>randNrGen.Uniform(0,1);}

}
  


