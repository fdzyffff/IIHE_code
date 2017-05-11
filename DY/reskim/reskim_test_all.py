import ROOT
import os

ROOT.gSystem.Load("./reskim_C.so")    

root_dir = "rB/00111"
root_file_list = os.listdir(root_dir)
for root_file in root_file_list:

    tmp_chain = ROOT.TChain("IIHEAnalysis") 
    tmp_chain.Add("%s/%s"%(root_dir,root_file)) 
    
    tmp_reskim = ROOT.reskim(tmp_chain, True, False, False, False, 51, 0, 276453 )
    tmp_reskim.Loop("ntuples/test/%s"%(root_file))
    print '***finish***'  
