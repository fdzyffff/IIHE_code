from hist_make import *
from input_sys import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-r","--input_dir",dest="input_dir",default="null",type="str")

(options,args)=parser.parse_args()

def merge_plot(input_class,input_root_list,sample):
    for root_file in input_root_list:
        tmp_root_file = ROOT.TFile(root_file)
        for path in input_class.value_dic:
            tmp_h1 = tmp_root_file.Get("%s_out"%(input_class.input_dic[sample].hist[path].GetName()))
            #tmp_h1.Sumw2()
            input_class.input_dic[sample].hist[path].Add(input_class.input_dic[sample].hist[path],tmp_h1,1,1)
        tmp_root_file.Close()

def main():
    global GLOBAL_YEAR
    for cut in cut_dic:
        if options.input_dir != "null":
            if cut != options.input_dir:
                continue
        for sys_type in sys_dic:
            if not (GLOBAL_USE_SYS or (sys_type == "nominal") ) : continue
            if (not sys_dic[sys_type][1]): continue
            input_class = hist_make(GLOBAL_YEAR)
            input_class.sys_type = sys_type
            input_class.set_value_dic(pre_value_dic)
            input_class.set_plot_dic(pre_plot_dic, "23")
            input_class.set_input_dic(pre_input_dic, "23")
            input_class.cut_str = cut_dic[cut]
            input_class.hist_input_dir = os.path.join(cut,sys_type)
            input_class.hist_output_dir = os.path.join(cut,sys_type)
            input_class.Init_hist_sample(input_class.input_dic, input_class.value_dic)

            print "merging %s"%(sys_type)
            for sample in input_class.input_dic:
                input_root_list = []
                input_dir = os.path.join(input_class.hist_output_dir, "split", sample)
                for root_file in os.listdir(input_dir):
                    if ".root" in root_file:
                        input_root_list.append("%s/%s"%(input_dir, root_file))
                merge_plot(input_class,input_root_list,sample)
            input_class.Store_hist(input_class.input_dic, input_class.value_dic, input_class.hist_output_dir)
            input_class.close()

main()
