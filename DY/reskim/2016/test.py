import os
filelist=os.listdir("/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/")
#print files


tmp_file=open("test_wjets.c","w")

i=0

for fil in filelist:
    tmp_file.write('TChain* ch_%s = new TChain("IIHEAnalysis") ;\n' % (str(i)))
    tmp_file.write('ch_%s->Add("/pnfs/iihe/cms/store/user/rgoldouz/RunIIFall15MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/%s") ; \n' % (str(i),fil))
    tmp_file.write('reskim reskim_WJets_%s(ch_%s, false, false, true ) ;\n' % (str(i),str(i)))
    tmp_file.write('reskim_WJets_%s.Loop("test/%s") ;\n\n' % (str(i),fil))
    i+=1
tmp_file.close()
