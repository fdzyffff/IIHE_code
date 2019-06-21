
#include "TMath.h"
#include "TRandom3.h"

TRandom3 randNrGen;
float turnOnfunction(float Et, float p0, float p1, float p2, float p3, float p4, float p5){
  float eff = 0.0;
  eff = 0.5*p0*(1+erf((Et-p1)/(1.414*p2)))+0.5*p3*(1+erf((Et-p4)/(1.414*p5)));
  return eff;
}

namespace trigEle33_2016{

  float turnOn(float gsf_Et,float sc_Eta){
    if (0.0<=fabs(sc_Eta) && fabs(sc_Eta)<0.79)
      return turnOnfunction(gsf_Et, 0.8066, 32.92, 0.5816, 0.1747, 32.66, 1.441);
    else if (0.79<=fabs(sc_Eta) && fabs(sc_Eta)<1.1)
      return turnOnfunction(gsf_Et, 0.901, 33.02, 0.7304, 0.08336, 33.37, 2.464);
    else if (1.1<=fabs(sc_Eta) && fabs(sc_Eta)<1.4442)
      return turnOnfunction(gsf_Et, 0.6564, 32.97, 0.7031, 0.3334, 33.33, 1.533);
    else if (1.566<=fabs(sc_Eta) && fabs(sc_Eta)<1.70)
      return turnOnfunction(gsf_Et, 0.8954, 33.05, 1.022, 0.0973, 32.32, 4.124);
    else if (1.70<=fabs(sc_Eta) && fabs(sc_Eta)<2.1)
      return turnOnfunction(gsf_Et, 0.7767, 33.08, 0.9646, 0.2196, 33.36, 2.014);
    else if (2.1<=fabs(sc_Eta) && fabs(sc_Eta)<2.5)
      return turnOnfunction(gsf_Et, 0.3626, 34.05, 1.935, 0.6339, 33.59, 1.064);
      return -1.0;
  }
  float turnOn_MW(float gsf_Et,float sc_Eta){
    if (0.0<=fabs(sc_Eta) && fabs(sc_Eta)<0.79)
      return turnOnfunction(gsf_Et, 0.8315, 33.03, 0.6641, 0.1618, 32.81, 1.666);
    else if (0.79<=fabs(sc_Eta) && fabs(sc_Eta)<1.1)
      return turnOnfunction(gsf_Et, 0.8558, 33.22, 0.757, 0.1391, 33.4, 2.021);
    else if (1.1<=fabs(sc_Eta) && fabs(sc_Eta)<1.4442)
      return turnOnfunction(gsf_Et, 0.6471, 33.21, 0.7441, 0.3484, 33.66, 1.642);
    else if (1.566<=fabs(sc_Eta) && fabs(sc_Eta)<1.70)
      return turnOnfunction(gsf_Et, 0.9065, 33.11, 1.079, 0.08481, 31.92, 5.275);
    else if (1.70<=fabs(sc_Eta) && fabs(sc_Eta)<2.1)
      return turnOnfunction(gsf_Et, 0.8312, 33.48, 1.157, 0.1627, 34.04, 2.213);
    else if (2.1<=fabs(sc_Eta) && fabs(sc_Eta)<2.5)
      return turnOnfunction(gsf_Et, 0.9055, 34.45, 1.538, 0.08972, 37.21, 1.672);
    else
      return -1.0;
  }
  
  bool passTrig(float gsf_Et,float sc_Eta){return (11.021/36.459)*turnOn(gsf_Et,sc_Eta)+(25.438/36.459)*turnOn_MW(gsf_Et,sc_Eta)>randNrGen.Uniform(0,1);}
  //bool passTrig(float gsf_Et,float sc_Eta){return turnOn_MW(gsf_Et,sc_Eta)>randNrGen.Uniform(0,1);}

}
  

namespace trigEle33_2017{

  float turnOn_MW(float gsf_Et,float sc_Eta){
    if (0.0<=fabs(sc_Eta) && fabs(sc_Eta)<0.79)
      return turnOnfunction(gsf_Et, 0.9699, 33.9, 0.6848, 0.2808, -114.5, -1.165);
    else if (0.79<=fabs(sc_Eta) && fabs(sc_Eta)<1.1)
      return turnOnfunction(gsf_Et, 0.9189, 34.09, 0.7909, 0.0554, 34.61, 3.159);
    else if (1.1<=fabs(sc_Eta) && fabs(sc_Eta)<1.4442)
      return turnOnfunction(gsf_Et, 0.9012, 34.45, 0.9212, 0.07256, 34.15, 2.83);
    else if (1.566<=fabs(sc_Eta) && fabs(sc_Eta)<1.70)
      return turnOnfunction(gsf_Et, 0.5081, 34.41, 0.7987, 0.4611, 35.57, 2.103);
    else if (1.70<=fabs(sc_Eta) && fabs(sc_Eta)<2.1)
      return turnOnfunction(gsf_Et, 0.5552, 34.66, 0.8383, 0.4215, 35.89, 1.971);
    else if (2.1<=fabs(sc_Eta) && fabs(sc_Eta)<2.5)
      return turnOnfunction(gsf_Et, 0.5317, 34.4, 1.065, 0.4395, 36.43, 2.328);
    else
      return -1.0;
  }
  
  bool passTrig(float gsf_Et,float sc_Eta){return turnOn_MW(gsf_Et,sc_Eta)>randNrGen.Uniform(0,1);}

}

namespace trigEle25_2018{

  float turnOn_MW(float gsf_Et,float sc_Eta){
    if (0.0<=fabs(sc_Eta) && fabs(sc_Eta)<0.79)
      return turnOnfunction(gsf_Et, 0.9388, 25.72, 0.4894, 0.03604, 26.4, 3.559);
    else if (0.79<=fabs(sc_Eta) && fabs(sc_Eta)<1.1)
      return turnOnfunction(gsf_Et, 0.9369, 25.76, 0.6161, 0.03935, 25.84, 3.949);
    else if (1.1<=fabs(sc_Eta) && fabs(sc_Eta)<1.4442)
      return turnOnfunction(gsf_Et, 0.9179, 26.12, 0.7177, 0.05055, 25.58, 2.612);
    else if (1.566<=fabs(sc_Eta) && fabs(sc_Eta)<1.70)
      return turnOnfunction(gsf_Et, 0.8715, 25.98, 0.8073, 0.09576, 26.4, 3.822);
    else if (1.70<=fabs(sc_Eta) && fabs(sc_Eta)<2.1)
      return turnOnfunction(gsf_Et, 0.926, 26.1, 0.7879, 0.0584, 27.24, 3.451);
    else if (2.1<=fabs(sc_Eta) && fabs(sc_Eta)<2.5)
      return turnOnfunction(gsf_Et, 0.7165, 26.46, 0.8912, 0.2593, 27.34, 1.969);
    else
      return -1.0;
  }
  
  bool passTrig(float gsf_Et,float sc_Eta){return turnOn_MW(gsf_Et,sc_Eta)>randNrGen.Uniform(0,1);}

}
