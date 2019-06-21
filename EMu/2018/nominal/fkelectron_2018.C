#include "TMath.h"
#include "TRandom3.h"

namespace fkelectron_2018{

  float frFuncData_1(float sc_et, float eta);
  float frFuncData_2(float sc_et, float eta);
  float frFuncData_3(float sc_et, float eta);
  
  float frFuncData(int run_no, float sc_et, float sc_eta, float gsf_eta, float gsf_phi) {
    if (run_no < 319077) {
      return frFuncData_1(sc_et, sc_eta);
    } else if (gsf_eta > -3.0 && gsf_eta < -1.3 && gsf_phi > -1.57 && gsf_phi < -0.87 ) {
      // inside HEM
      return frFuncData_2(sc_et, sc_eta);
    } else {
      return frFuncData_3(sc_et, sc_eta);
    }
  }

  float frFuncData_1(float sc_et, float eta)
  {
    if(std::abs(eta)<1.5) {
      if(sc_et < 130.0) {
        return (2.02017e-06 * sc_et * sc_et - 0.000843135 * sc_et + 0.0876231) ;
      } else if (sc_et < 359.3) {
        return (-1.341e-09 * sc_et * sc_et * sc_et + 1.11091e-06 * sc_et * sc_et - 0.000311271 * sc_et + 0.0358143) ;
      } else {
        return (2.18947e-07 * sc_et + 0.00598619) ;
      }
    } else if(std::abs(eta)<2.0) {
      if(sc_et < 70.0) {
        return (-0.00163634 * sc_et + 0.167095) ;
      } else if (sc_et < 155.0) {
        return (-0.000340279 * sc_et + 0.0802441) ;
      } else {
        return 0.026187 ;
      }  
    } else {
      if(sc_et < 220.0) {
        return (1.34086e-06 * sc_et * sc_et - 0.00058487 * sc_et + 0.106484) ;
      } else {
        return 0.0427328 ;
      }
    }
  }

  float frFuncData_2(float sc_et,float eta)
  {
    if(std::abs(eta)<1.5) {
      if(sc_et < 97.0) {
        return (-0.000641136 * sc_et + 0.0681215) ;
      } else {
        return (0.0084599) ;
      }
    } else if(std::abs(eta)<2.0) {
      if(sc_et < 100.0) {
        return (-0.000468076 * sc_et + 0.0663296) ;
      } else {
        return 0.0210277 ;
      }  
    } else {
      return 0.0392853 ;
    }
  }

  float frFuncData_3(float sc_et,float eta)
  {
    if(std::abs(eta)<1.5) {
      if(sc_et < 130.0) {
        return (1.18124e-06 * sc_et * sc_et - 0.000689288 * sc_et + 0.0801178) ;
      } else if (sc_et < 359.3) {
        return (-8.21182e-10 * sc_et * sc_et * sc_et + 7.09363e-07 * sc_et * sc_et - 0.00020855 * sc_et + 0.0268764) ;
      } else {
        return (7.65758e-06 * sc_et + 0.00291191) ;
      }
    } else if(std::abs(eta)<2.0) {
      if(sc_et < 160.0) {
        return (-0.000360437 * sc_et + 0.0831656) ;
      } else {
        return 0.0266372 ;
      }  
    } else {
      if(sc_et < 220.0) {
        return (1.37424e-06 * sc_et * sc_et - 0.00056355 * sc_et + 0.100376) ;
      } else {
        return 0.0419409 ;
      }
    }
  }
}
  


