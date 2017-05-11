import ROOT
import os

split_dic = {
}

root_dir_dic ={
"madgraph_DYToLL_10to50":["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",[]],
"madgraph_DYToLL_50"	:["/pnfs/iihe/cms/store/user/xgao/2017MC_Moriond/2017-04/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",[]],
#"DYToLL_10to50"	:["/pnfs/iihe/cms/store/user/xgao/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToLL_50"	:["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"WWTo2L2Nu"	:["/pnfs/iihe/cms/store/user/xgao/WWTo2L2Nu_13TeV-powheg",[]],
#"WZTo3LNu"	:["/pnfs/iihe/cms/store/user/xgao/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8",[]],
#"WZTo2L2Q"	:["/pnfs/iihe/cms/store/user/xgao/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8",[]],
#"ZZTo2L2Nu"	:["/pnfs/iihe/cms/store/user/xgao/ZZTo2L2Nu_13TeV_powheg_pythia8",[]],
#"ZZTo4L"	:["/pnfs/iihe/cms/store/user/xgao/ZZTo4L_13TeV_powheg_pythia8",[]],
#"tW"		:["/pnfs/iihe/cms/store/user/xgao/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1",[]],
#"tW_anti"	:["/pnfs/iihe/cms/store/user/xgao/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1",[]],
#"TTTo2L2Nu"	:["/pnfs/iihe/cms/store/user/xgao/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8",[]],
#"TTWJetsToQQ"	:["/pnfs/iihe/cms/store/user/xgao/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8",[]],
#"TTWJetsToLNu"	:["/pnfs/iihe/cms/store/user/xgao/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8",[]],
#"TTZToLLNuNu_10":["/pnfs/iihe/cms/store/user/xgao/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8",[]],
#"TTZToQQ"	:["/pnfs/iihe/cms/store/user/xgao/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8",[]],
#"TTGJets"	:["/pnfs/iihe/cms/store/user/xgao/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8",[]],
#"WJetsToLNu"	:["/pnfs/iihe/cms/store/user/xgao/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",[]],
#"WGToLNuG"	:["/pnfs/iihe/cms/store/user/xgao/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],

#""		:["",[]],
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
