from input_card import *
from SFs import *

class hist_make():
	def __init__(self, label = "none"):
		self.global_year_label = label
		self.ana_2016 = False
		self.ana_2017 = False
		self.ana_2018 = False
		if label == "2016":
			self.ana_2016 = True
			self.init_2016()
		elif label == "2017":
			self.ana_2017 = True
			self.init_2017()
		elif label == "2018":
			self.ana_2018 = True
			self.init_2018()
		else:
			return

		self.log_level = 0
		self.error_range_dic = {"0-500":[1,500,0], "500-1000":[2,500,0], "1000-1500":[3,500,0], "1500-2000":[4,500,0]}
	
		self.plot_list = ["_tW","_ttbar","_ZG_jets","_others","qcd_jet"]
		self.plot_list_sys = ["_tW","_ttbar","_ZG_jets","_others"]
		self.plot_list_common_sys = ["qcd_jet"]
		self.isSplit_mode = False
		self.input_dic = {}
		self.cut = ""
		self.sys_type = ""
		self.text_list = []
		self.n_range_l = -1
		self.n_range_h = -1
		self.target_sample = "null"
		self.hist_input_dir = ""
		self.hist_output_dir = ""
		self.cut_str = "none"
		self.total_lumi = 0.0
		if self.ana_2016:
			self.lumi_sys = 0.024
		if self.ana_2017:
			self.lumi_sys = 0.024
		if self.ana_2018:
			self.lumi_sys = 0.024
	
		self.input_dic = {}
		self.value_dic = {}
		self.plot_dic = {}
		self.sys_sum_dic = {}
		self.store_hist_plot_list = []
		self.SFs = SFs()

		if (GLOBAL_USE_MVA):
			self.MVA_reader = my_TMVA_reader("MLP","TMVA/MLP/weights/TMVA_MLP_1b_MLP.weights.xml")

	def close(self):
		if (GLOBAL_USE_MVA):
			self.MVA_reader.close()

	def init_2016(self):
		#self.MuonTriggerSF_dic		= self.Load_json("SF_json/SF_json_2016/Muon/Trigger/Muon_Trigger_2018_SF.json")
		return

	def init_2017(self):

		return

	def init_2018(self):

		return

	def constrain_float(self, float_in, float_l, float_u):
		if float_l >= float_u:
			print "error, low edge (%s) > high edge (%s)"%(float_l, float_u)
			return float_in
		if float_in <= float_l:
			return float_l
		if float_in >= float_u:
			return float_u
		return float_in
	
	def get_graph_ratio(self, g1, g2):
		g_ratio=g1.Clone(g1.GetName())
		for ibin in range(0, g_ratio.GetN()):
			ratio=999
			err_down=0
			err_up=0
			if float(g1.GetY()[ibin]) !=0:
				if float(g2.GetY()[ibin]) !=0:
					#ratio=float((g1.GetY()[ibin]-g2.GetY()[ibin])/g2.GetY()[ibin])
					ratio=float((g1.GetY()[ibin])/g2.GetY()[ibin])
					err_down=float(g1.GetErrorYlow(ibin)/g2.GetY()[ibin])
					err_up  =float(g1.GetErrorYhigh(ibin)/g2.GetY()[ibin])
			g_ratio.SetPoint(ibin,g_ratio.GetX()[ibin],ratio)
			g_ratio.SetPointEYlow(ibin,err_down)
			g_ratio.SetPointEYhigh(ibin,err_up)
		return g_ratio
	
	def remove_graph_zero(self, gr_in):
		for i in range(gr_in.GetN()-1, 0-1,-1):
			N = gr_in.GetY()[i]
			#print "%d : %f"%(i,N)
			if N==0:
				gr_in.RemovePoint(i)
	
	def histTograph(self, h_data, isWeight=False):  
		h_data_bin_value={}
		h_data_bin_width={}
		for bin in range(1, h_data.GetNbinsX()+1):
			h_data_bin_value[bin]=h_data.GetBinContent(bin)*h_data.GetBinWidth(bin) 
			h_data_bin_width[bin]=h_data.GetBinWidth(bin) 
		g_data = ROOT.TGraphAsymmErrors(h_data)
		g_data.SetMarkerSize(0.5)
		g_data.SetMarkerStyle (20)
		alpha = float(1 - 0.6827)
		for i in range(0,g_data.GetN()): 
			N = g_data.GetY()[i]
			error_up=0
			error_low=0
			if isWeight:
				N = h_data_bin_value[i+1]
			L = 0
			if N==0:
				L=0
			else: 
				L= float( ROOT.Math.gamma_quantile(alpha/2,N,1.) )
			U =float( ROOT.Math.gamma_quantile_c(alpha/2,N+1,1) )
			error_low=N-L
			error_up=U-N
			if isWeight:
				if h_data_bin_width[i+1] !=0:
					error_low= (N-L)/h_data_bin_width[i+1]
					error_up=(U-N)/h_data_bin_width[i+1]
				else:
					error_up=0
					error_low=0
			if N==0:
				error_up=0
				error_low=0
			g_data.SetPointEYlow (i, error_low)
			g_data.SetPointEYhigh(i, error_up)
		return g_data
	
	def Graph_Xerror0(self, graph_in):
		for i in range(0,graph_in.GetN()):
			graph_in.SetPointEXlow (i, 0)
			graph_in.SetPointEXhigh(i, 0)
	
	def my_setzero(self, h2):
		for i in range(1,h2.GetNbinsX()+1):
			h2.SetBinContent(i,0.0)
	
	def my_setErrorzero(self, h2):
		for i in range(1,h2.GetNbinsX()+1):
			h2.SetBinError(i,0.0)
	
	def getYmax(self, h1):
		tmp_max = 0
		for i in range(1,h1.GetNbinsX()+1):
			if tmp_max < h1.GetBinContent(i):
				tmp_max = h1.GetBinContent(i)
		return tmp_max
	
	def my_abs(self, h2):
		for i in range(1,h2.GetNbinsX()+1):
			if h2.GetBinContent(i)<0:
				h2.SetBinContent(i,0.0)
	#		print "%d, %f"%(i,h2.GetBinContent(i))
	
	def Load_json(self, dic_name):
		return eval(open(dic_name).read().replace("\n",""))
	
	def Get_lep_SF(self, lep_pt,lep_eta,lep_isE,lep_isMu):
		lep_SF = 0.0
		if lep_isE:
			lep_SF = Get_ele_SF(lep_pt,lep_eta)
		elif lep_isMu:
			lep_SF = Get_mu_SF(lep_pt,lep_eta)
	        if lep_SF == 0.0:print 1/0
		return lep_SF
	
	def Get_SF_2D(self, dic_in, pt_in, eta_in):
		pt = pt_in
		eta = eta_in
		eff = 1.0
		for (pt_l, pt_u) in dic_in:
			if pt>=pt_l and pt<pt_u:
				for (eta_l, eta_u) in dic_in[(pt_l,pt_u)]:
					if eta>=eta_l and eta<eta_u:
						eff = dic_in[(pt_l,pt_u)][(eta_l,eta_u)]
						#print "(%s, %s) : %s"%(pt_in, eta_in, eff)
						return eff
		#print "warning: eff not find (%s, %s)"%(pt_in, eta_in)
		return eff
	
	def Get_SF_1D(self, dic_in, value_in):
		value = value_in
		eff = 1.0
		for (value_l, value_u) in dic_in:
			if value>=value_l and value<value_u:
				eff = dic_in[(value_l,value_u)]
				return eff
		return eff
	
	def Get_HEEP_ID_sys(self, et, region):
		ret = 0.0
		if region == 1 :
			if (et < 90) :
				ret = 0.01
			elif (et < 1000) :
				ret = 0.01 + (0.02 * (et - 90) / 910.0)
			else :
				ret = 0.03

		elif region == 3 :
			if (et < 90) :
				ret = 0.01
			elif (et < 300) :
				ret = 0.01 + (0.03 * (et - 90) / 210.0)
			else :
				ret = 0.04
		return ret

	def pm(self, x):
		if x>0:
			return 1
		elif x<0:
			return -1
		else:
			return 0

	def DYNNPDF_weight_2017_2018(self, event):
		Gen_Led_Et = t1.gen_leading_pt
		Gen_Z_mass = t1.gen_mass
		region_ele = t1.ele_region
		region_muon = t1.muon_region
		NNPDF_weight = 1.0
		region = 0

		if (region_ele == 1 and region_muon == 1):
			region = 1
		elif ( (region_ele == 1 and region_muon == 3) or (region_ele == 3 and region_muon == 1) ):
			region = 2
		elif (region_ele == 3 and region_muon == 3):
			region = 3
		
		if(Gen_Z_mass<120):
			if(region==1): 
				if (Gen_Led_Et<150):
					NNPDF_weight=3.596-0.2076 *Gen_Led_Et+0.005795*pow(Gen_Led_Et,2)-7.421e-05*pow(Gen_Led_Et,3)+4.447e-07*pow(Gen_Led_Et,4)-1.008e-9 *pow(Gen_Led_Et,5)
				else:
					NNPDF_weight=0.969125
			elif(region==2):
				if (Gen_Led_Et<150):
					NNPDF_weight=2.066-0.09495*Gen_Led_Et+0.002664*pow(Gen_Led_Et,2)-3.242e-05*pow(Gen_Led_Et,3)+1.755e-07*pow(Gen_Led_Et,4)-3.424e-10*pow(Gen_Led_Et,5)
				else:
					NNPDF_weight=1.191875
			elif(region==3): 
				if (Gen_Led_Et<150):
					NNPDF_weight=2.865-0.1443 *Gen_Led_Et+0.003799*pow(Gen_Led_Et,2)-4.482e-05*pow(Gen_Led_Et,3)+2.429e-07*pow(Gen_Led_Et,4)-4.93e-10 *pow(Gen_Led_Et,5)
				else:
					NNPDF_weight=0.9609375
		else:
			if(region==1):
				if(Gen_Z_mass<5000):
					NNPDF_weight=0.8934+0.0002193 *Gen_Z_mass-1.961e-7*pow(Gen_Z_mass,2)+8.704e-11*pow(Gen_Z_mass,3)-1.551e-14*pow(Gen_Z_mass,4)+1.112e-18*pow(Gen_Z_mass,5)
				else:
					NNPDF_weight=1.74865
			elif(region==2):
				if(Gen_Z_mass<5000):
					NNPDF_weight=0.8989+0.000182  *Gen_Z_mass-1.839e-7*pow(Gen_Z_mass,2)+1.026e-10*pow(Gen_Z_mass,3)-2.361e-14*pow(Gen_Z_mass,4)+1.927e-18*pow(Gen_Z_mass,5)
				else:
					NNPDF_weight=1.302025
			elif(region==3):
				if(Gen_Z_mass<5000):
					NNPDF_weight=0.9328-7.23e-6   *Gen_Z_mass+3.904e-9*pow(Gen_Z_mass,2)+2.454e-11*pow(Gen_Z_mass,3)-1.038e-14*pow(Gen_Z_mass,4)+1.543e-18*pow(Gen_Z_mass,5)
				else:
					NNPDF_weight=2.396125
		return NNPDF_weight

	def check_trigger_2016(self,event,leaf_name_list):
		return (True, True)

	def check_trigger_2017(self,event,leaf_name_list):
		return (True, True)

	def check_trigger_2018(self,event,leaf_name_list):
		return (True, True)

	def pass_MET_filters_2016(self, event, leaf_name_list, isData):
		ret = False
		if isData:
			ret = False
		else:
			ret = False
		return ret

	def pass_MET_filters_2017(self, t1, leaf_name_list, isData):
		trig_Flag_goodVertices_accept = False
		trig_Flag_globalSuperTightHalo2016Filter_accept = False
		trig_Flag_HBHENoiseFilter_accept = False
		trig_Flag_HBHENoiseIsoFilter_accept = False
		trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept = False
		trig_Flag_BadPFMuonFilter_accept = False
		trig_Flag_eeBadScFilter_accept = False
		trig_Flag_ecalBadCalibReduced = False
		if ( ('trig_Flag_goodVertices_accept' in leaf_name_list) and t1.trig_Flag_goodVertices_accept ):
			trig_Flag_goodVertices_accept = True
		if ( ('trig_Flag_globalSuperTightHalo2016Filter_accept' in leaf_name_list) and t1.trig_Flag_globalSuperTightHalo2016Filter_accept ):
			trig_Flag_globalSuperTightHalo2016Filter_accept = True
		if ( ('trig_Flag_HBHENoiseFilter_accept' in leaf_name_list) and t1.trig_Flag_HBHENoiseFilter_accept ):
			trig_Flag_HBHENoiseFilter_accept = True
		if ( ('trig_Flag_HBHENoiseIsoFilter_accept' in leaf_name_list) and t1.trig_Flag_HBHENoiseIsoFilter_accept ):
			trig_Flag_HBHENoiseIsoFilter_accept = True
		if ( ('trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept' in leaf_name_list) and t1.trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept ):
			trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept = True
		if ( ('trig_Flag_BadPFMuonFilter_accept' in leaf_name_list) and t1.trig_Flag_BadPFMuonFilter_accept ):
			trig_Flag_BadPFMuonFilter_accept = True
		if ( ('trig_Flag_eeBadScFilter_accept' in leaf_name_list) and t1.trig_Flag_eeBadScFilter_accept ):
			trig_Flag_eeBadScFilter_accept = True
		if ( ('trig_Flag_ecalBadCalibReduced' in leaf_name_list) and t1.trig_Flag_ecalBadCalibReduced ):
			trig_Flag_ecalBadCalibReduced = True

		ret = False
		if isData:
			ret = trig_Flag_goodVertices_accept \
							and trig_Flag_globalSuperTightHalo2016Filter_accept \
							and trig_Flag_HBHENoiseFilter_accept \
							and trig_Flag_HBHENoiseIsoFilter_accept \
							and trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept \
							and trig_Flag_BadPFMuonFilter_accept \
							and trig_Flag_eeBadScFilter_accept \
							and trig_Flag_ecalBadCalibReduced
		else:
			ret = trig_Flag_goodVertices_accept \
							and trig_Flag_globalSuperTightHalo2016Filter_accept \
							and trig_Flag_HBHENoiseFilter_accept \
							and trig_Flag_HBHENoiseIsoFilter_accept \
							and trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept \
							and trig_Flag_BadPFMuonFilter_accept \
							and trig_Flag_ecalBadCalibReduced
