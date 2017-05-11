import ROOT

try:
    tchain=ROOT.TChain('tap')
    tchain.Add('data_2016B_DoubleEG.root')
    #tchain.Add('DYToEE.root')
except:
    print "errors!"

#print tchain.GetListOfLeaves()
n_passed1 = 0
n_passed2 = 0
n_BB1 = 0
n_BB2 = 0
n_BE1 = 0
n_BE2 = 0
totalEntry = tchain.GetEntries()
for iEntry in range(0, tchain.GetEntries()):
    tchain.GetEntry(iEntry)
    if iEntry%50000==0 and iEntry > 0:
        print '%d / %d  Prossed'%(iEntry,totalEntry)
    #print len(tchain.mc_mass),tchain.mc_n
#    if 60<=tchain.M_ee and tchain.M_ee<=120:
    if 60<=tchain.M_ee and tchain.M_ee<=120 :
        n_passed1+=tchain.w_PU_combined
        if tchain.HLT_Ele33 == 1:
            n_passed2+=tchain.w_PU_combined
    else : continue
    if tchain.t_region == 1 and tchain.heep2_region == 1:
        n_BB1+=tchain.w_PU_combined
        if tchain.HLT_Ele33 == 1:
            n_BB2+=tchain.w_PU_combined
    if (tchain.t_region == 1 and tchain.heep2_region == 3) or (tchain.t_region == 3 and tchain.heep2_region == 1):
        n_BE1+=tchain.w_PU_combined
        if tchain.HLT_Ele33 == 1:
            n_BE2+=tchain.w_PU_combined

print 'n_BB with trigger: ', n_BB2
print 'n_BB without trigger: ', n_BB1
print 'n_BE with trigger: ', n_BE2
print 'n_BE without trigger: ', n_BE1
print 'n total with trigger: ', n_passed2
print 'n total without trigger: ', n_passed1
