import ROOT
import os

rootfile_dir = 'Data/rA_1/0000'
if '.root' in rootfile_dir:
    tmp_file = ROOT.TFile.Open(rootfile_dir)
    print 'open file : %s'%rootfile_dir
else:
    for filename in os.listdir(rootfile_dir):
        if 'root' in filename:
            tmp_file = ROOT.TFile.Open(rootfile_dir+'/'+filename)
            print 'open file : %s'%filename
            break

tree = ROOT.gDirectory.Get('IIHEAnalysis')
for leaf in tree.GetListOfLeaves():
    name = leaf.GetName()
    print name
