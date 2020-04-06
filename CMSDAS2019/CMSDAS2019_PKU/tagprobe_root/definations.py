import ROOT, array, os, sys, time, threading
from multiprocessing import Pool
from math import *

ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gErrorIgnoreLevel=ROOT.kError

### a C/C++ structure is required, to allow memory based access
ROOT.gROOT.ProcessLine(
"struct HEEPinfo_t {\
   UInt_t          pass_isEcalDriven;\
   UInt_t          pass_dEtaIn;\
   UInt_t          pass_dPhiIn;\
   UInt_t          pass_HoverE;\
   UInt_t          pass_SigmaIeIe;\
   UInt_t          pass_showershape;\
   UInt_t          pass_lostHits;\
   UInt_t          pass_dxy;\
   UInt_t          pass_isolEMHadDepth1;\
   UInt_t          pass_pTIso;\
};" );

const_m_el = 0.000511 ;
const_m_mu = 0.10566 ;


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

class electron_C():
	def __init__(self, charge):
		self.p4 = ROOT.TLorentzVector()
		self.p4_sc = ROOT.TLorentzVector()
		self.isTag = False
		self.pass_HEEPID = False
		self.sc_Eta = -99.99
		self.charge = charge
		self.region = 0

		self.pass_isEcalDriven = False
		self.pass_dEtaIn = False
		self.pass_dPhiIn = False
		self.pass_HoverE = False
		self.pass_SigmaIeIe = False
		self.pass_showershape = False
		self.pass_lostHits = False
		self.pass_dxy = False
		self.pass_isolEMHadDepth1 = False
		self.pass_pTIso = False

	def get_region(self):
		if   (abs(self.sc_Eta)<1.4442): self.region = 1
		elif (abs(self.sc_Eta)<1.566 ): self.region = 2
		elif (abs(self.sc_Eta)<2.5   ): self.region = 3
		else: self.region = 4

	def check_HEEPID(self, dPhiIn, Sieie, missingHits, dxyFirstPV, HOverE, caloEnergy, E1x5OverE5x5, E2x5OverE5x5, isolEMHadDepth1, IsolPtTrks, EcalDriven, dEtaIn, rho):
		eta = self.p4.Eta()
		Et = self.p4.Et()
		if   (self.region == 1): self.pass_HoverE = ( HOverE < (0.05 + 1.0/caloEnergy) )
		elif (self.region == 3): self.pass_HoverE = ( HOverE < (0.05 + (-0.4 + 0.4*abs(eta)) * rho / caloEnergy) )

		accept_E1x5OverE5x5 = ( E1x5OverE5x5 > 0.83 )
		accept_E2x5OverE5x5 = ( E2x5OverE5x5 > 0.94 )
		if   (self.region == 1): self.pass_showershape  = (accept_E1x5OverE5x5 or accept_E2x5OverE5x5)
		elif (self.region == 3): self.pass_showershape = True

		if   (self.region == 1): self.pass_SigmaIeIe = True
		elif (self.region == 3): self.pass_SigmaIeIe = ( Sieie < 0.03 )

		self.pass_isEcalDriven = ( int(EcalDriven) == 1 )

		if   (self.region == 1): 
			self.pass_dEtaIn = (abs(dEtaIn) < 0.004)
			self.pass_dPhiIn = (abs(dPhiIn) < 0.06 )
		elif (self.region == 3): 
			self.pass_dEtaIn = (abs(dEtaIn) < 0.006)
			self.pass_dPhiIn = (abs(dPhiIn) < 0.06 )

		if  (self.region == 1): 
			self.pass_isolEMHadDepth1 = ( isolEMHadDepth1 < (2.0+ 0.03*Et + 0.28*rho) )
		elif(self.region == 3): 
			if (Et<50.0):
				self.pass_isolEMHadDepth1 = ( isolEMHadDepth1 < (2.5 + (0.15+0.07*abs(eta))*rho) )
			else:
				self.pass_isolEMHadDepth1 = ( isolEMHadDepth1 < (2.5 + 0.03*(Et-50.0) + (0.15+0.07*abs(eta))*rho) )

		self.pass_pTIso = (IsolPtTrks < 5)
		self.pass_lostHits = ( int(missingHits) <= 1 )

		if   (self.region == 1):self.pass_dxy = ( abs(dxyFirstPV) < 0.02 )
		elif (self.region == 3):self.pass_dxy = ( abs(dxyFirstPV) < 0.05 )

		self.pass_HEEPID = self.pass_isEcalDriven \
						and self.pass_dEtaIn \
						and self.pass_dPhiIn \
						and self.pass_HoverE \
						and self.pass_SigmaIeIe \
						and self.pass_showershape \
						and self.pass_lostHits \
						and self.pass_dxy \
						and self.pass_isolEMHadDepth1 \
						and self.pass_pTIso

		
