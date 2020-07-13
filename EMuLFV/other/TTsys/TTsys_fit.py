import sys
try:
	sys.path.append("C:/root_v5.34.36/bin")
except:
	pass
import ROOT
import array

ROOT.gROOT.SetBatch(ROOT.kTRUE)

class my_fit():
	def __init__(self, root_file, gr_name, label):
		tmp_f1 = ROOT.TFile(root_file)
		self.input_gr = tmp_f1.Get(gr_name)
		tmp_f1.Close()
		self.label = label
		print self.label

	def run_fit(self):
		self.gr_fit = ROOT.TGraph()
		i_x = self.input_gr.GetX()
		i_y = self.input_gr.GetY()
		i_ye = self.input_gr.GetEYhigh()
		for i_point in range(self.input_gr.GetN()):
			self.gr_fit.SetPoint(i_point, i_x[i_point], i_y[i_point] + i_ye[i_point])
			print i_point, i_x[i_point], i_y[i_point] + i_ye[i_point]
		
		c1 = ROOT.TCanvas( 'c1', 'A Simple Graph with error bars', 50,50,865,780 )

		pad1=ROOT.TPad("pad1", "pad1", 0, 0.5, 1, 1.0 , 0)#used for ratio, the gr plot
		pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.45 , 0)#used for ratio, the fit text
		pad1.Draw()
		pad1.cd()
		self.input_gr.Draw("APE")
		#self.input_gr.GetYaxis().SetRangeUser(-2.0, 2.2)
		self.gr_fit.Draw("P")
		self.gr_fit.SetMarkerSize(0.5)
		self.gr_fit.SetMarkerStyle(21)
		self.gr_fit.SetMarkerColor(2)
		fit_function = "pol2"
		self.gr_fit.Fit(fit_function, "", "", 0, 2500)

		self.gr_fit.SetTitle(self.input_gr.GetTitle())
		self.gr_fit.GetXaxis().SetTitle(self.input_gr.GetXaxis().GetTitle())
		c1.Update()
		c1.cd()

		pad2.Draw()
		pad2.cd()

		fit_text = ROOT.TPaveText(0.1,0.1, 0.9,0.9,"blNDC")
		fit_text.SetBorderSize(0)
		fit_text.SetFillStyle(0)
		fit_text.SetTextAlign(12)
		fit_text.SetTextColor(2)
		fit_text.SetTextFont(42)
		fit_text.SetTextSize(0.1)
		fit_text.AddText("Fit Func : %s\n\n"%(fit_function))
		fit_text.AddText("")
		for i in range(6):
			fit_text.AddText('P%d  %0.4g'%(i, self.gr_fit.GetFunction(fit_function).GetParameter(i)))
		fit_text.Draw()
		c1.Print("fit_%s.png"%(self.label))
		c1.Close()

fit_instance = my_fit("TTSYS.root", "AEMll_PDF", "AEMll_PDF")
fit_instance.run_fit()

fit_instance = my_fit("TTSYS.root", "AEMll_QS", "AEMll_QS")
fit_instance.run_fit()
