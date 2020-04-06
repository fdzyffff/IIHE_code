from dependencies import *
from input_setting import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nevent_DYToLL_10to50 = 39360792
nevent_DYToLL_50 = 131615987
nevent_TTGJets = 1842387
nevent_TTTo2L2Nu = 63791484
nevent_TTWJetsToLNu = 2686095
nevent_TTWJetsToQQ = 458226
nevent_TTZToLLNuNu_10 = 6274046
nevent_TTZToQQ = 4576760
nevent_WGToLNuG = 6108058
nevent_WJetsToLNu = 70966439
nevent_WWTo2L2Nu = 7729266
nevent_WZTo2L2Q = 17048434
nevent_WZTo3LNu = 13789395
nevent_ZZTo2L2Nu = 47984296
nevent_ZZTo4L = 104627766
nevent_tw = 7602101
nevent_tw_anti = 5796514
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
tmp_sample_t.input_file = "data_2018_EMu.root"
tmp_sample_t.isData = True
tmp_sample_t.useToNorm = True
tmp_sample_t.lumi = 59970
pre_input_dic[tmp_sample_t.label] = tmp_sample_t

if QCD_JET_BKG_TYPE == "same sign":

	tmp_sample_t = sample_t("ss_data")
	tmp_sample_t.input_file = "data_2018_EMu.root"
	tmp_sample_t.isSS = True
	tmp_sample_t.isData = True
	pre_input_dic[tmp_sample_t.label] = tmp_sample_t