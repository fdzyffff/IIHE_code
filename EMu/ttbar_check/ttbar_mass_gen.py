import os
import sys
import ROOT
from optparse import OptionParser
from input_ttbar_mass_gen import *

parser=OptionParser()
parser.add_option("-i","--input_file",dest="input_file",default="",type="str")
parser.add_option("-o","--output_file",dest="output_file",default="",type="str")
parser.add_option("-w","--weight_factor",dest="weight_factor",default=0,type="float")
parser.add_option("-c","--cut_value",dest="cut_value",default=0,type="float")
(options,args)=parser.parse_args()


def fill_hist(input_file, output_file, weight_factor, cut_value):
	global reskim_dic
	f_out = ROOT.TFile(output_file,"RECREATE")
	weight_lumi_1fb = weight_factor

	f1 = ROOT.TFile(input_file, "read")
	tmp_tree = f1.Get("IIHEAnalysis")
	print tmp_tree.GetEntries()
	process_bar = ShowProcess(tmp_tree.GetEntries())
	for event in tmp_tree:
		process_bar.show_process()
		vector_ele = []
		vector_muon = []
		vector_mc_pdgId = getattr(event, "mc_pdgId")
		vector_mc_pt = getattr(event, "mc_pt")
		vector_mc_eta = getattr(event, "mc_eta")
		vector_mc_phi = getattr(event, "mc_phi")
		for i in range(len(vector_mc_pdgId)):
			if abs(vector_mc_pdgId[i]) == 11:
				tmp_ele = ele_obj()
				tmp_ele.p4.SetPtEtaPhiM(vector_mc_pt[i],vector_mc_eta[i],vector_mc_phi[i],0.000511)
				if tmp_ele.pass_acc():
					vector_ele.append(tmp_ele)
			if abs(vector_mc_pdgId[i]) == 13:
				tmp_muon = muon_obj()
				tmp_muon.p4.SetPtEtaPhiM(vector_mc_pt[i], vector_mc_eta[i],vector_mc_phi[i],0.10566)
				if tmp_muon.pass_acc():
					vector_muon.append(tmp_muon)
		tmp_Z = Z_obj(vector_ele, vector_muon, cut_value)
		if tmp_Z.Find_ee():
			hist_dic["ee_M"].h1.Fill((tmp_Z.p4_leading + tmp_Z.p4_subleading).Mag() ,weight_lumi_1fb)
			hist_dic["ee_pt_leading"].h1.Fill(tmp_Z.p4_leading.Pt() ,weight_lumi_1fb)
			hist_dic["ee_pt_subleading"].h1.Fill(tmp_Z.p4_subleading.Pt() ,weight_lumi_1fb)
		if tmp_Z.Find_em():
			hist_dic["em_M"].h1.Fill((tmp_Z.p4_leading + tmp_Z.p4_subleading).Mag() ,weight_lumi_1fb)
			hist_dic["em_pt_leading"].h1.Fill(tmp_Z.p4_leading.Pt() ,weight_lumi_1fb)
			hist_dic["em_pt_subleading"].h1.Fill(tmp_Z.p4_subleading.Pt() ,weight_lumi_1fb)
		if tmp_Z.Find_mm():
			hist_dic["mm_M"].h1.Fill((tmp_Z.p4_leading + tmp_Z.p4_subleading).Mag() ,weight_lumi_1fb)
			hist_dic["mm_pt_leading"].h1.Fill(tmp_Z.p4_leading.Pt() ,weight_lumi_1fb)
			hist_dic["mm_pt_subleading"].h1.Fill(tmp_Z.p4_subleading.Pt() ,weight_lumi_1fb)
	process_bar.close()
	f1.Close()
	f_out.cd()
	for hist in hist_dic:
		hist_dic[hist].h1.Write()
	f_out.Close()

fill_hist(options.input_file, options.output_file, options.weight_factor, options.cut_value)
