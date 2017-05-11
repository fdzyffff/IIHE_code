import os
import sys
import ROOT
from input_card_fk import *
from optparse import OptionParser

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")

(options,args)=parser.parse_args()

MYDIR=os.getcwd()
Sample_plot_dic={}

cut = ""
def get_nEntries(root_file):
    f1 = ROOT.TFile(root_file,"read")
    t1 = f1.Get("tap")
    n = t1.GetEntries()
    f1.Close()
    return n

def get_plot_dic(check_dir = ""):
    print "%s making file list %s"%("#"*15,"#"*15)
    for sample in input_dic:
        if isCheck:
            Sample_plot_dic[sample] = [get_nEntries(input_dic[sample]["input_file"]),[my_walk_dir(os.path.join(check_dir,"split"),[],True)]]
            cut = check_dir.replace("/","")
        else:
            Sample_plot_dic[sample] = [get_nEntries(input_dic[sample]["input_file"]),[]]
        print "### %s : \t%d"%(sample,Sample_plot_dic[sample][0])

def my_walk_dir(my_dir,my_list,onlyFile=False):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            if 'failed'         in tmp_file_name:continue
            if not '.root'      in tmp_file_name:continue
            if onlyFile:
                my_list.append(tmp_file)
            else:
                my_list.append(tmp_file_name)
        else:
            my_walk_dir(tmp_file_name,my_list)
    return my_list

def make_sub(label,n_per_job):
    print "%s making jobs script, %d events/job %s"%("#"*15,n_per_job,"#"*15)
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
    sub_log_name = "pEMu_log_%s.log"%(label)
    sub_log = open(MYDIR+'/'+tmp_dir+'/'+sub_log_name,'w')

    n_total_job = 0
    for sample in Sample_plot_dic:
        if options.sample_name !="null":
            if options.sample_name != sample:continue
        n_job = 0
        for i in range(1,Sample_plot_dic[sample][0],n_per_job):
            n_l = i
            n_h = i + n_per_job - 1
            if (isCheck) and ("%s_hist_%s_%s_%s.root"%(cut,sample,n_l,n_h) in Sample_plot_dic[sample][1]):continue
            job_text = ""
            job_text+=("curr_dir=%s\n"%(MYDIR))
            job_text+=("cd %s\n"%(MYDIR))
            job_text+=("source env2.sh\n")
            job_text+=("python plot_fk1.py -s %s --n_range_l %s --n_range_h %s\n"%(sample, n_l, n_h))
            n_job += 1
            n_total_job += 1
            tmp_label = "%s_%s"%(sample,n_job)
            tmp_jobname="pEMu_%s.jobb"%(tmp_label)
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
#get_plot_dic("_EMu")
get_plot_dic()
make_sub("fk_split_plot_80",50000)
