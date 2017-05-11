job_input_name ="/user/xgao/CMSSW_7_6_3/src/2016B/Dielectron/Dielectron_DY_rereco/withCorr/script/sub_DoubleEG_rereco_loop/BigSubmit_DoubleEG_rereco_loop.jobb"
job_output_name = "BigSubmit_DoubleEG_rereco_loop_failed.jobb"

failed_job_input_name = "/user/xgao/tmp.txt"

def getfailedlist(failed_job_input_name):
    nlines = 1
    tmp_list = []
    for line in open(failed_job_input_name,"r"):
        if nlines >= 62: break
        jobnr = line[13:].split(".root")[0]
        tmp_list.append(["B",str(jobnr)])
        print jobnr
        nlines += 1
    return tmp_list

job_failed_list = getfailedlist(failed_job_input_name)
job_output = open(job_output_name,"w")

for line in open(job_input_name,"r"):
    for l in job_failed_list:
        if "rB_%s.jobb"%(l[1]) in line:
            job_output.write(line)
            break
