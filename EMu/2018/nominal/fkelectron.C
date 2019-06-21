#include "TMath.h"
#include "TRandom3.h"

namespace fkelectron{

float frFuncData(float et,float eta)
{
/*   if(std::abs(eta)<1.5){
     if(et<131.6) return 
0.14+-0.0029*et+2.56e-05*et*et+-8.48e-08*et*et*et;
     else if(et>=131.6 && et<359.3) return 
0.020+-0.00013*et+3.50e-07*et*et+-2.90e-10*et*et*et;
     else return 0.00514+4.73e-07*et;
   }else if(std::abs(eta)<2.0){
     if(et<125.0) return 0.1012+-0.00094*et+3.37e-06*et*et;
     else if(et>=125.0 && et<226.3) return 0.0488+-11.37e-05*et;
     else return 0.0241+-1.24e-06*et;
   }else if(std::abs(eta)<2.5){
     if(et<152.0) return 0.0622+-0.00012*et;
     else return 0.0387;
   }else return 0.;
}*/
  if(std::abs(eta)<1.5) {
    if(et < 130.0) {
      return (2.02017e-06 * et * et - 0.000843135 * et + 0.0876231) ;
    } else if (et < 359.3) {
      return (-1.341e-09 * et * et * et + 1.11091e-06 * et * et - 0.000311271 * et + 0.0358143) ;
    } else {
      return (2.18947e-07 * et + 0.00598619) ;
    }
  } else if(std::abs(eta)<2.0) {
    if(et < 70.0) {
      return (-0.00163634 * et + 0.167095) ;
    } else if (et < 155.0) {
      return (-0.000340279 * et + 0.0802441) ;
    } else {
      return 0.026187 ;
    }  
  } else {
    if(et < 220.0) {
      return (1.34086e-06 * et * et - 0.00058487 * et + 0.106484) ;
    } else {
      return 0.0427328 ;
    }
  }
}


}
  


