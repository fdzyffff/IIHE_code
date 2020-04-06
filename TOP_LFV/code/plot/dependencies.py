import sys
try:
    sys.path.append("C:/root_v5.34.30/bin")
except:
    pass

from array import array
import os
import ROOT
import time
from copy import deepcopy
from math import *
import collections

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gErrorIgnoreLevel=ROOT.kWarning

##Cross sections:
#xsection_ttbar2l2u = 87.31
#xsection_ttbar2l2u_M500to800 = 0.326
#xsection_ttbar2l2u_M800to1200 = 0.0326
#xsection_ttbar2l2u_M1200to1800 = 0.00305
#xsection_ttbar2l2u_M1800toInf = 0.000174
#
#xsection_WW2l2u = 12.178
#xsection_WW2l2u_M200to600 = 1.39
#xsection_WW2l2u_M600to1200 = 0.057
#xsection_WW2l2u_M1200to2500 = 0.0036
#xsection_WW2l2u_M2500toInf = 0.000054
#
#xsection_DYToLL = 5765.4
#xsection_WZ = 47.13
#xsection_ZZ = 16.523
#xsection_ST = 19.47 + 19.47
#
#xsection_WZTo2L2Q = 5.595
#xsection_WZTo3LNu = 5.052
#xsection_ZZTo2L2Nu = 0.564
#xsection_ZZTo2L2Q = 3.22
#xsection_ZZTo4L = 1.212
#
#
#xsection_QBHtoEMu_M200 = 24066.378
#xsection_QBHtoEMu_M400 = 1773.9027
#xsection_QBHtoEMu_M600 = 332.7039
#xsection_QBHtoEMu_M800 = 93.89556
#xsection_QBHtoEMu_M1000 = 32.822153
#xsection_QBHtoEMu_M1200 = 13.262773
#xsection_QBHtoEMu_M1400 = 5.9366958
#xsection_QBHtoEMu_M1600 = 2.8184958
#xsection_QBHtoEMu_M1800 = 1.4130132
#xsection_QBHtoEMu_M2000 = 0.74754306
#xsection_QBHtoEMu_M2500 = 0.16704102
#xsection_QBHtoEMu_M3000 = 0.04210492
#xsection_QBHtoEMu_M3500 = 0.011567997
#xsection_QBHtoEMu_M4000 = 0.0033187364
#xsection_QBHtoEMu_M4500 = 0.000949752
#xsection_QBHtoEMu_M5000 = 0.00027582334
#xsection_QBHtoEMu_M5500 = 7.88E-05
#xsection_QBHtoEMu_M6000 = 2.23E-05
#xsection_QBHtoEMu_M7000 = 1.58E-06
#xsection_QBHtoEMu_M8000 = 9.32E-08
#xsection_QBHtoEMu_M9000 = 4.48E-09
#xsection_QBHtoEMu_M10000 = 1.60E-10
#
#xsection_RPVresonantToEMu_M200 = 1
#xsection_RPVresonantToEMu_M300 = 1
#xsection_RPVresonantToEMu_M400 = 1
#xsection_RPVresonantToEMu_M500 = 1
#xsection_RPVresonantToEMu_M600 = 1
#xsection_RPVresonantToEMu_M700 = 1
#xsection_RPVresonantToEMu_M800 = 1
#xsection_RPVresonantToEMu_M900 = 1
#xsection_RPVresonantToEMu_M1000 = 1
#xsection_RPVresonantToEMu_M1200 = 1
#xsection_RPVresonantToEMu_M1400 = 1
#xsection_RPVresonantToEMu_M1600 = 1
#xsection_RPVresonantToEMu_M1800 = 1
#xsection_RPVresonantToEMu_M2000 = 1
#xsection_RPVresonantToEMu_M2500 = 1
#xsection_RPVresonantToEMu_M3000 = 1
#xsection_RPVresonantToEMu_M3500 = 1
#xsection_RPVresonantToEMu_M4000 = 1
#xsection_RPVresonantToEMu_M4500 = 1
#xsection_RPVresonantToEMu_M5000 = 1
#xsection_RPVresonantToEMu_M5500 = 1
#xsection_RPVresonantToEMu_M6000 = 1
#xsection_RPVresonantToEMu_M6500 = 1
#
#xsection_ZPrimeToEMu_M500 = 9.56
#xsection_ZPrimeToEMu_M600 = 5.03
#xsection_ZPrimeToEMu_M700 = 2.83
#xsection_ZPrimeToEMu_M800 = 1.704
#xsection_ZPrimeToEMu_M900 = 1.075
#xsection_ZPrimeToEMu_M1000 = 0.7141
#xsection_ZPrimeToEMu_M1100 = 0.4775
#xsection_ZPrimeToEMu_M1200 = 0.329
#xsection_ZPrimeToEMu_M1300 = 0.234
#xsection_ZPrimeToEMu_M1400 = 0.1675
#xsection_ZPrimeToEMu_M1500 = 0.1226
#xsection_ZPrimeToEMu_M1600 = 0.09071
#xsection_ZPrimeToEMu_M1700 = 0.06808
#xsection_ZPrimeToEMu_M1800 = 0.05166
#xsection_ZPrimeToEMu_M1900 = 0.03912
#xsection_ZPrimeToEMu_M2000 = 0.03027
#xsection_ZPrimeToEMu_M2200 = 0.01847
#xsection_ZPrimeToEMu_M2400 = 0.01147
#xsection_ZPrimeToEMu_M2600 = 0.007258
#xsection_ZPrimeToEMu_M2800 = 0.004695
#xsection_ZPrimeToEMu_M3000 = 0.003079
#xsection_ZPrimeToEMu_M3500 = 0.001163
#xsection_ZPrimeToEMu_M4000 = 0.0004841
#xsection_ZPrimeToEMu_M4500 = 0.0002196
#xsection_ZPrimeToEMu_M5000 = 0.0001113
#xsection_ZPrimeToEMu_M5500 = 6.238e-05# +- 3.722e-07
#xsection_ZPrimeToEMu_M6000 = 3.896e-05# +- 2.435e-07

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n_jet_bjet_dic = {
"(0,0)":[0,1,"(0,0)"],
"(1,0)":[1,2,"(1,0)"],
"(1,1)":[2,3,"(1,1)"],
"(2,0)":[3,4,"(2,0)"],
"(2,1)":[4,5,"(2,1)"],
"(2,2)":[5,6,"(2,2)"],
"(3,0)":[6,7,"(3,0)"],
"(3,1)":[7,8,"(3,1)"],
"(3,2)":[8,9,"(3,2)"],
"(3,3)":[9,10,"(3,3)"],
"(4,0)":[10,11,"(4,0)"],
"(4,1)":[11,12,"(4,1)"],
"(4,2)":[12,13,"(4,2)"],
"(4,3)":[13,14,"(4,3)"],
"(4,4)":[14,15,"(4,4)"],
"(>4,n)":[15,16,"(>4,n)"],
}
n_jet_bjet_dic2 = {
"(1,0)":[0,1,"(1,0)"],
"(1,1)":[1,2,"(1,1)"],
"(2,1)":[2,3,"(2,1)"],
"(>=3,1)":[3,4,"(>=3,1)"],
"(>=3,>1)":[4,5,"(>=3,>1)"],
}

