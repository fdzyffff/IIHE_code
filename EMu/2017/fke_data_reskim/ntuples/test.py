import ROOT

tchain = ROOT.TChain("tap")
tchain.Add("batchdata_loop_2/*root")

print tchain.GetEntries()
