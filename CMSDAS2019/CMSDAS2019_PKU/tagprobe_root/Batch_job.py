from definations import *

main_file_list = []
my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_A/', main_file_list)
my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_B/', main_file_list)
my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_C/', main_file_list)
my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_D/', main_file_list)
MYDIR=os.getcwd()

def make_sub(label,n_file_per_job):
    global main_file_list
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

    n_total_job = 0
    try :
        os.system("mkdir output")
    except:
        pass
    for i in range(0, len(main_file_list), n_file_per_job):
        job_text = ""
        job_text+=("curr_dir=%s\n"%(MYDIR))
        job_text+=("cd %s\n"%(MYDIR))
        job_text+=("source env2.sh\n")
        job_text+=("python tagprobe1.py -s %s -n %s \n"%(i, n_file_per_job))
        n_total_job += 1

        tmp_label = "TaP_%s"%(n_total_job)
        tmp_jobname="sub_%s.jobb"%(tmp_label)
        tmp_job=open(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname,'w')
        tmp_job.write(job_text)
        tmp_job.close()
        os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+"sub_job/"+tmp_jobname))
        sub_log_command = "qsub -q localgrid -e %s/sub_err/err_%s_%s.dat -o %s/sub_out/out_%s_%s.dat %s"%(tmp_dir,label,tmp_label,tmp_dir,label,tmp_label,MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname)
        BigSub_job.write("qsub -q localgrid %s\n"%(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname))
    os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname))
    print "%d jobs created"%(n_total_job)

make_sub("2018_EGamma",80)