def getP4(pt, eta, phi, isE, isMu):
	p4 = ROOT.TLorentzVector()
	if isE:
		p4.SetPtEtaPhiM(pt,eta,phi,0.000511)
	else:
		p4.SetPtEtaPhiM(pt,eta,phi,0.10566)
	return p4

def getbinwidth(x,x1):
	for i in range(len(x1)):
		if x < x1[i] and i>0:
			return (x1[i]-x1[i-1])
		elif x < x1[i]:
			return -1.0
	return -1.0

def global_map_value(path, t1, leaf_name_list, value_dic_s):
	final_value = []
	final_value_max_constrain = True
	bin_weight = 1.0
	pi = 3.1415926
	jet_pt_vector = t1.jet_pt
	jet_eta_vector = t1.jet_eta
	jet_phi_vector = t1.jet_phi
	jet_ID_vector = t1.jet_IDLoose
	jet_CSVv2_vector = t1.jet_DeepCSV
	leading_jet_id = -1
	sub_leading_jet_id = -1
	tmp_jet_pt_1 = -1.0
	tmp_jet_pt_2 = -1.0
	for i in range(len(jet_pt_vector)):
		if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
			if jet_pt_vector[i] > tmp_jet_pt_1:
				sub_leading_jet_id = leading_jet_id
				tmp_jet_pt_2 = tmp_jet_pt_1
				tmp_jet_pt_1 = jet_pt_vector[i]
				leading_jet_id = i
			elif jet_pt_vector[i] > tmp_jet_pt_2:
				tmp_jet_pt_2 = jet_pt_vector[i]
				sub_leading_jet_id = i

	tmp_leading_p4 = getP4(t1.leading_pt,t1.leading_eta,t1.leading_phi,t1.leading_isE,t1.leading_isMu)
	tmp_subleading_p4 = getP4(t1.sub_leading_pt,t1.sub_leading_eta,t1.sub_leading_phi,t1.sub_leading_isE,t1.sub_leading_isMu)

	# Get value and weight to Fill the hist
	if path == "pt_muon" and ("pt_muon" not in leaf_name_list):
		if t1.leading_isMu:
			final_value.append(t1.leading_pt)
		if t1.sub_leading_isMu:
			final_value.append(t1.sub_leading_pt)
	elif path == "eta_muon" and ("eta_muon" not in leaf_name_list):
		if t1.leading_isMu:
			final_value.append(t1.leading_eta)
		if t1.sub_leading_isMu:
			final_value.append(t1.sub_leading_eta)
	elif path == "pt_ele" and ("pt_ele" not in leaf_name_list):
		if t1.leading_isE:
			final_value.append(t1.leading_pt)
		if t1.sub_leading_isE:
			final_value.append(t1.sub_leading_pt)
	elif path == "eta_ele" and ("eta_ele" not in leaf_name_list):
		if t1.leading_isE:
			final_value.append(t1.leading_pt)
		if t1.sub_leading_isE:
			final_value.append(t1.sub_leading_pt)

	elif path == "Pt_ll" and ("Pt_ll" not in leaf_name_list):
		tmp_pt = (tmp_leading_p4 + tmp_subleading_p4).Pt()
		final_value.append(tmp_pt)

	elif path == "phi_ll" and ("phi_ll" not in leaf_name_list):
		tmp_phi = (tmp_leading_p4 + tmp_subleading_p4).Phi()
		final_value.append(tmp_phi)

	elif path == "deltaR_ll" and ("deltaR_ll" not in leaf_name_list):
		tmp_dR = tmp_leading_p4.DeltaR(tmp_subleading_p4)
		final_value.append(tmp_dR)

	elif path == "rapidity_ll" and ("rapidity_ll" not in leaf_name_list):
		tmp_rapidity = (tmp_leading_p4 + tmp_subleading_p4).Rapidity()
		final_value.append(tmp_rapidity)

	elif path == "Z_MET_T1Txy_delta_phi" and ("Z_MET_T1Txy_delta_phi" not in leaf_name_list):
		tmp_phi = (tmp_leading_p4 + tmp_subleading_p4).Phi()
		delta_phi = fabs(tmp_phi - t1.MET_T1Txy_phi)
		if delta_phi > pi:delta_phi = 2*pi - delta_phi
		final_value.append(fabs(delta_phi))

	elif path == "n_jet_bjet2" and ("n_jet_bjet2" not in leaf_name_list):
		final_value_max_constrain = False
		n_jet = t1.n_jet
		n_bjet = t1.n_bjet
		if n_jet == 1 and n_bjet == 0:
			final_value.append(n_jet_bjet_dic2["(1,0)"][0])
		elif n_jet == 1 and n_bjet == 1:
			final_value.append(n_jet_bjet_dic2["(1,1)"][0])
		elif n_jet == 2 and n_bjet == 1:
			final_value.append(n_jet_bjet_dic2["(2,1)"][0])
		elif n_jet >= 3 and n_bjet == 1:
			final_value.append(n_jet_bjet_dic2["(>=3,1)"][0])
		elif n_jet >= 3 and n_bjet > 1:
			final_value.append(n_jet_bjet_dic2["(>=3,>1)"][0])

	elif path == "n_jet_bjet" and ("n_jet_bjet" not in leaf_name_list):
		final_value_max_constrain = False
		n_jet = t1.n_jet
		n_bjet = t1.n_bjet
		if n_jet <=4:
			final_value.append(n_jet_bjet_dic["(%s,%s)"%(n_jet,n_bjet)][0])
		else:
			final_value.append(n_jet_bjet_dic["(>4,n)"][0])

	elif path == "n_bjet2" and ("n_bjet2" not in leaf_name_list):
		final_value_max_constrain = False
		tmp_n_bjet = 0
		for i in range(len(jet_pt_vector)):
			if jet_pt_vector[i] > 20 and jet_pt_vector[i] < 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i] and jet_CSVv2_vector[i] > 0.4941:
				tmp_n_bjet += 1
		final_value.append(tmp_n_bjet)

	elif path == "n_fjet1" and ("n_fjet1" not in leaf_name_list):
		final_value_max_constrain = False
		tmp_n_fjet = 0
		for i in range(len(jet_pt_vector)):
			if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])>2.4 and fabs(jet_eta_vector[i])<5.2 and jet_ID_vector[i]:
				tmp_n_fjet += 1
		final_value.append(tmp_n_fjet)

	elif path == "n_fjet2" and ("n_fjet2" not in leaf_name_list):
		final_value_max_constrain = False
		tmp_n_fjet = 0
		for i in range(len(jet_pt_vector)):
			if jet_pt_vector[i] > 40 and fabs(jet_eta_vector[i])>2.4 and fabs(jet_eta_vector[i])<5.2 and jet_ID_vector[i]:
				tmp_n_fjet += 1
		final_value.append(tmp_n_fjet)

	elif path == "jet_leading_pt" and ("jet_leading_pt" not in leaf_name_list):
		tmp_value = 0
		if leading_jet_id >= 0:
			tmp_value = jet_pt_vector[leading_jet_id]
			final_value.append(tmp_value)

	elif path == "jet_leading_eta" and ("jet_leading_eta" not in leaf_name_list):
		tmp_value = 0
		if leading_jet_id >= 0:
			tmp_value = jet_eta_vector[leading_jet_id]
			final_value.append(tmp_value)

	elif path == "jet_leading_phi" and ("jet_leading_phi" not in leaf_name_list):
		tmp_value = 0
		if leading_jet_id >= 0:
			tmp_value = jet_phi_vector[leading_jet_id]
			final_value.append(tmp_value)

	elif path == "jet_leading_CSV" and ("jet_leading_CSV" not in leaf_name_list):
		tmp_value = 0
		if leading_jet_id >= 0:
			tmp_value = jet_CSVv2_vector[leading_jet_id]
			final_value.append(tmp_value)

	elif path == "jet_sub_leading_pt" and ("jet_sub_leading_pt" not in leaf_name_list):
		tmp_value = 0
		if sub_leading_jet_id >= 0:
			tmp_value = jet_pt_vector[sub_leading_jet_id]
			final_value.append(tmp_value)

	elif path == "jet_sub_leading_eta" and ("jet_sub_leading_eta" not in leaf_name_list):
		tmp_value = 0
		if sub_leading_jet_id >= 0:
			tmp_value = jet_eta_vector[sub_leading_jet_id]
			final_value.append(tmp_value)

	elif path == "jet_sub_leading_phi" and ("jet_sub_leading_phi" not in leaf_name_list):
		tmp_value = 0
		if sub_leading_jet_id >= 0:
			tmp_value = jet_phi_vector[sub_leading_jet_id]
			final_value.append(tmp_value)

	elif path == "jet_sub_leading_CSV" and ("jet_sub_leading_CSV" not in leaf_name_list):
		tmp_value = 0
		if sub_leading_jet_id >= 0:
			tmp_value = jet_CSVv2_vector[sub_leading_jet_id]
			final_value.append(tmp_value)

	elif (path == "HT" and ("HT" not in leaf_name_list) ) or (path == "HT_log" and ("HT_log" not in leaf_name_list) ):
		tmp_HT = 0
		for i in range(len(jet_pt_vector)):
			if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
				tmp_HT += jet_pt_vector[i]
		#if tmp_HT == 0:return
		final_value.append(tmp_HT)
	elif (path == "sys_HT" and ("sys_HT" not in leaf_name_list) ) or (path == "sys_HT_log" and ("sys_HT_log" not in leaf_name_list) ):
		tmp_HT = 0
		for i in range(len(jet_pt_vector)):
			if jet_pt_vector[i] > 30 and fabs(jet_eta_vector[i])<2.4 and jet_ID_vector[i]:
				tmp_HT += jet_pt_vector[i]
		tmp_HT += t1.leading_pt + t1.sub_leading_pt
		#if tmp_HT == 0:return
		final_value.append(tmp_HT)
	elif path == "n_stat" and ("n_stat" not in leaf_name_list):
		final_value.append(0.5)
	else:
		exec 'tmp_value = t1.%s'%(value_dic_s.branch_name)
		final_value.append(tmp_value)

	return final_value, final_value_max_constrain

