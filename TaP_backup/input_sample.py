isUpdate = True
isUpdate = False

def Load_json(dic_name):
	return eval(open(dic_name).read().replace("\n",""))

sample_dic={
"runD":{
	"isFromRoot":True,
	"input_file_dir":"data_2017D_SingleElectron",
	"isData":True,
	"lumi":3.93,
	"N_total": 0.0,
	"hist":{},
	"isUpdate":isUpdate
	},
}