#							and trig_Flag_eeBadScFilter_accept \
		return ret

	def pass_MET_filters_2018(self, t1, leaf_name_list, isData):
		ret = False
		if isData:
			ret = False
		else:
			ret = False
		return ret

	def get_MC_weight_2016(self, t1):
		MuonSF_weight = 1.0
		ElectronSF_weight = 1.0
		top_weight = 1.0
		prefiring_weight = 1.0
		Trigger_SF = 1.0
		jet_BtagSF_medium_weight = 1.0
			
		#sys top case
		if self.sys_type == "top1_u":
			top_weight = t1.w_ts1_up
		elif self.sys_type == "top1_d":
			top_weight = t1.w_ts1_down
		else:
			top_weight = t1.w_top

		if t1.n_bjet > 0:
			jet_BtagSF_medium_weight = t1.w_Btag_offline
		#print "w_Btag_medium : %s"%(jet_BtagSF_medium_weight)

		tmp_leading_p4 = getP4(t1.leading_pt,t1.leading_eta,t1.leading_phi,t1.leading_isE,t1.leading_isMu)
		tmp_subleading_p4 = getP4(t1.sub_leading_pt,t1.sub_leading_eta,t1.sub_leading_phi,t1.sub_leading_isE,t1.sub_leading_isMu)
		if (t1.leading_isE):
			Ele_p4 = tmp_leading_p4
			Muon_p4 = tmp_subleading_p4
		else:
			Muon_p4 = tmp_leading_p4
			Ele_p4 = tmp_subleading_p4

		ele_sf_reco = self.SFs.get_ele_reco_sf("2016", "EleSFReco", Ele_p4.Pt(), Ele_p4.Eta())
		ElectronSF_weight *= ele_sf_reco
		ele_sf_id = self.SFs.get_ele_ID_sf("2016", "EleSFID", Ele_p4.Pt(), Ele_p4.Eta())
		ElectronSF_weight *= ele_sf_id

		muon_sf_id = self.SFs.get_mu_ID_sf("2016", "MuonSFID",Muon_p4.Pt(), Muon_p4.Eta() )
		MuonSF_weight *= muon_sf_id
		muon_sf_iso = self.SFs.get_mu_Iso_sf("2016", "MuonSFIso",Muon_p4.Pt(), Muon_p4.Eta() )
		MuonSF_weight *= muon_sf_iso

		#sys trigger sf
		Trigger_SF *= self.SFs.get_trigger_sf("2016", "TTT",t1.leading_pt,abs(t1.sub_leading_pt))

		#print "event :%s , sf_ele_reco : %0.6f , sf_ele_id : %0.6f , sf_mu_id : %0.6f , sf_mu_iso : %0.6f sf_trig : %0.6f , PU_w : %0.6f"%(t1.ev_event, ele_sf_reco, ele_sf_id, muon_sf_id, muon_sf_iso, Trigger_SF, t1.w_PU)
		return MuonSF_weight * ElectronSF_weight * top_weight * prefiring_weight * Trigger_SF * jet_BtagSF_medium_weight

	def get_MC_weight_2017(self, t1, pass_trigger_onlyMuon, isDY, isTTbar):
		MuonSF_weight = 1.0
		ElectronSF_weight = 1.0
		top_weight = 1.0
		prefiring_weight = 1.0
		Trigger_SF = 1.0
		jet_BtagSF_medium_weight = 1.0
		prefiring_weight = t1.ev_prefiringweight
			
		#sys top case
		if self.sys_type == "top1_u":
			top_weight = t1.w_ts1_up
		elif self.sys_type == "top1_d":
			top_weight = t1.w_ts1_down
		else:
			top_weight = t1.w_top

		if t1.n_bjet > 0:
			jet_BtagSF_medium_weight = t1.w_Btag_medium
		#print "w_Btag_medium : %s"%(jet_BtagSF_medium_weight)

		tmp_leading_p4 = getP4(t1.leading_pt,t1.leading_eta,t1.leading_phi,t1.leading_isE,t1.leading_isMu)
		tmp_subleading_p4 = getP4(t1.sub_leading_pt,t1.sub_leading_eta,t1.sub_leading_phi,t1.sub_leading_isE,t1.sub_leading_isMu)
		if (t1.leading_isE):
			Ele_p4 = tmp_leading_p4
			Muon_p4 = tmp_subleading_p4
		else:
			Muon_p4 = tmp_leading_p4
			Ele_p4 = tmp_subleading_p4

		ele_sf_reco = self.SFs.get_ele_reco_sf("2017", "EleSFReco", Ele_p4.Pt(), Ele_p4.Eta())
		ElectronSF_weight *= ele_sf_reco
		ele_sf_id = self.SFs.get_ele_ID_sf("2017", "EleSFID", Ele_p4.Pt(), Ele_p4.Eta())
		ElectronSF_weight *= ele_sf_id

		muon_sf_id = self.SFs.get_mu_ID_sf("2017", "MuonSFID",Muon_p4.Pt(), Muon_p4.Eta() )
		MuonSF_weight *= muon_sf_id
		muon_sf_iso = self.SFs.get_mu_Iso_sf("2017", "MuonSFIso",Muon_p4.Pt(), Muon_p4.Eta() )
		MuonSF_weight *= muon_sf_iso

		#sys trigger sf
		Trigger_SF *= self.SFs.get_trigger_sf("2017", "TTT",t1.leading_pt,abs(t1.sub_leading_pt))

		#print "event :%s , sf_ele_reco : %0.6f , sf_ele_id : %0.6f , sf_mu_id : %0.6f , sf_mu_iso : %0.6f sf_trig : %0.6f , PU_w : %0.6f"%(t1.ev_event, ele_sf_reco, ele_sf_id, muon_sf_id, muon_sf_iso, Trigger_SF, t1.w_PU)
		return MuonSF_weight * ElectronSF_weight * top_weight * prefiring_weight * Trigger_SF * jet_BtagSF_medium_weight

	def get_MC_weight_2018(self, t1, pass_trigger_onlyMuon, isDY, isTTbar):
		MuonSF_weight = 1.0
		ElectronSF_weight = 1.0
		top_weight = 1.0
		prefiring_weight = 1.0
		Trigger_SF = 1.0
		jet_BtagSF_medium_weight = 1.0
		prefiring_weight = t1.ev_prefiringweight
			
		#sys top case
		if self.sys_type == "top1_u":
			top_weight = t1.w_ts1_up
		elif self.sys_type == "top1_d":
			top_weight = t1.w_ts1_down
		else:
			top_weight = t1.w_top

		if t1.n_bjet > 0:
			jet_BtagSF_medium_weight = t1.w_Btag_medium
		#print "w_Btag_medium : %s"%(jet_BtagSF_medium_weight)

		tmp_leading_p4 = getP4(t1.leading_pt,t1.leading_eta,t1.leading_phi,t1.leading_isE,t1.leading_isMu)
		tmp_subleading_p4 = getP4(t1.sub_leading_pt,t1.sub_leading_eta,t1.sub_leading_phi,t1.sub_leading_isE,t1.sub_leading_isMu)
		if (t1.leading_isE):
			Ele_p4 = tmp_leading_p4
			Muon_p4 = tmp_subleading_p4
		else:
			Muon_p4 = tmp_leading_p4
			Ele_p4 = tmp_subleading_p4

		ele_sf_reco = self.SFs.get_ele_reco_sf("2018", "EleSFReco", Ele_p4.Pt(), Ele_p4.Eta())
		ElectronSF_weight *= ele_sf_reco
		ele_sf_id = self.SFs.get_ele_ID_sf("2018", "EleSFID", Ele_p4.Pt(), Ele_p4.Eta())
		ElectronSF_weight *= ele_sf_id

		muon_sf_id = self.SFs.get_mu_ID_sf("2018", "MuonSFID",Muon_p4.Pt(), Muon_p4.Eta() )
		MuonSF_weight *= muon_sf_id
		muon_sf_iso = self.SFs.get_mu_Iso_sf("2018", "MuonSFIso",Muon_p4.Pt(), Muon_p4.Eta() )
		MuonSF_weight *= muon_sf_iso

		#sys trigger sf
		Trigger_SF *= self.SFs.get_trigger_sf("2018", "TTT",t1.leading_pt,abs(t1.sub_leading_pt))

		#print "event :%s , sf_ele_reco : %0.6f , sf_ele_id : %0.6f , sf_mu_id : %0.6f , sf_mu_iso : %0.6f sf_trig : %0.6f , PU_w : %0.6f"%(t1.ev_event, ele_sf_reco, ele_sf_id, muon_sf_id, muon_sf_iso, Trigger_SF, t1.w_PU)
		return MuonSF_weight * ElectronSF_weight * top_weight * prefiring_weight * Trigger_SF * jet_BtagSF_medium_weight

	def	fill_value_hist(self, h1, final_info, final_value_max_constrain):
		final_value = final_info[0]
		final_weight = final_info[1]
		for value_i in range(len(final_value)):
			h1_nbin = h1.GetXaxis().GetNbins()
			if (final_value_max_constrain):
				if final_value[value_i] >= h1.GetXaxis().GetBinUpEdge(h1_nbin):
					final_value[value_i] = h1.GetXaxis().GetBinCenter(h1_nbin)
			h1.Fill(final_value[value_i], final_weight)

	def Fill_hist(self, sample_name, sample_dic, value_dic, cut_str):
		root_file = sample_dic.input_file
	
		f1 = ROOT.TFile(root_file,"read")
		t1 = f1.Get("tap")
		isData = False
		isFake = False
		isSS = False

		isTTbar = False
		isDY = False
	
		isData = sample_dic.isData
		isFake = sample_dic.isFake
		isSS = sample_dic.isSS

		if "_DYToLL" in sample_name:
			isDY = True
		if "_ttbar2l2u" in sample_name:
			isTTbar = True
	
		event_i = 0
		event_nl = self.n_range_l
		event_nh = self.n_range_h
		if self.isSplit_mode:
			if (event_nl<0):event_nl=1
			if (event_nh<0):event_nh=t1.GetEntries()
			print "### using split mode, get event from %d to %d"%(self.n_range_l,self.n_range_h)

		event_nl = max(event_nl-1, 0)
		event_nh = min(event_nh, t1.GetEntries())
		process_bar_t1 = ShowProcess(event_nh-event_nl)

		leaf_name_list = []
		for leaf in t1.GetListOfLeaves():
			leaf_name_list.append(leaf.GetName())

		print "(%s)Fill hist from file : %s, isData: %s, isFake: %s, isSS: %s, nEvent: [%d - %d]"%(self.global_year_label,root_file,isData,isFake,isSS,event_nl, event_nh)
		for event_i in range(event_nl, event_nh):
			t1.GetEntry(event_i)
			process_bar_t1.show_process()
			#check same sign event
			if (isSS and t1.leading_charge != t1.sub_leading_charge): continue
			elif ((not isSS) and (t1.leading_charge == t1.sub_leading_charge)): continue
			passed = global_cut_func(cut_str, t1)
			if not passed: continue 

			pass_trigger = False
			pass_trigger_onlyMuon = False

			if self.ana_2016:
				pass_trigger,pass_trigger_onlyMuon = self.check_trigger_2016(t1,leaf_name_list)
			if self.ana_2017:
				pass_trigger,pass_trigger_onlyMuon = self.check_trigger_2017(t1,leaf_name_list)
			if self.ana_2018:
				pass_trigger,pass_trigger_onlyMuon = self.check_trigger_2018(t1,leaf_name_list)

			if not pass_trigger:
				continue

			MC_weight = 0.0
			pu_weight = 1.0
			fake_weight = 1.0

			if not isData:
				if self.ana_2016:
					MC_weight = self.get_MC_weight_2016(t1)
				if self.ana_2017:
					MC_weight = self.get_MC_weight_2017(t1, pass_trigger_onlyMuon, isDY, isTTbar)
				if self.ana_2018:
					MC_weight = self.get_MC_weight_2018(t1, pass_trigger_onlyMuon, isDY, isTTbar)
			else:
				MC_weight = 1.0
			
			if isFake:
				fake_weight = t1.w_fake

			tmp_path_value_dic = collections.OrderedDict()
	
			for path in value_dic:
				if not isData:
					pu_weight = t1.w_PU
					#sys case
					if self.sys_type == "pu_u":
						pu_weight = t1.w_PU_up
					if self.sys_type == "pu_d":
						pu_weight = t1.w_PU_down

					if not value_dic[path].PU_reweight:
						pu_weight = self.pm(pu_weight)
	
				event_weight = MC_weight * fake_weight * pu_weight

				bin_weight = 1.0
				if self.value_dic[path].use_array:
					bin_weight = 1.0/getbinwidth(t1.aluevalue_dic[path].hist_para[1])
				final_weight = event_weight * bin_weight
				
				# Fill hist
				if ("TMVA" in path):
					tmp_path_value_dic[path] = ([], final_weight)
				else:
					final_value, final_value_max_constrain = global_map_value(path, t1, leaf_name_list, value_dic[path])
					tmp_path_value_dic[path] = [final_value, final_weight]
					self.fill_value_hist(sample_dic.hist[path], tmp_path_value_dic[path], final_value_max_constrain)

			if (GLOBAL_USE_MVA):
				self.MVA_reader.update_variables(tmp_path_value_dic)
				for path in value_dic:
					if "TMVA" in path:
						tmp_path_value_dic[path][0].append(self.MVA_reader.evaluateMVA())
						self.fill_value_hist(sample_dic.hist[path], tmp_path_value_dic[path], final_value_max_constrain)

		process_bar_t1.close('done')
	


	def Get_hist_from_together(self, sample, sample_dic, value_dic, cut):
		root_file = "%s/%s_hist.root"%(cut,cut)
		f1 = ROOT.TFile(root_file,"read")
		isData = sample_dic.isData
		isFake = sample_dic.isFake
		if self.log_level > 0: print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
		for path in value_dic:
			sample_dic.hist[path] = f1.Get("%s_%s_out"%(sample,value_dic[path].hist_name))
		f1.Close()
	
	def Get_hist_from_tmp(self, sample, sample_dic, value_dic, hist_input_dir):
		root_file = "%s/hist_%s.root"%(hist_input_dir,sample)
		f1 = ROOT.TFile(root_file,"Read")
		isData = sample_dic.isData
		isFake = sample_dic.isFake
		if self.log_level > 0: print "%s: Get hist from file : %s, isData: %s, isFake: %s"%(self.sys_type,root_file,isData,isFake)
		for path in value_dic:
			sample_dic.hist[path] = f1.Get("%s_%s_out"%(sample,value_dic[path].hist_name))
		f1.Close()
	
	def Get_hist_from_split(self, sample, sample_dic, value_dic, cut):
		root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
		f1 = ROOT.TFile(root_file,"Read")
		isData = sample_dic.isData
		isFake = sample_dic.isFake
		if self.log_level > 0: print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
		for path in value_dic:
			sample_dic.hist[path] = f1.Get("%s_%s_out"%(sample,value_dic[path].hist_name))
		f1.Close()
	
	def Get_hist_from_file(self, sample,sample_dic,value_dic):
		root_file = sample_dic.input_file
		f1 = ROOT.TFile(root_file,"read")
		isData = sample_dic.isData
		isFake = sample_dic.isFake
		if self.log_level > 0: print "Read hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
		for path in value_dic:
			sample_dic.hist[path] = f1.Get("%s_%s_out"%(sample,value_dic[path].hist_name))
		f1.Close()
	
	def Get_hist(self, input_dic, value_dic, cut_str):
		for sample in input_dic:
			sample_dic = input_dic[sample]
			if self.isSplit_mode:
				if sample == self.target_sample:
					self.Fill_hist(sample, sample_dic, value_dic, cut_str)
			#elif (sample_dic.isFromRoot and sample_dic.isUpdate):
			#	self.Fill_hist(sample_dic, value_dic, cut)
			elif sample_dic.isFromRoot:
				self.Get_hist_from_tmp(sample, sample_dic, value_dic, self.hist_input_dir)
			elif not sample_dic.isFromRoot:
				self.Get_hist_from_file(sample, sample_dic, value_dic)
			if "n_stat" in value_dic :
				sample_dic.N_total = sample_dic.hist["n_stat"].Integral()
	
	def Store_hist_together(self, input_dic, value_dic, cut):
		root_file = "%s/%s_hist.root"%(cut,cut)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for sample in input_dic:
			for path in value_dic:
					if "_out" in input_dic[sample].hist[path].GetName()[-4:]:
						input_dic[sample].hist[path].SetName(input_dic[sample].hist[path].GetName()[:-4])
					tmp_name = input_dic[sample].hist[path].GetName()
					input_dic[sample].hist[path].SetName("%s_out"%(input_dic[sample].hist[path].GetName()))
					input_dic[sample].hist[path].Write()
					input_dic[sample].hist[path].SetName(tmp_name)
		f1.Close()
	
	def Store_hist_plot_total(self, option = "2"):
		if (self.sys_type == "nominal"):
			option += "123"

		tmp_list = []
		if ("1" in option):
			self.Store_hist_plot("compare_1", "data", self.input_dic, self.value_dic, self.plot_dic, self.hist_output_dir)
		if ("2" in option):
			self.Store_hist_plot("compare_2", "mc", self.input_dic, self.value_dic, self.plot_dic, self.hist_output_dir)
		if ("3" in option):
			self.Store_hist_plot("compare_3", "signal_mc", self.input_dic, self.value_dic, self.plot_dic, self.hist_output_dir)

	def Store_hist_plot(self, plot_name, root_name, input_dic, value_dic, plot_dic, hist_output_dir):
		part = plot_name
		root_file = "%s/%s_plot_hist_%s.root"%(hist_output_dir.split("/")[0], root_name, self.sys_type)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for plot in plot_dic[part]:
			tmp_plot_dic = plot_dic[part][plot]
			for path in value_dic:
