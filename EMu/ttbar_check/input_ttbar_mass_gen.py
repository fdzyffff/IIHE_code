import os
import sys
import ROOT
from array import array
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-i","--input_file",dest="input_file",default="",type="str")
parser.add_option("-o","--output_file",dest="output_file",default="",type="str")
parser.add_option("-w","--weight_factor",dest="weight_factor",default=0,type="float")
parser.add_option("-c","--cut_value",dest="cut_value",default=0,type="float")
(options,args)=parser.parse_args()



ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

MYDIR=os.getcwd()

xsection_ttbar2l2u = 87.31
xsection_ttbar2l2u_M500to800 = 0.326
xsection_ttbar2l2u_M800to1200 = 0.0326
xsection_ttbar2l2u_M1200to1800 = 0.00305
xsection_ttbar2l2u_M1800toInf = 0.000174

xsection_WW2l2u = 12.178
xsection_WW2l2u_M200to600 = 1.39
xsection_WW2l2u_M600to1200 = 0.057
xsection_WW2l2u_M1200to2500 = 0.0036
xsection_WW2l2u_M2500toInf = 0.000054


nrawevent_ttbar2l2u = 8634992
nrawevent_ttbar2l2u_M500to800 = 755907
nrawevent_ttbar2l2u_M800to1200 = 199636
nrawevent_ttbar2l2u_M1200to1800 = 17507
nrawevent_ttbar2l2u_M1800toInf = 953

nrawevent_WW2l2u = 1992522
nrawevent_WW2l2u_M200to600 = 7922808
nrawevent_WW2l2u_M600to1200 = 567614
nrawevent_WW2l2u_M1200to2500 = 161573
nrawevent_WW2l2u_M2500toInf = 2349

file_root_dir_dic={
	    #[[n_event, cross_section, mass cut],[file_list]]
#"../MC/ST_antitop"		:[[],[]],
#"../MC/ST_top"			:[[],[]],
"MC/ttbar2l2u_Mall"		:[[nrawevent_ttbar2l2u , xsection_ttbar2l2u, 500],[]],
"MC/ttbar2l2u_M500to800"	:[[nrawevent_ttbar2l2u_M500to800 , xsection_ttbar2l2u_M500to800, 99999],[]],
"MC/ttbar2l2u_M800to1200"	:[[nrawevent_ttbar2l2u_M800to1200 , xsection_ttbar2l2u_M800to1200, 99999],[]],
"MC/ttbar2l2u_M1200to1800"	:[[nrawevent_ttbar2l2u_M1200to1800 , xsection_ttbar2l2u_M1200to1800, 99999],[]],
"MC/ttbar2l2u_M1800toInf"	:[[nrawevent_ttbar2l2u_M1800toInf , xsection_ttbar2l2u_M1800toInf, 99999],[]],
#"../MC/WW2l2u"			:[[],[]],
#"../MC/WW_M200to600"		:[[],[]],
#"../MC/WW_M600to1200"		:[[],[]],
#"../MC/WW_M1200to2500"		:[[],[]],
#"../MC/WW_M2500toInf"		:[[],[]],
#"../MC/WZ"			:[[],[]],
#"../MC/ZZ"			:[[],[]],

}

reskim_dic={}
hist_dic={}

class ShowProcess():
	i = 0
	max_steps = 0
	max_arrow = 50
	step_length = 1
	print_enable = True

	def __init__(self, max_steps):
		self.max_steps = max_steps
		self.i = 0

	def show_process(self, i=None):
		if i is not None:
			self.i = i
		else:
			self.i += 1
		if not self.print_enable:return
		if self.step_length > 1:
			if (self.max_steps > 100):
				if (not int(self.i) % int(float(self.max_steps)/float(self.step_length)) == 0):return
		num_arrow = int(self.i * self.max_arrow / self.max_steps)
		num_line = self.max_arrow - num_arrow
		percent = self.i * 100.0 / self.max_steps
		process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
					  + '%.2f' % percent + '%' + '\r'
		sys.stdout.write(process_bar)
		sys.stdout.flush()

	def close(self, words='done'):
		print ''
		print words
		self.i = 0

