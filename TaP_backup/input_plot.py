run_label = "(2017 runD)"
plot_dic = {
"DouEle33_Et_barrel":{
	"hist":{
		"DouEle33Et_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle33Et_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle33Et_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[30, 45],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle33_CaloIdL_MW Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle33_Et_barrel",
		},
	},
"DouEle33_Et_endcap":{
	"hist":{
		"DouEle33Et_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle33Et_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle33Et_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[30, 45],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle33_CaloIdL_MW Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle33_Et_endcap",
		},
	},
"DouEle33_ID":{
	"hist":{
		"DouEle33ID_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','[0]',35,140],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.1,0.15,0.35,0.3],
				},
			},
		"DouEle33ID_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"endcap",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','[0]',35,140],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.4,0.15,0.75,0.3],
				},
			},
		},
	"para":{
		"legend":[0.12,0.35,0.3,0.45],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[35, 140],
		"yaxis":[0.9, 1.0],
		"title":"HLT_DoubleEle33_CaloIdL_MW ID effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle33_ID",
		},
	},
"DouEle33_barrel":{
	"hist":{
		"DouEle33_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle33_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle33_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[30, 45],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle33_CaloIdL_MW effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle33_barrel",
		},
	},
"DouEle33_endcap":{
	"hist":{
		"DouEle33_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle33_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle33_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',30,45],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[30, 45],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle33_CaloIdL_MW effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle33_endcap",
		},
	},
#DoubleEle33 vs pvn
"DouEle33_pvn_barrel":{
	"hist":{
		"DouEle33_pvn_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":False,
			},
		"DouEle33_pvn_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":False,
			},
		"DouEle33_pvn_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle33_CaloIdL_MW effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle33_pvn_barrel",
		},
	},
"DouEle33_pvn_endcap":{
	"hist":{
		"DouEle33_pvn_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":False,
			},
		"DouEle33_pvn_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":False,
			},
		"DouEle33_pvn_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle33_CaloIdL_MW effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle33_pvn_endcap",
		},
	},
#DouEle25
"DouEle25_Et_barrel":{
	"hist":{
		"DouEle25Et_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle25Et_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle25Et_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 40],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_Et_barrel",
		},
	},
"DouEle25_Et_endcap":{
	"hist":{
		"DouEle25Et_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle25Et_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle25Et_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 40],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_Et_endcap",
		},
	},
"DouEle25_ID":{
	"hist":{
		"DouEle25ID_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','[0]',25,130],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.1,0.15,0.35,0.3],
				},
			},
		"DouEle25ID_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"endcap",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','[0]',25,130],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.4,0.15,0.75,0.3],
				},
			},
		},
	"para":{
		"legend":[0.12,0.35,0.3,0.45],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[25, 130],
		"yaxis":[0.9, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW ID effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_ID",
		},
	},
"DouEle25_barrel":{
	"hist":{
		"DouEle25_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle25_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle25_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 40],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_barrel",
		},
	},
"DouEle25_endcap":{
	"hist":{
		"DouEle25_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"DouEle25_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"DouEle25_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,40],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 40],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_endcap",
		},
	},
#DoubleEle25 vs pvn
"DouEle25_pvn_barrel":{
	"hist":{
		"DouEle25_pvn_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":False,
			},
		"DouEle25_pvn_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":False,
			},
		"DouEle25_pvn_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_pvn_barrel",
		},
	},
"DouEle25_pvn_endcap":{
	"hist":{
		"DouEle25_pvn_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":False,
			},
		"DouEle25_pvn_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":False,
			},
		"DouEle25_pvn_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_pvn_endcap",
		},
	},
#DouEle25 given DiEle27CaloOnly vs pv_z
"DouEle25_pvz_barrel":{
	"hist":{
		"DouEle25_pvz_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":False,
			},
		"DouEle25_pvz_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":False,
			},
		"DouEle25_pvz_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[0, 10],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_pvz_barrel",
		},
	},
