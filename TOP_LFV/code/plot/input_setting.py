from dependencies import *

GLOBAL_YEAR = "2016"

isUpdate = True
isUpdate = False

GLOBAL_USE_SYS = False
GLOBAL_USE_MVA = True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#QCD_JET_BKG_TYPE = "MC"
#QCD_JET_BKG_TYPE = "fake rate"
QCD_JET_BKG_TYPE = "same sign"

global_cut_dic = collections.OrderedDict()

global_cut_dic['_EMu_ll'] = ["e#mu","ll"]
#cut_dic['_EMu_llB1'] = ["e#mu","llB1"]
#cut_dic['_EMu_llBg1'] = ["e#mu","llBg1"]
#cut_dic['_EMu_llMetg30'] = ["e#mu","llMetg30"]
#cut_dic['_EMu_llMetg30Jetg2B1'] = ["e#mu","llMetg30Jetg2B1"]
#cut_dic['_EMu_llMetg30Jetg2Bg1'] = ["e#mu","llMetg30Jetg2Bg1"]
#cut_dic['_EMu_llMetl30'] = ["e#mu","llMetl30"]
#cut_dic['_EMu_llMetl30Jetg2B1'] = ["e#mu","llMetl30Jetg2B1"]
#cut_dic['_EMu_llMetl30Jetg2Bg1'] = ["e#mu","llMetl30Jetg2Bg1"]
#'_MEu_llOffZ' = ["e#mu","llOffZ" ]

def global_cut_func(cut_str, t1):
	ret = False
	if cut_str == "_EMu_ll":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1
	if cut_str == "_EMu_llB1":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.n_bjet == 1)
	if cut_str == "_EMu_llBg1":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.n_bjet > 1)
	if cut_str == "_EMu_llMetg30":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.MET_FinalCollection_Pt > 30)
	if cut_str == "_EMu_llMetg30Jetg2B1":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.MET_FinalCollection_Pt > 30) and (t1.n_jet > 3) and (t1.n_bjet == 1)
	if cut_str == "_EMu_llMetg30Jetg2Bg1":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.MET_FinalCollection_Pt > 30) and (t1.n_jet > 3) and (t1.n_bjet > 1)
	if cut_str == "_EMu_llMetl30":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.MET_FinalCollection_Pt < 30)
	if cut_str == "_EMu_llMetl30Jetg2B1":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.MET_FinalCollection_Pt < 30) and (t1.n_jet > 3) and (t1.n_bjet == 1)
	if cut_str == "_EMu_llMetl30Jetg2Bg1":
		ret = t1.pass_MET_filters and t1.isEMu and t1.pass_trigger_EMu_step2 and t1.pass_step1 and (t1.MET_FinalCollection_Pt < 30) and (t1.n_jet > 3) and (t1.n_bjet > 1)
	if cut_str == "_MEu_llOffZ":
		ret = True
	return ret