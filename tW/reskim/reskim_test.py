import ROOT
import os
from optparse import OptionParser
ROOT.gSystem.Load("reskim_C.so")    

parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
parser.add_option("-p","--p_number",dest="p_number",default=0,type="int")
(options,args)=parser.parse_args()


nfile = 0
tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add("%s"%(options.root_dir)) 
#print "Total Entries %d"%(tmp_chain.GetEntries())

if options.p_number > 0:
    tmp_reskim = ROOT.reskim(tmp_chain, False, False, False, False, options.p_number)
else: 
    tmp_reskim = ROOT.reskim(tmp_chain, True, False, False, False,0)
tmp_reskim.Loop("%s"%(options.output_name))
print '***%s finish***'%(options.root_dir)
print '***finish***'  
