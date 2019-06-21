import os
import sys
import ROOT

from input_ttbar_mass_gen import *


def make_sub(label,n_file_per_job):
    global reskim_dic
    print "%s making jobs script, %d root files/job %s"%("#"*15,n_file_per_job,"#"*15)
    try:
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
    try :
        os.system("mkdir batchmc")
    except:
        pass
    for reskim in reskim_dic:
        weight_lumi_1fb = reskim_dic[reskim][0][1] / reskim_dic[reskim][0][0]
        cut_value = reskim_dic[reskim][0][2]
        n_job = 0
        sub_n_total_job = 0
        n_start = True
        job_text = ""
        i = 0
        for root_file in reskim_dic[reskim][1]:
            sample_name = root_file.split("/")[-3] 
            subdir_name = root_file.split("/")[-2] 
            file_name = root_file.split("/")[-1] 
            output_name = "batchmc/%s_%s_%s_%s"%(label,sample_name,subdir_name,file_name)
            tmp_label = reskim
            if n_start:
                n_start=False
                job_text = ""
                job_text+=("curr_dir=%s\n"%(MYDIR))
                job_text+=("cd %s\n"%(MYDIR))
                job_text+=("source env2.sh\n")
                #job_text+=("cd ../\n")
            job_text+=("python ttbar_mass_gen.py -i %s -o %s -w %s -c %s \n"%(root_file, output_name, weight_lumi_1fb, cut_value))
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

make_dic()
make_sub("2017_ttbar",10)
