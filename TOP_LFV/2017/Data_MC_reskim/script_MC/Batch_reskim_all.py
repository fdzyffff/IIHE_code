import os
import sys

MYDIR=os.getcwd()
file_root_dir_dic={
	    #[isData,isZToTT,isTTbin,isWWbin,

#"../MC/1j_DY_50"           :[[False,False,False,False],[0]],
#"../MC/2j_DY_50"           :[[False,False,False,False],[0]],
#"../MC/3j_DY_50"           :[[False,False,False,False],[0]],
#"../MC/4j_DY_50"           :[[False,False,False,False],[0]],
#"../MC/1j_DY_10_50"           :[[False,False,False,False],[0]],
#"../MC/2j_DY_10_50"           :[[False,False,False,False],[0]],
#"../MC/3j_DY_10_50"           :[[False,False,False,False],[0]],
#"../MC/4j_DY_10_50"           :[[False,False,False,False],[0]],

"../MC/DYToLL_10to50"           :[[False,False,False,False],["MC"]],
"../MC/DYToLL_50"               :[[False,False,False,False],["MC"]],

"../MC/TTGJets"                 :[[False,False,True,False],["MC"]],
"../MC/TTTo2L2Nu"               :[[False,False,True,False],["MC"]],
"../MC/TTWJetsToLNu"            :[[False,False,True,False],["MC"]],
"../MC/TTWJetsToQQ"             :[[False,False,True,False],["MC"]],
"../MC/TTZToLLNuNu_10"          :[[False,False,True,False],["MC"]],
"../MC/TTZToQQ"                 :[[False,False,True,False],["MC"]],

"../MC/WGToLNuG"                :[[False,False,False,False],["MC"]],
"../MC/WJetsToLNu"              :[[False,False,False,False],["MC"]],
"../MC/WWTo2L2Nu"               :[[False,False,False,False],["MC"]],
"../MC/WZTo2L2Q"                :[[False,False,False,False],["MC"]],
"../MC/WZTo3LNu"                :[[False,False,False,False],["MC"]],
"../MC/ZZTo2L2Nu"               :[[False,False,False,False],["MC"]],
"../MC/ZZTo4L"                  :[[False,False,False,False],["MC"]],
"../MC/tW"                      :[[False,False,False,False],["MC"]],
"../MC/tW_anti"                 :[[False,False,False,False],["MC"]],
#
#"../MC/ST_tug_FCNC"                 :[[False,False,False,False],[0]],
#"../MC/ST_tcg_FCNC"                 :[[False,False,False,False],[0]],
#
#"../MC/inc_TT"                 :[[False,False,False,False],[0]],
#"../MC/inc_ST_top"                 :[[False,False,False,False],[0]],
#"../MC/inc_ST_antitop"                 :[[False,False,False,False],[0]],

#"../MC/ggHWW"           :[[False,False,False,False],[0]],
#"../MC/VBFHWW"           :[[False,False,False,False],[0]],
}
reskim_dic={
}

def my_walk_dir(my_dir,my_list):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            if 'failed'         in tmp_file_name:continue
            if not '.root'      in tmp_file_name:continue
            my_list.append(tmp_file_name[3:])
        else:
            my_walk_dir(tmp_file_name,my_list)
    return my_list

def make_dic(check_dir = ""):
    if check_dir != "":isCheck = True
    print "%s making file list %s"%("#"*15,"#"*15)
    n_total = 0
    for file_dir in file_root_dir_dic:
        tmp_name = ""
        for i in file_dir.split("/"):
            if (not i == ".") and (not i == ".."):
                tmp_name += "%s_"%(i)
        file_list = my_walk_dir(file_dir,[])
        file_list.sort()
        if check_dir == "":
            reskim_dic[tmp_name] = [file_root_dir_dic[file_dir][0],file_list,file_root_dir_dic[file_dir][1],[]]
        else:
            reskim_dic[tmp_name] = [file_root_dir_dic[file_dir][0],file_list,file_root_dir_dic[file_dir][1],my_walk_dir(check_dir,[])]
        print "     %s : %d"%(file_dir,len(reskim_dic[tmp_name][1]))
        n_total += len(reskim_dic[tmp_name][1])
    print "     Total root files : %d"%(n_total)