class ShowProcess():
	i = 0
	max_steps = 0
	max_arrow = 50
	step_length = 1
	pre_percent = -1

	def __init__(self, max_steps, print_enable = True):
		self.max_steps = max_steps
		self.i = 0
		self.pre_percent = -1
		self.print_enable = print_enable

	def show_process(self, i=None):
		if i is not None:
			self.i = i
		else:
			self.i += 1
		if not self.print_enable:return
		if self.step_length > 1:
			if (self.max_steps > 100):
				if (not int(self.i) % int(float(self.max_steps)/float(self.step_length)) == 0):return
		percent = int(self.i * 100.0 / self.max_steps)
		if self.pre_percent == percent:return
		self.pre_percent = percent
		num_arrow = int(self.i * self.max_arrow / self.max_steps)
		num_line = self.max_arrow - num_arrow
		process_bar = '[' + '>' * num_arrow + '-' * num_line + ']' + '%2d' % percent + '%' + '\r'
		sys.stdout.write(process_bar)
		sys.stdout.flush()

	def close(self, words='done'):
		if self.print_enable: print "\n%s"%(words)
		self.i = 0

class my_TMVA_reader():
	def __init__(self, label, weight_file):
		self.leading_pt = array( 'f', [0] )
		self.deltaR_ll = array( 'f', [0] )
		self.M_ll = array( 'f', [0] )
		self.MET_pt = array( 'f', [0] )
		self.n_jet = array( 'f', [0] )
	
		self.TMVA_reader = ROOT.TMVA.Reader()
		self.TMVA_reader.AddVariable("leading_pt",	self.leading_pt)
		self.TMVA_reader.AddVariable("deltaR_ll",	self.deltaR_ll)
		self.TMVA_reader.AddVariable("M_ll",	self.M_ll)
		self.TMVA_reader.AddVariable("MET_FinalCollection_Pt",	self.MET_pt)
		self.TMVA_reader.AddVariable("n_jet",	self.n_jet)

		self.TMVA_reader.BookMVA(label,weight_file)
		self.label = label

	def update_variables(self, variable_dic):
		self.leading_pt[0] = variable_dic["leading_pt"][0][0]
		self.deltaR_ll[0] = variable_dic["deltaR_ll"][0][0]
		self.M_ll[0] = variable_dic["M_ll"][0][0]
		self.MET_pt[0] = variable_dic["MET_pt"][0][0]
		self.n_jet[0] = variable_dic["n_jet"][0][0]

	def evaluateMVA(self):
		return self.TMVA_reader.EvaluateMVA(self.label)

	def close(self):
		del self.TMVA_reader

