import sys
try:
    sys.path.append("C:/root_v5.34.30/bin")
except:
    pass

from array import array
import os
import ROOT
import time
from copy import deepcopy
from math import *

isUpdate = True
isUpdate = False

use_sys = True

GLOBAL_YEAR = "2016"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QCD_JET_BKG_TYPE = "fake rate"
#QCD_JET_BKG_TYPE = "same sign"

# start run
cut_name={
'_ALL':["e#mu",""],
'_highEleEt':["e#mu","Et^{ele} > 50"],
'_ALL_lepveto':["e#mu","lepton veto"],
'_highEleEt_lepveto':["e#mu","lepton veto Et^{ele} > 50"],
'_ALL_2b':["e#mu","N(bjet) == 2"],
'_BB':["e#mu","Barrel(e),Barrel(mu)"],
'_BE':["e#mu","Barrel(e),Endcap(mu)"],
'_EB':["e#mu","Endcap(e),Barrel(mu)"],
'_EE':["e#mu","Endcap(e),Endcap(mu)"],
'_ETA_1':["e#mu","pT_{#mu} in [-2.5,-2.0]"],
'_ETA_2':["e#mu","pT_{#mu} in [2.0,2.5]"],
'_MET_50to100':["e#mu","MET in [50,100]"],
'_MET_100toInf':["e#mu","MET in [100,]"],
'_Nvtx_0to25':["e#mu","N_{vtx} < 25"],
'_Nvtx_25toInf':["e#mu","N_{vtx} > 25"],
}
# start run
cut_dic={
'_ALL':'True',
'_highEleEt':'(getattr(event,"ele_Et") > 50)',
#'_ALL_lepveto':'(getattr(event,"pass_lepton_veto"))',
#'_highEleEt_lepveto':'(getattr(event,"pass_lepton_veto")) and (getattr(event,"ele_Et") > 50)',
#'_BB':'(getattr(event,"ele_region") ==1 and getattr(event,"muon_region") == 1)',
#'_BE':'(getattr(event,"ele_region") ==1 and getattr(event,"muon_region") == 3)',
#'_EB':'(getattr(event,"ele_region") ==3 and getattr(event,"muon_region") == 1)',
#'_EE':'(getattr(event,"ele_region") ==3 and getattr(event,"muon_region") == 3)',
#'_ETA_1':'getattr(event,"muon_eta") <= -2.0',
#'_ETA_2':'getattr(event,"muon_eta") >= 2.0',
#'_MET_25to50':'getattr(event,"MET_T1Txy_Pt") > 25 and getattr(event,"MET_T1Txy_Pt") <= 50',
#'_MET_50to100':'getattr(event,"MET_T1Txy_Pt") > 50 and getattr(event,"MET_T1Txy_Pt") <= 100',
#'_MET_100toInf':'getattr(event,"MET_T1Txy_Pt") > 100',
#'_Nvtx_0to25':'getattr(event,"pv_n") <= 25',
#'_Nvtx_25toInf':'getattr(event,"pv_n") > 25',
}
