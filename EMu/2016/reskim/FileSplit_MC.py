import ROOT
import os

split_dic = {
}

root_dir_dic ={
#"ttbar" 	: ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8",[]],
#"ttbar2l2u_1" 	: ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8",[]],
#"ttbar2l2u_2" 	: ["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC/TTToLL_MLL_500To800_TuneCUETP8M1_13TeV-powheg-pythia8",[]],
#"ttbar2l2u_3" 	: ["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC/TTToLL_MLL_800To1200_TuneCUETP8M1_13TeV-powheg-pythia8",[]],
#"ttbar2l2u_4" 	: ["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC/TTToLL_MLL_1200To1800_TuneCUETP8M1_13TeV-powheg-pythia8",[]],
#"ttbar2l2u_5" 	: ["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC/TTToLL_MLL_1800ToInf_TuneCUETP8M1_13TeV-powheg-pythia8",[]],
#"WW1"           : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/WWTo2L2Nu_13TeV-powheg",[]],
#"WW2"		: ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/WWTo2L2Nu_Mll_200To600_13TeV-powheg",[]],
#"WW3"		: ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/WWTo2L2Nu_Mll_600To1200_13TeV-powheg",[]],
#"WW4"		: ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/WWTo2L2Nu_Mll_1200To2500_13TeV-powheg",[]],
#"WW5"		: ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/WWTo2L2Nu_Mll_2500ToInf_13TeV-powheg",[]],
#"WZ"            : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/WZ_TuneCUETP8M1_13TeV-pythia8",[]],
#"ZZ"            : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/ZZ_TuneCUETP8M1_13TeV-pythia8",[]],
#"DYToLL_2"      : ["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_1"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_3"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-400to500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_4"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-500to700_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_5"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-700to800_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_6"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-800to1000_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_7"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-1000to1500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_8"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-1500to2000_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_9"      : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-2000to3000_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"ST_top"        : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_top",[]],
#"ST_antitop"    : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_antitop",[]],

"QBH_n4_M1000"    : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/QBHToEMu_M-1000_n4_ADD_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"ZPrime_M1000"    : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/ZPrimeToEMu_M_1000_TuneCUETP8M1_13TeV_pythia8",[]],
"RPV_M1000"    : ["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/RPVresonantToEMu_M-1000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
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
