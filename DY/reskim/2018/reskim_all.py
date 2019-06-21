import ROOT
import os
from optparse import OptionParser
ROOT.gSystem.Load("reskim_C.so")    

parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
parser.add_option("-p","--p_number",dest="p_number",default=0,type="int")
parser.add_option("-t","--triggerVersion",dest="triggerVersion",default=0,type="int")
parser.add_option("-s","--mc_str",dest="mc_str",default="",type="str")
parser.add_option("--isData",dest="isData",default="True",type="str")
parser.add_option("--isDYToTT",dest="isDYToTT",default="False",type="str")
parser.add_option("--isDYToEE",dest="isDYToEE",default="False",type="str")
parser.add_option("--isWWbin",dest="isWWbin",default="False",type="str")
(options,args)=parser.parse_args()


nfile = 0
tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add("%s"%(options.root_dir)) 

isData  = False 
isDYToTT = False
isDYToEE = False
isWWbin = False

if options.isData == "True":
    isData = True
if options.isDYToTT == "True":
    isDYToTT = True
if options.isDYToEE == "True":
    isDYToEE = True
if options.isWWbin == "True":
    isWWbin = True

mc_str = options.mc_str

print "########## Parameter ##########"
print "isData : ",isData
print "isDYToTT : ",isDYToTT
print "isDYToEE : ",isDYToEE
print "isWWbin : ",isWWbin
print "mc_str : ",mc_str

if options.p_number > 0:
    tmp_reskim = ROOT.reskim(tmp_chain, isData , isDYToTT, isDYToEE, isWWbin, mc_str, options.p_number, options.triggerVersion)
else: 
    tmp_reskim = ROOT.reskim(tmp_chain, isData , isDYToTT, isDYToEE, isWWbin, mc_str, 0, options.triggerVersion)
tmp_reskim.Loop("%s"%(options.output_name))
