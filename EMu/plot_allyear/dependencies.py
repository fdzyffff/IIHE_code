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