#				if not (path in self.store_hist_plot_list):continue
				if "_out" in tmp_plot_dic["hist"][path].GetName()[-4:]:
					tmp_plot_dic["hist"][path].SetName(tmp_plot_dic["hist"][path].GetName()[:-4])
				tmp_name = tmp_plot_dic["hist"][path].GetName()
				tmp_plot_dic["hist"][path].SetName("%s_out"%(tmp_plot_dic["hist"][path].GetName()))
				tmp_plot_dic["hist"][path].Write()
				tmp_plot_dic["hist"][path].SetName(tmp_name)
		f1.Close()

	def Store_hist(self, input_dic, value_dic, hist_output_dir):
		for sample in input_dic:
			root_file = "%s/hist_%s.root"%(hist_output_dir,sample)
			f1 = ROOT.TFile(root_file,"RECREATE")
			for path in value_dic:
					if "_out" in input_dic[sample].hist[path].GetName()[-4:]:
						input_dic[sample].hist[path].SetName(input_dic[sample].hist[path].GetName()[:-4])
					tmp_name = input_dic[sample].hist[path].GetName()
					input_dic[sample].hist[path].SetName("%s_out"%(input_dic[sample].hist[path].GetName()))
					input_dic[sample].hist[path].Write()
					input_dic[sample].hist[path].SetName(tmp_name)
			f1.Close()
	
	def Store_hist_split(self, input_dic, value_dic, hist_output_dir):
		try:os.mkdir("%s/split"%(hist_output_dir))
		except:pass
		for sample in input_dic:
			if not sample == self.target_sample:continue
			try:os.mkdir("%s/split/%s"%(hist_output_dir,sample))
			except:pass
			root_file = "%s/split/%s/hist_%s_%s_%s.root"%(hist_output_dir,sample,sample,self.n_range_l,self.n_range_h)
			f1 = ROOT.TFile(root_file,"RECREATE")
			for path in value_dic:
					if "_out" in input_dic[sample].hist[path].GetName()[-4:]:
						input_dic[sample].hist[path].SetName(input_dic[sample].hist[path].GetName()[:-4])
					tmp_name = input_dic[sample].hist[path].GetName()
					input_dic[sample].hist[path].SetName("%s_out"%(input_dic[sample].hist[path].GetName()))
					input_dic[sample].hist[path].Write()
					input_dic[sample].hist[path].SetName(tmp_name)
			f1.Close()
	
	
	def Norm_hist(self, input_dic, value_dic):
		total_lumi = self.Get_total_lumi(input_dic)
		# sys case
		if self.sys_type == "xs_ttbar_u":
			input_dic["_ttbar2l2u"].Xsection *= (1.0 + 0.05)
			input_dic["_ttbar2l2u_M500to800"].Xsection *= (1.0 + 0.05)
			input_dic["_ttbar2l2u_M800to1200"].Xsection *= (1.0 + 0.05)
			input_dic["_ttbar2l2u_M1200to1800"].Xsection *= (1.0 + 0.05)
			input_dic["_ttbar2l2u_M1800toInf"].Xsection *= (1.0 + 0.05)
		if self.sys_type == "xs_ttbar_d":
			input_dic["_ttbar2l2u"].Xsection *= (1.0 - 0.05)
			input_dic["_ttbar2l2u_M500to800"].Xsection *= (1.0 - 0.05)
			input_dic["_ttbar2l2u_M800to1200"].Xsection *= (1.0 - 0.05)
			input_dic["_ttbar2l2u_M1200to1800"].Xsection *= (1.0 - 0.05)
			input_dic["_ttbar2l2u_M1800toInf"].Xsection *= (1.0 - 0.05)
		if self.sys_type == "xs_ww_u":
			input_dic["_WW2l2u"].Xsection *= (1.0 + 0.03)
			input_dic["_WW2l2u_M200to600"].Xsection *= (1.0 + 0.03)
			input_dic["_WW2l2u_M600to1200"].Xsection *= (1.0 + 0.03)
			input_dic["_WW2l2u_M1200to2500"].Xsection *= (1.0 + 0.03)
			input_dic["_WW2l2u_M2500toInf"].Xsection *= (1.0 + 0.03)
		if self.sys_type == "xs_ww_d":
			input_dic["_WW2l2u"].Xsection *= (1.0 - 0.03)
			input_dic["_WW2l2u_M200to600"].Xsection *= (1.0 - 0.03)
			input_dic["_WW2l2u_M600to1200"].Xsection *= (1.0 - 0.03)
			input_dic["_WW2l2u_M1200to2500"].Xsection *= (1.0 - 0.03)
			input_dic["_WW2l2u_M2500toInf"].Xsection *= (1.0 - 0.03)
		if self.sys_type == "xs_st_u":
			input_dic["_ST"].Xsection *= (1.0 + 0.05)
		if self.sys_type == "xs_st_d":
			input_dic["_ST"].Xsection *= (1.0 - 0.05)
		if self.sys_type == "xs_dy_u":
			input_dic["_DYToLL"].Xsection *= (1.0 + 0.02)
		if self.sys_type == "xs_dy_d":
			input_dic["_DYToLL"].Xsection *= (1.0 - 0.02)
		if self.sys_type == "xs_wz_u":
			#input_dic["_WZ"].Xsection *= (1.0 + 0.04)
			input_dic["_WZTo2L2Q"].Xsection *= (1.0 + 0.04)
			input_dic["_WZTo3LNu"].Xsection *= (1.0 + 0.04)
		if self.sys_type == "xs_wz_d":
			#input_dic["_WZ"].Xsection *= (1.0 - 0.04)
			input_dic["_WZTo2L2Q"].Xsection *= (1.0 - 0.04)
			input_dic["_WZTo3LNu"].Xsection *= (1.0 - 0.04)
		if self.sys_type == "xs_zz_u":
			#input_dic["_ZZ"].Xsection *= (1.0 + 0.04)
			input_dic["_ZZTo2L2Nu"].Xsection *= (1.0 + 0.04)
			input_dic["_ZZTo2L2Q"].Xsection *= (1.0 + 0.04)
			input_dic["_ZZTo4L"].Xsection *= (1.0 + 0.04)
		if self.sys_type == "xs_zz_d":
			#input_dic["_ZZ"].Xsection *= (1.0 - 0.04)
			input_dic["_ZZTo2L2Nu"].Xsection *= (1.0 - 0.04)
			input_dic["_ZZTo2L2Q"].Xsection *= (1.0 - 0.04)
			input_dic["_ZZTo4L"].Xsection *= (1.0 - 0.04)
		if self.sys_type == "lumi_u":
			for sample in input_dic:
				input_dic[sample].Xsection *= (1.0 + self.lumi_sys)
		if self.sys_type == "lumi_d":
			for sample in input_dic:
				input_dic[sample].Xsection *= (1.0 - self.lumi_sys)

		
		for sample in input_dic:
			if not input_dic[sample]["isData"]:
				input_dic[sample].Norm_Factor = total_lumi * input_dic[sample].Xsection / float(input_dic[sample].Raw_total)
				for path in value_dic:
					self.my_abs(input_dic[sample].hist[path])
					input_dic[sample].hist[path].Scale(input_dic[sample].Norm_Factor)
			input_dic[sample].N_norm = input_dic[sample].N_total * input_dic[sample].Norm_Factor * input_dic[sample].weight_factor
	
	def Print_table(self, input_dic):
		total_lumi = self.Get_total_lumi(input_dic)
		total_num = self.Get_total_num(input_dic)
		for sample in input_dic:
			if input_dic[sample]["isData"] and input_dic[sample].useToNorm:
				print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic[sample].Norm_Factor, input_dic[sample].N_norm, 100.0*input_dic[sample].N_norm/total_num)
		print "#"*50
	
		for sample in input_dic:
			if self.check_sys_sample(sample, "3f"):continue
			if not (input_dic[sample]["isData"] and input_dic[sample].useToNorm):
				print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic[sample].Norm_Factor, input_dic[sample].N_norm, 100.0*input_dic[sample].N_norm/total_num)
		print "#"*50
	
	def Get_part_hist(self, input_dic, value_dic, plot_dic):
		for path in value_dic:
			for part in plot_dic:
				for plot in plot_dic[part]:
					if (self.sys_type != "nominal") and (plot in self.plot_list_common_sys): continue
					hist_list = plot_dic[part][plot]["data_list"]
					for sample in hist_list:
						plot_dic[part][plot]["hist"][path].Add(plot_dic[part][plot]["hist"][path], input_dic[sample].hist[path], 1, input_dic[sample].weight_factor)
					if plot_dic[part][plot]["ABS"]: 
						#print path
						self.my_abs(plot_dic[part][plot]["hist"][path])
					if "weight_factor" in plot_dic[part][plot]:
						plot_dic[part][plot]["hist"][path].Scale(plot_dic[part][plot]["weight_factor"])
					#if plot == "fake_rate":
						#self.my_setErrorzero(plot_dic[part][plot]["hist"][path])
	
		for part in plot_dic:
			for plot in plot_dic[part]:
				if (self.sys_type != "nominal") and (plot in self.plot_list_common_sys): continue
				hist_list = plot_dic[part][plot]["data_list"]
				for sample in hist_list:
					plot_dic[part][plot]["N_total"]+=input_dic[sample].N_norm
	
	def Get_total_lumi(self, input_dic):
		if self.sys_type == "nominal":
			total_lumi = 0.0
			for sample in input_dic:
				if input_dic[sample].useToNorm:
					total_lumi += input_dic[sample].lumi
			return total_lumi
		else:
			return self.total_lumi
	
	def Get_total_num(self, input_dic):
		total_num = 0.0
		for sample in input_dic:
			if input_dic[sample].useToNorm:
				total_num += input_dic[sample].N_total
		return total_num
	
	def set_dir(self):
		#self.my_mkdir(self.hist_input_dir)
		self.my_mkdir(self.hist_output_dir)

	def my_mkdir(self, dir_str):
		tmp_list = dir_str.split("/")
		tmp_dir = ""
		for part in tmp_list:
			if len(part)>0:
				tmp_dir = os.path.join(tmp_dir,part)
				try:os.mkdir(tmp_dir)
				except:pass

	def Init_hist_sample(self, input_dic, value_dic):
		for path in value_dic:
			if value_dic[path].use_array:
				for sample in input_dic:
					print value_dic[path].hist_para[0]
					print value_dic[path].hist_para[1]
					input_dic[sample].hist[path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path].hist_name), "", value_dic[path].hist_para[0], value_dic[path].hist_para[1])
			else:
				for sample in input_dic:
					input_dic[sample].hist[path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path].hist_name), "", value_dic[path].hist_para[0], value_dic[path].hist_para[2], value_dic[path].hist_para[3])
	
	def Init_hist_plot(self, value_dic, plot_dic, specific_path = "null"):
		for path in value_dic:
			if value_dic[path].use_array:
				for part in plot_dic:
					for plot in plot_dic[part]:
						if (specific_path != "null" and plot != specific_path):continue
						plot_dic[part][plot]["hist"][path] = ROOT.TH1F("%s_%s"%(plot,value_dic[path].hist_name), "", value_dic[path].hist_para[0], value_dic[path].hist_para[1])
			else:
				for part in plot_dic:
					for plot in plot_dic[part]:
						if (specific_path != "null" and plot != specific_path):continue
						plot_dic[part][plot]["hist"][path] = ROOT.TH1F("%s_%s"%(plot,value_dic[path].hist_name), "", value_dic[path].hist_para[0], value_dic[path].hist_para[2], value_dic[path].hist_para[3])
	
	def Set_hist_sample(self, input_dic, value_dic):
		for path in value_dic:
			for sample in input_dic:
				input_dic[sample].hist[path].Sumw2()
	
	def Set_hist_plot(self, value_dic, plot_dic):
		for path in value_dic:
			for part in plot_dic:
				for plot in plot_dic[part]:
					plot_dic[part][plot]["hist"][path].Sumw2()
					plot_dic[part][plot]["hist"][path].SetFillColorAlpha(plot_dic[part][plot]["color"],1.0)
					plot_dic[part][plot]["hist"][path].SetLineColorAlpha(plot_dic[part][plot]["color"],1.0)
	
	def print_error(self, error_range_dic, input_dic, value_dic, plot_dic):
		error_range_dic = {"0-200":[1,200,0,0], "200-3200":[2,3000,0,0]}
		for error_range in error_range_dic:
			print "%s print sum table %s %s"%("#"*20,error_range, "#"*20)
			for sample in input_dic:
				tmp_N = input_dic[sample].hist["mass_err_stat"].GetBinContent(error_range_dic[error_range][0]) * error_range_dic[error_range][1]
				tmp_err = input_dic[sample].hist["mass_err_stat"].GetBinError(error_range_dic[error_range][0]) * error_range_dic[error_range][1]
				print "%s,%s,%s"%(sample,tmp_N,tmp_err)
			print "%s finish %s"%("#"*20,"#"*20)
	
	def print_error2(self, error_range_dic, input_dic, value_dic, plot_dic):
		error_range_dic = {"0-1":[1,1,0,0]}
	
		path = "n_stat"
		for error_range in error_range_dic:
			print "%s print sum table %s %s"%("#"*20,error_range, "#"*20)
			for p in sorted(plot_dic["compare_2"].iteritems(),key=lambda d:d[1]["N_total"],reverse = False):
				plot = p[0]
				tmp_N   = plot_dic["compare_2"][plot]["hist"][path].GetBinContent(error_range_dic[error_range][0]) * error_range_dic[error_range][1]
				tmp_err = plot_dic["compare_2"][plot]["hist"][path].GetBinError(error_range_dic[error_range][0]) * error_range_dic[error_range][1]
				print "%10s,\t %0.1f +/- %0.1f"%(plot,tmp_N,tmp_err)
			print "%s finish %s"%("#"*20,"#"*20)
	
	def get_plot_nevent(self):
		tmp_dic = {}
		path = "n_stat"

		plot = 'data'
		tmp_N   = self.plot_dic["compare_1"][plot]["hist"][path].GetBinContent(1)
		tmp_err = self.plot_dic["compare_1"][plot]["hist"][path].GetBinError(1)
		tmp_dic[plot] = [tmp_N, tmp_err]

		for plot in self.plot_list:
			tmp_N   = self.plot_dic["compare_2"][plot]["hist"][path].GetBinContent(1)
			tmp_err = self.plot_dic["compare_2"][plot]["hist"][path].GetBinError(1)
			tmp_dic[plot] = [tmp_N, tmp_err]
		return tmp_dic

	def set_input_dic(self, tmp_dic, option = "2"):
		force_set = False
		if option == "-1":force_set = True
		if (self.sys_type == "nominal"):
			option = "123"

		self.input_dic = {}
		if self.sys_type == "nominal" or force_set:
			for part in tmp_dic:
				self.input_dic[part] = deepcopy(tmp_dic[part])
		elif self.sys_type == "muptscalu":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part].input_file = self.input_dic[part].input_file[:-5] + "_muptu" + self.input_dic[part].input_file[-5:]
		elif self.sys_type == "muptscald":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part].input_file = self.input_dic[part].input_file[:-5] + "_muptd" + self.input_dic[part].input_file[-5:]
		elif self.sys_type == "muptresu":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part].input_file = self.input_dic[part].input_file[:-5] + "_muresu" + self.input_dic[part].input_file[-5:]
		elif self.sys_type == "eletscalu":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part].input_file = self.input_dic[part].input_file[:-5] + "_eletu" + self.input_dic[part].input_file[-5:]
		elif self.sys_type == "eletscald":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part].input_file = self.input_dic[part].input_file[:-5] + "_eletd" + self.input_dic[part].input_file[-5:]
		else :
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
		#redirect dir to input file:
		for part in self.input_dic:
			self.input_dic[part].input_file = os.path.join("MC_data",self.input_dic[part].input_file)



	def check_sys_sample(self,sample_name,option = "2"):

		if (self.sys_type == "nominal") and (not "f" in option):
			option += "123"

		if "2" in option:
			for plot in self.plot_list_sys:
				if sample_name in self.plot_dic["compare_2"][plot]["data_list"]:
					return True
		if "3" in option:
			for plot in self.plot_dic["compare_3"]:
				if sample_name in self.plot_dic["compare_3"][plot]["data_list"]:
					return True
		return False

	def set_value_dic(self, tmp_dic):
		self.value_dic = {}
		for part in tmp_dic:
			self.value_dic[part] = deepcopy(tmp_dic[part])

	def set_plot_dic(self, tmp_dic, option = "2"):
		self.plot_dic = {}

		if (self.sys_type == "nominal"):
			option += "123"

		tmp_list = []
		if ("1" in option):
			tmp_list.append("compare_1")
		if ("2" in option):
			tmp_list.append("compare_2")
		if ("3" in option):
			tmp_list.append("compare_3")

		for part in tmp_list:
			self.plot_dic[part] = deepcopy(tmp_dic[part])

	def get_sys_sum(self, path):
		if self.value_dic[path].use_array:
			tmp_sum = ROOT.TH1F("sum_%s"%(self.value_dic[path].hist_name), "", self.value_dic[path].hist_para[0], self.value_dic[path].hist_para[1])
		else:
			tmp_sum = ROOT.TH1F("sum_%s"%(self.value_dic[path].hist_name), "", self.value_dic[path].hist_para[0], self.value_dic[path].hist_para[2], self.value_dic[path].hist_para[3])
		tmp_sum.Sumw2()
	
		for i in range(len(self.plot_list)):
			plot = self.plot_list[len(self.plot_list)-1-i]
			if plot in self.plot_dic["compare_2"]:
				tmp_sum.Add(tmp_sum, self.plot_dic["compare_2"][plot]["hist"][path], 1, 1)

		self.sys_sum_dic[path] = tmp_sum

	def set_common_hist(self, plot, tmp_common_dic):
		part = "compare_2"
		self.plot_dic[part][plot] = deepcopy(tmp_common_dic)
		self.plot_dic[part][plot]["hist"] = {}
		self.Init_hist_plot(self.value_dic, self.plot_dic, plot)
		for path in tmp_common_dic["hist"]:
			self.plot_dic[part][plot]["hist"][path] = tmp_common_dic["hist"][path].Clone(self.plot_dic[part][plot]["hist"][path].GetName())
			if plot == "qcd_jet":
				if self.sys_type == "qcd_u":
					self.plot_dic[part][plot]["hist"][path].Scale(1.5)
				elif self.sys_type == "qcd_d":
					self.plot_dic[part][plot]["hist"][path].Scale(0.5)

	def main_plot(self):
		#Initialize hist for sample_dic and plot_dic
		self.Init_hist_sample(self.input_dic, self.value_dic)
		self.Init_hist_plot(self.value_dic, self.plot_dic)
		#set up hist parameters
		self.Set_hist_sample(self.input_dic, self.value_dic)
		self.Set_hist_plot(self.value_dic, self.plot_dic)
		#get hist from root file using Get() or Fill()
		self.Get_hist(self.input_dic, self.value_dic, self.cut_str)
		#Store hist to root file
		#self.Store_hist(self.input_dic, self.value_dic, self.hist_output_dir)
		#Normalize hist
		self.Norm_hist(self.input_dic, self.value_dic)
		#print contribution of each dataset
		if self.sys_type == "nominal": self.Print_table(self.input_dic)
		#get hist for self.plot_dic
		print "processing : %s"%(self.sys_type)
		self.Get_part_hist(self.input_dic, self.value_dic, self.plot_dic)
	
		if self.sys_type == "nominal": self.print_error2(self.error_range_dic, self.input_dic, self.value_dic, self.plot_dic)
		#print_sum(self.input_dic)
	
	def main_plot_split(self):
		#Initialize hist for sample_dic and plot_dic
		self.Init_hist_sample(self.input_dic, self.value_dic)
		#set up hist parameters
		self.Set_hist_sample(self.input_dic, self.value_dic)
		#get hist from root file using Get() or Fill()
		self.Get_hist(self.input_dic, self.value_dic, self.cut_str)
		#Store hist to root file
		self.Store_hist_split(self.input_dic, self.value_dic, self.hist_output_dir)
	
	##########################################

