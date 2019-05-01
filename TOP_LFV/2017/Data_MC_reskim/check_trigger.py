import ROOT
import os
from optparse import OptionParser
parser=OptionParser()

parser.add_option("-r","--root_dir",dest="root_dir",default="",type="str")
parser.add_option("-l","--label",dest="label",default="",type="str")
(options,args)=parser.parse_args()

t1 = ROOT.TChain("tap") 
t1.Add("%s"%(options.root_dir)) 

total_p1 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1")
total_p2 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2")
total_p3 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3")
total_p411 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step411")
total_p412 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412")
total_p5_1 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412&&pass_step5")
total_p421 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step421")
total_p422 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422")
total_p5_2 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422&&pass_step5")
total_p43 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step43")
total_p5_3 	= t1.Draw("","(isEE&&pass_trigger_EE || isEMu&&pass_trigger_EMu || isMuMu&&pass_trigger_MuMu)&&pass_step1&&pass_step2&&pass_step3&pass_step43&pass_step5")

EE_p1        = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1")
EE_p2        = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2")
EE_p3        = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3")
EE_p411      = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step411")
EE_p412      = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412")
EE_p5_1      = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412&&pass_step5")
EE_p421      = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step421")
EE_p422      = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422")
EE_p5_2      = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422&&pass_step5")
EE_p43       = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step43")
EE_p5_3      = t1.Draw("","pass_trigger_EE&&isEE&&pass_step1&&pass_step2&&pass_step3&pass_step43&pass_step5")

EMu_p1        = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1")
EMu_p2        = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2")
EMu_p3        = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3")
EMu_p411      = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step411")
EMu_p412      = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412")
EMu_p5_1      = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412&&pass_step5")
EMu_p421      = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step421")
EMu_p422      = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422")
EMu_p5_2      = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422&&pass_step5")
EMu_p43       = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step43")
EMu_p5_3      = t1.Draw("","pass_trigger_EMu&&isEMu&&pass_step1&&pass_step2&&pass_step3&pass_step43&pass_step5")

MuMu_p1        = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1")
MuMu_p2        = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2")
MuMu_p3        = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3")
MuMu_p411      = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step411")
MuMu_p412      = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412")
MuMu_p5_1      = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step411&pass_step412&&pass_step5")
MuMu_p421      = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step421")
MuMu_p422      = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422")
MuMu_p5_2      = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step421&pass_step422&&pass_step5")
MuMu_p43       = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step43")
MuMu_p5_3      = t1.Draw("","pass_trigger_MuMu&&isMuMu&&pass_step1&&pass_step2&&pass_step3&pass_step43&pass_step5")

print "%s pass trigger step1 %s  %s"%("#"*30, options.label, "#"*30)
print "%s,%s,%s,%s,%s,%s,%s,||,%s,%s,%s,||,%s,%s,"%("Category","step 1","step 2","step 3","step 4.1.1","step 4.1.2","step 5","step 4.2.1","step 4.2.2","step 5","step 4.3","step 5")
print "%s,%s,%s,%s,%s,%s,%s,||,%s,%s,%s,||,%s,%s,"%("Total",total_p1,total_p2,total_p3,total_p411,total_p412,total_p5_1,total_p421,total_p422,total_p5_2,total_p43,total_p5_3)
print "%s,%s,%s,%s,%s,%s,%s,||,%s,%s,%s,||,%s,%s,"%("E E",EE_p1,EE_p2,EE_p3,EE_p411,EE_p412,EE_p5_1,EE_p421,EE_p422,EE_p5_2,EE_p43,EE_p5_3)
print "%s,%s,%s,%s,%s,%s,%s,||,%s,%s,%s,||,%s,%s,"%("E Mu",EMu_p1,EMu_p2,EMu_p3,EMu_p411,EMu_p412,EMu_p5_1,EMu_p421,EMu_p422,EMu_p5_2,EMu_p43,EMu_p5_3)
print "%s,%s,%s,%s,%s,%s,%s,||,%s,%s,%s,||,%s,%s,"%("Mu Mu",MuMu_p1,MuMu_p2,MuMu_p3,MuMu_p411,MuMu_p412,MuMu_p5_1,MuMu_p421,MuMu_p422,MuMu_p5_2,MuMu_p43,MuMu_p5_3)