class my_hist():
	def __init__(self, name):
		self.h1 = ROOT.TH1F()
		self.name = "default"
		self.name = name

	def Init_hist(self):
		self.h1.SetName(self.name)
		self.h1.Sumw2()
		for i in range(1,self.h1.GetNbinsX()+1):
			self.h1.SetBinContent(i,0.0)

def make_hist():
	global hist_dic
	for hist in hist_dic:
		hist_dic[hist].Init_hist()

def my_walk_dir(my_dir,my_list):
    for tmp_file in os.listdir(my_dir):
        tmp_file_name = my_dir+'/'+tmp_file
        if os.path.isfile(tmp_file_name):
            if 'failed'         in tmp_file_name:continue
            if not '.root'      in tmp_file_name:continue
            #my_list.append(tmp_file_name[3:])
            my_list.append(tmp_file_name)
        else:
            my_walk_dir(tmp_file_name,my_list)
    return my_list

def make_dic(check_dir = ""):
    if check_dir != "":isCheck = True
    print "%s making file list %s"%("#"*15,"#"*15)
    n_total = 0
    for file_dir in file_root_dir_dic:
        tmp_name = ""
        for i in file_dir.split("/"):
            if (not i == ".") and (not i == ".."):
                tmp_name += "%s_"%(i)
        file_list = my_walk_dir(file_dir,[])
        file_list.sort()
        if check_dir == "":
            reskim_dic[tmp_name] = [file_root_dir_dic[file_dir][0],file_list]
        print "     %s : %d"%(file_dir,len(reskim_dic[tmp_name][1]))
        n_total += len(reskim_dic[tmp_name][1])
    print "     Total root files : %d"%(n_total)

class ele_obj():
	def __init__(self):
		self.p4 = ROOT.TLorentzVector()
		self.p4.SetPtEtaPhiM(0.1,0,0,0.1)

	def pass_acc(self):
		if abs(self.p4.Eta()) < 2.5 and self.p4.Et() > 35:
			return True
		return False

class muon_obj():
	def __init__(self):
		self.p4 = ROOT.TLorentzVector()
		self.p4.SetPtEtaPhiM(0.1,0,0,0.1)

	def pass_acc(self):
		if abs(self.p4.Eta()) < 2.4 and self.p4.Pt() > 53:
			return True
		return False

class Z_obj():
	def __init__(self, ele_in, muon_in, mass_cut_in):
		self.ele_list = []
		self.muon_list = []
		self.mass_cut = 99999999
		self.p4_leading = ROOT.TLorentzVector()
		self.p4_subleading = ROOT.TLorentzVector()
		self.ele_list = ele_in
		self.muon_list = muon_in
		self.mass_cut = mass_cut_in
	def Find_ee(self):
		if len(self.ele_list) < 2:
			return False
		tmp_leading_pt = -1
		tmp_subleading_pt = -1
		leading_flag = -1
		subleading_flag = -1
		for i in range(len(self.ele_list)):
			if self.ele_list[i].p4.Pt() > tmp_leading_pt:
				subleading_flag = leading_flag
				leading_flag = i
				tmp_subleading_pt = tmp_leading_pt	
				tmp_leading_pt = self.ele_list[i].p4.Pt()
			elif self.ele_list[i].p4.Pt() > tmp_subleading_pt:
				subleading_flag = i
				tmp_subleading_pt = self.ele_list[i].p4.Pt()
		self.p4_leading = self.ele_list[leading_flag].p4
		self.p4_subleading = self.ele_list[subleading_flag].p4
		if (self.p4_leading + self.p4_subleading).Mag() < self.mass_cut:
			return True
		return False
	def Find_mm(self):
		if len(self.muon_list) < 2:
			return False
		tmp_leading_pt = -1
		tmp_subleading_pt = -1
		leading_flag = -1
		subleading_flag = -1
		for i in range(len(self.muon_list)):
			if self.muon_list[i].p4.Pt() > tmp_leading_pt:
				subleading_flag = leading_flag
				leading_flag = i
				tmp_subleading_pt = tmp_leading_pt	
				tmp_leading_pt = self.muon_list[i].p4.Pt()
			elif self.muon_list[i].p4.Pt() > tmp_subleading_pt:
				subleading_flag = i
				tmp_subleading_pt = self.muon_list[i].p4.Pt()
		self.p4_leading = self.muon_list[leading_flag].p4
		self.p4_subleading = self.muon_list[subleading_flag].p4
		if (self.p4_leading + self.p4_subleading).Mag() < self.mass_cut:
			return True
		return False

	def Find_em(self):
		if len(self.muon_list) < 1 or len(self.ele_list) < 1:
			return False
		tmp_mass = -1
		ele_flag = -1
		muon_flag = -1
		for i in range(len(self.ele_list)):
			for j in range(len(self.muon_list)):
				if (self.ele_list[i].p4 + self.muon_list[j].p4).Mag() > tmp_mass:
					tmp_mass = (self.ele_list[i].p4 + self.muon_list[j].p4).Mag()
					ele_flag = i
					muon_flag = j
		if self.ele_list[ele_flag].p4.Pt() > self.muon_list[muon_flag].p4.Pt():
			self.p4_leading = self.ele_list[ele_flag].p4
			self.p4_subleading = self.muon_list[muon_flag].p4
		else:
			self.p4_leading = self.muon_list[muon_flag].p4
			self.p4_subleading = self.ele_list[ele_flag].p4
		if (self.p4_leading + self.p4_subleading).Mag() < self.mass_cut:
			return True
		return False

