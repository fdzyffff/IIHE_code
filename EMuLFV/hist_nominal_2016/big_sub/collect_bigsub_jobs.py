from inputcard_collect_bigsub_jobs import *

def main(label = ""):
	if options.global_dir == "null":
		print "No global_dir specified, will set to current dir automatically"
		options.global_dir == "./"
	job_file_list = []
	for job_dir in job_dir_list:
		tmp_dir = os.path.join(options.global_dir, job_dir)
		for file_name in os.listdir(tmp_dir):
			tmp_file_name = os.path.join(tmp_dir, file_name)
			if os.path.isfile(tmp_file_name) and ("BigSub" in file_name) and file_name[-5:] == ".jobb":
				f_tmp_in=open(tmp_file_name)
				nline = 0
				for line in f_tmp_in:
					nline += 1
				f_tmp_in.close()
				print "%s  :   (%4d )   %s"%(time.ctime(os.path.getmtime(tmp_file_name)), nline, tmp_file_name)
				job_file_list.append(tmp_file_name)

	if not ("BigSub" in os.listdir("./")):
		try:
			os.mkdir("BigSub")
		except:
			return "Error in creating BigSub/"
	f_out = open("BigSub/BigSub_%s.jobb"%(label), "w")
	for job_file in job_file_list:
		f_tmp_in = open (job_file)
		for line in f_tmp_in:
			line = line.replace("\n","")
			f_out.write("%s\n"%(line))
		f_tmp_in.close()
	f_out.close()

main("2016_all")