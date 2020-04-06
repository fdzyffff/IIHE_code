from definations import *
from optparse import OptionParser

parser=OptionParser()

parser.add_option("-i","--in_file_name",dest="in_file_name",default="",type="str")
parser.add_option("-o","--out_file_name",dest="out_file_name",default="out_hist",type="str")
parser.add_option("-n","--n_event",dest="n_event",default="-1",type="int")
parser.add_option("-r","--skip_run",dest="skip_run",action='store_false')
parser.add_option("-p","--n_proc",dest="n_proc",default="1",type="int")

(options,args)=parser.parse_args()

global_hist_dic = {}
tmp_hist = ROOT.TH1F("tmp", " a hist ", 51 , -2.55, 2.55)
global_hist_dic["HEEPID_Eff_Eta"] = eff_hist("HEEPID_Eff_Eta", tmp_hist)
tmp_hist = ROOT.TH1F("tmp", " a hist ", 100 , 20, 120)
global_hist_dic["HEEPID_Eff_Pt_barrel"] = eff_hist("HEEPID_Eff_Pt_barrel", tmp_hist)
global_hist_dic["HEEPID_Eff_Pt_endcap"] = eff_hist("HEEPID_Eff_Pt_endcap", tmp_hist)
tmp_hist = ROOT.TH1F("tmp", " a hist ", 100 , 20, 40)
global_hist_dic["Trig_Eff_Et1"] = eff_hist("Trig_Eff_Et1", tmp_hist)
tmp_hist = ROOT.TH1F("tmp", " a hist ", 100 , 20, 120)
global_hist_dic["Trig_Eff_Et2"] = eff_hist("Trig_Eff_Et2", tmp_hist)
global_hist_dic["Trig_EffID_Et"] = eff_hist("Trig_EffID_Et", tmp_hist)