class sample_t():
	def __init__(self, label):
		self.label = label
		self.isFromRoot = True
		self.input_file = ""
		self.isData = False
		self.isFake = False
		self.isSS = False
		self.useToNorm = False
		self.lumi = 0.0
		self.Xsection = 0.0
		self.N_total =  0.0
		self.Raw_total = 0.0
		self.N_norm = 1.0
		self.Norm_Factor = 1
		self.Fill_color = 50
		self.weight_factor = 1.0
		self.hist = {}
		self.isUpdate = True

	def print_info(self):
		print "label : %s"%(self.label)
		print "isFromRoot : %s"%(self.isFromRoot)
		print "input_file : %s"%(self.input_file)
		print "isData : %s"%(self.isData)
		print "isFake : %s"%(self.isFake)
		print "isSS : %s"%(self.isSS)
		print "useToNorm : %s"%(self.useToNorm)
		print "lumi : %s"%(self.lumi)
		print "Xsection : %s"%(self.Xsection)
		print "N_total : %s"%(self.N_total)
		print "Raw_total : %s"%(self.Raw_total)
		print "N_norm : %s"%(self.N_norm)
		print "Norm_Factor : %s"%(self.Norm_Factor)
		print "Fill_color : %s"%(self.Fill_color)
		print "weight_factor : %s"%(self.weight_factor)
		print "hist : %s"%(self.hist)
		print "isUpdate : %s"%(self.isUpdate)

class value_t():
	def __init__(self, label):
		self.label = label
		self.branch_name = label
		self.hist_name = "default name"
		self.hist_title = "Idefault title"
		self.use_array = False
		self.PU_reweight = True
		self.hist_para = []
		self.y_axis = ["null","null"]
		self.x_label = ['label x',0.1]
		self.y_label = ['label y',0.05]
		self.x_log = False
		self.y_log = False
		self.lenend = {
			"useLegend":True,
			"position":[],
			}

	def print_info(self):
		print "label : %s"%(self.label)
		print "branch_name : %s"%(self.branch_name)
		print "hist_name : %s"%(self.hist_name)
		print "hist_title : %s"%(self.hist_title)
		print "use_array : %s"%(self.use_array)
		print "PU_reweight : %s"%(self.PU_reweight)
		print "hist_para : %s"%(self.hist_para)
		print "y_axis : %s"%(self.y_axis)
		print "x_label : %s"%(self.x_label)
		print "y_label : %s"%(self.y_label)
		print "x_log : %s"%(self.x_log)
		print "y_log : %s"%(self.y_log)
		print "lenend : %s"%(self.lenend)
