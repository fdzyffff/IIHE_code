import os
import sys
import ROOT

sample_path = {
#"DYToTT"		:"MC/DYToTT",
"DYToEE"		:"MC/DYToEE",
#"ST_antitop"		:"MC/ST_antitop",
#"ST_top"		:"MC/ST_top",
#"ttbar2l2u"		:"MC/ttbar2l2u",
#"WW"		:"MC/WW",
#"WZ"		:"MC/WZ",
#"ZZ"		:"MC/ZZ",
}

class ShowProcess():
    i = 0
    max_steps = 0
    max_arrow = 50
    step_length = 1
    print_enable = True

    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.i = 0

    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        if not self.print_enable:return
        if self.step_length > 1:
            if (self.max_steps > 100):
                if (not int(self.i) % int(float(self.max_steps)/float(self.step_length)) == 0):return
        num_arrow = int(self.i * self.max_arrow / self.max_steps)
        num_line = self.max_arrow - num_arrow
        percent = self.i * 100.0 / self.max_steps
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r'
        sys.stdout.write(process_bar)
        sys.stdout.flush()

    def close(self, words='done'):
        print ''
        print words
        self.i = 0


def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #if s == "failed":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList

def check_crab(input_dir):
    if len(os.listdir(input_dir)) > 1:
         return True
    return False

for sample_name in sample_path:
    if check_crab(sample_path[sample_name]):
        print "Warning: more than 1 sub_dir in %s"%(sample_path[sample_name])
    filenames = GetFileList(sample_path[sample_name],[])
    #print filenames
    #break
    nEventsraw = 0
    neventsweight = 0
    nEventsStored = 0
    nEventsiihe = 0
    nFiles = 0
    print '+++++++++++++++++++++++'
    print "%s : %d"%(sample_name, len(filenames))
    process_bar = ShowProcess(len(filenames))
    #process_bar.step_length = 50
    #process_bar.print_enable = False
    for fname in filenames:
        #print fname
        if 'fail' in fname:
            continue
        if not ".root" in fname:
            continue
        try:
            f = ROOT.TFile.Open(fname)
            if not f:
                print 'not exist'+fname
            tree_in = f.Get('IIHEAnalysis')
            tree_meta = f.Get('meta')
        except:
            continue
        nEventsiihe += tree_in.GetEntries()
        tree_meta.GetEntry(0)
        nEventsraw += tree_meta.nEventsRaw
        nEventsStored += tree_meta.nEventsStored
        neventsweight += tree_meta.mc_nEventsWeighted
        nFiles += 1
        #print int(len(filenames)/50)
        #if nFiles%100 == 0: print nFiles
        #if nFiles > 300 and nFiles%int(len(filenames)/50)==0:
            #print "%d Files processed, %.2f %%"%(nFiles,nFiles*100/len(filenames))
        process_bar.show_process()
    process_bar.close('done')
    print '#####################'
    print '%s'%(sample_name) 
    print 'nFiles %d'%(nFiles) 
    print 'nEventsraw %d   '%(nEventsraw)
    print 'neventsweight %d   '%(neventsweight)
    print 'nEventsStored %d   '%(nEventsStored)
    print 'nEventsiihe %d   '%(nEventsiihe)
    print '#####################' 