def run_process(para_in):
	out_tmp_root_name = para_in[0]
	n_start = para_in[1][0]
	n_end = para_in[1][1]
	print_enable = para_in[2]

	pre_time = time.time()
	probe_HEEPinfo = ROOT.HEEPinfo_t()
	probe_p4 = array.array( 'f', [0, 0, 0, 0] )
	probe_sc_Eta = array.array('f', [0] )
	probe_charge = array.array('i', [0] )
	probe_region = array.array('i', [0] )
	probe_pass_HEEPID = array.array('i', [0] )
	probe_trig_DouEle25_seededleg = array.array('i', [0, 0] )
	probe_trig_DouEle25_unseededleg = array.array('i', [0, 0] )
	probe_trig_Ele35WPTight = array.array('i', [0] )
	probe_trig_Ele32WPTight = array.array('i', [0] )

	tag_HEEPinfo = ROOT.HEEPinfo_t()
	tag_p4 = array.array( 'f', [0, 0, 0, 0] )
	tag_sc_Eta = array.array('f', [0] )
	tag_charge = array.array('i', [0] )
	tag_region = array.array('i', [0] )
	tag_pass_HEEPID = array.array('i', [0] )
	tag_trig_DouEle25_seededleg = array.array('i', [0, 0] )
	tag_trig_DouEle25_unseededleg = array.array('i', [0, 0] )
	tag_trig_Ele35WPTight = array.array('i', [0] )
	tag_trig_Ele32WPTight = array.array('i', [0] )
		
		
	f_in = ROOT.TFile( options.in_file_name, 'READ' )
		
	tree_in = f_in.Get( 'TreeName' )
	tree_in.SetBranchAddress( 'probe_HEEPinfo' , ROOT.AddressOf(probe_HEEPinfo, 'pass_isEcalDriven') )
	tree_in.SetBranchAddress( 'probe_p4' , probe_p4 )
	tree_in.SetBranchAddress( 'probe_sc_Eta'   , probe_sc_Eta   )
	tree_in.SetBranchAddress( 'probe_charge'   , probe_charge   )
	tree_in.SetBranchAddress( 'probe_region'   , probe_region   )
	tree_in.SetBranchAddress( 'probe_pass_HEEPID', probe_pass_HEEPID)
	tree_in.SetBranchAddress( 'probe_trig_DouEle25_seededleg' , probe_trig_DouEle25_seededleg )
	tree_in.SetBranchAddress( 'probe_trig_DouEle25_unseededleg' , probe_trig_DouEle25_unseededleg )
	tree_in.SetBranchAddress( 'probe_trig_Ele32WPTight' , probe_trig_Ele32WPTight )
	tree_in.SetBranchAddress( 'probe_trig_Ele35WPTight' , probe_trig_Ele35WPTight )

	tree_in.SetBranchAddress( 'tag_HEEPinfo' , ROOT.AddressOf(tag_HEEPinfo, 'pass_isEcalDriven') )
	tree_in.SetBranchAddress( 'tag_p4' , tag_p4 )
	tree_in.SetBranchAddress( 'tag_sc_Eta'   , tag_sc_Eta   )
	tree_in.SetBranchAddress( 'tag_charge'   , tag_charge   )
	tree_in.SetBranchAddress( 'tag_region'   , tag_region   )
	tree_in.SetBranchAddress( 'tag_pass_HEEPID', tag_pass_HEEPID)
	tree_in.SetBranchAddress( 'tag_trig_DouEle25_seededleg' , tag_trig_DouEle25_seededleg )
	tree_in.SetBranchAddress( 'tag_trig_DouEle25_unseededleg' , tag_trig_DouEle25_unseededleg )
	tree_in.SetBranchAddress( 'tag_trig_Ele32WPTight' , tag_trig_Ele32WPTight )
	tree_in.SetBranchAddress( 'tag_trig_Ele35WPTight' , tag_trig_Ele35WPTight )

	f_out = ROOT.TFile( "_tmp/"+out_tmp_root_name, 'RECREATE' )

	n_range = min(n_end, tree_in.GetEntries()) - n_start
	process_bar = ShowProcess(n_range, print_enable)
	for iEvent in range(n_start, min(n_end, tree_in.GetEntries())):
		tree_in.GetEntry(iEvent)
		process_bar.show_process()

		L_tag_p4 = ROOT.TLorentzVector()
		L_tag_p4.SetPxPyPzE(tag_p4[0], tag_p4[1], tag_p4[2], tag_p4[3])
		L_probe_p4 = ROOT.TLorentzVector()
		L_probe_p4.SetPxPyPzE(probe_p4[0], probe_p4[1], probe_p4[2], probe_p4[3])
		TaP_mass = (L_tag_p4 + L_probe_p4).Mag()

		ret = tag_trig_Ele32WPTight[0] and ( TaP_mass > 70 and TaP_mass < 110 )
		#ret = ret and HEEPinfo.pass_isEcalDriven
		#ret = ret and HEEPinfo.pass_dEtaIn
		#ret = ret and HEEPinfo.pass_dPhiIn
		#ret = ret and HEEPinfo.pass_HoverE
		#ret = ret and HEEPinfo.pass_SigmaIeIe
		#ret = ret and HEEPinfo.pass_showershape
		#ret = ret and HEEPinfo.pass_lostHits
		#ret = ret and HEEPinfo.pass_dxy
		#ret = ret and HEEPinfo.pass_isolEMHadDepth1
		#ret = ret and HEEPinfo.pass_pTIso

		if (ret and L_probe_p4.Et()>35 ):
			global_hist_dic["HEEPID_Eff_Eta"].h_denominator.Fill(probe_sc_Eta[0])
			if (probe_pass_HEEPID[0]):
				global_hist_dic["HEEPID_Eff_Eta"].h_numerator.Fill(probe_sc_Eta[0])

		if (ret and L_probe_p4.Et()>35 and probe_region[0] == 1):	
			global_hist_dic["HEEPID_Eff_Pt_barrel"].h_denominator.Fill(L_probe_p4.Et())
			if (probe_pass_HEEPID[0]):
				global_hist_dic["HEEPID_Eff_Pt_barrel"].h_numerator.Fill(L_probe_p4.Et())

		if (ret and L_probe_p4.Et()>35 and probe_region[0] == 3):	
			global_hist_dic["HEEPID_Eff_Pt_endcap"].h_denominator.Fill(L_probe_p4.Et())
			if (probe_pass_HEEPID[0]):
				global_hist_dic["HEEPID_Eff_Pt_endcap"].h_numerator.Fill(L_probe_p4.Et())

		ret = tag_pass_HEEPID[0] and  tag_trig_Ele35WPTight[0] and tag_trig_DouEle25_seededleg[0]
		if (ret and probe_pass_HEEPID[0]):
			global_hist_dic["Trig_Eff_Et1"].h_denominator.Fill(L_probe_p4.Et())
			global_hist_dic["Trig_Eff_Et2"].h_denominator.Fill(L_probe_p4.Et())
			if (probe_trig_DouEle25_unseededleg[1]):
				global_hist_dic["Trig_Eff_Et1"].h_numerator.Fill(L_probe_p4.Et())
				global_hist_dic["Trig_Eff_Et2"].h_numerator.Fill(L_probe_p4.Et())

		if (ret and probe_trig_DouEle25_unseededleg[0] and probe_pass_HEEPID[0]):
			global_hist_dic["Trig_EffID_Et"].h_denominator.Fill(L_probe_p4.Et())
			if (probe_trig_DouEle25_unseededleg[1]):
				global_hist_dic["Trig_EffID_Et"].h_numerator.Fill(L_probe_p4.Et())


	for part_hist in global_hist_dic:
		global_hist_dic[part_hist].h_denominator.Write()
		global_hist_dic[part_hist].h_numerator.Write()

	f_out.Close()
	f_in.Close()

	if print_enable: print "\n %0.1f event / s , waiting for other processes"%(n_range / float(time.time() - pre_time))

def run():
	para_list = []
	f_in = ROOT.TFile( options.in_file_name, 'READ' )
	tmptree_in = f_in.Get( 'TreeName' )
	n_range = tmptree_in.GetEntries()
	if options.n_event > 0: n_range = min(options.n_event, tmptree_in.GetEntries())
	f_in.Close()
	print "\n %d events in total"%(n_range)
	if n_range < 100:
		options.n_proc = 1
	os.system("rm _tmp/*.root")
	tmp_n_start = 0
	tmp_n_end = 0
	for i_proc in range(options.n_proc):
		tmp_n_start = tmp_n_end
		tmp_n_end = tmp_n_start + n_range//options.n_proc + (1 if i_proc < n_range%options.n_proc else 0)

		tmp_out_name = "%s_%d_%d.root"%(options.out_file_name, tmp_n_start, tmp_n_end)
		tmp_list = [tmp_out_name, [tmp_n_start,tmp_n_end], (i_proc == 0)]
		para_list.append( tmp_list )
		print tmp_list
	pool=Pool(options.n_proc)
	pool.map(run_process, para_list)
	pool.close()
	pool.join()

	tmp_text = "hadd -f %s.root"%(options.out_file_name)
	for para_part in para_list:
		tmp_text += " _tmp/" + para_part[0]
	os.system(tmp_text)

def draw (in_file_name):
	for part_hist in global_hist_dic:
		global_hist_dic[part_hist].draw(in_file_name)


if not options.skip_run:
	run()
	draw(options.out_file_name+".root")
else :
	draw(options.in_file_name)
