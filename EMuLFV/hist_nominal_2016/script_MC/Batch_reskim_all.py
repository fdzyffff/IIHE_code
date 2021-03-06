import os
import sys

from optparse import OptionParser

parser=OptionParser()
parser.add_option("-e", "--fke", action='store_true', default=False)
parser.add_option("-m", "--fkm", action='store_true', default=False)
(options,args)=parser.parse_args()

MYDIR=os.getcwd()

file_root_dir_dic={
	    #[isData,isZToTT,isTTbin,isWWbin,
"../MC/DYToLL"			:[" isData=False useSYS=True usePDF=False",[0]],
"../MC/ST_antitop"		:[" isData=False useSYS=True usePDF=False",[0]],
"../MC/ST_top"			:[" isData=False useSYS=True usePDF=False",[0]],
"../MC/ttbar2l2u_Mall"		:[" isData=False useSYS=True usePDF=False isTTbar=True ttbarreweight=True",[0]],
"../MC/ttbar2l2u_M500to800"	:[" isData=False useSYS=True usePDF=False ttbarreweight=True",[0]],
"../MC/ttbar2l2u_M800to1200"	:[" isData=False useSYS=True usePDF=False ttbarreweight=True",[0]],
"../MC/ttbar2l2u_M1200to1800"	:[" isData=False useSYS=True usePDF=False ttbarreweight=True",[0]],
"../MC/ttbar2l2u_M1800toInf"	:[" isData=False useSYS=True usePDF=False ttbarreweight=True",[0]],
"../MC/WW2l2u"			:[" isData=False useSYS=True usePDF=False isWW=True",[0]],
"../MC/WW_M200to600"		:[" isData=False useSYS=True usePDF=False",[0]],
"../MC/WW_M600to1200"		:[" isData=False useSYS=True usePDF=False",[0]],
"../MC/WW_M1200to2500"		:[" isData=False useSYS=True usePDF=False",[0]],
"../MC/WW_M2500toInf"		:[" isData=False useSYS=True usePDF=False",[0]],
#"../MC/WZ"			:[" isData=False useSYS=True usePDF=False",[0]],
#"../MC/ZZ"			:[" isData=False useSYS=True usePDF=False",[0]],

"../MC/ZZTo2L2Nu"               :[" isData=False useSYS=True usePDF=False", [0]],
"../MC/WZTo2L2Q"                :[" isData=False useSYS=True usePDF=False", [0]],
"../MC/ZZTo4L"                 :[" isData=False useSYS=True usePDF=False", [0]],
"../MC/WZTo3LNu"               :[" isData=False useSYS=True usePDF=False", [0]],
"../MC/ZZTo2L2Q"               :[" isData=False useSYS=True usePDF=False", [0]],

"../MC/QBHtoEMu_M200"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M400"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M600"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M800"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M1000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M1200"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M1400"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M1600"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M1800"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M2000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M2500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M3000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M3500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M4000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M4500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M5000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M5500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M6000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M7000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M8000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M9000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/QBHtoEMu_M10000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M200"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M300"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M400"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M600"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M700"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M800"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M900"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M1000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M1200"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M1400"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M1600"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M1800"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M2000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M2500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M3000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M3500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M4000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M4500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M5000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M5500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M6000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/RPVresonantToEMu_M6500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1100"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1200"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1300"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1400"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1600"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1700"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1800"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M1900"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M2000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M2200"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M2400"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M2600"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M2800"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M3000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M3500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M4000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M4500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M5000"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M500"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M600"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M700"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M800"		:[" isData=False useSYS=True usePDF=True",[0]],
"../MC/ZPrimeToEMu_M900"		:[" isData=False useSYS=True usePDF=True",[0]],

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

def make_sub(year, label,n_file_per_job):
    print "%s making jobs script, %d root files/job %s"%("#"*15,n_file_per_job,"#"*15)
    try:
        tmp_dir = ""
        if isCheck:
            tmp_dir='check_sub_%s'%(label)
        else:
            if options.fke:
                tmp_dir='sub_fke_%s_%s'%(year, label)
            elif options.fkm:
                tmp_dir='sub_fkm_%s_%s'%(year, label)
            else:
                tmp_dir='sub_%s_%s'%(year, label)
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

    out_dir = "batchdata_%s"%(label)
    if options.fke:
        out_dir = "batchdata_%s_fke"%(label)
    if options.fkm:
        out_dir = "batchdata_%s_fkm"%(label)
    try :
        os.system("mkdir ../ntuples")
        os.system("mkdir ../ntuples/%s"%(out_dir))
    except:
        pass
    n_total_job = 0
    for reskim in reskim_dic:
        para_str = reskim_dic[reskim][0]
        if options.fke:
            para_str = para_str+" isFakee=True"
        if options.fkm:
            para_str = para_str+" isFakemu=True"
        n_job = 0
        sub_n_total_job = 0
        n_start = True
        job_text = ""
        i = 0
        for root_file in reskim_dic[reskim][1]:
            sample_name = root_file.split("/")[-3] 
            subdir_name = root_file.split("/")[-2] 
            file_name = root_file.split("/")[-1] 
            output_name = "ntuples/%s/%s_%s_%s_%s_%s"%(out_dir, year, label, sample_name, subdir_name, file_name)
            tmp_label = reskim
            if n_start:
                n_start=False
                job_text = ""
                job_text+=("curr_dir=%s\n"%(MYDIR))
                job_text+=("cd %s\n"%(MYDIR))
                job_text+=("eval `scramv1 runtime -sh`\n")
                job_text+=("cd ../\n")
            if (not isCheck) or (not output_name in reskim_dic[reskim][3]):
                #if isCheck:print output_name
                job_text+=("cmsRun EMuLFVAnalysis_test.py year=%s InputFile=%s outFilename=%s %s\n"%(year, root_file, output_name, para_str))
                n_job+=1
            i+=1
            if (n_job%n_file_per_job==0 and n_job>0) or (i >= len(reskim_dic[reskim][1])):
                n_job=0
                n_start=True
                n_total_job += 1
                sub_n_total_job += 1
                tmp_label = "%s_%s"%(reskim, sub_n_total_job)
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

if options.fke:
    print ("is fake electron jobs!")
if options.fkm:
    print ("is fake muon jobs!")

make_dic()
#make_dic("../ntuples/batchmc")
make_sub("2016", "MC",500)
