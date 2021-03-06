from dependencies import *
from input_setting import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nevent_DYToLL_10to50 = 78994955
nevent_DYToLL_50 = 84597528
nevent_TTGJets = 10703723
nevent_TTTo2L2Nu = 8926992
nevent_TTWJetsToLNu = 5394782
nevent_TTWJetsToQQ = 883120
nevent_TTZToLLNuNu_10 = 3745298
nevent_TTZToQQ = 4958390
nevent_WGToLNuG = 6282853
nevent_WJetsToLNu = 33043732
nevent_WWTo2L2Nu = 1992522
nevent_WZTo2L2Q = 16620982
nevent_WZTo3LNu = 6887413
nevent_ZZTo2L2Nu = 8733658
nevent_ZZTo4L = 6893887
nevent_tw = 4917240
nevent_tw_anti = 5592819
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
xsection_DYToLL_10to50 = 18610
xsection_DYToLL_50 = 5765.4
xsection_TTGJets = 3.697
xsection_TTTo2L2Nu = 87.31
xsection_TTWJetsToLNu = 0.2043
xsection_TTWJetsToQQ = 0.4062
xsection_TTZToLLNuNu_10 = 0.2529
xsection_TTZToQQ = 0.5297
xsection_WGToLNuG = 489
xsection_WJetsToLNu = 61526.7
xsection_WWTo2L2Nu = 12.178
xsection_WZTo2L2Q = 5.595
xsection_WZTo3LNu = 4.42965
xsection_ZZTo2L2Nu = 0.564
xsection_ZZTo4L = 1.212
xsection_tw = 19.47
xsection_tw_anti = 19.47
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pre_plot_dic=collections.OrderedDict()
pre_plot_dic["compare_1"] = collections.OrderedDict()
pre_plot_dic["compare_2"] = collections.OrderedDict()
pre_plot_dic["compare_3"] = collections.OrderedDict()

pre_plot_dic_ss=collections.OrderedDict()
pre_plot_dic_ss["compare_1"] = collections.OrderedDict()
pre_plot_dic_ss["compare_2"] = collections.OrderedDict()

pre_value_dic=collections.OrderedDict()
pre_input_dic=collections.OrderedDict()

tmp_sample_t = sample_t("data")
tmp_sample_t.input_file = "data_2017_EMu.root"
tmp_sample_t.isData = True
tmp_sample_t.useToNorm = True
tmp_sample_t.lumi = 41530
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

if QCD_JET_BKG_TYPE == "same sign":

	tmp_sample_t = sample_t("ss_data")
	tmp_sample_t.input_file = "data_2017_EMu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.isData = True
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t