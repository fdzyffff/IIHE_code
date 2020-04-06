from definations import *
from optparse import OptionParser

parser=OptionParser()

parser.add_option("-i","--in_file_name",dest="in_file_name",default="",type="str")
parser.add_option("-o","--out_file_name",dest="out_file_name",default="out_hist",type="str")
parser.add_option("-n","--n_event",dest="n_event",default="-1",type="int")
parser.add_option("-r","--skip_run",dest="skip_run",action='store_false')
parser.add_option("-p","--n_proc",dest="n_proc",default="1",type="int")

(options,args)=parser.parse_args()



def run_process(para_in):
	out_tmp_root_name = para_in[0]
	n_start = para_in[1][0]
	n_end = para_in[1][1]
	print_enable = para_in[2]

	pre_time = time.time()
	tag_p4 = array.array( 'f', [0, 0, 0, 0] )
	probe_p4 = array.array( 'f', [0, 0, 0, 0] )
	sc_Eta = array.array('f', [0] )
	charge = array.array('i', [0] )
	region = array.array('i', [0] )
	pass_HEEPID = array.array('i', [0] )
	trig_DouEle25_seededleg = array.array('i', [0, 0] )
	trig_DouEle25_unseededleg = array.array('i', [0, 0] )
	trig_Ele35WPTight = array.array('i', [0] )
	trig_Ele32WPTight = array.array('i', [0] )
		
	HEEPinfo = ROOT.HEEPinfo_t()
		
	f_in = ROOT.TFile( options.in_file_name, 'READ' )
		
	tree_in = f_in.Get( 'TreeName' )
	tree_in.SetBranchAddress( 'HEEPinfo' , ROOT.AddressOf(HEEPinfo, 'pass_isEcalDriven') )
	tree_in.SetBranchAddress( 'tag_p4'   , tag_p4   )
	tree_in.SetBranchAddress( 'probe_p4' , probe_p4 )
	tree_in.SetBranchAddress( 'sc_Eta'   , sc_Eta   )
	tree_in.SetBranchAddress( 'charge'   , charge   )
	tree_in.SetBranchAddress( 'region'   , region   )
	tree_in.SetBranchAddress( 'pass_HEEPID', pass_HEEPID)
	tree_in.SetBranchAddress( 'trig_DouEle25_seededleg' , trig_DouEle25_seededleg )
	tree_in.SetBranchAddress( 'trig_DouEle25_unseededleg' , trig_DouEle25_unseededleg )
	tree_in.SetBranchAddress( 'trig_Ele32WPTight' , trig_Ele32WPTight )
	tree_in.SetBranchAddress( 'trig_Ele35WPTight' , trig_Ele35WPTight )

	f_out = ROOT.TFile( "_tmp/"+out_tmp_root_name, 'RECREATE' )

	#h_denominator = ROOT.TH1F("probe_d", " a hist ", 51 , -2.55, 2.55)
	h_denominator = ROOT.TH1F("probe_d", " a hist ", 100 , 20, 120)
	h_numerator = h_denominator.Clone("probe_n")

	n_range = min(n_end, tree_in.GetEntries()) - n_start
	process_bar = ShowProcess(n_range, print_enable)
	for iEvent in range(n_start, min(n_end, tree_in.GetEntries())):
		tree_in.GetEntry(iEvent)
		process_bar.show_process()

		tmp_tag_p4 = ROOT.TLorentzVector()
		tmp_tag_p4.SetPxPyPzE(tag_p4[0], tag_p4[1], tag_p4[2], tag_p4[3])
		tmp_probe_p4 = ROOT.TLorentzVector()
		tmp_probe_p4.SetPxPyPzE(probe_p4[0], probe_p4[1], probe_p4[2], probe_p4[3])
		TaP_mass = (tmp_tag_p4 + tmp_probe_p4).Mag()
		if ( TaP_mass < 70 or TaP_mass > 110 ): continue
		if (region[0] != 1 and region[0] != 3): continue

		Fill_value = tmp_probe_p4.Et()
		ret = True
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

		ret = 
		if (ret and tmp_probe_p4.Et()>35 and sc_Eta[0] < 1.4442):
			h_denominator.Fill(Fill_value)
			if (pass_HEEPID[0]):
				h_numerator.Fill(Fill_value)

	h_denominator.Write()
	h_numerator.Write()

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


def Graph_Xerror0(graph_in):
        for i in range(0,graph_in.GetN()):
                graph_in.SetPointEXlow (i, 0)
                graph_in.SetPointEXhigh(i, 0)

def draw(in_file_name):
	#ROOT.gROOT.SetBatch(ROOT.kFALSE)
	f_out = ROOT.TFile( in_file_name, 'READ')
	c1 = ROOT.TCanvas( 'c2', ' a Canvas ', 50,50,865,780 )

	h_denominator = ROOT.TH1F()
	h_numerator = ROOT.TH1F()
	h_denominator = f_out.Get( 'probe_d' )
	h_numerator = f_out.Get( 'probe_n' )
	gr1 = ROOT.TGraphAsymmErrors()
	gr1.SetName("eff_plot")
	gr1.Divide(h_numerator,h_denominator,"cl=0.683 b(1,1) mode")
	Graph_Xerror0(gr1)
	gr1.SetMarkerStyle( 22 )
	gr1.SetMarkerColor(4)
	gr1.SetLineColor(4)
	gr1.GetYaxis().SetRangeUser(0.0, 1.1)

	gr1.Draw( 'AP' )
	c1.Update()

	plot_name = 'eff_plot_%s.png'%(options.out_file_name.replace(".root",""))
	print "Draw %s"%(plot_name)
	c1.Print( plot_name )

if not options.skip_run:
	run()
	draw(options.out_file_name+".root")
else :
	draw(options.in_file_name)
