import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-l","--label",dest="label",default="",type="str")
(options,args)=parser.parse_args()


def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%d\n'%(line))

try:
    tchain=ROOT.TChain('tap')
    tchain.Add(options.root_dir)
except:
    print "errors!"

List = []

iEntry = 0
totalEntry = tchain.GetEntries()
for event in tchain:
#    if iEntry >1000:break
    if iEntry%50000==0 and iEntry > 0:
        print '%d / %d  Prossed'%(iEntry,totalEntry)
    ev_event = getattr(event,'ev_event_out') & 0xffffffff
    ev_run = getattr(event,'ev_run_out')# & 0xffffffff
    if ev_event <0: print ev_event
    ev_luminosityBlock = getattr(event,'ev_luminosityBlock_out')
    isEE = getattr(event, "isEE")
    isEMu = getattr(event, "isEMu")
    isMuMu = getattr(event, "isMuMu")
    pass_step1 = getattr(event, "pass_step1")
    pass_step2 = getattr(event, "pass_step2")
    pass_step3 = getattr(event, "pass_step3")
    pass_step411 = getattr(event, "pass_step411")
    pass_step412 = getattr(event, "pass_step412")
    pass_step5 = getattr(event, "pass_step5")
    if (isEE and pass_step1):# and pass_step2 and pass_step3 and pass_step411 and pass_step412):
        #tmp_list = [ev_run, ev_luminosityBlock, ev_event]
        List.append(ev_event)
    iEntry+=1

print '************ read from file finish **************'

List.sort()

print len(List)

write_to_file('%s_event.list'%(options.label),List)
