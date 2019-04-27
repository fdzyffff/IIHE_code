import ROOT
import os

split_dic = {
}

root_dir_dic ={
"ttbar2l2u"     : ["/pnfs/iihe/cms/store/user/xgao/2017samples-20190418/MC/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_TTTo2L2Nu_TuneCP5_13TeV/",[]],
"WW"            : ["/pnfs/iihe/cms/store/user/xgao/2017samples-20190418/MC/WW_TuneCP5_13TeV-pythia8/crab_WW-v2/",[]],
"WZ"            : ["/pnfs/iihe/cms/store/user/xgao/2017samples-20190418/MC/WZ_TuneCP5_13TeV-pythia8/crab_WZ/",[]],
"ZZ"            : ["/pnfs/iihe/cms/store/user/xgao/2017samples-20190418/MC/ZZ_TuneCP5_13TeV-pythia8/crab_ZZ",[]],
"DYToLL"        : ["/pnfs/iihe/cms/store/user/xgao/2017samples-20190418/MC/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_TuneCP5_13TeV/",[]],
"ST_top"        : ["/pnfs/iihe/cms/store/user/xgao/2017samples-20190418/MC/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV/",[]],
"ST_antitop"    : ["/pnfs/iihe/cms/store/user/xgao/2017samples-20190418/MC/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-v2/",[]],

#"ttbar2l2u_1" 	: ["/2017-04/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8",[]],
#"WW1"           : ["/2017-04/WWTo2L2Nu_13TeV-powheg",[]],

#"QBH_n4_M1000"    : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/QBHToEMu_M-1000_n4_ADD_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
#"ZPrime_M1000"    : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/ZPrimeToEMu_M_1000_TuneCUETP8M1_13TeV_pythia8",[]],
#"RPV_M1000"    : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/RPVresonantToEMu_M-1000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
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
        #print root_dir_dic[rootfile_dir][1]
    
def setlink(branch_name, filelist):
    nFiles_uplimit = 0
    nFiles_step = 100
    sub_dir_ori = "0000"
    sub_dir = "0000"
    for i in range(len(root_dir_dic[branch_name][1])):
        if i >= nFiles_uplimit*nFiles_step:
            sub_dir = ("0000"+str(nFiles_uplimit))[-4:]
            try:
                os.mkdir("MC/"+branch_name+'/'+sub_dir)
            except:
                pass
            nFiles_uplimit += 1
        link_set_command = "ln -s %s ./MC/%s/%s"%(root_dir_dic[branch_name][1][i],branch_name, sub_dir)
        os.system(link_set_command)
        print "link set : %s"%(root_dir_dic[branch_name][1][i])

scanFile()
try:
    os.mkdir("MC")
except:
    pass

sum_file = 0
total_file = 0
for mc_name in root_dir_dic:
    if not root_dir_dic[mc_name][1]: continue
    try:
        os.mkdir("MC/"+mc_name)
    except:
        pass
    setlink(mc_name,root_dir_dic[mc_name][1])
    sum_file+=len(root_dir_dic[mc_name][1])

print "splited files: %d , total files: %d"%(sum_file,len(rootfile_list))