"DouEle25_pvz_endcap":{
	"hist":{
		"DouEle25_pvz_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":False,
			},
		"DouEle25_pvz_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":False,
			},
		"DouEle25_pvz_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[0, 10],
		"yaxis":[0.0, 1.0],
		"title":"HLT_DoubleEle25_CaloIdL_MW effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"DouEle25_pvz_endcap",
		},
	},
#Ele32 WPTight
"Ele32_Et":{
	"hist":{
		"Ele32Et_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',33,125],
				"fit_para":[0.8, 20, 16, 0.1, 35, 1],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele32Et_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',33,125],
				"fit_para":[0.8, 20, 16, 0.1, 35, 1],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		},
	"para":{
		"legend":[0.6,0.5,0.8,0.7],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[25, 125],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele32_WPTight Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele32_Et",
		},
	},
"Ele32_ID":{
	"hist":{
		"Ele32ID_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','[0]',25,125],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.1,0.15,0.35,0.3],
				},
			},
		"Ele32ID_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"endcap",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','[0]',25,125],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.4,0.15,0.75,0.3],
				},
			},
		},
	"para":{
		"legend":[0.12,0.35,0.3,0.45],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[25, 125],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele32_WPTight ID effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele32_ID",
		},
	},
"Ele32":{
	"hist":{
		"Ele32_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',33,125],
				"fit_para":[0.8, 20, 16, 0.1, 35, 1],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele32_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"endcap",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',33,125],
				"fit_para":[0.8, 20, 16, 0.1, 35, 1],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		},
	"para":{
		"legend":[0.6,0.5,0.8,0.7],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[25, 125],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele32_WPTight effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele32",
		},
	},
#Ele32_WPTight vs pvn
"Ele32_pvn":{
	"hist":{
		"Ele32_pvn_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":False,
			},
		"Ele32_pvn_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"endcap",
			"legend_order":2,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.6,0.5,0.8,0.7],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[25, 125],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele32_WPTight effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele32_pvn",
		},
	},
#Ele23_Ele12
"Ele23_Ele12_Et_Leg1_barrel":{
	"hist":{
		"Ele23_Ele12_EtLeg1_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_EtLeg1_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_EtLeg1_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 35],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Et_Leg1_barrel",
		},
	},
"Ele23_Ele12_Et_Leg1_endcap":{
	"hist":{
		"Ele23_Ele12_EtLeg1_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_EtLeg1_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_EtLeg1_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 35],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Et_Leg1_endcap",
		},
	},
"Ele23_Ele12_ID_Leg1":{
	"hist":{
		"Ele23_Ele12_IDLeg1_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','[0]',20,100],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.1,0.15,0.35,0.3],
				},
			},
		"Ele23_Ele12_IDLeg1_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"endcap",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','[0]',20,100],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.4,0.15,0.75,0.3],
				},
			},
		},
	"para":{
		"legend":[0.12,0.35,0.3,0.45],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 100],
		"yaxis":[0.9, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL ID effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_ID_Leg1_endcap",
		},
	},
"Ele23_Ele12_Leg1_barrel":{
	"hist":{
		"Ele23_Ele12_Leg1_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_Leg1_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_Leg1_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 35],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg1 effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg1_barrel",
		},
	},
"Ele23_Ele12_Leg1_endcap":{
	"hist":{
		"Ele23_Ele12_Leg1_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_Leg1_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_Leg1_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',20,35],
				"fit_para":[0.8, 23, 0.5, 0.2, 23, 2],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 35],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg1 effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg1_endcap",
		},
	},
"Ele23_Ele12_Et_Leg2_barrel":{
	"hist":{
		"Ele23_Ele12_EtLeg2_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_EtLeg2_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_EtLeg2_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[8, 22],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg2 Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Et_Leg2_barrel",
		},
	},
"Ele23_Ele12_Et_Leg2_endcap":{
	"hist":{
		"Ele23_Ele12_EtLeg2_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_EtLeg2_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_EtLeg2_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[8, 22],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg2 Et effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Et_Leg2_endcap",
		},
	},