def my_walk_dir(my_dir,my_list,n_file = [-1]):
	for tmp_file in os.listdir(my_dir):
		if n_file[0] > 0 and len(my_list) >= n_file[0]:	return
		tmp_file_name = my_dir+'/'+tmp_file
		if os.path.isfile(tmp_file_name):
			if 'failed'         in tmp_file_name:continue
			if not '.root'      in tmp_file_name:continue
			my_list.append(tmp_file_name)
		else:
			my_walk_dir(tmp_file_name,my_list,n_file)
	return

class eff_hist():
	def __init__(self, hist_name, hist_in):
		self.h_denominator = hist_in.Clone("probe_d_%s"%(hist_name))
		self.h_numerator = hist_in.Clone("probe_n_%s"%(hist_name))
		self.hist_name = hist_name


	def Graph_Xerror0(self, graph_in):
		for i in range(0,graph_in.GetN()):
			graph_in.SetPointEXlow (i, 0)
			graph_in.SetPointEXhigh(i, 0)

	def draw(self, in_file_name):
		#ROOT.gROOT.SetBatch(ROOT.kFALSE)
		f_out = ROOT.TFile( in_file_name, 'READ')
		c1 = ROOT.TCanvas( 'c2', ' a Canvas ', 50,50,865,780 )
	
		h_denominator = ROOT.TH1F()
		h_numerator = ROOT.TH1F()
		h_denominator = f_out.Get( self.h_denominator.GetName() )
		h_numerator = f_out.Get( self.h_numerator.GetName() )
		gr1 = ROOT.TGraphAsymmErrors()
		gr1.SetName("gr_%s"%(self.hist_name))
		gr1.Divide(h_numerator,h_denominator,"cl=0.683 b(1,1) mode")
		self.Graph_Xerror0(gr1)
		gr1.SetMarkerStyle( 22 )
		gr1.SetMarkerColor(4)
		gr1.SetLineColor(4)
		gr1.GetYaxis().SetRangeUser(0.0, 1.1)
	
		gr1.Draw( 'AP' )
		c1.Update()
	
		out_hist_name = '%s.png'%(self.hist_name)
		print "Draw %s"%( out_hist_name )
		c1.Print( out_hist_name )

