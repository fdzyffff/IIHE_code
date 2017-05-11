import ROOT
import os

split_dic = {
'D_v3':[['trig_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v3_accept'],[],[]],
'D_v4':[['trig_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v4_accept'],[],[]],
'D_v5':[['trig_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v5_accept'],[],[]],
'D_v6':[['trig_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v6_accept'],[],[]],
}

root_dir_dic ={
'DoubleEG_Run2016B_PromptReco_v2_AOD': '/group/HEEP/Golden_2016_400to765/DoubleEG_Run2016B_PromptReco_v2_AOD',
'DoubleEG_Run2016C_PromptReco_v2_AOD': '/group/HEEP/Golden_2016_400to765/DoubleEG_Run2016C_PromptReco_v2_AOD',
}
file_list = []
rootfile_list = []



def my_walk_dir(my_dir,my_list):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            my_list.append(tmp_file_name)
        else:
            my_walk_dir(tmp_file_name,my_list)
    return 

for rootfile_dir in root_dir_dic:
    my_walk_dir(root_dir_dic[rootfile_dir],file_list)
for filename in file_list:
    if '.root' in filename and (not 'failed' in filename):
        rootfile_list.append(filename)

for rootfilename in rootfile_list:
    print rootfilename
    file0 = ROOT.TFile.Open(rootfilename)
    tree = ROOT.gDirectory.Get('IIHEAnalysis')
    tmp_name_list = []
    appended = False
    for leaf in tree.GetListOfLeaves():
        name = leaf.GetName()
        tmp_name_list.append(name)
    for branch_name in split_dic:
#        if appended:break
        tmp_in = True
        for tmp_name in split_dic[branch_name][0]:
            if not (tmp_name in tmp_name_list):
                tmp_in = False
                break
#        if tmp_in and not appended:
        if tmp_in :
            split_dic[branch_name][1].append(rootfilename)
            appended = True
            run_list = []
            entry_total = tree.GetEntries()
            for event in tree:
                runNo = getattr(event,'ev_run')
                if runNo not in run_list:
                    run_list.append(runNo)
                sum = 0
                for run in run_list:
                    sum+=tree.Draw('','ev_run == %s'%(str(runNo)))
                if int(sum) == entry_total:
                    break
            for run in run_list: 
                if not run in split_dic[branch_name][2]:
                    split_dic[branch_name][2].append(run)
    #break
sum_file = 0
for branch_name in split_dic:
    if not split_dic[branch_name][1]: continue
    split_dic[branch_name][2].sort()
    print "*"*20
    print "Run No: from %d to %d , triggerversion: %s"%(split_dic[branch_name][2][0],split_dic[branch_name][2][-1],split_dic[branch_name][0])
    sum_file+=len(split_dic[branch_name][1])

print "#"*20
print "splited files: %d , total files: %d"%(sum_file,len(rootfile_list))
