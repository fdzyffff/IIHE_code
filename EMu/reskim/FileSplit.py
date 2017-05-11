import ROOT
import os

split_dic = {
}

root_dir_dic ={
"rB" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_SingleMuon_2016B",[]],
"rC" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_SingleMuon_2016C",[]],
"rD" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_SingleMuon_2016D",[]],
"rE" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_SingleMuon_2016E",[]],
"rF" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_SingleMuon_2016F",[]],
"rG" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_SingleMuon_2016G",[]],
"H2" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_runH_reco_v2",[]],
"H3" : ["/pnfs/iihe/cms/store/user/xgao/SingleMuon/crab_runH_reco_v3",[]],
}

file_list = []
rootfile_list = []



def my_walk_dir(my_dir,my_list):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            if 'failed' 	in tmp_file_name:continue
#            if not '_skimed' 	in tmp_file_name:continue
            if not '.root' 	in tmp_file_name:continue
            my_list.append(tmp_file_name)
        else:
            my_walk_dir(tmp_file_name,my_list)
    return 

def scanFile():
    for rootfile_dir in root_dir_dic:
        my_walk_dir(root_dir_dic[rootfile_dir][0],root_dir_dic[rootfile_dir][1])
        root_dir_dic[rootfile_dir][1].sort()
    
def setlink(branch_name, filelist):
    nFiles_uplimit = 0
    nFiles_step = 100
    sub_dir_ori = "0000"
    sub_dir = "0000"
    for i in range(len(root_dir_dic[branch_name][1])):
        if i >= nFiles_uplimit*nFiles_step:
            sub_dir = ("0000"+str(nFiles_uplimit))[-4:]
            try:
                os.mkdir("Data/"+branch_name+'/'+sub_dir)
            except:
                pass
            nFiles_uplimit += 1
        link_set_command = "ln -s %s ./Data/%s/%s"%(root_dir_dic[branch_name][1][i],branch_name, sub_dir)
        os.system(link_set_command)
        print "link set : %s"%(root_dir_dic[branch_name][1][i])

scanFile()
try:
    os.mkdir("Data")
except:
    pass

sum_file = 0
total_file = 0
for mc_name in root_dir_dic:
    if not root_dir_dic[mc_name][1]: continue
    try:
        os.mkdir("Data/"+mc_name)
    except:
        pass
#    setlink(mc_name,root_dir_dic[mc_name][1])
    sum_file+=len(root_dir_dic[mc_name][1])

print "splited files: %d , total files: %d"%(sum_file,len(rootfile_list))
