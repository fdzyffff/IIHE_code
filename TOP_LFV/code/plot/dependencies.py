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
import collections

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gErrorIgnoreLevel=ROOT.kWarning

##Cross sections:
#xsection_ttbar2l2u = 87.31
#xsection_ttbar2l2u_M500to800 = 0.326
#xsection_ttbar2l2u_M800to1200 = 0.0326
#xsection_ttbar2l2u_M1200to1800 = 0.00305
#xsection_ttbar2l2u_M1800toInf = 0.000174
#
#xsection_WW2l2u = 12.178
#xsection_WW2l2u_M200to600 = 1.39
#xsection_WW2l2u_M600to1200 = 0.057
#xsection_WW2l2u_M1200to2500 = 0.0036
#xsection_WW2l2u_M2500toInf = 0.000054
#
#xsection_DYToLL = 5765.4
#xsection_WZ = 47.13
#xsection_ZZ = 16.523
#xsection_ST = 19.47 + 19.47
#
#xsection_WZTo2L2Q = 5.595
#xsection_WZTo3LNu = 5.052
#xsection_ZZTo2L2Nu = 0.564
#xsection_ZZTo2L2Q = 3.22
#xsection_ZZTo4L = 1.212
#
#
#xsection_QBHtoEMu_M200 = 24066.378
#xsection_QBHtoEMu_M400 = 1773.9027
#xsection_QBHtoEMu_M600 = 332.7039
#xsection_QBHtoEMu_M800 = 93.89556
#xsection_QBHtoEMu_M1000 = 32.822153
#xsection_QBHtoEMu_M1200 = 13.262773
#xsection_QBHtoEMu_M1400 = 5.9366958
#xsection_QBHtoEMu_M1600 = 2.8184958
#xsection_QBHtoEMu_M1800 = 1.4130132
#xsection_QBHtoEMu_M2000 = 0.74754306
#xsection_QBHtoEMu_M2500 = 0.16704102
#xsection_QBHtoEMu_M3000 = 0.04210492
#xsection_QBHtoEMu_M3500 = 0.011567997
#xsection_QBHtoEMu_M4000 = 0.0033187364
#xsection_QBHtoEMu_M4500 = 0.000949752
#xsection_QBHtoEMu_M5000 = 0.00027582334
#xsection_QBHtoEMu_M5500 = 7.88E-05
#xsection_QBHtoEMu_M6000 = 2.23E-05
#xsection_QBHtoEMu_M7000 = 1.58E-06
#xsection_QBHtoEMu_M8000 = 9.32E-08
#xsection_QBHtoEMu_M9000 = 4.48E-09
#xsection_QBHtoEMu_M10000 = 1.60E-10
#
#xsection_RPVresonantToEMu_M200 = 1
#xsection_RPVresonantToEMu_M300 = 1
#xsection_RPVresonantToEMu_M400 = 1
#xsection_RPVresonantToEMu_M500 = 1
#xsection_RPVresonantToEMu_M600 = 1
#xsection_RPVresonantToEMu_M700 = 1
#xsection_RPVresonantToEMu_M800 = 1
#xsection_RPVresonantToEMu_M900 = 1
#xsection_RPVresonantToEMu_M1000 = 1
#xsection_RPVresonantToEMu_M1200 = 1
#xsection_RPVresonantToEMu_M1400 = 1
#xsection_RPVresonantToEMu_M1600 = 1
#xsection_RPVresonantToEMu_M1800 = 1
#xsection_RPVresonantToEMu_M2000 = 1
#xsection_RPVresonantToEMu_M2500 = 1
#xsection_RPVresonantToEMu_M3000 = 1
#xsection_RPVresonantToEMu_M3500 = 1
#xsection_RPVresonantToEMu_M4000 = 1
#xsection_RPVresonantToEMu_M4500 = 1
#xsection_RPVresonantToEMu_M5000 = 1
#xsection_RPVresonantToEMu_M5500 = 1
#xsection_RPVresonantToEMu_M6000 = 1
#xsection_RPVresonantToEMu_M6500 = 1
#
#xsection_ZPrimeToEMu_M500 = 9.56
#xsection_ZPrimeToEMu_M600 = 5.03
#xsection_ZPrimeToEMu_M700 = 2.83
#xsection_ZPrimeToEMu_M800 = 1.704
#xsection_ZPrimeToEMu_M900 = 1.075
#xsection_ZPrimeToEMu_M1000 = 0.7141
#xsection_ZPrimeToEMu_M1100 = 0.4775
#xsection_ZPrimeToEMu_M1200 = 0.329
#xsection_ZPrimeToEMu_M1300 = 0.234
#xsection_ZPrimeToEMu_M1400 = 0.1675
#xsection_ZPrimeToEMu_M1500 = 0.1226
#xsection_ZPrimeToEMu_M1600 = 0.09071
#xsection_ZPrimeToEMu_M1700 = 0.06808
#xsection_ZPrimeToEMu_M1800 = 0.05166
#xsection_ZPrimeToEMu_M1900 = 0.03912
#xsection_ZPrimeToEMu_M2000 = 0.03027
#xsection_ZPrimeToEMu_M2200 = 0.01847
#xsection_ZPrimeToEMu_M2400 = 0.01147
#xsection_ZPrimeToEMu_M2600 = 0.007258
#xsection_ZPrimeToEMu_M2800 = 0.004695
#xsection_ZPrimeToEMu_M3000 = 0.003079
#xsection_ZPrimeToEMu_M3500 = 0.001163
#xsection_ZPrimeToEMu_M4000 = 0.0004841
#xsection_ZPrimeToEMu_M4500 = 0.0002196
#xsection_ZPrimeToEMu_M5000 = 0.0001113
#xsection_ZPrimeToEMu_M5500 = 6.238e-05# +- 3.722e-07
#xsection_ZPrimeToEMu_M6000 = 3.896e-05# +- 2.435e-07
