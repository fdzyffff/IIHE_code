import ROOT
import os
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
(options,args)=parser.parse_args()


file_list = []
rootfile_list = []



def my_walk_dir(my_dir,my_list):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            if 'failed' 	in tmp_file_name:continue
            if not '.root' 	in tmp_file_name:continue
            my_list.append(tmp_file_name)
        else:
            my_walk_dir(tmp_file_name,my_list)
    return 

def scanFile():
    my_walk_dir(options.root_dir,rootfile_list)
    
scanFile()

print "total files: %d in dir : %s"%(len(rootfile_list),options.root_dir)
