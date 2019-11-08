import os
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-r","--input_dir",dest="input_dir",default="null",type="str")

(options,args)=parser.parse_args()


def main(input_dir):
    if input_dir == "null":
        print "need input dir/folder!"
        return
    target_dir = "_plot_"+input_dir.split("/")[0]
    try:
    	os.mkdir(target_dir)
    except:
    	pass
    print "copying PNG from %s to %s"%(input_dir, target_dir)
    os.system("cp %s/*.png %s/"%(input_dir, target_dir) )

main(options.input_dir)
