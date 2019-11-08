from hist_make import *
from input_sys import *
from optparse import OptionParser

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")

(options,args)=parser.parse_args()

MYDIR=os.getcwd()
Sys_sample_plot_dic = {}

cut = ""
def get_nEntries(root_file):
    f1 = ROOT.TFile(root_file,"read")
    t1 = f1.Get("tap")
    n = t1.GetEntries()
    f1.Close()
    return n

def get_plot_dic(input_class, sys_type, check_dir = ""):
    print "%s |%s| making file list %s"%("#"*15,sys_type,"#"*15)

    Sample_plot_dic={}
    for sample in input_class.input_dic:
        #print input_class.input_dic[sample]["input_file"]
        Sample_plot_dic[sample] = [get_nEntries(input_class.input_dic[sample]["input_file"]),[]]
        #print "### (%s) %s : \t%d"%(sample,input_class.input_dic[sample]["input_file"],Sample_plot_dic[sample][0])
    Sys_sample_plot_dic[input_class.sys_type] = Sample_plot_dic

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

def write_to_job(current_job_name, job_text):
    job_file = open(current_job_name,"w")

    const_str = ""
    const_str+=("curr_dir=%s\n"%(MYDIR))
    const_str+=("cd %s\n"%(MYDIR))
    const_str+=("source env2.sh\n\n")
    
    job_file.write(const_str + job_text)
    job_file.close()
    os.system("chmod +x %s"%(current_job_name))

def make_sub(label,n_per_job):
    print "%s making jobs script, %d events/job %s"%("#"*15,n_per_job,"#"*15)
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
    n_job = 1
    current_n = 0
    current_job_name = MYDIR+'/'+tmp_dir+'/'+"sub_job/Zp_LFV_%s.jobb"%(n_job)
    job_text = ""
    for sys_type in Sys_sample_plot_dic:
        Sample_plot_dic = Sys_sample_plot_dic[sys_type]
        for sample in Sample_plot_dic:
            local_n = 0
            if options.sample_name !="null":
                if options.sample_name != sample:continue
            while(local_n < Sample_plot_dic[sample][0]):
                #Sample_plot_dic[sample][0]
                if ((Sample_plot_dic[sample][0] - local_n) >= (n_per_job - current_n) ):
                    n_l = local_n + 1
                    n_h = local_n + (n_per_job - current_n)
                    local_n += (n_per_job - current_n)
                    job_text+=("python plot1.py -s %s -u %s --n_range_l %s --n_range_h %s\n"%(sample, sys_type, n_l, n_h))
                    write_to_job(current_job_name, job_text)
                    BigSub_job.write("qsub -q localgrid %s\n"%(current_job_name))
                    n_total_job += 1
                    current_n = 0
                    n_job += 1
                    current_job_name = MYDIR+'/'+tmp_dir+'/'+"sub_job/Zp_LFV_%s.jobb"%(n_job)
                    job_text = ""
                else:
                    n_l = local_n + 1
                    n_h = Sample_plot_dic[sample][0]
                    current_n += (Sample_plot_dic[sample][0] - local_n)
                    local_n += (Sample_plot_dic[sample][0] - local_n)
                    job_text+=("python plot1.py -s %s -u %s --n_range_l %s --n_range_h %s\n"%(sample, sys_type, n_l, n_h))
    if (job_text != ""):
        write_to_job(os.path.join("%s/sub_job"%(tmp_dir),current_job_name), job_text)
        BigSub_job.write("qsub -q localgrid %s\n"%(current_job_name))
        n_total_job += 1
    os.system("chmod +x %s"%(MYDIR+'/'+tmp_dir+'/'+tmp_bigsubname))
    print "%d jobs created"%(n_total_job)

for sys_type in sys_dic:
    if (not sys_dic[sys_type][1]): continue
    input_class = hist_make(GLOBAL_YEAR)
    input_class.sys_type = sys_type
    input_class.set_value_dic(pre_value_dic)
    input_class.set_plot_dic(pre_plot_dic, "23")
    input_class.set_input_dic(pre_input_dic, "23")
    get_plot_dic(input_class, input_class.sys_type)
make_sub("split_plot_80",500000)
