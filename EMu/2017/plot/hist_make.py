import sys
try:
    sys.path.append("C:/root_v5.34.30/bin")
except:
    pass
import ROOT
import time
from math import *
from array import array
from input_card import *
from copy import deepcopy
import os
	#from input_card import *
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

class hist_make():
	def __init__(self):
		self.MuonTriggerSF_dic		= self.Load_json("SF_json/Muon/Trigger/Muon_Trigger_run2017BCDEF_json.txt")
		self.MuonISOSF_dic			= self.Load_json("SF_json/Muon/Iso/Muon_ISO_RunBCDEF_SF_ISO.json")
		self.MuonIDSF_dic			= self.Load_json("SF_json/Muon/ID/Muon_ID_RunBCDEF_SF_ID.json")
		self.dic_Ele_reco_pt_eta	= self.Load_json("SF_json/Electron/reco/Electron_reco_run2017BCDEF_json.txt")
		
		self.ElectronIDSF_dic = {
				(0,1.4442):0.963,
				(1.566,2.5):0.967,
			}

	
		self.error_range_dic = {"0-500":[1,500,0], "500-1000":[2,500,0], "1000-1500":[3,500,0], "1500-2000":[4,500,0]}
	
		self.plot_list = ["_ttbar","ST","Di_boson","Z","qcd_jet","qcd_jet_mu"]#,"fake_rate_e"],"fake_rate_m"]
		self.plot_list_sys = ["_ttbar","ST","Di_boson","Z"]
		self.plot_list_common_sys = ["qcd_jet"]
		self.plot_list_jet = ["_ttbar","Di_boson","ST","Z"]
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
		self.cut_str = "True"
		self.total_lumi = 0.0
	
		self.input_dic = {}
		self.value_dic = {}
		self.plot_dic = {}
		self.sys_sum_dic = {}
		self.store_hist_plot_list = ["M_emu_massDep", "M_emu_massDep_2"]


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
			if isWeight and h_data_bin_width[i+1] !=0:
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
		print "warning: eff not find (%s, %s)"%(pt_in, eta_in)
		return eff
	
	def Get_SF_1D(self, dic_in, value_in):
		value = value_in
		eff = 1.0
		for (value_l, value_u) in dic_in:
			if value>=value_l and value<value_u:
				eff = dic_in[(value_l,value_u)]
				return eff
		return eff
	
	def pm(self, x):
		if x>0:
			return 1
		elif x<0:
			return -1
		else:
			return 0
	
	def Fill_hist(self, sample_dic, value_dic, cut_str):
		root_file = sample_dic["input_file"]
	
		f1 = ROOT.TFile(root_file,"read")
		t1 = f1.Get("tap")
		isData = False
		isFake = False
		isSS = False
	
		if "isData" in sample_dic:
			isData = sample_dic["isData"]
		if "isFake" in sample_dic:
			isFake = sample_dic["isFake"]
		if "isSS" in sample_dic:
			isSS = sample_dic["isSS"]
	
		print "Fill hist from file : %s, isData: %s, isFake: %s, isSS: %s, nEvent: %d"%(root_file,isData,isFake,isSS,t1.GetEntries())
		n_process = 0
		if self.isSplit_mode:
			if (self.n_range_l<0):self.n_range_l=1
			if (self.n_range_h<0):self.n_range_h=t1.GetEntries()
			print "### using split mode, get event from %d to %d"%(self.n_range_l,self.n_range_h)

		leaf_name_list = []
		for leaf in t1.GetListOfLeaves():
			leaf_name_list.append(leaf.GetName())

		for event in t1:
			n_process += 1
			if(n_process%50000==0):print n_process,'processed\n'
			if self.isSplit_mode:
				if (self.n_range_l > n_process):
					continue
				elif (self.n_range_h < n_process):
					break
			#if n_process >100:break
			#check same sign event
			if (isSS and getattr(event,"ele_charge") != getattr(event,"muon_charge")): continue
			exec 'passed = (%s)'%(cut_str)
			if not passed: continue 
			if (not isData):
				if (not (getattr(event,"ele_MC_matched") and getattr(event,"muon_MC_matched"))):
					continue
			pass_trigger = False
			if (Muon50_trig_fire) and ("Muon50_trig_fire" in leaf_name_list) and  getattr(event,"Muon50_trig_fire"):
				pass_trigger = True
			if (TkMu100_trig_fire) and ("TkMu100_trig_fire" in leaf_name_list) and  getattr(event,"TkMu100_trig_fire"):
				pass_trigger = True
			if (OldMu100_trig_fire) and ("OldMu100_trig_fire" in leaf_name_list) and  getattr(event,"OldMu100_trig_fire"):
				pass_trigger = True
			if (Ele115_trig_fire) and ("Ele115_trig_fire" in leaf_name_list) and  getattr(event,"Ele115_trig_fire"):
				pass_trigger = True
			if (Photon175_trig_fire) and ("Photon175_trig_fire" in leaf_name_list) and  getattr(event,"Photon175_trig_fire"):
				pass_trigger = True
			if not pass_trigger:
				continue
			#if not getattr(event, "trig_Flag_goodVertices_accept"): continue
			event_weight = 1.0
			MuonSF_weight = 1.0
			ElectronSF_weight = 1.0
			pu_weight = 1.0
			fake_weight = 1.0
			top_weight = 1.0
			other_weight = 1.0
			bin_weight = 1.0
			sys_weight = 1.0
			if not isData:
				#if getattr(event,"Photon175_trig_fire") != 1:
				MuonSF_weight *= self.Get_SF_2D(self.MuonISOSF_dic,abs(getattr(event,"muon_eta")),self.constrain_float(getattr(event,"muon_pt"),0.0,119))
				MuonSF_weight *= self.Get_SF_2D(self.MuonIDSF_dic,abs(getattr(event,"muon_eta")),self.constrain_float(getattr(event,"muon_pt"),0.0,119))
				MuonSF_weight *= self.Get_SF_2D(self.MuonTriggerSF_dic,self.constrain_float(getattr(event,"muon_pt"),0.0,1199),abs(getattr(event,"muon_eta")))
				ElectronSF_weight *= self.Get_SF_1D(self.ElectronIDSF_dic,abs(getattr(event,"ele_eta")))
				ElectronSF_weight *= self.Get_SF_2D(self.dic_Ele_reco_pt_eta,self.constrain_float(getattr(event,"ele_Et"),0.0,499.0),getattr(event,"ele_eta"))
				#other_weight = getattr(event,"w_other")
				top_weight *= getattr(event,"w_top")
				#sys case
				if self.sys_type == "top1_u":
					sys_weight *= getattr(event,"w_ts1_up")
				if self.sys_type == "top1_d":
					sys_weight *= getattr(event,"w_ts1_down")

			if isFake:
				fake_weight = getattr(event,"w_fake")
	
			for path in value_dic:
				if not isData:
					w_PU_str = "w_PU"
					#sys case
					if self.sys_type == "pu_u":
						w_PU_str = "w_PU_up"
					if self.sys_type == "pu_d":
						w_PU_str = "w_PU_down"

					if value_dic[path]["PU_reweight"]:
						pu_weight = getattr(event,w_PU_str)
					else:
						pu_weight = self.pm(getattr(event,w_PU_str))
	
				tmp_value_dic = {}
				if isData:
					tmp_value_dic = value_dic[path]["Data_value_dic"]
				else:
					tmp_value_dic = value_dic[path]["MC_value_dic"]
	
				event_weight = MuonSF_weight * ElectronSF_weight * pu_weight * fake_weight * top_weight * other_weight * sys_weight
				self.map_value(path, event, sample_dic["hist"][path],tmp_value_dic,event_weight)
	
	def getP4_ele(self, Et, eta, phi):
		p4 = ROOT.TLorentzVector()
		p4.SetPtEtaPhiM(Et,eta,phi,0.000511)
		return p4
	
	def getP4_muon(self, pt, eta, phi):
		p4 = ROOT.TLorentzVector()
		p4.SetPtEtaPhiM(pt,eta,phi,0.10566)
		return p4
	
	def getbinwidth(self, x,x1):
		for i in range(len(x1)):
			if x < x1[i] and i>0:
				return (x1[i]-x1[i-1])
			elif x < x1[i]:
				return -1.0
		return -1.0
	
	def map_value(self, path, event, h1, tmp_value_dic, event_weight_factor):
		pi = 3.1415926
		bin_weight = 1.0
		if path == "":
			return
		elif path == "Pt_ll":
			tmp_ele_p4 = self.getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
			tmp_muon_p4 = self.getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
			tmp_pt = (tmp_ele_p4 + tmp_muon_p4).Pt()
			#print tmp_pt
			if tmp_pt < 259:
				h1.Fill(tmp_pt,event_weight_factor)
			else:
				h1.Fill(259,event_weight_factor)
		elif path == "rapidity_ll":
			tmp_ele_p4 = self.getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
			tmp_muon_p4 = self.getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
			tmp_rapidity = (tmp_ele_p4 + tmp_muon_p4).Rapidity()
			h1.Fill(tmp_rapidity,event_weight_factor)
		elif path == "phi_ll":
			tmp_ele_p4 = self.getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
			tmp_muon_p4 = self.getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
			tmp_phi = (tmp_ele_p4 + tmp_muon_p4).Phi()
			h1.Fill(tmp_phi,event_weight_factor)
		elif path == "deltaR_ll":
			tmp_ele_p4 = self.getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
			tmp_muon_p4 = self.getP4_muon(getattr(event,"muon_pt"),getattr(event,"muon_eta"),getattr(event,"muon_phi"))
			tmp_dR = tmp_ele_p4.DeltaR(tmp_muon_p4)
			h1.Fill(tmp_dR,event_weight_factor)
		elif path == "delta_eta_ll":
			delta_eta = fabs(getattr(event, "ele_eta") - getattr(event, "muon_eta"))
			h1.Fill(delta_eta,event_weight_factor)
		elif path == "delta_phi_ll":
			delta_phi = fabs(getattr(event, "ele_phi") - getattr(event, "muon_phi"))
			if delta_phi > pi:delta_phi = 2*pi - delta_phi
			h1.Fill(delta_phi,event_weight_factor)
		elif path == "n_jet_bjet":
			n_jet = getattr(event,"n_jet")
			n_bjet = getattr(event,"n_bjet")
			if n_jet <=4:
				h1.Fill(n_jet_bjet_dic["(%s,%s)"%(n_jet,n_bjet)][0],event_weight_factor)
			else:
				h1.Fill(n_jet_bjet_dic["(>4,n)"][0],event_weight_factor)
		elif path == "HT":
			tmp_HT = 0
			jet_pt_vector = getattr(event,"jet_pt")
			jet_eta_vector = getattr(event,"jet_eta")
			#jet_ID_vector = getattr(event,"jet_IDLoose")
			jet_pass_vector = getattr(event,"jet_passed")
			for i in range(len(jet_pt_vector)):
				if jet_pass_vector[i]:
					tmp_HT += jet_pt_vector[i]
			#if tmp_HT == 0:return
			if tmp_HT > 500:
				h1.Fill(499,event_weight_factor)
			else:
				h1.Fill(tmp_HT,event_weight_factor)
		elif path == "sys_HT":
			tmp_HT = 0
			jet_pt_vector = getattr(event,"jet_pt")
			jet_eta_vector = getattr(event,"jet_eta")
			jet_pass_vector = getattr(event,"jet_passed")
			#jet_ID_vector = getattr(event,"jet_IDLoose")
			for i in range(len(jet_pt_vector)):
				#if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
				if jet_pass_vector[i]:
					tmp_HT += jet_pt_vector[i]
			tmp_ele_p4 = self.getP4_ele(getattr(event,"ele_Et"),getattr(event,"ele_eta"),getattr(event,"ele_phi"))
			tmp_HT += tmp_ele_p4.Pt() + getattr(event,"muon_pt")
			#if tmp_HT == 0:return
			if tmp_HT > 500:
				h1.Fill(499,event_weight_factor)
			else:
				h1.Fill(tmp_HT,event_weight_factor)
		elif path == "n_stat":
			h1.Fill(0.5,event_weight_factor)
		else:
			for value in tmp_value_dic:
				exec 'passed = (%s)'%(tmp_value_dic[value])
				if not passed: continue 
				#print "passed"
				bin_weight = 1.0
				if self.value_dic[path]["bin_weight"]:
					if self.value_dic[path]["use_array"]:
						bin_weight = 1.0/self.getbinwidth(getattr(event,value),self.value_dic[path]["hist_para"][1])
				total_weight = event_weight_factor * bin_weight
				h1.Fill(getattr(event,value),total_weight)

	def Get_hist_from_together(self, sample, sample_dic, value_dic, cut):
		root_file = "%s/%s_hist.root"%(cut,cut)
		f1 = ROOT.TFile(root_file,"read")
		isData = sample_dic["isData"]
		isFake = sample_dic["isFake"]
		print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
		for path in value_dic:
			sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
		f1.Close()
	
	def Get_hist_from_tmp(self, sample, sample_dic, value_dic, hist_input_dir):
		root_file = "%s/hist_%s.root"%(hist_input_dir,sample)
		f1 = ROOT.TFile(root_file,"Read")
		isData = sample_dic["isData"]
		isFake = sample_dic["isFake"]
		print "%s: Get hist from file : %s, isData: %s, isFake: %s"%(self.sys_type,root_file,isData,isFake)
		for path in value_dic:
			sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
		f1.Close()
	
	def Get_hist_from_split(self, sample, sample_dic, value_dic, cut):
		root_file = "%s/%s_hist_%s.root"%(cut,cut,sample)
		f1 = ROOT.TFile(root_file,"Read")
		isData = sample_dic["isData"]
		isFake = sample_dic["isFake"]
		print "Get hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
		for path in value_dic:
			sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
		f1.Close()
	
	def Get_hist_from_file(self, sample,sample_dic,value_dic):
		root_file = sample_dic["input_file"]
		f1 = ROOT.TFile(root_file,"read")
		isData = sample_dic["isData"]
		isFake = sample_dic["isFake"]
		print "Read hist from file : %s, isData: %s, isFake: %s"%(root_file,isData,isFake)
		for path in value_dic:
			sample_dic["hist"][path] = f1.Get("%s_%s_out"%(sample,value_dic[path]["hist_name"]))
		f1.Close()
	
	def Get_hist(self, input_dic, value_dic, cut_str):
		for sample in input_dic:
			sample_dic = input_dic[sample]
			if self.isSplit_mode:
				if sample == self.target_sample:
					self.Fill_hist(sample_dic, value_dic, cut_str)
			#elif (sample_dic["isFromRoot"] and sample_dic["isUpdate"]):
			#	self.Fill_hist(sample_dic, value_dic, cut)
			elif sample_dic["isFromRoot"]:
				self.Get_hist_from_tmp(sample, sample_dic, value_dic, self.hist_input_dir)
			elif not sample_dic["isFromRoot"]:
				self.Get_hist_from_file(sample, sample_dic, value_dic)
			if "n_stat" in value_dic :
				sample_dic["N_total"] = sample_dic["hist"]["n_stat"].Integral()
	
	def Store_hist_together(self, input_dic, value_dic, cut):
		root_file = "%s/%s_hist.root"%(cut,cut)
		f1 = ROOT.TFile(root_file,"RECREATE")
		for sample in input_dic:
			for path in value_dic:
					if "_out" in input_dic[sample]["hist"][path].GetName()[-4:]:
						input_dic[sample]["hist"][path].SetName(input_dic[sample]["hist"][path].GetName()[:-4])
					tmp_name = input_dic[sample]["hist"][path].GetName()
					input_dic[sample]["hist"][path].SetName("%s_out"%(input_dic[sample]["hist"][path].GetName()))
					input_dic[sample]["hist"][path].Write()
					input_dic[sample]["hist"][path].SetName(tmp_name)
		f1.Close()
	
	def Store_hist_plot_total(self, option = "2"):
		if (self.sys_type == "norminal"):
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
				if not (path in self.store_hist_plot_list):continue
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
					if "_out" in input_dic[sample]["hist"][path].GetName()[-4:]:
						input_dic[sample]["hist"][path].SetName(input_dic[sample]["hist"][path].GetName()[:-4])
					tmp_name = input_dic[sample]["hist"][path].GetName()
					input_dic[sample]["hist"][path].SetName("%s_out"%(input_dic[sample]["hist"][path].GetName()))
					input_dic[sample]["hist"][path].Write()
					input_dic[sample]["hist"][path].SetName(tmp_name)
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
					if "_out" in input_dic[sample]["hist"][path].GetName()[-4:]:
						input_dic[sample]["hist"][path].SetName(input_dic[sample]["hist"][path].GetName()[:-4])
					tmp_name = input_dic[sample]["hist"][path].GetName()
					input_dic[sample]["hist"][path].SetName("%s_out"%(input_dic[sample]["hist"][path].GetName()))
					input_dic[sample]["hist"][path].Write()
					input_dic[sample]["hist"][path].SetName(tmp_name)
			f1.Close()
	
	
	def Norm_hist(self, input_dic, value_dic):
		total_lumi = self.Get_total_lumi(input_dic)
		# sys case
		if self.sys_type == "xs_ttbar_u":
			input_dic["_ttbar2l2u"]["Xsection"] *= (1.0 + 0.05)
		if self.sys_type == "xs_ttbar_d":
			input_dic["_ttbar2l2u"]["Xsection"] *= (1.0 - 0.05)
		if self.sys_type == "xs_ww_u":
			input_dic["_WW"]["Xsection"] *= (1.0 + 0.03)
		if self.sys_type == "xs_ww_d":
			input_dic["_WW"]["Xsection"] *= (1.0 - 0.03)
		if self.sys_type == "xs_st_u":
			input_dic["_ST"]["Xsection"] *= (1.0 + 0.05)
		if self.sys_type == "xs_st_d":
			input_dic["_ST"]["Xsection"] *= (1.0 - 0.05)
		if self.sys_type == "xs_dy_u":
			input_dic["_DYToLL"]["Xsection"] *= (1.0 + 0.02)
		if self.sys_type == "xs_dy_d":
			input_dic["_DYToLL"]["Xsection"] *= (1.0 - 0.02)
		if self.sys_type == "xs_wz_u":
			input_dic["_WZ"]["Xsection"] *= (1.0 + 0.04)
		if self.sys_type == "xs_wz_d":
			input_dic["_WZ"]["Xsection"] *= (1.0 - 0.04)
		if self.sys_type == "xs_zz_u":
			input_dic["_ZZ"]["Xsection"] *= (1.0 + 0.04)
		if self.sys_type == "xs_zz_d":
			input_dic["_ZZ"]["Xsection"] *= (1.0 - 0.04)

		
		for sample in input_dic:
			if not input_dic[sample]["isData"]:
				input_dic[sample]["Norm_Factor"] = total_lumi * input_dic[sample]["Xsection"] / float(input_dic[sample]["Raw_total"])
				for path in value_dic:
					self.my_abs(input_dic[sample]["hist"][path])
					input_dic[sample]["hist"][path].Scale(input_dic[sample]["Norm_Factor"])
			input_dic[sample]["N_norm"] = input_dic[sample]["N_total"] * input_dic[sample]["Norm_Factor"] * input_dic[sample]["weight_factor"]
	
	def Print_table(self, input_dic):
		total_lumi = self.Get_total_lumi(input_dic)
		total_num = self.Get_total_num(input_dic)
		for sample in input_dic:
			if input_dic[sample]["isData"] and input_dic[sample]["useToNorm"]:
				print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic[sample]["Norm_Factor"], input_dic[sample]["N_norm"], 100.0*input_dic[sample]["N_norm"]/total_num)
		print "#"*50
	
		for sample in input_dic:
			if self.check_sys_sample(sample, "3f"):continue
			if not (input_dic[sample]["isData"] and input_dic[sample]["useToNorm"]):
				print "%s :  %s  ;  %s  ;  %0.2f%%  "%(sample, input_dic[sample]["Norm_Factor"], input_dic[sample]["N_norm"], 100.0*input_dic[sample]["N_norm"]/total_num)
		print "#"*50
	
	def Get_part_hist(self, input_dic, value_dic, plot_dic):
		for path in value_dic:
			for part in plot_dic:
				for plot in plot_dic[part]:
					if (self.sys_type != "norminal") and (plot in self.plot_list_common_sys): continue
					hist_list = plot_dic[part][plot]["data_list"]
					for sample in hist_list:
						plot_dic[part][plot]["hist"][path].Add(plot_dic[part][plot]["hist"][path], input_dic[sample]["hist"][path], 1, input_dic[sample]["weight_factor"])
					if plot_dic[part][plot]["ABS"]: 
						#print path
						self.my_abs(plot_dic[part][plot]["hist"][path])
					if "weight_factor" in plot_dic[part][plot]:
						plot_dic[part][plot]["hist"][path].Scale(plot_dic[part][plot]["weight_factor"])
					#if plot == "fake_rate":
						#self.my_setErrorzero(plot_dic[part][plot]["hist"][path])
	
		for part in plot_dic:
			for plot in plot_dic[part]:
				if (self.sys_type != "norminal") and (plot in self.plot_list_common_sys): continue
				hist_list = plot_dic[part][plot]["data_list"]
				for sample in hist_list:
					plot_dic[part][plot]["N_total"]+=input_dic[sample]["N_norm"]
	
	def Get_total_lumi(self, input_dic):
		if self.sys_type == "norminal":
			total_lumi = 0.0
			for sample in input_dic:
				if input_dic[sample]["useToNorm"]:
					total_lumi += input_dic[sample]["lumi"]
			return total_lumi
		else:
			return self.total_lumi
	
	def Get_total_num(self, input_dic):
		total_num = 0.0
		for sample in input_dic:
			if input_dic[sample]["useToNorm"]:
				total_num += input_dic[sample]["N_total"]
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
			if value_dic[path]["use_array"]:
				for sample in input_dic:
					input_dic[sample]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
			else:
				for sample in input_dic:
					input_dic[sample]["hist"][path] = ROOT.TH1F("%s_%s"%(sample,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])
	
	def Init_hist_plot(self, value_dic, plot_dic, specific_path = "null"):
		for path in value_dic:
			if value_dic[path]["use_array"]:
				for part in plot_dic:
					for plot in plot_dic[part]:
						if (specific_path != "null" and plot != specific_path):continue
						plot_dic[part][plot]["hist"][path] = ROOT.TH1F("%s_%s"%(plot,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][1])
			else:
				for part in plot_dic:
					for plot in plot_dic[part]:
						if (specific_path != "null" and plot != specific_path):continue
						plot_dic[part][plot]["hist"][path] = ROOT.TH1F("%s_%s"%(plot,value_dic[path]["hist_name"]), "", value_dic[path]["hist_para"][0], value_dic[path]["hist_para"][2], value_dic[path]["hist_para"][3])
	
	def Set_hist_sample(self, input_dic, value_dic):
		for path in value_dic:
			for sample in input_dic:
				input_dic[sample]["hist"][path].Sumw2()
	
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
				tmp_N = input_dic[sample]["hist"]["mass_err_stat"].GetBinContent(error_range_dic[error_range][0]) * error_range_dic[error_range][1]
				tmp_err = input_dic[sample]["hist"]["mass_err_stat"].GetBinError(error_range_dic[error_range][0]) * error_range_dic[error_range][1]
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
				print "%s,%s,%s"%(plot,tmp_N,tmp_err)
			print "%s finish %s"%("#"*20,"#"*20)
	
	def set_input_dic(self, tmp_dic, option = "2"):
		force_set = False
		if option == "-1":force_set = True
		if (self.sys_type == "norminal"):
			option = "123"

		self.input_dic = {}
		if self.sys_type == "norminal" or force_set:
			for part in tmp_dic:
				self.input_dic[part] = deepcopy(tmp_dic[part])
		elif self.sys_type == "muptscalu":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part]["input_file"] = self.input_dic[part]["input_file"][:-5] + "_muptu" + self.input_dic[part]["input_file"][-5:]
		elif self.sys_type == "muptresu":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part]["input_file"] = self.input_dic[part]["input_file"][:-5] + "_muresu" + self.input_dic[part]["input_file"][-5:]
		elif self.sys_type == "eletscalu":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part]["input_file"] = self.input_dic[part]["input_file"][:-5] + "_eletu" + self.input_dic[part]["input_file"][-5:]
		elif self.sys_type == "eletscald":
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
					self.input_dic[part]["input_file"] = self.input_dic[part]["input_file"][:-5] + "_eletd" + self.input_dic[part]["input_file"][-5:]
		else :
			for part in tmp_dic:
				if self.check_sys_sample(part,option):
					self.input_dic[part] = deepcopy(tmp_dic[part])
		#redirect dir to input file:
		for part in self.input_dic:
			self.input_dic[part]["input_file"] = os.path.join("MC_data",self.input_dic[part]["input_file"])



	def check_sys_sample(self,sample_name,option = "2"):

		if (self.sys_type == "norminal") and (not "f" in option):
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

		if (self.sys_type == "norminal"):
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

	def get_sys_sum(self, path, common_sys):
		if self.value_dic[path]["use_array"]:
			tmp_sum = ROOT.TH1F("sum_%s"%(self.value_dic[path]["hist_name"]), "", self.value_dic[path]["hist_para"][0], self.value_dic[path]["hist_para"][1])
		else:
			tmp_sum = ROOT.TH1F("sum_%s"%(self.value_dic[path]["hist_name"]), "", self.value_dic[path]["hist_para"][0], self.value_dic[path]["hist_para"][2], self.value_dic[path]["hist_para"][3])
		tmp_sum.Sumw2()
	
		for i in range(len(self.plot_list_sys)):
			plot = self.plot_list_sys[len(self.plot_list_sys)-1-i]
			if plot in self.plot_dic["compare_2"]:
			#print self.plot_dic["compare_2"][plot]["N_total"]
				tmp_sum.Add(tmp_sum, self.plot_dic["compare_2"][plot]["hist"][path], 1, 1)
		tmp_sum.Add(tmp_sum, self.plot_dic["compare_2"]["qcd_jet"]["hist"][path], 1, 1)


#		if self.sys_type == "qcd_u":
#			tmp_sum.Add(tmp_sum, common_sys, 1, 1.5)
#		elif self.sys_type == "qcd_d":
#			tmp_sum.Add(tmp_sum, common_sys, 1, 0.5)
#		else:
#			tmp_sum.Add(tmp_sum, common_sys, 1, 1)

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
		if self.sys_type == "norminal": self.Print_table(self.input_dic)
		#get hist for self.plot_dic
		print self.sys_type
		self.Get_part_hist(self.input_dic, self.value_dic, self.plot_dic)
	
		if self.sys_type == "norminal": self.print_error2(self.error_range_dic, self.input_dic, self.value_dic, self.plot_dic)
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
