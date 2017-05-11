import os
import sys

MYDIR=os.getcwd()
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

def make_dic(input_dir,check_dir = ""):
    tmp_name = "filter"
    print "%s making file list %s"%("#"*15,"#"*15)
    n_total = 0
    file_list = my_walk_dir(input_dir,[])
    file_list.sort()
    if check_dir == "":
        reskim_dic[tmp_name] = [file_list,[]]
    else:
        reskim_dic[tmp_name] = [file_list,my_walk_dir(check_dir,[])]
    print "     %s : %d"%(input_dir,len(reskim_dic[tmp_name][0]))
    n_total += len(reskim_dic[tmp_name][0])
    print "     Total root files : %d"%(n_total)

def make_sub(label,n_file_per_job):
    print "%s making jobs script, %d root files/job %s"%("#"*15,n_file_per_job,"#"*15)
    try:
        if isCheck:
            tmp_dir='check_filter_%s'%(label)
        else:
            tmp_dir='filter_%s'%(label)
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
        n_job = 0
        sub_n_total_job = 0
        n_start = True
        job_text = ""
        i = 0
        for root_file in reskim_dic[reskim][0]:
            file_name = root_file.split("/")[-1] 
            output_name = "ntuples/batchdata_filter_out/%s"%(file_name)
            if n_start:
                n_start=False
                job_text = ""
                job_text+=("curr_dir=%s\n"%(MYDIR))
                job_text+=("cd %s\n"%(MYDIR))
                job_text+=("source env2.sh\n")
                job_text+=("cd ../\n")
            if (not isCheck) or (not output_name in reskim_dic[reskim][1]):
                job_text+=("python event_filter_split.py -r %s -o %s\n"%(root_file, output_name))
                n_job+=1
            i+=1
            if (n_job%n_file_per_job==0 and n_job>0) or (i >= len(reskim_dic[reskim][0])):
                n_job=0
                n_start=True
                n_total_job += 1
                sub_n_total_job += 1
                tmp_label = "%s_%s"%(reskim,sub_n_total_job)
                tmp_jobname="flt_%s.jobb"%(tmp_label)
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
#make_dic("../ntuples/batchdata_loop_2","../ntuples/batchdata_filter_out")
make_dic("../ntuples/batchdata_loop_2")
make_sub("2016_DoubleEG",150)
