import ROOT
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--out_name",dest="out_name",default="",type="str")
parser.add_option("-d","--isData",dest="isData",default="",type="str")
parser.add_option("-t","--isZToTT",dest="isZToTT",default="",type="str")
parser.add_option("-w","--isWJets",dest="isWJets",default="",type="str")
parser.add_option("-e","--isZToEE",dest="isZToEE",default="",type="str")
(options,args)=parser.parse_args()

ROOT.gSystem.Load("./reskim_C.so")    
tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add("%s/*.root"%(options.root_dir)) 

#reskim(TTree *tree=0, bool isData_in=false, bool isZToTT_in=false, bool isWJets_in=false, bool isZToEE_in=false, int triggerVersion_in=0, int runNo1_in=0, int runNo2_in=0);
isData = True if options.isData == "1" else False
isZToTT = True if options.isZToTT == "1" else False
isWJets = True if options.isWJets == "1" else False
isZToEE = True if options.isZToEE == "1" else False
print "isData: ",isData
print "isZToTT: ",isZToTT
print "isWJets: ",isWJets
print "isZToEE: ",isZToEE
tmp_reskim = ROOT.reskim(tmp_chain,  isData, isZToTT, isWJets, isZToEE)
tmp_reskim.Loop("%s"%(options.out_name))
print '***finish***'  
