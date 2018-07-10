import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

List_file = 'events_ele_et_fix.txt'

def getnumberfromstr(str_in):
    str_in = str_in.replace(' ',"")
    str_out=''
    for i in range(len(str_in)):
        if str_in[i].isdigit() or str_in[i] == '.':
            str_out = str_out + str_in[i]
    return str_out

def write_to_file(filename, my_list):
    tmp_file = open(filename,'w')
    for line in my_list:
        tmp_file.write('%s\n'%(line))

def read_from_file(filename):
    tmp_file = open(filename)
    line_list = []
    for line in tmp_file:
        line_list.append(line.replace("\n","")[:-1])
    return line_list

# main #
List_from_soren = []
soren_list = read_from_file('only_only_soren_ele_result.list')
for Line in open(List_file,'r'):
    if '#' in Line:continue
    #print Line
    line = Line.split(',')
    runnr = getnumberfromstr(line[1])
    lsnr = getnumberfromstr(line[2])
    eventnr = getnumberfromstr(line[3])
    tmp_str = '%s %s %s'%(str(runnr), str(lsnr), str(eventnr))
    #print tmp_str
    if tmp_str in soren_list:
        List_from_soren.append(Line.replace('\n',''))
print '************ read from file finish **************'

List_from_soren.sort()

print len(List_from_soren)

write_to_file('missed_from_soren_result.list',List_from_soren)