def make_sub(label,n_file_per_job):
    print "%s making jobs script, %d root files/job %s"%("#"*15,n_file_per_job,"#"*15)
    try:
        if isCheck:
            tmp_dir='check_sub_%s'%(label)
        else:
            tmp_dir='sub_%s'%(label)
        os.mkdir(tmp_dir)
    except:
        pass
    try:
        os.system('mkdir %s/sub_err'%tmp_dir)
        os.system('mkdir %s/sub_out'%tmp_dir)
        os.system('mkdir %s/sub_job'%tmp_dir)
        os.system('mkdir %s/BigSub'%tmp_dir)
    except:
        print "err!"
        pass
    i=0
    tmp_bigsubname = "BigSubmit_%s.jobb"%(label)
    BigSub_job = open(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname,'w')
    sub_log_name = "sub_log_%s.log"%(label)
    sub_log = open(MYDIR+'/'+tmp_dir+'/'+sub_log_name,'w')

    n_total_job = 0
    for reskim in reskim_dic:
        isData = reskim_dic[reskim][0][0]
        isDY = reskim_dic[reskim][0][1]
        isTTbin = reskim_dic[reskim][0][2]
        isWWbin = reskim_dic[reskim][0][3]
        mc_str = reskim_dic[reskim][2][0]
        n_job = 0
        sub_n_total_job = 0
        n_start = True
        job_text = ""
        i = 0
        for root_file in reskim_dic[reskim][1]:
            sample_name = root_file.split("/")[-3] 
            subdir_name = root_file.split("/")[-2] 
            file_name = root_file.split("/")[-1] 
            output_name = "ntuples/batchmc/%s_%s_%s_%s"%(label,sample_name,subdir_name,file_name)
            tmp_label = reskim
            if n_start:
                n_start=False
                job_text = ""
                job_text+=("curr_dir=%s\n"%(MYDIR))
                job_text+=("cd %s\n"%(MYDIR))
                job_text+=("source env2.sh\n")
                job_text+=("cd ../\n")
            if (not isCheck) or (not output_name in reskim_dic[reskim][3]):
                #if isCheck:print output_name
                job_text+=("python reskim_all.py -r %s -o %s --isData %s --isDY %s --isTTbin %s --isWWbin %s -s %s\n"%(root_file, output_name, isData, isDY, isTTbin, isWWbin, mc_str))
                n_job+=1
            i+=1
            if (n_job%n_file_per_job==0 and n_job>0) or (i >= len(reskim_dic[reskim][1])):
                n_job=0
                n_start=True
                n_total_job += 1
                sub_n_total_job += 1
                tmp_label = "%s%s"%(reskim,sub_n_total_job)
                tmp_jobname="sub_%s.jobb"%(tmp_label)
                tmp_job=open(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname,'w')
                tmp_job.write(job_text)
                tmp_job.close()
                os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+"sub_job/"+tmp_jobname))
                sub_log_command = "qsub -q localgrid -e %s/sub_err/err_%s_%s.dat -o %s/sub_out/out_%s_%s.dat %s"%(tmp_dir,label,tmp_label,tmp_dir,label,tmp_label,MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname)
                #os.system(sub_log_command)
                sub_log.write("%s\n"%(sub_log_command))
                BigSub_job.write("qsub -q localgrid %s\n"%(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname))
    os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname))
    print "%d jobs created"%(n_total_job)

isCheck = True
isCheck = False
make_dic()
#make_dic("../ntuples/batchmc")
make_sub("2017_MC_80",100)
