import ROOT
import os

split_dic = {
}

root_dir_dic ={
"ttbar2l2u_Mall"     	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8",[]], 
"ttbar2l2u_M500to800"   : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/TTToLL_MLL_500To800_TuneCUETP8M1_13TeV-powheg-pythia8",[]], 
"ttbar2l2u_M800to1200"  : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/TTToLL_MLL_800To1200_TuneCUETP8M1_13TeV-powheg-pythia8",[]], 
"ttbar2l2u_M1200to1800" : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/TTToLL_MLL_1200To1800_TuneCUETP8M1_13TeV-powheg-pythia8",[]], 
"ttbar2l2u_M1800toInf"  : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/TTToLL_MLL_1800ToInf_TuneCUETP8M1_13TeV-powheg-pythia8",[]], 
"WW2l2u"            	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/WWTo2L2Nu_13TeV-powheg",[]], 
"WW_M200to600"          : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/WWTo2L2Nu_Mll_200To600_13TeV-powheg",[]], 
"WW_M600to1200"         : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/WWTo2L2Nu_Mll_600To1200_13TeV-powheg",[]], 
"WW_M1200to2500"        : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/WWTo2L2Nu_Mll_1200To2500_13TeV-powheg",[]], 
"WW_M2500toInf"         : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/WWTo2L2Nu_Mll_2500ToInf_13TeV-powheg",[]], 
"WZ"            	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/WZ_TuneCUETP8M1_13TeV-pythia8",[]], 
"ZZ"            	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ZZ_TuneCUETP8M1_13TeV-pythia8",[]], 
"DYToLL"        	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]], 
"ST_top"        	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1",[]], 
"ST_antitop"    	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1",[]],
"WZTo2L2Q"              : ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8",[]],
"WZTo3LNu"              : ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/crab_WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8",[]],
"ZZTo2L2Nu"             : ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZZTo2L2Nu_13TeV_powheg_pythia8/crab_ZZTo2L2Nu_13TeV_powheg_pythia8",[]],
"ZZTo2L2Q"              : ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZZTo2L2Q_13TeV_powheg_pythia8/crab_ZZTo2L2Q_13TeV_powheg_pythia8",[]],
"ZZTo4L"                : ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZZTo4L_13TeV_powheg_pythia8/crab_ZZTo4L_13TeV_powheg_pythia8",[]],

#######################################
"QBHtoEMu_M200"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M200_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M400"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M400_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M600"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M600_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M800"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M800_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M1000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M1000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M1200"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M1200_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M1400"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M1400_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M1600"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M1600_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M1800"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M1800_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M2000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M2000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M2500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M2500_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M3000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M3000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M3500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M3500_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M4000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M4000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M4500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M4500_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M5000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M5000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M5500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M5500_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M6000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M6000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M7000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M7000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M8000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M8000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M9000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M9000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],
"QBHtoEMu_M10000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/QBHtoEMu_n4_ADD_M10000_TuneCUETP8M1_13TeV-QBH-pythia8",[]],

"RPVresonantToEMu_M200"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-200_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M300"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-300_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M400"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-400_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-500_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M600"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-600_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M700"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-700_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M800"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-800_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M900"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-900_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M1000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-1000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M1200"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-1200_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M1400"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-1400_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M1600"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-1600_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M1800"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-1800_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M2000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-2000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M2500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-2500_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M3000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-3000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M3500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-3500_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M4000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-4000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M4500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-4500_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M5000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-5000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M5500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-5500_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M6000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-6000_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],
"RPVresonantToEMu_M6500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/RPVresonantToEMu_M-6500_LLE_LQD-001_TuneCUETP8M1_13TeV-calchep-pythia8",[]],

"ZPrimeToEMu_M1000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1000_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1100"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1100_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1200"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1200_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1300"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1300_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1400"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1400_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1500_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1600"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1600_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1700"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1700_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1800"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1800_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M1900"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_1900_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M2000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_2000_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M2200"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_2200_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M2400"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_2400_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M2600"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_2600_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M2800"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_2800_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M3000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_3000_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M3500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_3500_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M4000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_4000_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M4500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_4500_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M5000"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_5000_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M500"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_500_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M600"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_600_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M700"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_700_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M800"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_800_TuneCUETP8M1_13TeV_pythia8",[]],
"ZPrimeToEMu_M900"	:["/pnfs/iihe/cms/store/user/dbeghin/Legacy/2016/ZPrimeToEMu_M_900_TuneCUETP8M1_13TeV_pythia8",[]],
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
