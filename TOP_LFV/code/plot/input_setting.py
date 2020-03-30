from dependencies import *

GLOBAL_YEAR = "2016"

isUpdate = True
isUpdate = False

use_sys = False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#QCD_JET_BKG_TYPE = "MC"
#QCD_JET_BKG_TYPE = "fake rate"
QCD_JET_BKG_TYPE = "same sign"

# start run
cut_name={

'_EMu_ll':["e#mu","ll" ],
'_EMu_llB1':["e#mu","llB1" ],
'_EMu_llBg1':["e#mu","llBg1" ],
'_EMu_llMetg30':["e#mu","llMetg30" ],
'_EMu_llMetg30Jetg2B1':["e#mu","llMetg30Jetg2B1" ],
'_EMu_llMetg30Jetg2Bg1':["e#mu","llMetg30Jetg2Bg1" ],
'_EMu_llMetl30':["e#mu","llMetl30" ],
'_EMu_llMetl30Jetg2B1':["e#mu","llMetl30Jetg2B1" ],
'_EMu_llMetl30Jetg2Bg1':["e#mu","llMetl30Jetg2Bg1" ],
'_EMu_llOffZ':["e#mu","llOffZ" ],
}

cut_dic = collections.OrderedDict()

cut_dic['_EMu_ll'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") '
cut_dic['_EMu_llB1'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"n_bjet") == 1)'
cut_dic['_EMu_llBg1'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"n_bjet") > 1)'
cut_dic['_EMu_llMetg30'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"MET_FinalCollection_Pt") > 30)'
cut_dic['_EMu_llMetg30Jetg2B1'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"MET_FinalCollection_Pt") > 30) and (getattr(event,"n_jet") > 3) and (getattr(event,"n_bjet") == 1)'
cut_dic['_EMu_llMetg30Jetg2Bg1'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"MET_FinalCollection_Pt") > 30) and (getattr(event,"n_jet") > 3) and (getattr(event,"n_bjet") > 1)'
cut_dic['_EMu_llMetl30'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"MET_FinalCollection_Pt") < 30)'
cut_dic['_EMu_llMetl30Jetg2B1'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"MET_FinalCollection_Pt") < 30) and (getattr(event,"n_jet") > 3) and (getattr(event,"n_bjet") == 1)'
cut_dic['_EMu_llMetl30Jetg2Bg1'] = 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and (getattr(event,"MET_FinalCollection_Pt") < 30) and (getattr(event,"n_jet") > 3) and (getattr(event,"n_bjet") > 1)'
#'_MEu_llOffZ' : 'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu_step2") and getattr(event,"pass_step1") and ',