"Ele23_Ele12_ID_Leg2":{
	"hist":{
		"Ele23_Ele12_IDLeg2_1":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"barrel",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','[0]',10,100],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.1,0.15,0.35,0.3],
				},
			},
		"Ele23_Ele12_IDLeg2_2":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"endcap",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','[0]',10,100],
				"fit_para":[0.9],
				"print_fit":True,
				"position":[0.4,0.15,0.75,0.3],
				},
			},
		},
	"para":{
		"legend":[0.12,0.35,0.3,0.45],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[10, 100],
		"yaxis":[0.9, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg2 ID effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_ID_Leg2_endcap",
		},
	},
"Ele23_Ele12_Leg2_barrel":{
	"hist":{
		"Ele23_Ele12_Leg2_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_Leg2_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_Leg2_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[8, 22],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg2 effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg2_barrel",
		},
	},
"Ele23_Ele12_Leg2_endcap":{
	"hist":{
		"Ele23_Ele12_Leg2_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_1','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.52,0.12,0.69,0.42]
				},
			},
		"Ele23_Ele12_Leg2_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_2','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.12,0.9,0.42]
				},
			},
		"Ele23_Ele12_Leg2_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":True,
			"fit_func":{
				"fit_function":['eff_func_3','0.5*[0]*(1+erf((x-[1])/(1.414*[2])))+0.5*[3]*(1+erf((x-[4])/(1.414*[5])))',8,22],
				"fit_para":[0.871, 26.106, 0.810, 0.127, 26.831, 2.014],
				"print_fit":True,
				"position":[0.7,0.45,0.9,0.75]
				},
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[8, 22],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg2 effciency ",
		"x_title":"E_{T}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg2_endcap",
		},
	},
#Ele23_Ele12 vs pvn
"Ele23_Ele12_Leg1_pvn_barrel":{
	"hist":{
		"Ele23_Ele12_Leg1_pvn_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg1_pvn_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg1_pvn_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg1 effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg1_pvn_barrel",
		},
	},
"Ele23_Ele12_Leg1_pvn_endcap":{
	"hist":{
		"Ele23_Ele12_Leg1_pvn_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg1_pvn_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg1_pvn_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg1 effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg1_pvn_endcap",
		},
	},
"Ele23_Ele12_Leg2_pvn_barrel":{
	"hist":{
		"Ele23_Ele12_Leg2_pvn_11":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"0.0 < |#eta| < 0.79",
			"legend_order":1,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg2_pvn_12":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"0.79 < |#eta| < 1.1",
			"legend_order":2,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg2_pvn_13":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"1.1 < |#eta| < 1.4442",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg2 effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg2_pvn_barrel",
		},
	},
"Ele23_Ele12_Leg2_pvn_endcap":{
	"hist":{
		"Ele23_Ele12_Leg2_pvn_21":{
			"Color":1,
			"MarkerStyle":22,
			"legend_title":"1.566 < |#eta| < 1.7",
			"legend_order":1,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg2_pvn_22":{
			"Color":2,
			"MarkerStyle":22,
			"legend_title":"1.7 < |#eta| < 2.1",
			"legend_order":2,
			"do_fit":False,
			},
		"Ele23_Ele12_Leg2_pvn_23":{
			"Color":4,
			"MarkerStyle":22,
			"legend_title":"2.1 < |#eta| < 2.5",
			"legend_order":3,
			"do_fit":False,
			},
		},
	"para":{
		"legend":[0.12,0.75,0.3,0.9],
		"text":[0.12,0.6,0.3,0.7],
		"xaxis":[20, 70],
		"yaxis":[0.0, 1.0],
		"title":"HLT_Ele23_Ele12_CaloIdL_TrackIdL Leg2 effciency ",
		"x_title":"N_{vtx}",
		"y_title":"Efficiency",
		"x_log":False,
		"y_log":False,
		"plot_name":"Ele23_Ele12_Leg2_pvn_endcap",
		},
	},
}
