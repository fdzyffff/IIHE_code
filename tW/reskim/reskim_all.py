import ROOT
import os
from optparse import OptionParser
ROOT.gSystem.Load("reskim_C.so")    

parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
parser.add_option("-p","--p_number",dest="p_number",default=0,type="int")
parser.add_option("-t","--triggerVersion",dest="triggerVersion",default=0,type="int")
parser.add_option("--isData",dest="isData",default="True",type="str")
parser.add_option("--isDY",dest="isDY",default="False",type="str")
parser.add_option("--isTTbin",dest="isTTbin",default="False",type="str")
parser.add_option("--isWWbin",dest="isWWbin",default="False",type="str")
(options,args)=parser.parse_args()


nfile = 0
tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add(options.root_dir) 

isData  = False 
isDY = False
isTTbin = False
isWWbin = False

if options.isData == "True":
    isData = True
if options.isDY == "True":
    isDY = True
if options.isTTbin == "True":
    isTTbin = True
if options.isWWbin == "True":
    isWWbin = True

print "########## Parameter ##########"
print "isData : ",isData
print "isDY : ",isDY
print "isTTbin : ",isTTbin
print "isWWbin : ",isWWbin

if options.p_number > 0:
    tmp_reskim = ROOT.reskim(tmp_chain, isData , isDY, isTTbin, isWWbin, options.p_number, options.triggerVersion)
else: 
    tmp_reskim = ROOT.reskim(tmp_chain, isData , isDY, isTTbin, isWWbin, 0, options.triggerVersion)
tmp_reskim.Loop("%s"%(options.output_name))
