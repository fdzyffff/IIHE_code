import ROOT
import os
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-o","--output_name",dest="output_name",default="",type="str")
parser.add_option("-d","--trigger_Ele33",dest="trigger_Ele33",default="",type="str")
parser.add_option("-s","--trigger_Ele27",dest="trigger_Ele27",default="",type="str")

parser.add_option("-e","--run_end",dest="run_end",default="",type="str")
(options,args)=parser.parse_args()

ROOT.gSystem.Load("./reskim_C.so")    

root_dir = options.root_dir

tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add("%s"%(root_dir)) 

nfile = 0
for tmp_file in os.listdir(options.root_dir):
    if not ".root" in tmp_file:continue
    tmp_chain = ROOT.TChain("IIHEAnalysis")
    tmp_chain.Add("%s"%(os.path.join(options.root_dir,tmp_file)))

    tmp_reskim = ROOT.reskim(tmp_chain, True, False, False, int(options.trigger_Ele33), int(options.trigger_Ele27))
    tmp_reskim.Loop("%s_%s"%(options.output_name, tmp_file))
    nfile += 1
    print '***%s finish***'%(os.path.join(options.root_dir,tmp_file))
    print '***(%d / %d)finish***'%(nfile, len(os.listdir(options.root_dir)))
print '***finish***'
