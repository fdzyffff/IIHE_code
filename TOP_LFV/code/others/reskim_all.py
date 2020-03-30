import ROOT
import os
from optparse import OptionParser
ROOT.gSystem.Load("reskim_C.so")    

parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
parser.add_option("-p","--p_number",dest="p_number",default=0,type="int")
parser.add_option("-s","--mc_str",dest="mc_str",default='none',type="str")
parser.add_option("-y","--year_str",dest="year_str",default='2016',type="str")
parser.add_option("--isData",dest="isData",default="True",type="str")
parser.add_option("--isDY",dest="isDY",default="False",type="str")
parser.add_option("--isTTbin",dest="isTTbin",default="False",type="str")
parser.add_option("--isWWbin",dest="isWWbin",default="False",type="str")
#parser.add_option("-p", "--print_table", action='store_true', default=False)
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
 
tmp_reskim = ROOT.reskim()
tmp_reskim.isData =  isData
tmp_reskim.isDY =  isDY
tmp_reskim.isTTbar =  isTTbin
tmp_reskim.isWW =  isWWbin
tmp_reskim.No_print = options.p_number
tmp_reskim.mc_str =  options.mc_str
tmp_reskim.year = options.year_str

tmp_reskim.Init(tmp_chain)
tmp_reskim.Loop("%s"%(options.output_name))