x_emu_new = array('f')
n_index = 0
x_emu_new.append(50)
for i in range(50,100,10):
        x_emu_new.append(i)
        n_index += 1
for i in range(100,200,20):
        x_emu_new.append(i)
        n_index += 1
for i in range(200,600,40):
        x_emu_new.append(i)
        n_index += 1
for i in range(600,1000,80):
        x_emu_new.append(i)
        n_index += 1
for i in range(1000,1600,150):
        x_emu_new.append(i)
        n_index += 1
for i in range(1600,2100,250):
        x_emu_new.append(i)
        n_index += 1
#for i in range(2100,4100,500):
#        x_emu_new.append(i)
#        n_index += 1
#for i in range(4100,5700,800):
#        x_emu_new.append(i)
#        n_index += 1
#for i in range(5700, 7900, 1100):
#        x_emu_new.append(i)
#        n_index += 1
#x_emu_new.append(7900)
#n_index += 1

x_pt = array('f')
for i in range(34,65):
	x_pt.append(1.12**i)


hist_dic = {}
hist_dic["em_M"] = my_hist("M_emu")
hist_dic["em_M"].h1 = ROOT.TH1F("x", "", n_index, x_emu_new)
hist_dic["em_pt_leading"] = my_hist("M_emu_pt_leading")
hist_dic["em_pt_leading"].h1 = ROOT.TH1F("x", "", 30, x_pt)
hist_dic["em_pt_subleading"] = my_hist("M_emu_pt_subleading")
hist_dic["em_pt_subleading"].h1 = ROOT.TH1F("x", "", 30, x_pt)

hist_dic["ee_M"] = my_hist("M_ee")
hist_dic["ee_M"].h1 = ROOT.TH1F("x", "", n_index, x_emu_new)
hist_dic["ee_pt_leading"] = my_hist("M_ee_pt_leading")
hist_dic["ee_pt_leading"].h1 = ROOT.TH1F("x", "", 30, x_pt)
hist_dic["ee_pt_subleading"] = my_hist("M_ee_pt_subleading")
hist_dic["ee_pt_subleading"].h1 = ROOT.TH1F("x", "", 30, x_pt)

hist_dic["mm_M"] = my_hist("M_mumu")
hist_dic["mm_M"].h1 = ROOT.TH1F("x", "", n_index, x_emu_new)
hist_dic["mm_pt_leading"] = my_hist("M_mumu_pt_leading")
hist_dic["mm_pt_leading"].h1 = ROOT.TH1F("x", "", 30, x_pt)
hist_dic["mm_pt_subleading"] = my_hist("M_mumu_pt_subleading")
hist_dic["mm_pt_subleading"].h1 = ROOT.TH1F("x", "", 30, x_pt)

make_hist()
