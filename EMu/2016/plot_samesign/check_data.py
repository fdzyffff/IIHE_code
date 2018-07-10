import ROOT

try:
    tchain=ROOT.TChain('tap')
    tchain.Add('data_2016B_DoubleEG.root')
except:
    print "errors!"

run_list = []
n_passed1 = 0
totalEntry = tchain.GetEntries()
for iEntry in range(0, tchain.GetEntries()):
    tchain.GetEntry(iEntry)
    if tchain.ev_run_out not in run_list:run_list.append(tchain.ev_run_out)
    if iEntry%50000==0 and iEntry > 0:
        print '%d / %d  Prossed'%(iEntry,totalEntry)
    if 60<=tchain.M_ee and tchain.M_ee<=120 :
        if (tchain.t_region == 1 and tchain.heep2_region == 1) or (tchain.t_region == 3 and tchain.heep2_region == 3) or (tchain.t_region == 1 and tchain.heep2_region == 3) or (tchain.t_region == 3 and tchain.heep2_region == 1):
            n_passed1+=tchain.w_PU_combined

print 'n total : ', n_passed1
run_list.sort()
for run in run_list:
    print run
