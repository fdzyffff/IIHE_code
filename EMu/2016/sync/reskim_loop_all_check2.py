import ROOT
import os
from optparse import OptionParser

root_dir = "./ntuples/pk_batchdata_loop_1"
output_name = "ntuples/batchdata_out/sync"
ROOT.gSystem.Load("reskim_C.so")    

n_target = -1
nfile = 0
for tmp_file in os.listdir(root_dir):
    nfile += 1
    if nfile != n_target and n_target > 0:continue
    if not ".root" in tmp_file:continue
    tmp_chain = ROOT.TChain("IIHEAnalysis") 
    tmp_chain.Add("%s"%(os.path.join(root_dir,tmp_file))) 
    print tmp_file

    tmp_reskim = ROOT.reskim(tmp_chain, True, False, False, False,0, 0, 0, 999999 )
    tmp_reskim.Loop("%s_%s"%(output_name, tmp_file))
    #print '***%s finish***'%(os.path.join(root_dir,tmp_file))
    #print '***(%d / %d)finish***'%(nfile, len(os.listdir(root_dir)))  
    if n_target > 0:break
print '***finish***'  
