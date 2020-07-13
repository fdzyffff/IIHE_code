import os
import time
from optparse import OptionParser

parser=OptionParser()

parser.add_option("-i","--global_dir",dest="global_dir",default="null",type="str")

(options,args)=parser.parse_args()

job_dir_list = [
"script_dataSingleMuon/sub_2016_SingleMuon",
"script_dataSingleMuon/sub_fke_2016_SingleMuon",
"script_dataSingleMuon/sub_fkm_2016_SingleMuon",

"script_MC/sub_2016_MC",
"script_MC/sub_fke_2016_MC",
"script_MC/sub_fkm_2016_MC",

"script_dataSinglePhoton/sub_2016_SinglePhoton",
"script_dataSinglePhoton/sub_fke_2016_SinglePhoton",
"script_dataSinglePhoton/sub_fkm_2016_SinglePhoton",
]
