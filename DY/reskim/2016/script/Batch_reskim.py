import os
import sys

MYDIR=os.getcwd()
file_root_dir_dic={
"../Data/rB":[[0,276452],['0','51']],#[run min, run max][version_ele27, version_ele33]
"../Data/rC":[[0,276452],['0','51']],#[run min, run max][version_ele27, version_ele33]
"../Data/rD":[[276453, 278822],['0','1']],#[run min, run max][version_ele27, version_ele33]
"../Data/rD_MW":[[0,276452],['0','51']],#[run min, run max][version_ele27, version_ele33]
"../Data/rE":[[276453, 278822],['0','1']],#[run min, run max][version_ele27, version_ele33]
"../Data/rF":[[276453, 278822],['0','1']],#[run min, run max][version_ele27, version_ele33]
"../Data/rG":[[276453, 278822],['0','1']],#[run min, run max][version_ele27, version_ele33]
"../Data/rG_MW":[[278823, 999999],['0','51']],#[run min, run max][version_ele27, version_ele33]"../rG__rMW":[[278823, 999999],['0','51']],#[run min, run max][version_ele27, version_ele33]
"../Data/H2":[[278823, 999999],['0','51']],#[run min, run max][version_ele27, version_ele33]
"../Data/H3":[[278823, 999999],['0','51']],#[run min, run max][version_ele27, version_ele33]
}
reskim_dic={
#"0_D_v51_S_v2":["D_v51_S_v2/0000"],
#"0_D_v61_S_v5":["D_v61_S_v5/0000"],
}

def make_dic():
    for file_dir in file_root_dir_dic:
        dir_name = file_dir.split("/")[-1]
        tmp_dir_name = os.path.join(file_dir.split("/")[-2],file_dir.split("/")[-1])
        for s in os.listdir(file_dir):
            reskim_dic[s+"_"+dir_name]=[]
            reskim_dic[s+"_"+dir_name].append(os.path.join(tmp_dir_name,s))
            version_ele27 = file_root_dir_dic[file_dir][1][0]
            version_ele33 = file_root_dir_dic[file_dir][1][1]
            reskim_dic[s+"_"+dir_name].append(version_ele33)
            reskim_dic[s+"_"+dir_name].append(version_ele27)
            reskim_dic[s+"_"+dir_name].append(file_root_dir_dic[file_dir][0][0])
            reskim_dic[s+"_"+dir_name].append(file_root_dir_dic[file_dir][0][1])
            print "%s: %s"%(s+"_"+dir_name,reskim_dic[s+"_"+dir_name])

def subpu(label):
    try:
        tmp_dir='sub_%s'%(label)
        os.mkdir(tmp_dir)
    except:
        pass
    try:
        os.system('mkdir %s/sub_err'%tmp_dir)
        os.system('mkdir %s/sub_out'%tmp_dir)
        os.system('mkdir %s/sub_job'%tmp_dir)
    except:
        print "err!"
        pass
    i=0
    tmp_bigsubname = "BigSubmit_%s.jobb"%(label)
    BigSub_job = open(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname,'w')
    sub_log_name = "sub_log_%s.log"%(label)
    sub_log = open(MYDIR+'/'+tmp_dir+'/'+sub_log_name,'w')

    for reskim in reskim_dic:
        try:
            root_dir = reskim_dic[reskim][0]
            trig_vd = reskim_dic[reskim][1]
            trig_vs = reskim_dic[reskim][2]
            run_start = reskim_dic[reskim][3]
            run_end = reskim_dic[reskim][4]
            output_name = "ntuples/batchdata_2/data_2016_DoubleEG_%s.root"%(reskim)
            tmp_label = reskim
            tmp_jobname="sub_%s.jobb"%(reskim)
            tmp_job=open(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname,'w')
            tmp_job.write("curr_dir=%s\n"%(MYDIR))
            tmp_job.write("cd %s\n"%(MYDIR))
            tmp_job.write("source env2.sh\n")
            tmp_job.write("cd ../\n")
            tmp_job.write("python reskim_all.py -r %s -o %s -d %s -s %s -e %s\n"%(root_dir, output_name, trig_vd, run_start, run_end))
            tmp_job.write("\n")
            tmp_job.close()
            os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+"sub_job/"+tmp_jobname))
            sub_log_command = "qsub -q localgrid -e %s/sub_err/err_%s_%s.dat -o %s/sub_out/out_%s_%s.dat %s"%(tmp_dir,label,tmp_label,tmp_dir,label,tmp_label,MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname)
#            os.system(sub_log_command)
            sub_log.write("%s\n"%(sub_log_command))
            BigSub_job.write("qsub -q localgrid %s\n"%(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname))
        except:
            print "job created failed"
        i+=1
        print "%d / %d jobs created (%0.2f%%)"%(i, len(reskim_dic), float(i)*100.0/float(len(reskim_dic)))
        #break
    os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname))

make_dic()
subpu("DoubleEG_rereco_2")
