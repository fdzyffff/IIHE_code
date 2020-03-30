import os
import sys
import ROOT
import collections

sample_nevent = collections.OrderedDict() 
sample_path = collections.OrderedDict()

sample_path['DYToLL_10to50'] = 'MC/DYToLL_10to50'
sample_path['DYToLL_50'] = 'MC/DYToLL_50'
sample_path['TTGJets'] = 'MC/TTGJets'
sample_path['TTTo2L2Nu'] = 'MC/TTTo2L2Nu'
sample_path['TTWJetsToLNu'] = 'MC/TTWJetsToLNu'
sample_path['TTWJetsToQQ'] = 'MC/TTWJetsToQQ'
sample_path['TTZToLLNuNu_10'] = 'MC/TTZToLLNuNu_10'
sample_path['TTZToQQ'] = 'MC/TTZToQQ'
sample_path['tW'] = 'MC/tW'
sample_path['tW_anti'] = 'MC/tW_anti'
sample_path['WGToLNuG'] = 'MC/WGToLNuG'
sample_path['WJetsToLNu'] = 'MC/WJetsToLNu'
sample_path['WWTo2L2Nu'] = 'MC/WWTo2L2Nu'
sample_path['WZTo2L2Q'] = 'MC/WZTo2L2Q'
sample_path['WZTo3LNu'] = 'MC/WZTo3LNu'
sample_path['ZZTo2L2Nu'] = 'MC/ZZTo2L2Nu'
sample_path['ZZTo4L'] = 'MC/ZZTo4L'

#sample_path['ST_ctemu_scalar'] = 'MC/ST_ctemu_scalar'
#sample_path['ST_ctemu_tensor'] = 'MC/ST_ctemu_tensor'
#sample_path['ST_ctemu_vector'] = 'MC/ST_ctemu_vector'
#sample_path['ST_utemu_scalar'] = 'MC/ST_utemu_scalar'
#sample_path['ST_utemu_tensor'] = 'MC/ST_utemu_tensor'
#sample_path['ST_utemu_vector'] = 'MC/ST_utemu_vector'
#sample_path['TT_ctemu_scalar'] = 'MC/TT_ctemu_scalar'
#sample_path['TT_ctemu_tensor'] = 'MC/TT_ctemu_tensor'
#sample_path['TT_utemu_scalar'] = 'MC/TT_utemu_scalar'
#sample_path['TT_utemu_tensor'] = 'MC/TT_utemu_tensor'
#sample_path['TT_utemu_vector'] = 'MC/TT_utemu_vector'

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
    sample_nevent[sample_name] = neventsweight

f_out = open("ntuples/signal_plot_part2.out","w")
tmplate_text = """
pre_input_dic[\"_#sample_name#\"] = {
\t\t\"isFromRoot\":True,
\t\t\"input_file\":\"#sample_name#.root\",
\t\t\"isData\":False,
\t\t\"isFake\":False,
\t\t\"useToNorm\":False,
\t\t\"lumi\":0.0,
\t\t\"Xsection\":xsection_#sample_name#,
\t\t\"N_total\": 0.0,
\t\t\"Raw_total\":#nevent#,
\t\t\"N_norm\":1.0,
\t\t\"Norm_Factor\":1,
\t\t\"Fill_color\":30,
\t\t\"weight_factor\":1,
\t\t\"hist\":{},
\t\t\"isUpdate\":isUpdate
\t\t}"""
for sample_name in sample_nevent:
    f_out.write("%s\n"%(tmplate_text.replace("#sample_name#",sample_name).replace("#nevent#",str(sample_nevent[sample_name]))))
f_out.close()
