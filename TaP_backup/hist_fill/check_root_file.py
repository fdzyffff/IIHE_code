import os
import sys

import ROOT
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
(options,args)=parser.parse_args()

def my_walk_dir(my_dir,my_list):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            if 'failed'         in tmp_file_name:continue
            if not '.root'      in tmp_file_name:continue
            my_list.append(tmp_file_name)
        else:
            my_walk_dir(tmp_file_name,my_list)
    return my_list

def check_root_file(file_name,tree_name):
    is_good_file = False
    print "reading file : %s"%(file_name)
    try:
        tmp_file = ROOT.TFile(file_name, "read")
        tmp_tree = tmp_file.Get(tree_name)
        if tmp_tree.GetEntries() > 0:
            is_good_file = True
    except:
        pass
    return is_good_file
    

def check_dir(tree_name):
    txt = open("rm.sh","w")
    print "%s making file list %s"%("#"*15,"#"*15)
    n_pass = 0
    n_total = 0
    file_list = my_walk_dir(options.root_dir,[])
    file_list.sort()
    print "  Total root files : %d"%(len(file_list))
    for file_name in file_list:
        if check_root_file(file_name, tree_name):
            n_pass+=1
        else:
            print "can not open file: %s"%(file_name)
            txt.write("rm %s\n"%(file_name))
        n_total += 1

check_dir("tap")
