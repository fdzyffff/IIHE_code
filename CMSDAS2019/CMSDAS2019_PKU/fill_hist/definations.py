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
	def __init__(self, p4, charge):
		self.p4 = p4
		self.isTag = False
		self.pass_HEEPID = False
		self.sc_Eta = -99.99
		self.charge = charge
		self.region = 0
		self.match_trigger_ = False

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
		if   (self.region == 1): self.pass_HoverE = ( HOverE < (0.05 + 1.0/caloEnergy) )
		elif (self.region == 3): self.pass_HoverE = ( HOverE < (0.05 + (-0.4 + 0.4*abs(self.p4.Eta())) * rho / caloEnergy) )

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
			self.pass_isolEMHadDepth1 = ( isolEMHadDepth1 < (2.0+ 0.03*self.p4.Et() + 0.28*rho) )
		elif(self.region == 3): 
			if (self.p4.Et()<50.0):
				self.pass_isolEMHadDepth1 = ( isolEMHadDepth1 < (2.5 + (0.15+0.07*abs(self.p4.Eta()))*rho) )
			else:
				self.pass_isolEMHadDepth1 = ( isolEMHadDepth1 < (2.5 + 0.03*(self.p4.Et()-50.0) + (0.15+0.07*abs(self.p4.Eta()))*rho) )

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

