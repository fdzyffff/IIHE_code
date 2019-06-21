import ROOT
import os

split_dic = {
}

root_dir_dic ={
#"ttbar2l2u" 	: ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8",[]],
#"WW"            : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/WW_TuneCUETP8M1_13TeV-pythia8",[]],
#"WZ"            : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/WZ_TuneCUETP8M1_13TeV-pythia8",[]],
#"ZZ"            : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/ZZ_TuneCUETP8M1_13TeV-pythia8",[]],
#"DYToTT"        : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"ST_top"        : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1",[]],
#"ST_antitop"    : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1",[]],
#"Wjets"         : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],
#"DYToEE"        : ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",[]],

"ZToEE_M_50_120"        :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_50_120/crab_ZToEE_NNPDF30_13TeV-powheg_M_50_120",[]],
"ZToEE_M_120_200"       :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_120_200/crab_ZToEE_NNPDF30_13TeV-powheg_M_120_200",[]],
"ZToEE_M_200_400"       :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_200_400/crab_ZToEE_NNPDF30_13TeV-powheg_M_200_400",[]],
"ZToEE_M_400_800"       :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_400_800/crab_ZToEE_NNPDF30_13TeV-powheg_M_400_800/",[]],
"ZToEE_M_800_1400"      :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_800_1400/crab_ZToEE_NNPDF30_13TeV-powheg_M_800_1400",[]],
"ZToEE_M_1400_2300"     :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_1400_2300/crab_ZToEE_NNPDF30_13TeV-powheg_M_1400_2300",[]],
"ZToEE_M_2300_3500"     :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_2300_3500/crab_ZToEE_NNPDF30_13TeV-powheg_M_2300_3500",[]],
"ZToEE_M_3500_4500"     :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_3500_4500/crab_ZToEE_NNPDF30_13TeV-powheg_M_3500_4500",[]],
"ZToEE_M_4500_6000"     :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_4500_6000/crab_ZToEE_NNPDF30_13TeV-powheg_M_4500_6000",[]],
"ZToEE_M_6000_Inf"      :       ["/pnfs/iihe/cms/store/user/wenxing/Run2_2016/Prefiring/ForAccEff/ZToEE_NNPDF30_13TeV-powheg_M_6000_Inf/crab_ZToEE_NNPDF30_13TeV-powheg_M_6000_Inf",[]],

#"DYToEEmad"     : ["/pnfs/iihe/cms/store/user/wenxing/MC_102X_Scale_Smear/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",[]],
#"ZToEE_M_50_120"        :       ["/pnfs/iihe/cms/store/user/amkalsi/Moriond2018/ZToEE_NNPDF31_13TeV-powheg_M_50_120/crab_ZToEE_NNPDF31_13TeV-powheg_M_50_120/180218_161630/0000/",[]],

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
