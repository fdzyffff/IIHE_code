import os
import sys

MYDIR=os.getcwd()
file_root_dir_dic={
"../rB":[[0,276452],['0','51']],#[run min, run max][version_ele27, version_ele33]
#"../rE":[[276452, 278822],['0','1']],
#"../rF":[[276452, 278822],['0','1']],
#"../H2":[[278822, 999999],['0','51']],
}
reskim_dic={
#"0_D_v51_S_v2":["D_v51_S_v2/0000"],
#"0_D_v61_S_v5":["D_v61_S_v5/0000"],
}

def make_dic():
    ntotal = 0
    for file_dir in file_root_dir_dic:
        dir_name = file_dir.split("/")[-1]
        for s in os.listdir(file_dir):
            reskim_dic[s+"_"+dir_name]=[]
            reskim_dic[s+"_"+dir_name].append([])
            for tmp_file in os.listdir(os.path.join(file_dir,s)):
                reskim_dic[s+"_"+dir_name][0].append(os.path.join(dir_name,s,tmp_file))
                ntotal+=1
            version_ele27 = file_root_dir_dic[file_dir][1][0]
            version_ele33 = file_root_dir_dic[file_dir][1][1]
            reskim_dic[s+"_"+dir_name].append(version_ele33)
            reskim_dic[s+"_"+dir_name].append(version_ele27)
            reskim_dic[s+"_"+dir_name].append(file_root_dir_dic[file_dir][0][0])
            reskim_dic[s+"_"+dir_name].append(file_root_dir_dic[file_dir][0][1])
            print "%s: %s"%(s+"_"+dir_name,reskim_dic[s+"_"+dir_name])
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
        for reskim_file in reskim_dic[reskim][0]:
            try:
                reskim_file_name = reskim_file.split("/")[-1].replace(".root","").replace("outfile_","")
                root_dir = reskim_file
                trig_vd = reskim_dic[reskim][1]
                trig_vs = reskim_dic[reskim][2]
                run_start = reskim_dic[reskim][3]
                run_end = reskim_dic[reskim][4]
                output_name = "ntuples/batchdata_loop/data_2016_DoubleEG_%s_%s.root"%(reskim,reskim_file_name)
                tmp_label = reskim
                tmp_jobname="sub_%s_%s.jobb"%(reskim,reskim_file_name)
                tmp_job=open(MYDIR+'/'+tmp_dir+'/sub_job/'+tmp_jobname,'w')
                tmp_job.write("curr_dir=%s\n"%(MYDIR))
                tmp_job.write("cd %s\n"%(MYDIR))
                tmp_job.write("source env2.sh\n")
                tmp_job.write("cd ../\n")
                tmp_job.write("python reskim_loop_all.py -r %s -o %s -d %s -s %s -e %s\n"%(root_dir, output_name, trig_vd, run_start, run_end))
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
            #print "%d / %d jobs created (%0.2f%%)"%(i, len(reskim_dic), float(i)*100.0/float(len(reskim_dic)))
    print "%d / %d jobs created (%0.2f%%)"%(i, len(reskim_dic), float(i)*100.0/float(len(reskim_dic)))
            #break
    os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname))

make_dic()
subpu("DoubleEG_rereco_loop")
