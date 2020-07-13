from params import *

class sample_t():
	def __init__(self, sample, input_file):
		self.name = sample
		self.isFromRoot = True
		self.input_file = input_file
		self.Xsection = 0.0
		self.N_total =  0.0
		self.Raw_total = 0.0
		self.Need_norm = False
		self.Norm_Factor = 1
		self.weight_factor = 1.0
		self.hist_name_first = ""
		self.hist_name_list = []
		self.hist = collections.OrderedDict()

	def print_info(self):
		print "name : %s"%(self.name)
		print "isFromRoot : %s"%(self.isFromRoot)
		print "input_file : %s"%(self.input_file)
		print "Xsection : %s"%(self.Xsection)
		print "N_total : %s"%(self.N_total)
		print "Raw_total : %s"%(self.Raw_total)
		print "Need_norm : %s"%(self.Need_norm)
		print "Norm_Factor : %s"%(self.Norm_Factor)
		print "weight_factor : %s"%(self.weight_factor)
		print "hist_name_first : %s"%(self.hist_name_first)
		print "hist_name_list : %s"%(self.hist_name_list)
		print "hist : %s"%(self.hist)

	def read_hist(self):
		tmp_tf = ROOT.TFile(self.input_file)
		#print self.input_file
		for i_hist in self.hist_name_list:
			tmp_hist_name = ("emuhist/"+self.hist_name_first+"_"+i_hist)
			self.hist[i_hist] = tmp_tf.Get(tmp_hist_name).Clone(i_hist)
		tmp_tf.Close()

	def norm_hist(self, lumi):
		if self.Need_norm:
			self.Norm_Factor = lumi * self.Xsection / self.Raw_total
		else :
			self.Norm_Factor = 1.0

		for i_hist in self.hist:
			self.hist[i_hist].Scale(self.Norm_Factor * self.weight_factor)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class plot_t():
	def __init__(self, sys_type, para_c, year = "0000"):
		self.sys_type = sys_type
		self.sample_data = collections.OrderedDict()
		self.sample_bkg = collections.OrderedDict()
		self.sample_sig = collections.OrderedDict()
		self.use_data = False
		self.use_bkg = False
		self.use_sig = False
		self.hist_data = collections.OrderedDict()
		self.hist_bkg = collections.OrderedDict()
		self.hist_sig = collections.OrderedDict()
		self.para_data = collections.OrderedDict()
		self.para_bkg = collections.OrderedDict()
		self.para_sig = collections.OrderedDict()
		self.para = para_c
		self.lumi = self.para.lumi
		self.year = year
		self.hist_name_list = []

	def print_info(self):
		print "sys_type : %s"%(self.sys_type)
		print "lumi : %s"%(self.lumi)

	def prepare_hist(self):
		self.read_hist()
		self.set_sys()
		self.norm_hist()
		self.make_hist()

	def read_hist(self):
		if self.use_data:
			for plot_name in self.sample_data:
				for sample_name in self.sample_data[plot_name]:
					self.sample_data[plot_name][sample_name].read_hist()
		if self.use_bkg:
			for plot_name in self.sample_bkg:
				for sample_name in self.sample_bkg[plot_name]:
					self.sample_bkg[plot_name][sample_name].read_hist()
		if self.use_sig:
			for plot_name in self.sample_sig:
				for sample_name in self.sample_sig[plot_name]:
					self.sample_sig[plot_name][sample_name].read_hist()

	def norm_hist(self):
		global_sample = collections.OrderedDict()
		if self.use_bkg:
			for plot_name in self.sample_bkg:
				for sample_name in self.sample_bkg[plot_name]:
					self.sample_bkg[plot_name][sample_name].norm_hist(self.lumi)
		if self.use_sig:
			for plot_name in self.sample_sig:
				for sample_name in self.sample_sig[plot_name]:
					self.sample_sig[plot_name][sample_name].norm_hist(self.lumi)

	def set_sys(self):

		if self.use_bkg:
			if self.sys_type == "xs_ttbar_u":
				self.sample_bkg["TTbar"]["_ttbar2l2u"].Xsection *= (1.0 + 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M500to800"].Xsection *= (1.0 + 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M800to1200"].Xsection *= (1.0 + 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M1200to1800"].Xsection *= (1.0 + 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M1800toInf"].Xsection *= (1.0 + 0.05)
			if self.sys_type == "xs_ttbar_d":
				self.sample_bkg["TTbar"]["_ttbar2l2u"].Xsection *= (1.0 - 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M500to800"].Xsection *= (1.0 - 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M800to1200"].Xsection *= (1.0 - 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M1200to1800"].Xsection *= (1.0 - 0.05)
				self.sample_bkg["TTbar"]["_ttbar2l2u_M1800toInf"].Xsection *= (1.0 - 0.05)
			if self.sys_type == "xs_ww_u":
				self.sample_bkg["Di_boson"]["_WW2l2u"].Xsection *= (1.0 + 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M200to600"].Xsection *= (1.0 + 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M600to1200"].Xsection *= (1.0 + 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M1200to2500"].Xsection *= (1.0 + 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M2500toInf"].Xsection *= (1.0 + 0.03)
			if self.sys_type == "xs_ww_d":
				self.sample_bkg["Di_boson"]["_WW2l2u"].Xsection *= (1.0 - 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M200to600"].Xsection *= (1.0 - 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M600to1200"].Xsection *= (1.0 - 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M1200to2500"].Xsection *= (1.0 - 0.03)
				self.sample_bkg["Di_boson"]["_WW2l2u_M2500toInf"].Xsection *= (1.0 - 0.03)
			if self.sys_type == "xs_st_u":
				self.sample_bkg["ST"]["_ST"].Xsection *= (1.0 + 0.05)
			if self.sys_type == "xs_st_d":
				self.sample_bkg["ST"]["_ST"].Xsection *= (1.0 - 0.05)
			if self.sys_type == "xs_dy_u":
				self.sample_bkg["Z"]["_DYToLL"].Xsection *= (1.0 + 0.02)
			if self.sys_type == "xs_dy_d":
				self.sample_bkg["Z"]["_DYToLL"].Xsection *= (1.0 - 0.02)
			if self.sys_type == "xs_wz_u":
				self.sample_bkg["Di_boson"]["_WZTo2L2Q"].Xsection *= (1.0 + 0.04)
				self.sample_bkg["Di_boson"]["_WZTo3LNu"].Xsection *= (1.0 + 0.04)
			if self.sys_type == "xs_wz_d":
				self.sample_bkg["Di_boson"]["_WZTo2L2Q"].Xsection *= (1.0 - 0.04)
				self.sample_bkg["Di_boson"]["_WZTo3LNu"].Xsection *= (1.0 - 0.04)
			if self.sys_type == "xs_zz_u":
				self.sample_bkg["Di_boson"]["_ZZTo2L2Nu"].Xsection *= (1.0 + 0.04)
				self.sample_bkg["Di_boson"]["_ZZTo2L2Q"].Xsection *= (1.0 + 0.04)
				self.sample_bkg["Di_boson"]["_ZZTo4L"].Xsection *= (1.0 + 0.04)
			if self.sys_type == "xs_zz_d":
				self.sample_bkg["Di_boson"]["_ZZTo2L2Nu"].Xsection *= (1.0 - 0.04)
				self.sample_bkg["Di_boson"]["_ZZTo2L2Q"].Xsection *= (1.0 - 0.04)
				self.sample_bkg["Di_boson"]["_ZZTo4L"].Xsection *= (1.0 - 0.04)

		if self.sys_type == "lumi_u":
				self.lumi *= (1.0 + self.para.lumi_sys)
		if self.sys_type == "lumi_d":
				self.lumi *= (1.0 - self.para.lumi_sys)

	def make_hist(self):
		if self.use_data:
			for plot_name in self.sample_data:
				if plot_name not in self.hist_data:
					self.hist_data[plot_name] =	collections.OrderedDict()	
				for sample_name in self.sample_data[plot_name]:
					tmp_sample = self.sample_data[plot_name][sample_name]
					for hist_name in tmp_sample.hist:
						if hist_name in self.hist_data[plot_name]:
							self.hist_data[plot_name][hist_name].Add(self.hist_data[plot_name][hist_name], tmp_sample.hist[hist_name], 1, 1)
						else:
							self.hist_data[plot_name][hist_name] = tmp_sample.hist[hist_name].Clone(tmp_sample.hist[hist_name].GetName()+"_plot")

			for plot_name in self.hist_data:
				for hist_name in self.hist_data[plot_name]:
					self.hist_data[plot_name][hist_name].Scale(self.para_data[plot_name]["weight_factor"])

		if self.use_bkg:
			for plot_name in self.sample_bkg:
				if plot_name not in self.hist_bkg:
					self.hist_bkg[plot_name] = collections.OrderedDict()
				for sample_name in self.sample_bkg[plot_name]:
					tmp_sample = self.sample_bkg[plot_name][sample_name]
					for hist_name in tmp_sample.hist:
						if hist_name in self.hist_bkg[plot_name]:
							self.hist_bkg[plot_name][hist_name].Add(self.hist_bkg[plot_name][hist_name], tmp_sample.hist[hist_name], 1, 1)
						else:
							self.hist_bkg[plot_name][hist_name] = tmp_sample.hist[hist_name].Clone(tmp_sample.hist[hist_name].GetName()+"_plot")

			for plot_name in self.hist_bkg:
				for hist_name in self.hist_bkg[plot_name]:
					self.hist_bkg[plot_name][hist_name].Scale(self.para_bkg[plot_name]["weight_factor"])
					
		if self.use_sig:
			for plot_name in self.sample_sig:
				if plot_name not in self.hist_sig:
					self.hist_sig[plot_name] =	collections.OrderedDict()
				for sample_name in self.sample_sig[plot_name]:
					tmp_sample = self.sample_sig[plot_name][sample_name]
					for hist_name in tmp_sample.hist:
						if hist_name in self.hist_sig[plot_name]:
							self.hist_sig[plot_name][hist_name].Add(self.hist_sig[plot_name][hist_name], tmp_sample.hist[hist_name], 1, 1)
						else:
							self.hist_sig[plot_name][hist_name] = tmp_sample.hist[hist_name].Clone(tmp_sample.hist[hist_name].GetName()+"_plot")

			for plot_name in self.hist_sig:
				for hist_name in self.hist_sig[plot_name]:
					self.hist_sig[plot_name][hist_name].Scale(self.para_sig[plot_name]["weight_factor"])

	def init_sample(self, input_dir, hist_name_list, ref_sys_type):
		self.hist_name_list = hist_name_list
		if self.use_data:
			self.sample_data["Data"] = collections.OrderedDict()
			self.para_data["Data"] = collections.OrderedDict()
			self.para_data["Data"]["weight_factor"] = 1
			tmp_sample = sample_t("data", os.path.join(input_dir, "data_emu.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			self.sample_data["Data"][tmp_sample.name] = tmp_sample

		if self.use_bkg:
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~ TTbar ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			self.sample_bkg["TTbar"] = collections.OrderedDict()
			self.para_bkg["TTbar"] = collections.OrderedDict()
			self.para_bkg["TTbar"]["weight_factor"] = 1

			tmp_sample = sample_t("_ttbar2l2u", os.path.join(input_dir, "ttbar2l2u_Mall.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u
			tmp_sample.Need_norm = True
			self.sample_bkg["TTbar"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_ttbar2l2u_M500to800", os.path.join(input_dir, "ttbar2l2u_M500to800.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M500to800
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M500to800
			tmp_sample.Need_norm = True
			self.sample_bkg["TTbar"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_ttbar2l2u_M800to1200", os.path.join(input_dir, "ttbar2l2u_M800to1200.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M800to1200
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M800to1200
			tmp_sample.Need_norm = True
			self.sample_bkg["TTbar"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_ttbar2l2u_M1200to1800", os.path.join(input_dir, "ttbar2l2u_M1200to1800.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M1200to1800
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M1200to1800
			tmp_sample.Need_norm = True
			self.sample_bkg["TTbar"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_ttbar2l2u_M1800toInf", os.path.join(input_dir, "ttbar2l2u_M1800toInf.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M1800toInf
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M1800toInf
			tmp_sample.Need_norm = True
			self.sample_bkg["TTbar"][tmp_sample.name] = tmp_sample

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~ Z ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			self.sample_bkg["Z"] = collections.OrderedDict()
			self.para_bkg["Z"] = collections.OrderedDict()
			self.para_bkg["Z"]["weight_factor"] = 1

			tmp_sample = sample_t("_DYToLL", os.path.join(input_dir, "DYToLL_all.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_DYToLL
			tmp_sample.Raw_total = self.para.nrawevent_DYToLL
			tmp_sample.Need_norm = True
			self.sample_bkg["Z"][tmp_sample.name] = tmp_sample

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~ ST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			self.sample_bkg["ST"] = collections.OrderedDict()
			self.para_bkg["ST"] = collections.OrderedDict()
			self.para_bkg["ST"]["weight_factor"] = 1

			tmp_sample = sample_t("_ST", os.path.join(input_dir, "ST.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ST
			tmp_sample.Raw_total = self.para.nrawevent_ST
			tmp_sample.Need_norm = True
			self.sample_bkg["ST"][tmp_sample.name] = tmp_sample

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~ Di_boson ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			self.sample_bkg["Di_boson"] = collections.OrderedDict()
			self.para_bkg["Di_boson"] = collections.OrderedDict()
			self.para_bkg["Di_boson"]["weight_factor"] = 1

			tmp_sample = sample_t("_WW2l2u", os.path.join(input_dir, "WW2l2u.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_WW2l2u_M200to600", os.path.join(input_dir, "WW2l2u_M200to600.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M200to600
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M200to600
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_WW2l2u_M600to1200", os.path.join(input_dir, "WW2l2u_M600to1200.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M600to1200
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M600to1200
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_WW2l2u_M1200to2500", os.path.join(input_dir, "WW2l2u_M1200to2500.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M1200to2500
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M1200to2500
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_WW2l2u_M2500toInf", os.path.join(input_dir, "WW2l2u_M2500toInf.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M2500toInf
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M2500toInf
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_WZTo2L2Q", os.path.join(input_dir, "WZTo2L2Q.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WZTo2L2Q
			tmp_sample.Raw_total = self.para.nrawevent_WZTo2L2Q
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_WZTo3LNu", os.path.join(input_dir, "WZTo3LNu.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WZTo3LNu
			tmp_sample.Raw_total = self.para.nrawevent_WZTo3LNu
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_ZZTo2L2Nu", os.path.join(input_dir, "ZZTo2L2Nu.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo2L2Nu
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo2L2Nu
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_ZZTo2L2Q", os.path.join(input_dir, "ZZTo2L2Q.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo2L2Q
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo2L2Q
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("_ZZTo4L", os.path.join(input_dir, "ZZTo4L.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo4L
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo4L
			tmp_sample.Need_norm = True
			self.sample_bkg["Di_boson"][tmp_sample.name] = tmp_sample

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~ QCD_jet ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~ QCD_jet ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~ QCD_jet ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			qcd_ref_sys_type = "nominal"
			self.sample_bkg["QCD_jet"] = collections.OrderedDict()
			self.para_bkg["QCD_jet"] = collections.OrderedDict()
			self.para_bkg["QCD_jet"]["weight_factor"] = 1
			if self.sys_type=="qcd_u":
				self.para_bkg["QCD_jet"]["weight_factor"] = 1+0.5
			if self.sys_type=="qcd_d":
				self.para_bkg["QCD_jet"]["weight_factor"] = 1-0.5

			tmp_sample = sample_t("fke_data", os.path.join(input_dir, "fke_data_emu.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ttbar2l2u", os.path.join(input_dir, "fke_ttbar2l2u_Mall.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ttbar2l2u_M500to800", os.path.join(input_dir, "fke_ttbar2l2u_M500to800.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M500to800
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M500to800
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ttbar2l2u_M800to1200", os.path.join(input_dir, "fke_ttbar2l2u_M800to1200.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M800to1200
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M800to1200
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ttbar2l2u_M1200to1800", os.path.join(input_dir, "fke_ttbar2l2u_M1200to1800.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M1200to1800
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M1200to1800
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ttbar2l2u_M1800toInf", os.path.join(input_dir, "fke_ttbar2l2u_M1800toInf.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M1800toInf
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M1800toInf
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_DYToLL", os.path.join(input_dir, "fke_DYToLL_all.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_DYToLL
			tmp_sample.Raw_total = self.para.nrawevent_DYToLL
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ST", os.path.join(input_dir, "fke_ST.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ST
			tmp_sample.Raw_total = self.para.nrawevent_ST
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_WW2l2u", os.path.join(input_dir, "fke_WW2l2u.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_WW2l2u_M200to600", os.path.join(input_dir, "fke_WW2l2u_M200to600.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M200to600
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M200to600
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_WW2l2u_M600to1200", os.path.join(input_dir, "fke_WW2l2u_M600to1200.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M600to1200
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M600to1200
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_WW2l2u_M1200to2500", os.path.join(input_dir, "fke_WW2l2u_M1200to2500.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M1200to2500
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M1200to2500
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_WW2l2u_M2500toInf", os.path.join(input_dir, "fke_WW2l2u_M2500toInf.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M2500toInf
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M2500toInf
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_WZTo2L2Q", os.path.join(input_dir, "fke_WZTo2L2Q.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WZTo2L2Q
			tmp_sample.Raw_total = self.para.nrawevent_WZTo2L2Q
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_WZTo3LNu", os.path.join(input_dir, "fke_WZTo3LNu.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WZTo3LNu
			tmp_sample.Raw_total = self.para.nrawevent_WZTo3LNu
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ZZTo2L2Nu", os.path.join(input_dir, "fke_ZZTo2L2Nu.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo2L2Nu
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo2L2Nu
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ZZTo2L2Q", os.path.join(input_dir, "fke_ZZTo2L2Q.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo2L2Q
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo2L2Q
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fke_ZZTo4L", os.path.join(input_dir, "fke_ZZTo4L.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo4L
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo4L
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			#########################################################################
			#########################################################################

			tmp_sample = sample_t("fkm_data", os.path.join(input_dir, "fkm_data_emu.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ttbar2l2u", os.path.join(input_dir, "fkm_ttbar2l2u_Mall.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ttbar2l2u_M500to800", os.path.join(input_dir, "fkm_ttbar2l2u_M500to800.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M500to800
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M500to800
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ttbar2l2u_M800to1200", os.path.join(input_dir, "fkm_ttbar2l2u_M800to1200.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M800to1200
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M800to1200
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ttbar2l2u_M1200to1800", os.path.join(input_dir, "fkm_ttbar2l2u_M1200to1800.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M1200to1800
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M1200to1800
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ttbar2l2u_M1800toInf", os.path.join(input_dir, "fkm_ttbar2l2u_M1800toInf.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ttbar2l2u_M1800toInf
			tmp_sample.Raw_total = self.para.nrawevent_ttbar2l2u_M1800toInf
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_DYToLL", os.path.join(input_dir, "fkm_DYToLL_all.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_DYToLL
			tmp_sample.Raw_total = self.para.nrawevent_DYToLL
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ST", os.path.join(input_dir, "fkm_ST.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ST
			tmp_sample.Raw_total = self.para.nrawevent_ST
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_WW2l2u", os.path.join(input_dir, "fkm_WW2l2u.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_WW2l2u_M200to600", os.path.join(input_dir, "fkm_WW2l2u_M200to600.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M200to600
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M200to600
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_WW2l2u_M600to1200", os.path.join(input_dir, "fkm_WW2l2u_M600to1200.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M600to1200
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M600to1200
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_WW2l2u_M1200to2500", os.path.join(input_dir, "fkm_WW2l2u_M1200to2500.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M1200to2500
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M1200to2500
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_WW2l2u_M2500toInf", os.path.join(input_dir, "fkm_WW2l2u_M2500toInf.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WW2l2u_M2500toInf
			tmp_sample.Raw_total = self.para.nrawevent_WW2l2u_M2500toInf
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_WZTo2L2Q", os.path.join(input_dir, "fkm_WZTo2L2Q.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WZTo2L2Q
			tmp_sample.Raw_total = self.para.nrawevent_WZTo2L2Q
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_WZTo3LNu", os.path.join(input_dir, "fkm_WZTo3LNu.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_WZTo3LNu
			tmp_sample.Raw_total = self.para.nrawevent_WZTo3LNu
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ZZTo2L2Nu", os.path.join(input_dir, "fkm_ZZTo2L2Nu.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo2L2Nu
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo2L2Nu
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ZZTo2L2Q", os.path.join(input_dir, "fkm_ZZTo2L2Q.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo2L2Q
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo2L2Q
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

			tmp_sample = sample_t("fkm_ZZTo4L", os.path.join(input_dir, "fkm_ZZTo4L.root"))
			tmp_sample.hist_name_first = qcd_ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZZTo4L
			tmp_sample.Raw_total = self.para.nrawevent_ZZTo4L
			tmp_sample.Need_norm = True
			tmp_sample.weight_factor = -1.0
			self.sample_bkg["QCD_jet"][tmp_sample.name] = tmp_sample

		if self.use_sig:
			self.sample_sig["ZPrimeToEMu_M1000"] = collections.OrderedDict()
			self.para_sig["ZPrimeToEMu_M1000"] = collections.OrderedDict()
			self.para_sig["ZPrimeToEMu_M1000"]["weight_factor"] = 1

			tmp_sample = sample_t("ZPrimeToEMu_M1000", os.path.join(input_dir, "ZPrimeToEMu_M1000.root"))
			tmp_sample.hist_name_first = ref_sys_type
			tmp_sample.hist_name_list = hist_name_list
			tmp_sample.Xsection = xsection_ZPrimeToEMu_M1000
			tmp_sample.Raw_total = self.para.nrawevent_ZPrimeToEMu_M1000
			tmp_sample.Need_norm = True
			self.sample_sig["ZPrimeToEMu_M1000"][tmp_sample.name] = tmp_sample


class final_plot_t():
	def __init__(self, input_plot_t, label = "0000"):
		self.sys_type = input_plot_t.sys_type
		self.use_data = input_plot_t.use_data
		self.use_bkg = input_plot_t.use_bkg
		self.use_sig = input_plot_t.use_sig
		self.hist_data = deepcopy(input_plot_t.hist_data)
		self.hist_bkg = deepcopy(input_plot_t.hist_bkg)
		self.hist_sig = deepcopy(input_plot_t.hist_sig)
		self.lumi = input_plot_t.lumi
		self.label = label
		self.year_list = [input_plot_t.year]
		self.hist_name_list = input_plot_t.hist_name_list

	def add_plot(self, input_plot_t):
		if self.sys_type != input_plot_t.sys_type:
			print ("Warning!!! self.sys_type(%s)!=input_plot_t.sys_type(%s)"%(self.sys_type, input_plot_t.sys_type) )
			return
		if self.use_data != input_plot_t.use_data:
			print ("Warning!!! self.use_data(%s)!=input_plot_t.use_data(%s)"%(self.use_data, input_plot_t.use_data) )
			return
		if self.use_bkg != input_plot_t.use_bkg:
			print ("Warning!!! self.use_bkg(%s)!=input_plot_t.use_bkg(%s)"%(self.use_bkg, input_plot_t.use_bkg) )
			return
		if self.use_sig != input_plot_t.use_sig:
			print ("Warning!!! self.use_sig(%s)!=input_plot_t.use_sig(%s)"%(self.use_sig, input_plot_t.use_sig) )
			return

		print ("\ncoping hist:")
		#showprocess = ShowProcess((len(self.hist_data) + len(self.hist_bkg) + len(self.hist_sig)) *len(self.hist_name_list))
		i_process = 1
		for plot_name in self.hist_data:
			for hist_name in self.hist_data[plot_name]:
				#showprocess.show_process(i_process)
				i_process+=1
				self.hist_data[plot_name][hist_name].Add(self.hist_data[plot_name][hist_name], input_plot_t.hist_data[plot_name][hist_name], 1, 1)
		for plot_name in self.hist_bkg:
			for hist_name in self.hist_bkg[plot_name]:
				#showprocess.show_process(i_process)
				i_process+=1
				self.hist_bkg[plot_name][hist_name].Add(self.hist_bkg[plot_name][hist_name], input_plot_t.hist_bkg[plot_name][hist_name], 1, 1)
		for plot_name in self.hist_sig:
			for hist_name in self.hist_sig[plot_name]:
				#showprocess.show_process(i_process)
				i_process+=1
				self.hist_sig[plot_name][hist_name].Add(self.hist_sig[plot_name][hist_name], input_plot_t.hist_sig[plot_name][hist_name], 1, 1)
		#showprocess.close("finish\n")

		self.year_list.append(input_plot_t.year)

	def get_hist_bkg(self, hist_name):
		tmp_hist = None
		if self.use_bkg:
			for plot_name in self.hist_bkg:
				if tmp_hist == None:
					tmp_hist = self.hist_bkg[plot_name][hist_name].Clone("hist_bkg_sum_out")
				else:
					tmp_hist.Add(tmp_hist, self.hist_bkg[plot_name][hist_name], 1, 1)
			return tmp_hist
