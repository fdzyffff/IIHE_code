import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-l","--label",dest="label",default="def",type="str")
(options,args)=parser.parse_args()


def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%s\n'%(line))

try:
    tchain=ROOT.TChain('tap')
    tchain.Add(options.root_dir)
except:
    print "errors!"

List = []

iEntry = 0
totalEntry = tchain.GetEntries()
for event in tchain:
    ev_event = getattr(event,'ev_event')
    ev_run = getattr(event,'ev_run')# & 0xffffffff
    if ev_event <0: print ev_event
    ev_event = getattr(event,'ev_event') & 0xffffffff
    ev_luminosityBlock = getattr(event,'ev_luminosityBlock')
    isEMu = getattr(event, "isEMu")
    pass_step1 = getattr(event, "pass_step1")
    pass_trigger_EMu_step2 = getattr(event, "pass_trigger_EMu_step2")
    pass_MET_filters = getattr(event, "pass_MET_filters")
    if (isEMu and pass_step1 and pass_trigger_EMu_step2 and pass_MET_filters):
        #tmp_list = [ev_run, ev_luminosityBlock, ev_event]
        List.append('%s,%s,%s'%(ev_event,ev_run,ev_luminosityBlock))
    iEntry+=1

print '************ read from file finish **************'

List.sort()

print len(List)

write_to_file('%s_event.list'%(options.label),List)
