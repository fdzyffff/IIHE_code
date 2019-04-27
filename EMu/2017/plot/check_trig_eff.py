import sys
try:
    sys.path.append("C:/root_v5.34.30/bin")
except:
    pass
import ROOT
import time
from math import *
from array import array
import os

Muon50_trig_fire = True
OldMu100_trig_fire = True
Ele115_trig_fire = False
Photon175_trig_fire = False

from optparse import OptionParser

parser=OptionParser()

parser.add_option("-r","--root_name",dest="root_name",default="null",type="str")

(options,args)=parser.parse_args()

trig_dic = {
	"Muon50"						:["Muon50_trig_fire",0],
	"Muon50 || Photon175"			:["Muon50_trig_fire || Photon175_trig_fire",1],
	"Muon50 || OldMu100"			:["Muon50_trig_fire || OldMu100_trig_fire",2],
	"Muon50 || Ele115"				:["Muon50_trig_fire || Ele115_trig_fire",3],
	"Muon50 || OldMu100 || Ele115"	:["Muon50_trig_fire || OldMu100_trig_fire || Ele115_trig_fire",4],
}

def main():

	nominal_trig = 100
	root_file = options.root_name
	
	f1 = ROOT.TFile(root_file,"read")
	t1 = f1.Get("tap")

	for p in sorted(trig_dic.iteritems(),key=lambda d:d[0][1],reverse = False):
		part = p[0]
		if trig_dic[part][1] == 0:
			nominal_trig = t1.Draw("",trig_dic[part][0])
			print "%s : %s"%(part, t1.Draw("",trig_dic[part][0]))
		else :
			ratio = float(t1.Draw("",trig_dic[part][0]) - nominal_trig) * 100 / nominal_trig 
			#print ratio
			print "%s : %s : (%0.2f)%%"%(part, t1.Draw("",trig_dic[part][0]), ratio)

main()