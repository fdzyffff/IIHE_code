#include "TCanvas.h"
#include "TF1.h"
#include "TMath.h"

#include "turnonEle33l1.C"
void tmp_turnOnTest()
{
   float P_barrel_35 = trigEle33l1::turnOn_MW(35.0, 1.0);
   float P_endcap_35 = trigEle33l1::turnOn_MW(35.0, 2.0);
   std::cout<<"barrel-barrel Et = 35 l1 weight : "<<(P_barrel_35 + P_barrel_35 - P_barrel_35 * P_barrel_35)<<std::endl;
   std::cout<<"barrel-endcap Et = 35 l1 weight : "<<(P_barrel_35 + P_endcap_35 - P_barrel_35 * P_endcap_35)<<std::endl;
}
