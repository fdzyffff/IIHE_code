import os
import sys

MYDIR=os.getcwd()
sys_dic={
"nor":"norminal",
#"muptu":"sys_mu_pt_scale_up",
#"muresu":"sys_mu_pt_res_up",
#"eletu":"sys_ele_et_scale_up",
}

file_root_dir_dic={
	    #[isData,isZToTT,isTTbin,isWWbin,
"../MC/DYToLL"		:[[False,False,False,False,"DYToLL_amc"],[0]],
"../MC/ST_antitop"	:[[False,False,False,False,"ST_anti"],[0]],
"../MC/ST_top"		:[[False,False,False,False,"ST"],[0]],
"../MC/WW"		:[[False,False,False,False,"WW"],[0]],
"../MC/WZ"		:[[False,False,False,False,"WZ"],[0]],
"../MC/ZZ"		:[[False,False,False,False,"ZZ"],[0]],
"../MC/ttbar2l2u"	:[[False,False,False,False,"TT_2L2Nu"],[0]],
#"../MC/QBH_n4_M1000"	:[[False,False,False,False],[0]],
#"../MC/RPV_M1000"	:[[False,False,False,False],[0]],
#"../MC/ZPrime_M1000"	:[[False,False,False,False],[0]],
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
    for sys_typ in sys_dic:
        sys_str = sys_dic[sys_typ]
        for reskim in reskim_dic:
            isData = reskim_dic[reskim][0][0]
            isDYbin = reskim_dic[reskim][0][1]
            isTTbin = reskim_dic[reskim][0][2]
            isWWbin = reskim_dic[reskim][0][3]
            mc_str = reskim_dic[reskim][0][4]
            triggerVersion = reskim_dic[reskim][2][0]
            n_job = 0
            sub_n_total_job = 0
            n_start = True
            job_text = ""
            i = 0
            for root_file in reskim_dic[reskim][1]:
                sample_name = root_file.split("/")[-3] 
                subdir_name = root_file.split("/")[-2] 
                file_name = root_file.split("/")[-1] 
                output_name = "ntuples/batchmc/%s_%s_%s_%s_%s"%(label,sample_name,subdir_name,sys_typ,file_name)
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
                    job_text+=("python reskim_all.py -r %s -o %s --isData %s --isDYbin %s --isTTbin %s --isWWbin %s -t %s -m %s -s %s\n"%(root_file, output_name, isData, isDYbin, isTTbin, isWWbin, triggerVersion, mc_str, sys_str))
                    n_job+=1
                i+=1
                if (n_job%n_file_per_job==0 and n_job>0) or (i >= len(reskim_dic[reskim][1])):
                    n_job=0
                    n_start=True
                    n_total_job += 1
                    sub_n_total_job += 1
                    tmp_label = "%s%s_%s"%(reskim,sub_n_total_job,sys_typ)
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
make_sub("fke_2017_MC",150)
