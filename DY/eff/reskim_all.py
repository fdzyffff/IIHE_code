import ROOT
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
parser.add_option("-d","--trigger_Ele33",dest="trigger_Ele33",default="",type="str")
parser.add_option("-s","--trigger_Ele27",dest="trigger_Ele27",default="",type="str")
(options,args)=parser.parse_args()

ROOT.gSystem.Load("./reskim_C.so")    
tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add("%s/*.root"%(options.root_dir)) 

tmp_reskim = ROOT.reskim(tmp_chain, True, False, False, int(options.trigger_Ele33), int(options.trigger_Ele27))
tmp_reskim.Loop("%s"%(options.output_name))
print '***finish***'  
