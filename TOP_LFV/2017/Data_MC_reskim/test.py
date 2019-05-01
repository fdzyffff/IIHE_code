import ROOT
import os
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
(options,args)=parser.parse_args()

rootfile_dir = options.root_dir
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
for event in tree:
#    print getattr(event,"MET_pfMetMuEGClean_et")
#@    print type(getattr(event,"MET_pfMetMuEGClean_et"))
    break
tree.Print()
