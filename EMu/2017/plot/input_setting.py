isUpdate = True
isUpdate = False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QCD_JET_BKG_TYPE = "fake rate"
#QCD_JET_BKG_TYPE = "same sign"

Muon50_trig_fire = True
TkMu100_trig_fire = True
OldMu100_trig_fire = True
Ele115_trig_fire = False
Photon175_trig_fire = True

#Cross sections:
xsection_ttbar2l2u = 87.31
xsection_DYToLL = 5765.4
xsection_WW = 118.7
xsection_WZ = 47.13
xsection_ZZ = 16.523
xsection_ST = 19.47 + 19.47

#N raw event:
nrawevent_ttbar2l2u = 8615776
nrawevent_DYToLL = 102878790
nrawevent_WW = 7547722
nrawevent_WZ = 3928630
nrawevent_ZZ = 1949768
nrawevent_ST = 4913271+5334538
# start run
cut_name={
'_ALL':["e#mu",""],
'_ALL_2b':["e#mu","N(bjet) == 2"],
'_BB':["e#mu","Barrel(e),Barrel(mu)"],
'_BE':["e#mu","Barrel(e),Endcap(mu)"],
'_EB':["e#mu","Endcap(e),Barrel(mu)"],
'_EE':["e#mu","Endcap(e),Endcap(mu)"],
'_ETA_1':["e#mu","pT_{#mu} in [-2.5,-2.0]"],
'_ETA_2':["e#mu","pT_{#mu} in [2.0,2.5]"],
'_MET_50to100':["e#mu","MET in [50,100]"],
'_MET_100toInf':["e#mu","MET in [100,]"],
'_Nvtx_0to25':["e#mu","N_{vtx} < 25"],
'_Nvtx_25toInf':["e#mu","N_{vtx} > 25"],
}
# start run
cut_dic={
'_ALL':'True',
#'_BB':'(getattr(event,"ele_region") ==1 and getattr(event,"muon_region") == 1)',
#'_BE':'(getattr(event,"ele_region") ==1 and getattr(event,"muon_region") == 3)',
#'_EB':'(getattr(event,"ele_region") ==3 and getattr(event,"muon_region") == 1)',
#'_EE':'(getattr(event,"ele_region") ==3 and getattr(event,"muon_region") == 3)',
#'_ETA_1':'getattr(event,"muon_eta") <= -2.0',
#'_ETA_2':'getattr(event,"muon_eta") >= 2.0',
#'_MET_25to50':'getattr(event,"MET_T1Txy_Pt") > 25 and getattr(event,"MET_T1Txy_Pt") <= 50',
#'_MET_50to100':'getattr(event,"MET_T1Txy_Pt") > 50 and getattr(event,"MET_T1Txy_Pt") <= 100',
#'_MET_100toInf':'getattr(event,"MET_T1Txy_Pt") > 100',
#'_Nvtx_0to25':'getattr(event,"pv_n") <= 25',
#'_Nvtx_25toInf':'getattr(event,"pv_n") > 25',
}