class reskim():
	def __init__(self, out_file_name):
		self.root_file_list = []
		self.print_enable = True
	
		self.tag_p4 = array.array( 'f', [0, 0, 0, 0] )
		self.probe_p4 = array.array( 'f', [0, 0, 0, 0] )
		self.sc_Eta = array.array('f', [0] )
		self.charge = array.array('i', [0] )
		self.region = array.array('i', [0] )
		self.pass_HEEPID = array.array('i', [0] )
		self.trig_DouEle25_seededleg = array.array('i', [0, 0] )
		self.trig_DouEle25_unseededleg = array.array('i', [0, 0] )
		self.trig_Ele35WPTight = array.array('i', [0] )
		self.trig_Ele32WPTight = array.array('i', [0] )
		
		self.HEEPinfo = ROOT.HEEPinfo_t()
		
		self.f_out = ROOT.TFile( out_file_name, 'RECREATE' )
		
		self.tree_out = ROOT.TTree( 'TreeName', 'tree comments here' )
		self.tree_out.Branch( 'HEEPinfo' , self.HEEPinfo,  'pass_isEcalDriven/I:pass_dEtaIn/I:pass_dPhiIn/I:pass_HoverE/I:pass_SigmaIeIe/I:pass	_showershape/I:pass_lostHits/I:pass_dxy/I:pass_isolEMHadDepth1/I:pass_pTIso/I' )
		self.tree_out.Branch( 'tag_p4'   , self.tag_p4   , 'tag_p4[4]/F')
		self.tree_out.Branch( 'probe_p4' , self.probe_p4 , 'probe_p4[4]/F')
		self.tree_out.Branch( 'sc_Eta'   , self.sc_Eta   , 'sc_Eta/F' )
		self.tree_out.Branch( 'charge'   , self.charge   , 'charge/I' )
		self.tree_out.Branch( 'region'   , self.region   , 'region/I' )
		self.tree_out.Branch( 'pass_HEEPID', self.pass_HEEPID, 'pass_HEEPID/I' )
		self.tree_out.Branch( 'trig_DouEle25_unseededleg' , self.trig_DouEle25_unseededleg, 'trig_DouEle25_unseededleg[2]/I' )
		self.tree_out.Branch( 'trig_Ele32WPTight' , self.trig_Ele32WPTight, 'trig_Ele32WPTight/I' )
		self.tree_out.Branch( 'trig_Ele35WPTight' , self.trig_Ele35WPTight, 'trig_Ele35WPTight/I' )

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
				tmp_p4 = ROOT.TLorentzVector()
				tmp_p4.SetPtEtaPhiM(tree_in.gsf_ecalEnergyPostCorr[iEl]*sin(tree_in.gsf_theta[iEl]), tree_in.gsf_eta[iEl], tree_in.gsf_phi[iEl], const_m_el)
				tmp_electron = electron_C(tmp_p4, tree_in.gsf_charge[iEl])
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

				tmp_match_trigger = False
				try : tmp_match_trigger = self.trig_match(tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta, tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi, tmp_electron.p4, 0.1)
				except : pass

				tmp_electron.isTag = (tmp_electron.p4.Et() > 35 \
										and tmp_electron.region == 1 \
										and tmp_electron.pass_HEEPID \
										and tmp_match_trigger)
				vector_electron.append(tmp_electron)
		
			iTag = -1
			for iEl in range(len(vector_electron)):
				if vector_electron[iEl].isTag:
					iTag = iEl
					break
		
			if iTag < 0:continue
			if len(vector_electron)	!= 2 : continue

			for iEl in range(len(vector_electron)):
				if iEl == iTag: continue
				self.tag_p4[0] = vector_electron[iTag].p4.Px()
				self.tag_p4[1] = vector_electron[iTag].p4.Py()
				self.tag_p4[2] = vector_electron[iTag].p4.Pz()
				self.tag_p4[3] = vector_electron[iTag].p4.E()

				self.HEEPinfo.pass_isEcalDriven = vector_electron[iEl].pass_isEcalDriven
				self.HEEPinfo.pass_dEtaIn = vector_electron[iEl].pass_dEtaIn
				self.HEEPinfo.pass_dPhiIn = vector_electron[iEl].pass_dPhiIn
				self.HEEPinfo.pass_HoverE = vector_electron[iEl].pass_HoverE
				self.HEEPinfo.pass_SigmaIeIe = vector_electron[iEl].pass_SigmaIeIe
				self.HEEPinfo.pass_showershape = vector_electron[iEl].pass_showershape
				self.HEEPinfo.pass_lostHits = vector_electron[iEl].pass_lostHits
				self.HEEPinfo.pass_dxy = vector_electron[iEl].pass_dxy
				self.HEEPinfo.pass_isolEMHadDepth1 = vector_electron[iEl].pass_isolEMHadDepth1
				self.HEEPinfo.pass_pTIso = vector_electron[iEl].pass_pTIso

				self.probe_p4[0] = vector_electron[iEl].p4.Px()
				self.probe_p4[1] = vector_electron[iEl].p4.Py()
				self.probe_p4[2] = vector_electron[iEl].p4.Pz()
				self.probe_p4[3] = vector_electron[iEl].p4.E()
				self.sc_Eta[0] = vector_electron[iEl].sc_Eta
				self.charge[0] = vector_electron[iEl].charge
				self.region[0] = vector_electron[iEl].region
				self.pass_HEEPID[0] = vector_electron[iEl].pass_HEEPID
				try :
					self.trig_DouEle25_unseededleg[0] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEG25EtUnseededFilter_phi, vector_electron[iEl].p4, 0.1)
					self.trig_DouEle25_unseededleg[1] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltDiEle25CaloIdLMWPMS2UnseededFilter_phi, vector_electron[iEl].p4, 0.1)
					self.trig_DouEle25_seededleg[1] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEle25CaloIdLMWPMS2Filter_phi, vector_electron[iEl].p4, 0.1)
					self.trig_DouEle25_seededleg[0] = self.trig_match(tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_eta, tree_in.trig_HLT_DoubleEle25_CaloIdL_MW_hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter_phi, vector_electron[iEl].p4, 0.1)
					self.trig_Ele32WPTight[0] = self.trig_match(tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_eta, tree_in.trig_HLT_Ele32_WPTight_Gsf_hltEle32WPTightGsfTrackIsoFilter_phi, vector_electron[iEl].p4, 0.1)
					self.trig_Ele35WPTight[0] = self.trig_match(tree_in.trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_eta, tree_in.trig_HLT_Ele35_WPTight_Gsf_hltEle35noerWPTightGsfTrackIsoFilter_phi, vector_electron[iEl].p4, 0.1)
				except :pass
		
				self.tree_out.Fill()
				n_saved += 1
				#break

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