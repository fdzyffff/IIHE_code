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
n_stat = ROOT.TH1F("n_stat", " a hist ", 10, 0, 10)
value_dic = {}
value_dic["dilepton"] = ["dilepton", 0]
value_dic["signal"] = ["MET<30, Njet>=3, Nbjet=1", 1]
value_dic["control"] = ["MET<30, Njet>=3, Nbjet>1", 2]

def run_process(para_in):
    out_tmp_root_name = para_in[0]
    n_start = para_in[1][0]
    n_end = para_in[1][1]
    print_enable = para_in[2]

    pre_time = time.time()

    f_in = ROOT.TFile( options.in_file_name, 'READ' )
    tree_in = f_in.Get('tap')
        
    f_out = ROOT.TFile( "_tmp/"+out_tmp_root_name, 'RECREATE' )

    n_range = min(n_end, tree_in.GetEntries()) - n_start
    process_bar = ShowProcess(n_range, print_enable)
    for iEvent in range(n_start, min(n_end, tree_in.GetEntries())):
        tree_in.GetEntry(iEvent)
        process_bar.show_process()
        ret = tree_in.pass_MET_filters and tree_in.isEMu and tree_in.pass_trigger_EMu_step2 and tree_in.pass_step1
        if (ret):
            n_stat.Fill(value_dic["dilepton"][1])
        if (ret and tree_in.MET_FinalCollection_Pt < 30 and tree_in.n_jet >= 3 and tree_in.n_bjet == 1):
            n_stat.Fill(value_dic["signal"][1])
        if (ret and tree_in.MET_FinalCollection_Pt < 30 and tree_in.n_jet >= 3 and tree_in.n_bjet > 1):
            n_stat.Fill(value_dic["control"][1])

    n_stat.Write()

    f_out.Close()
    f_in.Close()

    if print_enable: print "\n %0.1f event / s , waiting for other processes"%(n_range / float(time.time() - pre_time))

def run():
    para_list = []
    f_in = ROOT.TFile( options.in_file_name, 'READ' )
    tmptree_in = f_in.Get( 'tap' )
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
    f_out = ROOT.TFile( in_file_name, 'READ')
    c1 = ROOT.TCanvas( 'c2', ' a Canvas ', 50,50,865,780 )

    h1 = f_out.Get( n_stat.GetName() )    
    h1.Draw()
    c1.Update()
    
    out_hist_name = '%s.png'%(n_stat.GetName())
    print "Draw %s"%( out_hist_name)
    c1.Print( out_hist_name )
    
    print "#################"
    for part in value_dic:
        h1.GetXaxis().SetBinLabel(value_dic[part][1]+1,value_dic[part][0])
        print "%s, %d"%(value_dic[part][0], h1.GetXaxis().GetBinContent(value_dic[part][1]+1))


if not options.skip_run:
    run()
    draw(options.out_file_name+".root")
else :
    draw(options.in_file_name)
