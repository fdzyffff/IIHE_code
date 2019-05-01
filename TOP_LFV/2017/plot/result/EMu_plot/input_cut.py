cut_name={
'_EMu_80_step1_T1':["e#mu","no Nvtx reweight"],
'_EE_80_step1_T1':["ee","no Nvtx reweight"],
'_MuMu_80_step1_T1':["#mu#mu","no Nvtx reweight"],
'_EE_80_step2_T1':["ee","no Nvtx reweight, event selection step 2"],
'_MuMu_80_step2_T1':["#mu#mu","no Nvtx reweight event selection step 2"],

'_EMu_80_step1_T2':["e#mu","single lepton triggers added, no Nvtx reweight"],
'_EE_80_step1_T2':["ee","single lepton triggers added, no Nvtx reweight"],
'_MuMu_80_step1_T2':["#mu#mu","single lepton triggers added, no Nvtx reweight"],
'_EE_80_step2_T2':["ee","single lepton triggers added, no Nvtx reweight, event selection step 2"],
'_MuMu_80_step2_T2':["#mu#mu","single lepton triggers added, no Nvtx reweight event selection step 2"],

#'_EMu_74':["e#mu","[74 regression-no scale smearing]"],
#'_EE_74':["ee","[74 regression-no scale smearing]"],
#'_MuMu_74':["#mu#mu","[74 regression-no scale smearing]"],
#'_EE_74_zrm':["ee","[74 regression-no scale smearing] M_{ll}[81,101] removed"],
#'_MuMu_74_zrm':["#mu#mu","[74 regression-no scale smearing] M_{ll}[81,101] removed"],
}
cut_dic={
'_EMu_80_step1_T1':'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event, "pass_trigger_EMu") and getattr(event,"pass_step1")',
#'_EE_80_step1_T1':'getattr(event,"pass_MET_filters") and getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1")',
#'_MuMu_80_step1_T1':'getattr(event,"pass_MET_filters") and getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1")',

#'_EE_80_step2_T1':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101) and getattr(event,"MET_Et")>=50',
#'_MuMu_80_step2_T1':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101) and getattr(event,"MET_Et") >=50',

#'_EMu_80_step1_T2':'getattr(event,"pass_MET_filters") and getattr(event,"isEMu") and getattr(event,"pass_trigger_EMu_step2") and getattr(event,"pass_step1")',
#'_EE_80_step1_T2':'getattr(event,"pass_MET_filters") and getattr(event,"isEE") and getattr(event,"pass_trigger_EE_step2") and getattr(event,"pass_step1")',
#'_MuMu_80_step1_T2':'getattr(event,"pass_MET_filters") and getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu_step2") and getattr(event,"pass_step1")',

#'_EE_80_step2_T2':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE_step2") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101) and getattr(event,"MET_Et")>=50',
#'_MuMu_80_step2_T2':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu_step2") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101) and getattr(event,"MET_Et") >=50',

#'_EMu_74':'getattr(event,"isEMu") and getattr(event,"pass_trigger_EMu") and getattr(event,"pass_step1")',
#'_EE_74':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1")',
#'_MuMu_74':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1")',
#'_EE_74_zrm':'getattr(event,"isEE") and getattr(event,"pass_trigger_EE") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101',
#'_MuMu_74_zrm':'getattr(event,"isMuMu") and getattr(event,"pass_trigger_MuMu") and getattr(event,"pass_step1") and (getattr(event,"M_ll") < 81 or getattr(event,"M_ll") > 101',
}