class reskim():
	def __init__(self, out_file_name):
		self.root_file_list = []
		self.print_enable = True
	
		self.tag_HEEPinfo = ROOT.HEEPinfo_t()
		self.tag_p4 = array.array( 'f', [0, 0, 0, 0] )
		self.tag_sc_Eta = array.array('f', [0] )
		self.tag_charge = array.array('i', [0] )
		self.tag_region = array.array('i', [0] )
		self.tag_pass_HEEPID = array.array('i', [0] )
		self.tag_trig_DouEle25_seededleg = array.array('i', [0, 0] )
		self.tag_trig_DouEle25_unseededleg = array.array('i', [0, 0] )
		self.tag_trig_Ele35WPTight = array.array('i', [0] )
		self.tag_trig_Ele32WPTight = array.array('i', [0] )

		self.probe_HEEPinfo = ROOT.HEEPinfo_t()
		self.probe_p4 = array.array( 'f', [0, 0, 0, 0] )
		self.probe_sc_Eta = array.array('f', [0] )
		self.probe_charge = array.array('i', [0] )
		self.probe_region = array.array('i', [0] )
		self.probe_pass_HEEPID = array.array('i', [0] )
		self.probe_trig_DouEle25_seededleg = array.array('i', [0, 0] )
		self.probe_trig_DouEle25_unseededleg = array.array('i', [0, 0] )
		self.probe_trig_Ele35WPTight = array.array('i', [0] )
		self.probe_trig_Ele32WPTight = array.array('i', [0] )
		
		
		self.f_out = ROOT.TFile( out_file_name, 'RECREATE' )
		
		self.tree_out = ROOT.TTree( 'TreeName', 'tree comments here' )
		self.tree_out.Branch( 'tag_HEEPinfo', self.tag_HEEPinfo  ,  'pass_isEcalDriven/I:pass_dEtaIn/I:pass_dPhiIn/I:pass_HoverE/I:pass_SigmaIeIe/I:pass	_showershape/I:pass_lostHits/I:pass_dxy/I:pass_isolEMHadDepth1/I:pass_pTIso/I' )
		self.tree_out.Branch( 'tag_p4'      , self.tag_p4        , 'tag_p4[4]/F')
		self.tree_out.Branch( 'tag_sc_Eta'  , self.tag_sc_Eta    , 'tag_sc_Eta/F' )
		self.tree_out.Branch( 'tag_charge'  , self.tag_charge    , 'tag_charge/I' )
		self.tree_out.Branch( 'tag_region'  , self.tag_region    , 'tag_region/I' )
		self.tree_out.Branch( 'tag_pass_HEEPID', self.tag_pass_HEEPID, 'tag_pass_HEEPID/I' )
		self.tree_out.Branch( 'tag_trig_DouEle25_unseededleg' , self.tag_trig_DouEle25_unseededleg, 'tag_trig_DouEle25_unseededleg[2]/I' )
		self.tree_out.Branch( 'tag_trig_DouEle25_seededleg' , self.tag_trig_DouEle25_seededleg, 'tag_trig_DouEle25_seededleg[2]/I' )
		self.tree_out.Branch( 'tag_trig_Ele32WPTight' , self.tag_trig_Ele32WPTight, 'tag_trig_Ele32WPTight/I' )
		self.tree_out.Branch( 'tag_trig_Ele35WPTight' , self.tag_trig_Ele35WPTight, 'tag_trig_Ele35WPTight/I' )

		self.tree_out.Branch( 'probe_HEEPinfo', self.probe_HEEPinfo,  'pass_isEcalDriven/I:pass_dEtaIn/I:pass_dPhiIn/I:pass_HoverE/I:pass_SigmaIeIe/I:pass	_showershape/I:pass_lostHits/I:pass_dxy/I:pass_isolEMHadDepth1/I:pass_pTIso/I' )
		self.tree_out.Branch( 'probe_p4'      , self.probe_p4        , 'probe_p4[4]/F')
		self.tree_out.Branch( 'probe_sc_Eta'  , self.probe_sc_Eta    , 'probe_sc_Eta/F' )
		self.tree_out.Branch( 'probe_charge'  , self.probe_charge    , 'probe_charge/I' )
		self.tree_out.Branch( 'probe_region'  , self.probe_region    , 'probe_region/I' )
		self.tree_out.Branch( 'probe_pass_HEEPID', self.probe_pass_HEEPID, 'probe_pass_HEEPID/I' )
		self.tree_out.Branch( 'probe_trig_DouEle25_seededleg' , self.probe_trig_DouEle25_seededleg, 'probe_trig_DouEle25_seededleg[2]/I' )
		self.tree_out.Branch( 'probe_trig_DouEle25_unseededleg' , self.probe_trig_DouEle25_unseededleg, 'probe_trig_DouEle25_unseededleg[2]/I' )
		self.tree_out.Branch( 'probe_trig_Ele32WPTight' , self.probe_trig_Ele32WPTight, 'probe_trig_Ele32WPTight/I' )
		self.tree_out.Branch( 'probe_trig_Ele35WPTight' , self.probe_trig_Ele35WPTight, 'probe_trig_Ele35WPTight/I' )

	def trig_match(self, vector_eta, vector_phi, obj_eta, obj_phi, deltaR = 0.1):
		obj_p4 = ROOT.TLorentzVector()
		obj_p4.SetPtEtaPhiM(100.0, obj_eta, obj_phi, 10.0)
		return self.trig_match(vector_eta, vector_phi, obj_p4, deltaR)

	def trig_match(self, vector_eta, vector_phi, obj_p4, phi, deltaR = 0.1):
		for iVector in range(len(vector_eta)):
			tmp_p4 = ROOT.TLorentzVector()
			tmp_p4.SetPtEtaPhiM(100.0, vector_eta[iVector], vector_phi[iVector], 10.0)
			if (tmp_p4.DeltaR(obj_p4) < deltaR ):
				return True
		return False

	def Fill_branch(self, tree_in):
		pre_time = time.time()
		tree_in.SetBranchStatus("*", 0)

		tree_in.SetBranchStatus('gsf_*', 1)
		tree_in.SetBranchStatus('ev_*', 1)
		tree_in.SetBranchStatus('trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_*', 1)
		tree_in.SetBranchStatus('trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_*', 1)
		tree_in.SetBranchStatus('trig_HLT_DoubleEle25_CaloIdL_MW_*', 1)

		process_bar = ShowProcess(tree_in.GetEntries(), self.print_enable)
		n_saved = 0

		for iEvent in range(0, tree_in.GetEntries()):
			process_bar.show_process()
			tree_in.GetEntry(iEvent)
			vector_electron = []
			for iEl in range(0, tree_in.gsf_n):
				tmp_electron = electron_C(tree_in.gsf_charge[iEl])
				tmp_electron.p4.SetPtEtaPhiM(tree_in.gsf_ecalEnergyPostCorr[iEl]*sin(tree_in.gsf_theta[iEl]), tree_in.gsf_eta[iEl], tree_in.gsf_phi[iEl], const_m_el)
				tmp_electron.p4_sc.SetPtEtaPhiM(tree_in.gsf_sc_energy[iEl]*sin(tree_in.gsf_theta[iEl]), tree_in.gsf_sc_eta[iEl], tree_in.gsf_phi[iEl], const_m_el)
				tmp_electron.sc_Eta = tree_in.gsf_sc_eta[iEl]
				tmp_electron.get_region()
				if (tmp_electron.region != 1 and tmp_electron.region != 3): continue

				tmp_electron.check_HEEPID(\
					 tree_in.gsf_deltaPhiSuperClusterTrackAtVtx[iEl], \
					 tree_in.gsf_full5x5_sigmaIetaIeta[iEl],\
					 tree_in.gsf_nLostInnerHits[iEl], \
					 abs(tree_in.gsf_dxy_firstPVtx[iEl]), \
					 tree_in.gsf_hadronicOverEm[iEl],\
					 tree_in.gsf_sc_energy[iEl], \
					 ( float(tree_in.gsf_full5x5_e1x5[iEl])/float(tree_in.gsf_full5x5_e5x5[iEl]) ), \
					 ( float(tree_in.gsf_full5x5_e2x5Max[iEl])/float(tree_in.gsf_full5x5_e5x5[iEl]) ), \
					 (tree_in.gsf_dr03EcalRecHitSumEt[iEl] + tree_in.gsf_dr03HcalDepth1TowerSumEt[iEl]), \
					 tree_in.gsf_heepTrkPtIso[iEl], \
					 tree_in.gsf_ecaldrivenSeed[iEl], \
					 tree_in.gsf_deltaEtaSeedClusterTrackAtVtx[iEl], \
					 tree_in.ev_fixedGridRhoFastjetAll)

				tmp_electron.isTag = (tmp_electron.p4.Et() > 35 \
										and tmp_electron.region == 1 \
										and tmp_electron.pass_HEEPID)
				vector_electron.append(tmp_electron)
		
			iTag = -1
			iProbe = -1
			for iTag in range(len(vector_electron)):
				if vector_electron[iTag].isTag:
					for iProbe in range(len(vector_electron)):
						if iProbe == iTag: continue
						self.tag_HEEPinfo.pass_isEcalDriven = vector_electron[iTag].pass_isEcalDriven
						self.tag_HEEPinfo.pass_dEtaIn = vector_electron[iTag].pass_dEtaIn
						self.tag_HEEPinfo.pass_dPhiIn = vector_electron[iTag].pass_dPhiIn
						self.tag_HEEPinfo.pass_HoverE = vector_electron[iTag].pass_HoverE
						self.tag_HEEPinfo.pass_SigmaIeIe = vector_electron[iTag].pass_SigmaIeIe
						self.tag_HEEPinfo.pass_showershape = vector_electron[iTag].pass_showershape
						self.tag_HEEPinfo.pass_lostHits = vector_electron[iTag].pass_lostHits
						self.tag_HEEPinfo.pass_dxy = vector_electron[iTag].pass_dxy
						self.tag_HEEPinfo.pass_isolEMHadDepth1 = vector_electron[iTag].pass_isolEMHadDepth1
						self.tag_HEEPinfo.pass_pTIso = vector_electron[iTag].pass_pTIso
						self.tag_p4[0] = vector_electron[iTag].p4.Px()
						self.tag_p4[1] = vector_electron[iTag].p4.Py()
						self.tag_p4[2] = vector_electron[iTag].p4.Pz()
						self.tag_p4[3] = vector_electron[iTag].p4.E()
						self.tag_sc_Eta[0] = vector_electron[iProbe].sc_Eta
						self.tag_charge[0] = vector_electron[iProbe].charge
						self.tag_region[0] = vector_electron[iProbe].region
						self.tag_pass_HEEPID[0] = vector_electron[iProbe].pass_HEEPID
						try :
							self.tag_trig_DouEle25_unseededleg[0] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi, vector_electron[iTag].p4, 0.1)
							self.tag_trig_DouEle25_unseededleg[1] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi, vector_electron[iTag].p4, 0.1)
							self.tag_trig_DouEle25_seededleg[1] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi, vector_electron[iTag].p4, 0.1)
							self.tag_trig_DouEle25_seededleg[0] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi, vector_electron[iTag].p4, 0.1)
							self.tag_trig_Ele32WPTight[0] = self.trig_match(tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta, tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi, vector_electron[iTag].p4, 0.1)
							self.tag_trig_Ele35WPTight[0] = self.trig_match(tree_in.trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta, tree_in.trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi, vector_electron[iTag].p4, 0.1)
						except :pass

						self.probe_HEEPinfo.pass_isEcalDriven = vector_electron[iProbe].pass_isEcalDriven
						self.probe_HEEPinfo.pass_dEtaIn = vector_electron[iProbe].pass_dEtaIn
						self.probe_HEEPinfo.pass_dPhiIn = vector_electron[iProbe].pass_dPhiIn
						self.probe_HEEPinfo.pass_HoverE = vector_electron[iProbe].pass_HoverE
						self.probe_HEEPinfo.pass_SigmaIeIe = vector_electron[iProbe].pass_SigmaIeIe
						self.probe_HEEPinfo.pass_showershape = vector_electron[iProbe].pass_showershape
						self.probe_HEEPinfo.pass_lostHits = vector_electron[iProbe].pass_lostHits
						self.probe_HEEPinfo.pass_dxy = vector_electron[iProbe].pass_dxy
						self.probe_HEEPinfo.pass_isolEMHadDepth1 = vector_electron[iProbe].pass_isolEMHadDepth1
						self.probe_HEEPinfo.pass_pTIso = vector_electron[iProbe].pass_pTIso
						self.probe_p4[0] = vector_electron[iProbe].p4.Px()
						self.probe_p4[1] = vector_electron[iProbe].p4.Py()
						self.probe_p4[2] = vector_electron[iProbe].p4.Pz()
						self.probe_p4[3] = vector_electron[iProbe].p4.E()
						self.probe_sc_Eta[0] = vector_electron[iProbe].sc_Eta
						self.probe_charge[0] = vector_electron[iProbe].charge
						self.probe_region[0] = vector_electron[iProbe].region
						self.probe_pass_HEEPID[0] = vector_electron[iProbe].pass_HEEPID
						try :
							self.probe_trig_DouEle25_unseededleg[0] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi, vector_electron[iProbe].p4, 0.1)
							self.probe_trig_DouEle25_unseededleg[1] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi, vector_electron[iProbe].p4, 0.1)
							self.probe_trig_DouEle25_seededleg[1] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi, vector_electron[iProbe].p4, 0.1)
							self.probe_trig_DouEle25_seededleg[0] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi, vector_electron[iProbe].p4, 0.1)
							self.probe_trig_Ele32WPTight[0] = self.trig_match(tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta, tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi, vector_electron[iProbe].p4, 0.1)
							self.probe_trig_Ele35WPTight[0] = self.trig_match(tree_in.trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta, tree_in.trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi, vector_electron[iProbe].p4, 0.1)
						except :pass
		
						self.tree_out.Fill()
						n_saved += 1

		process_bar.close('Finish, %d saved'%(n_saved))
		
		if self.print_enable: print "%0.1f event / s  ,  waiting for other processes"%(tree_in.GetEntries() / float(time.time() - pre_time))
	
	def Loop(self):
		tChain = ROOT.TChain("IIHEAnalysis")
		if self.print_enable: print "TChian initializing, %d root files in total"%(len(self.root_file_list))
		process_bar1 = ShowProcess( len(self.root_file_list) , self.print_enable)
		for file_name in self.root_file_list:
			tChain.Add(file_name)
			process_bar1.show_process()
		process_bar1.close('TChian initialized, reskiming %d events'%(tChain.GetEntries()))

		self.Fill_branch(tChain)
		
		self.f_out.Write()
		self.f_out.Close()