from definations import *
from optparse import OptionParser

parser=OptionParser()

parser.add_option("-n","--n_file",dest="n_file",default="-1",type="int")
parser.add_option("-p","--n_proc",dest="n_proc",default="1",type="int")
parser.add_option("-s","--n_file_start",dest="n_file_start",default="0",type="int")
parser.add_option("-o","--out_file",dest="out_file",default="output",type="str")

(options,args)=parser.parse_args()



def main_run(para_in):
	output_name = para_in[0]
	file_list = para_in[1]
	print_enable = para_in[2]
	if print_enable: print "%s started at : %s"%(output_name, time.asctime( time.localtime(time.time()) ))
	main_process = reskim(output_name)
	main_process.print_enable = print_enable
	main_process.root_file_list = file_list
	main_process.Loop()

main_file_list = []
my_walk_dir( '/pnfs/iihe/cms/store/user/xgao/2019CMSDAS/2018_ReReco_v2_EGamma_A/', main_file_list)
#my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_A/', main_file_list)
#my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_B/', main_file_list)
#my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_C/', main_file_list)
#my_walk_dir( '/pnfs/iihe/cms/store/user/amkalsi/2018_ReReco_v2/EGamma/crab_EGamma_D/', main_file_list)
#
if (options.n_file > 0):
	n_start = options.n_file_start
	n_end = options.n_file_start+options.n_file
else:
	n_start = options.n_file_start
	n_end = len(main_file_list)

output_dir = 'output/'
n_jobs = int(n_end - n_start)
if options.n_proc > n_jobs:
	options.n_proc = n_jobs
	print "Run only %d files, set 1 file per process"%(n_jobs)

para_list = []
n_tmp = n_start
for i_proc in range(options.n_proc):
	tmp_start = n_tmp
	n_tmp = n_tmp + n_jobs//options.n_proc + (1 if (i_proc < n_jobs%options.n_proc) else 0)
	tmp_print_enable = True if i_proc == 0 else False
	tmp_list = [ output_dir+"%s_%d_%d.root"%(options.out_file, tmp_start, n_tmp), main_file_list[tmp_start:n_tmp], tmp_print_enable ]
	print "  Creating process: %s"%(tmp_list[0])
	para_list.append(tmp_list)

print "\n%d processes are created, print process bar ONLY for the first one\n"%(options.n_proc)

pool = Pool(options.n_proc)
pool.map(main_run, para_list)
pool.close()
pool.join()


