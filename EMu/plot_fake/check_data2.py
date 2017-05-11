import ROOT

try:
    tchain=ROOT.TChain('tap')
    tchain.Add('data_2016B_DoubleEG.root')
except:
    print "errors!"

diff_list = []
for line in open('output.txt','r'):
    if not '>' in line:continue
    l = line.split(' ')
    tmp_list = []
    tmp_list = [l[1], l[2], l[3]]
    diff_list.append(tmp_list)

print diff_list
n_passed1 = 0
totalEntry = tchain.GetEntries()
for iEntry in range(0, tchain.GetEntries()):
    tchain.GetEntry(iEntry)
    run = tchain.ev_run_out
    event = tchain.ev_event_out & 0xffffffff
    lumi = tchain.ev_luminosityBlock_out
    tmp_list = [run, lumi, event]
    if tmp_list in diff_list:
        print "*"*20
        print 'run : %d'%(run)
        print 'lumi : %d'%(lumi)
        print 'event : %d'%(event)
        print 'Invariant Mass : %f'%(tchain.M_ee)
        print 'heep1 Et : %f'%(tchain.t_Et)
        print 'heep1 eta : %f'%(tchain.t_eta)
        print 'heep1 phi : %f'%(tchain.t_phi)
        print 'heep2 Et : %f'%(tchain.heep2_pt)
        print 'heep2 eta : %f'%(tchain.heep2_eta)
        print 'heep2 phi : %f'%(tchain.heep2_phi)


