import sys
try:
    sys.path.append('C:/root_v5.34.30/bin')
except:
    pass
import ROOT

List_file = 'event_list.txt'

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
        tmp_file.write('%d %d %d \n'%(line[0],line[1],line[2]))

List_from_soren = []
for Line in open(List_file,'r'):
    if '#' in Line:continue
    #print Line
    line = Line.split(',')
    runnr = getnumberfromstr(line[1])
    lsnr = getnumberfromstr(line[2])
    eventnr = getnumberfromstr(line[3])
    tmp_list = [int(runnr), int(lsnr), int(eventnr)]
    List_from_soren.append(tmp_list)
print '************ read from file finish **************'

List_from_soren.sort()

print len(List_from_soren)

write_to_file('soren_result.list',List_from_soren)

print List_from_soren[1]
