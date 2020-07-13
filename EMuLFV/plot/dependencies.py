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
import collections
from math import *

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gErrorIgnoreLevel=ROOT.kWarning


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

class plot_setting():
	def __init__(self, i_hist, hist_data, hist_bkg, hist_bkg_sys, hist_bkg_dic):
		self.i_hist = i_hist
		self.hist_data = hist_data
		self.hist_bkg = hist_bkg
		self.hist_bkg_sys = hist_bkg_sys
		self.hist_bkg_dic = hist_bkg_dic

		self.x_label = "X"
		self.x_log = False
		self.y_label = "Y"
		self.y_log = False

		self.is_binwidth_weighted = False

		self.lumi = 0

	def make_common_setting(self, i_hist):
		if i_hist == "ele_pt":
			self.x_log = True
			self.x_label = "p_{T}^{e} (GeV)"
			self.y_log = True
			self.y_label = "Event"
		elif i_hist == "ele_eta":
			self.x_log = False
			self.x_label = "#eta (electron)"
			self.y_log = False
			self.y_label = "Event"
		elif i_hist == "ele_phi":
			self.x_log = False
			self.x_label = "#phi (electron)"
			self.y_log = False
			self.y_label = "Event"
		elif i_hist == "mu_pt":
			self.x_log = True
			self.x_label = "p_{T}^{#mu} (GeV)"
			self.y_log = True
			self.y_label = "Event"
		elif i_hist == "mu_eta":
			self.x_log = False
			self.x_label = "#eta (muon)"
			self.y_log = False
			self.y_label = "Event"
		elif i_hist == "mu_phi":
			self.x_log = False
			self.x_label = "#phi (muon)"
			self.y_log = False
			self.y_label = "Event"
		elif i_hist == "M_emu":
			self.x_log = True
			self.x_label = "Mass (e#mu) (GeV)"
			self.y_log = True
			self.y_label = "Event"
			self.is_binwidth_weighted = True
		elif i_hist == "M_emu_Ml":
			self.x_log = True
			self.x_label = "Mass (e#mu) (GeV)"
			self.y_log = True
			self.y_label = "Event"
		elif i_hist == "pv_n":
			self.x_log = False
			self.x_label = "N_{vtx}"
			self.y_log = False
			self.y_label = "Event"
		else :
			self.x_log = False
			self.x_label = self.i_hist
			self.y_log = False
			self.y_label = "Event"

