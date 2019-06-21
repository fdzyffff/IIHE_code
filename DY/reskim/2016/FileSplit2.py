import ROOT
import os

root_dir_dic ={
'rB_1'	:['/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DoubleEG/crab_DoubleEG_Run2016B-17Jul2018_v2',[]],
'rC_1'	:['/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DoubleEG/crab_DoubleEG_Run2016C-17Jul2018-v1',[]],
'rD_1'	:['/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DoubleEG/crab_DoubleEG_Run2016D-17Jul2018-v1',[]],
'rE_1'	:['/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DoubleEG/crab_DoubleEG_Run2016E-17Jul2018-v1',[]],
'rF_1'	:['/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DoubleEG/crab_DoubleEG_Run2016F-17Jul2018-v1',[]],
'rG_1'	:['/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DoubleEG/crab_DoubleEG_Run2016G-17Jul2018-v1',[]],
'rH_1'	:['/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DoubleEG/crab_DoubleEG_Run2016H-17Jul2018-v1',[]],
}
rootfile_list = []



def my_walk_dir(my_dir,my_list):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            if 'failed' 	in tmp_file_name:continue
#            if not '_skimed' 	in tmp_file_name:continue
            if not '.root' 	in tmp_file_name:continue
            my_list.append(tmp_file_name)
            print tmp_file_name
        else:
            my_walk_dir(tmp_file_name,my_list)
    return 

def scanFile():
    rootfile_list = []
    for rootfile_dir in root_dir_dic:
        my_walk_dir(root_dir_dic[rootfile_dir][0],root_dir_dic[rootfile_dir][1])
        root_dir_dic[rootfile_dir][1].sort()
        rootfile_list = rootfile_list + root_dir_dic[rootfile_dir][1]
    return rootfile_list

def setlink(branch_name, split_dic):
    n_total = 0
    nFiles_uplimit = 0
    nFiles_step = 50
    sub_dir_ori = "0000"
    sub_dir = "0000"
    for i in range(len(split_dic[branch_name][1])):
        if  i >= nFiles_uplimit*nFiles_step:
            sub_dir = ("0000"+str(nFiles_uplimit))[-4:]
            try:
                os.mkdir('Data/'+branch_name+'/'+sub_dir)
            except:
                pass
            nFiles_uplimit += 1
        os.system("ln -s %s Data/%s/%s"%(split_dic[branch_name][1][i],branch_name, sub_dir))
        print "link set : %s"%(split_dic[branch_name][1][i])
        n_total += 1

rootfile_list = scanFile()
print len(rootfile_list)

sum_file = 0
for branch_name in root_dir_dic:
    if not root_dir_dic[branch_name][1]: continue
    try:
        os.mkdir('Data')
    except:
        pass
    try:
        os.mkdir('Data/'+branch_name)
    except:
        pass
    setlink(branch_name,root_dir_dic)
    sum_file+=len(root_dir_dic[branch_name][1])

print "splited files: %d , total files: %d"%(sum_file,len(rootfile_list))
