import ROOT
import os
from optparse import OptionParser
from input_card import *

parser=OptionParser()
parser.add_option("-o","--output_dir",dest="output_dir",default="output_plot",type="str")

(options,args)=parser.parse_args()

def my_mkdir(dir_str):
	tmp_list = dir_str.split("/")
	tmp_dir = ""
	for part in tmp_list:
		if len(part)>0:
			tmp_dir = os.path.join(tmp_dir,part)
			try:os.mkdir(tmp_dir)
			except:pass

def my_walk_dir(my_dir,my_list,list_type=0):
	for tmp_file in os.listdir(my_dir):
		tmp_file_name = my_dir+'/'+tmp_file
		if os.path.isfile(tmp_file_name):
			if not '.png'		in tmp_file_name:continue
			if list_type == 1:
				my_list.append(tmp_file)
			elif list_type == 2:
				if my_dir in my_list:continue
				my_list.append(my_dir)
			else:
				my_list.append(tmp_file_name)
		else:
			my_walk_dir(tmp_file_name,my_list)
	return my_list

def main():
	for part in os.listdir("./"):
		if (not os.path.isfile(part)) and ("_" + part.split("_")[-1]) in cut_dic:
			# mkdir
			dir_list = []
			my_walk_dir(part, dir_list, 2)
			for dir_name in dir_list:
				print dir_name
				my_mkdir(os.path.join(options.output_dir,dir_name))

			file_list = []
			my_walk_dir(part, file_list)
			for filename in file_list:
				os.system("cp %s %s"%(filename, os.path.join(options.output_dir,filename))) 
	
main()
