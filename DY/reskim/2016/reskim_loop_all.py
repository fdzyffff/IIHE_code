import ROOT
import os
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
parser.add_option("-d","--trigger_SingleMuon",dest="trigger_SingleMuon",default="",type="str")
parser.add_option("-s","--run_start",dest="run_start",default="",type="str")
parser.add_option("-e","--run_end",dest="run_end",default="",type="str")
(options,args)=parser.parse_args()

ROOT.gSystem.Load("./reskim_C.so")

tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add("%s"%(options.root_dir)) 

tmp_reskim = ROOT.reskim(tmp_chain, True, False, False, False,0, int(options.trigger_SingleMuon), int(options.run_start), int(options.run_end) )
tmp_reskim.Loop("%s"%(options.output_name))
print '***finish***'

