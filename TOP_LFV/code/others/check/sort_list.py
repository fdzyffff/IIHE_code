import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

from optparse import OptionParser
parser=OptionParser()

parser.add_option("-f","--input_file",dest="input_file",default="",type="str")
parser.add_option("-l","--label",dest="label",default="",type="str")
(options,args)=parser.parse_args()


def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%d\n'%(line))

try:
    file_in = open(options.input_file,"r")
except:
    print "errors!"

List = []

for line in file_in:
    List.append(int(line.replace("\n","")))
List.sort()

print len(List)

write_to_file('%s_sorted.list'%(options.input_file.split(".")[0]),List)
