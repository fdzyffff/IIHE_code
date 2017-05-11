import ROOT
import os
ROOT.gSystem.Load("reskim_C.so")

input_dir = "Data/rB/0022"
tmp_file = "outfile_2277.root"
output_name = "ntuples/batchdata_loop/data_2016_SingleMuon_0022_rB"
tmp_chain = ROOT.TChain("IIHEAnalysis") 
tmp_chain.Add("%s"%(os.path.join(input_dir,tmp_file))) 

tmp_reskim = ROOT.reskim(tmp_chain, True, False, False, False,0, 0, 0, 999999 )
tmp_reskim.Loop("%s_%s"%(output_name, tmp_file))
