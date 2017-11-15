import sys
import os
if len(sys.argv)<2:
    print "please give user name"
    sys.exit(0)
print "creating job info for %s"%(sys.argv[1])
os.system("qstat -f > ./qstat_tmp.txt")
f=open("./qstat_tmp.txt","r")
lines=f.readlines()

li=0
max_wide=0
for line in lines:
    li+=1
    if str(sys.argv[1]+"@") in line:
        jobs_ID  =lines[li-3]
        jobs_name=lines[li-2]
        if len(line) > max_wide:
            max_wide=len(line)
        if len(jobs_ID) > max_wide:
            max_wide=len(jobs_ID)
        if len(jobs_name) > max_wide:
            max_wide=len(jobs_name)

length_ID=30
length_name=max_wide
length_user=30
length_runtime=20
length_stat=5

ID_str  ="Job ID".center(length_ID)
name_str="Job name".center(length_name)
user_str="Job user".center(length_user)
runtime_str="Run time".center(length_runtime)
stat_str="Stat".center(length_stat)
print (ID_str),
print (name_str),
print (user_str),
print (runtime_str),
print (stat_str),
print ("\n"),

li=0

for line in lines:
    li+=1
    if str(sys.argv[1]+"@") in line:
        job_ID  =lines[li-3].split("Job Id:")[-1]
        job_name=lines[li-2].split("Job_Name =")[-1]
        job_user=line.split("Job_Owner =")[-1]
        job_runtime=lines[li].split("resources_used.cput =")[-1]
        job_stat   =lines[li+4].split("job_state =")[-1]
        w_ID=job_ID[:-1].center(length_ID)
        w_name=job_name[:-1].center(length_name)
        w_user=job_user[:-1].center(length_user)
        w_runtime=job_runtime[:-1].center(length_runtime)
        w_stat=job_stat[:-1].center(length_stat)
        print (w_ID),
        print (w_name),
        print (w_user),
        print (w_runtime),
        print (w_stat),
        print ("\n"),

os.system("rm ./qstat_tmp.txt")
print "done !"
