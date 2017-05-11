import os
import sys

MYDIR=os.getcwd()
file_root_dir_dic={
"../Data/rB":[[0,999999],['0','0']],
"../Data/rC":[[0,999999],['0','0']],
"../Data/rD":[[0,999999],['0','0']],
"../Data/rE":[[0,999999],['0','0']],
"../Data/rF":[[0,999999],['0','0']],
"../Data/rG":[[0,999999],['0','0']],
"../Data/H2":[[0,999999],['0','0']],
"../Data/H3":[[0,999999],['0','0']],

"../Data/rB_re":[[0,999999],['0','0']],
"../Data/rC_re":[[0,999999],['0','0']],
"../Data/rD_re":[[0,999999],['0','0']],
"../Data/rE_re":[[0,999999],['0','0']],
"../Data/rG_re":[[0,999999],['0','0']],
"../Data/H2_re":[[0,999999],['0','0']],
}
reskim_dic={
#"0_D_v51_S_v2":["D_v51_S_v2/0000"],
#"0_D_v61_S_v5":["D_v61_S_v5/0000"],
}

def make_dic():
    ntotal = 0
    for file_dir in file_root_dir_dic:
        dir_name = file_dir.split("/")[-1]
        tmp_dir_name = os.path.join(file_dir.split("/")[-2],file_dir.split("/")[-1])
        for s in os.listdir(file_dir):
            reskim_dic[s+"_"+dir_name]=[]
            reskim_dic[s+"_"+dir_name].append(os.path.join(tmp_dir_name,s))
            ntotal += len(os.listdir(os.path.join(file_dir,s)))
            version_ele27 = file_root_dir_dic[file_dir][1][0]
            version_ele33 = file_root_dir_dic[file_dir][1][1]
            reskim_dic[s+"_"+dir_name].append(version_ele33)
            reskim_dic[s+"_"+dir_name].append(version_ele27)
            reskim_dic[s+"_"+dir_name].append(file_root_dir_dic[file_dir][0][0])
            reskim_dic[s+"_"+dir_name].append(file_root_dir_dic[file_dir][0][1])
            #print "%s: %s"%(s+"_"+dir_name,reskim_dic[s+"_"+dir_name])
    print "total number of files : %d"%(ntotal)

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
        root_dir = reskim_dic[reskim][0]
        trig_vd = reskim_dic[reskim][1]
        trig_vs = reskim_dic[reskim][2]
        run_start = reskim_dic[reskim][3]
        run_end = reskim_dic[reskim][4]
        output_name = "ntuples/pk_batchdata_loop_1/iihe_2016_SingleMuon_%s"%(reskim)
        tmp_label = reskim
        tmp_jobname="SMp_%s.jobb"%(reskim)
        tmp_job=open(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname,'w')
        tmp_job.write("curr_dir=%s\n"%(MYDIR))
        tmp_job.write("cd %s\n"%(MYDIR))
        tmp_job.write("source env2.sh\n")
        tmp_job.write("cd ../\n")
        tmp_job.write("python event_pick2.py -r %s -o %s\n"%(root_dir, output_name))
        #tmp_job.write("python event_pick.py -r %s -o %s -s %s -e %s\n"%(root_dir, output_name,run_start, run_end))
        tmp_job.write("\n")
        tmp_job.close()
        os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+"sub_job/"+tmp_jobname))
        sub_log_command = "qsub -q localgrid -e %s/sub_err/err_%s_%s.dat -o %s/sub_out/out_%s_%s.dat %s"%(tmp_dir,label,tmp_label,tmp_dir,label,tmp_label,MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname)
#        os.system(sub_log_command)
        sub_log.write("%s\n"%(sub_log_command))
        BigSub_job.write("qsub -q localgrid %s\n"%(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname))
        i+=1
        print "%d / %d jobs created (%0.2f%%)"%(i, len(reskim_dic), float(i)*100.0/float(len(reskim_dic)))
        #break
    os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname))

make_dic()
subpu("SingleMuon_rereco_pick_1")
