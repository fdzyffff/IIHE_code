import os
import sys

def write_to_file(filename, line_list):
    tmp_file = open(filename,'w')
    for line in line_list:
        tmp_file.write('%s\n'%(line))

def read_from_file(filename):
    tmp_file = open(filename)
    line_list = []
    for line in tmp_file:
        line_list.append(line.replace("\n",""))
    return line_list

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]
out_file_name1 = "only_"+sys.argv[1]
out_file_name2 = "only_"+sys.argv[2]
line_list_1 = read_from_file(file_name1)
line_list_2 = read_from_file(file_name2)

only_line_list_1 = []
only_line_list_2 = []
n_lines = 0
for line in line_list_1:
    if not line in line_list_2:
        only_line_list_1.append(line)
    if n_lines%10000 == 0:
        print "%d / %d processed in file : %s"%(n_lines, len(line_list_1), file_name1)
    n_lines +=1

n_lines = 0
for line in line_list_2:
    if not line in line_list_1:
        only_line_list_2.append(line)
    if n_lines%10000 == 0:
        print "%d / %d processed in file : %s"%(n_lines, len(line_list_2), file_name2)
    n_lines +=1

print "%d / %d in file: %s, output to %s"%(len(only_line_list_1), len(line_list_1), file_name1, out_file_name1)
print "%d / %d in file: %s, output to %s"%(len(only_line_list_2), len(line_list_2), file_name2, out_file_name2)
write_to_file(out_file_name1, only_line_list_1)
write_to_file(out_file_name2, only_line_list_2)
