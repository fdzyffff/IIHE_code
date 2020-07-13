import collections

common_sys = collections.OrderedDict()
pdf_sys = collections.OrderedDict()

#common_sys["nominal"]=[[use_data, use_bkg, use_sig], ref_sys_type, name]
common_sys["nominal"]=[[True, True, True], "nominal", "nominal"]
common_sys["muptscalu"]=[[False, True, True], "mu_pt_scale_up", "MuPtscal_up"]
common_sys["muptresu"]=[[False, True, True], "mu_pt_res_up", "MuPtres_up"]
common_sys["eletscalu"]=[[False, True, True], "ele_et_scale_up", "ElEtscal_up"]
common_sys["eletscald"]=[[False, True, True], "ele_et_scale_down", "ElEtscal_down"]
common_sys["top1_u"]=[[False, True, True], "top_w_up", "top_pt_up"]
common_sys["top1_d"]=[[False, True, True], "top_w_down", "top_pt_down"]
#common_sys["top_pdf_u"]=[[False, True, True], "top_pdf_up", "top_pdf_up"]
#common_sys["top_pdf_d"]=[[False, True, True], "top_pdf_down", "top_pdf_down"]
#common_sys["top_qs_u"]=[[False, True, True], "top_qs_up", "top_qs_up"]
#common_sys["top_qs_d"]=[[False, True, True], "top_qs_down", "top_qs_down"]
common_sys["pu_u"]=[[False, True, True], "pu_w_up", "pileup_up"]
common_sys["pu_d"]=[[False, True, True], "pu_w_down", "pileup_down"]

common_sys["mu_id_sfu"]=[[False, True, True],"mu_id_up", "MuIDSF_up"]
common_sys["mu_iso_sfu"]=[[False, True, True],"mu_iso_up", "MuISOSF_up"]
common_sys["mu_trig_sfu"]=[[False, True, True],"mu_trig_up", "MuTrig_up"]
common_sys["mu_id_sfd"]=[[False, True, True],"mu_id_down", "MuIDSF_down"]
common_sys["mu_iso_sfd"]=[[False, True, True],"mu_iso_down", "MuISOSF_down"]
common_sys["mu_trig_sfd"]=[[False, True, True],"mu_trig_down", "MuTrig_down"]
common_sys["el_id_sfu"]=[[False, True, True],"ele_id_up", "ElIDSF_up"]
common_sys["el_id_sfd"]=[[False, True, True],"ele_id_down", "ElIDSF_down"]
#common_sys["el_id_sfu"]=[[False, True, True],"ele_reco_up", "ElIDSF_up"]
#common_sys["el_id_sfd"]=[[False, True, True],"ele_reco_down", "ElIDSF_down"]

common_sys["qcd_u"]=[[False, True, True], "nominal", "QCD_up"]
common_sys["qcd_d"]=[[False, True, True], "nominal", "QCD_down"]
common_sys["xs_ttbar_u"]=[[False, True, True], "nominal", "XsTTbar_up"]
common_sys["xs_ttbar_d"]=[[False, True, True], "nominal", "XsTTbar_down"]
common_sys["xs_ww_u"]=[[False, True, True], "nominal", "XsWW_up"]
common_sys["xs_ww_d"]=[[False, True, True], "nominal", "XsWW_down"]
common_sys["xs_st_u"]=[[False, True, True], "nominal", "XsST_up"]
common_sys["xs_st_d"]=[[False, True, True], "nominal", "XsST_down"]
common_sys["xs_dy_u"]=[[False, True, True], "nominal", "XsDY_up"]
common_sys["xs_dy_d"]=[[False, True, True], "nominal", "XsDY_down"]
common_sys["xs_wz_u"]=[[False, True, True], "nominal", "XsWZ_up"]
common_sys["xs_wz_d"]=[[False, True, True], "nominal", "XsWZ_down"]
common_sys["xs_zz_u"]=[[False, True, True], "nominal", "XsZZ_up"]
common_sys["xs_zz_d"]=[[False, True, True], "nominal", "XsZZ_down"]
common_sys["lumi_u"]=[[False, True, True], "nominal", "Lumi_up"]
common_sys["lumi_d"]=[[False, True, True], "nominal", "Lumi_down"]

for i_pdf in range(101):
	pdf_sys["pdf%s"%(i_pdf)] = [[False, False, True],"nominal","pdf%s"%(i_pdf)]

sys_group_dic = collections.OrderedDict()
sys_group_dic["group_xs"] = {
	'list': ["xs_ttbar_u","xs_ttbar_d","xs_tw_u","xs_tw_d","xs_dy_u","xs_dy_d","xs_other_u","xs_other_d","lumi_u","lumi_d"],
	'color': 30,
	'legend_title' : 'Xsection & lumi'}

sys_group_dic["group_ele_reco"] = {
	'list': ["el_reco_sfu","el_reco_sfd"],
	'color': 1,
	'legend_title' : 'Ele Reco'}
sys_group_dic["group_ele_id"] = {
	'list': ["el_id_sfu","el_id_sfd"],
	'color': 2,
	'legend_title' : 'Ele ID'}

sys_group_dic["group_mu_id"] = {
	'list': ["mu_id_sfu","mu_id_sfd"],
	'color': 3,
	'legend_title' : 'Muon ID'}
sys_group_dic["group_mu_iso"] = {
	'list': ["mu_iso_sfu","mu_iso_sfd"],
	'color': 4,
	'legend_title' : 'Muon Iso'}

sys_group_dic["group_lep_trig"] = {
	'list': ["lep_trig_sfu","lep_trig_sfd"],
	'color': 5,
	'legend_title' : 'Lep Trigger'}

sys_group_dic["group_btag"] = {
	'list': ["btag_u","btag_d"],
	'color': 6,
	'legend_title' : 'btag'}

sys_group_dic["group_jet_pt"] = {
	'list': ["JetPtResUp","JetPtResDown","JetPtEnUp","JetPtEnDown"],
	'color': 7,
	'legend_title' : 'Jet pt'}

sys_group_dic["group_pu"] = {
	'list': ["pu_u","pu_d"],
	'color': 8,
	'legend_title' : 'Pile-up'}

#sys_group_dic["group_top"] = {
#	'list': ["top1_u","top1_d"],
#	'color': 8,
#	'legend_title' : 'top shape'}

sys_group_dic["group_qcd"] = {
	'list': ["qcd_u","qcd_d"],
	'color': 9,
	'legend_title' : 'QCD+jets'}

sys_group_dic["group_stat"] = {
	'list': [],
	'color': 19,
	'legend_title' : 'Stat.'}
sys_group_dic["group_total"] = {
	'list': [],
	'color': 29,
	'legend_title' : 'Total'}