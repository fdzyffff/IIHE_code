from plot import *

from optparse import OptionParser

parser=OptionParser()

parser.add_option("-s","--sample_name",dest="sample_name",default="null",type="str")
parser.add_option("-u","--sys_type",dest="sys_type",default="nominal",type="str")
parser.add_option("--n_range_l",dest="n_range_l",default=-1,type="int")
parser.add_option("--n_range_h",dest="n_range_h",default=-1,type="int")
parser.add_option("-l","--log_level",dest="log_level",default=0,type="int")
parser.add_option("-p", "--print_table", action='store_true', default=False)

(options,args)=parser.parse_args()

def make_year_plot(year, input_dir):
	tmp_plot_dic = collections.OrderedDict()
	for sys_type in common_sys:
		print ("(%s)sys_type : %s"%(year, sys_type))
		if year == "2016":
			my_para = para_2016()
		tmp_plot = plot_t(sys_type, my_para, "year")
		tmp_plot.use_data = common_sys[sys_type][0][0]
		tmp_plot.use_bkg = common_sys[sys_type][0][1]
		tmp_plot.use_sig = common_sys[sys_type][0][2]
		tmp_plot.init_sample(input_dir, pre_hist_name, common_sys[sys_type][1])
		tmp_plot_dic[sys_type] = tmp_plot

	for sys_type in pdf_sys:
		my_para = para_2016()
		print ("(%s)sys_type : %s"%(year, sys_type))
		if year == "2016":
			my_para = para_2016()
		tmp_plot = plot_t(sys_type, my_para, "year")
		tmp_plot.use_data = pdf_sys[sys_type][0][0]
		tmp_plot.use_bkg = pdf_sys[sys_type][0][1]
		tmp_plot.use_sig = pdf_sys[sys_type][0][2]
		tmp_plot.init_sample(input_dir, pre_hist_name, pdf_sys[sys_type][1])
		tmp_plot_dic[sys_type] = tmp_plot

	print ("\nInitializing (%s): "%(year))
	showprocess = ShowProcess(len(tmp_plot_dic))
	i_process = 1
	for plot_sys in tmp_plot_dic:
		tmp_plot_dic[plot_sys].prepare_hist()
		showprocess.show_process(i_process)
		i_process+=1
	showprocess.close("finish\n")
	return tmp_plot_dic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
	plot_2016 = make_year_plot("2016", "Data_MC")

	print ("\nCoping (2016): ")
	showprocess = ShowProcess(len(plot_2016))
	i_process = 1
	final_plot = collections.OrderedDict()
	for plot_sys in plot_2016:
		final_plot[plot_sys] = final_plot_t(plot_2016[plot_sys], "2016year")
		showprocess.show_process(i_process)
		i_process+=1
	showprocess.close("finish\n")
#	for plot_sys in plot_2017:
#		final_plot.add_plot(plot_2017[plot_sys])

	hist_bkg_sys = make_hist_sys_bkg(final_plot)

	for i_hist in pre_hist_name:
		hist_data = None
		hist_bkg = None
		hist_sig = None
		hist_bkg_dic = collections.OrderedDict()
		for plot_name in final_plot["nominal"].hist_data:
			if hist_data == None:
				hist_data = final_plot["nominal"].hist_data[plot_name][i_hist].Clone("final_data")
			else:
				hist_data.Add(hist_data, final_plot["nominal"].hist_data[plot_name][i_hist], 1, 1)
	
		for plot_name in final_plot["nominal"].hist_bkg:
			if hist_bkg == None:
				hist_bkg = final_plot["nominal"].hist_bkg[plot_name][i_hist].Clone("final_bkg")
			else:
				hist_bkg.Add(hist_bkg, final_plot["nominal"].hist_bkg[plot_name][i_hist], 1, 1)

#			if plot_name in hist_bkg_dic:
#				hist_bkg_dic[plot_name].Add(hist_bkg_dic[plot_name], final_plot["nominal"].hist_bkg[plot_name][i_hist], 1, 1)
#			else:
			hist_bkg_dic[plot_name] = final_plot["nominal"].hist_bkg[plot_name][i_hist].Clone("final_%s_%s"%(plot_name,i_hist))

		tmp_setting = plot_setting(i_hist, hist_data, hist_bkg, hist_bkg_sys[i_hist], hist_bkg_dic)
		tmp_setting.lumi = final_plot["nominal"].lumi
		tmp_setting.label = final_plot["nominal"].label
		tmp_setting.make_common_setting(i_hist)

		draw_final_plot(i_hist, tmp_setting)



main()