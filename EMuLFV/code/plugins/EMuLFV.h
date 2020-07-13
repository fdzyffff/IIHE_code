// -*- C++ -*-
//
// Package:    Plots/EMuLFV
// Class:      EMuLFV
// 
/**\class EMuLFV EMuLFV.cc Plots/EMuLFV/plugins/EMuLFV.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  kaur amandeepkalsi
//         Created:  Fri, 11 Dec 2015 06:28:12 GMT
//
//


// system include files
#include <memory>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <vector>                                                                  
#include <TTree.h>
#include <TBranch.h>
#include <TH1.h>
#include <TH2.h>
#include <TLorentzVector.h>
#include <iostream>
#include <cstring>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <map>
#include <sys/stat.h>
#include "TTreeReader.h"
#include "TTreeReaderValue.h"
#include "TTreeReaderArray.h"
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "TGraphErrors.h"
#include "TF1.h"
//#include "TF2.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"           
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/SimpleJetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/SimpleJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"

#include "LHAPDF/LHAPDF.h"

#include "IIHENtuples.h"
#include "SFs.h"

//#include "RoccoR.h"
const float m_el = 0.000511 ;
const float m_mu = 0.10565837;
//
// class declaration
//
#ifdef __MAKECINT__
#pragma link C++ class vector<TLorentzVector>+;
#endif
using namespace std;
template <typename T>
struct SortByPt
{    
	bool operator () (const T& a, const T& b) const {
		return a.first.Pt() > b.first.Pt();
	}  

};   

class EMuLFV : public edm::EDAnalyzer {
	public:
		explicit EMuLFV(const edm::ParameterSet&);
		~EMuLFV();

		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob() override;
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		virtual void endJob() override;
		void Fill_histo(vector<TH1D*> histo_vector, float final_weight, IIHENtuples* my_iihe);
		vector<TH1D*> make_histo(TString histoName);
		double get_bin_width(TH1D* h1, float value);

		//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
		//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
		//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
		//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

		// ----------member data ---------------------------
		//
		edm::Service<TFileService> fs;   
		TTree *myTree;
		std::vector<LHAPDF::PDF*> pdf;
		double AlphaS(double scale);
		//TTree *outTree;
        vector<TString> hist_name;
        vector<TString> h_nominal_name;
        vector<TString> h_pdf_name;
        vector<TString> h_other_name;
        vector<vector<TH1D*>> hist_nominal;
        vector<vector<TH1D*>> hist_pdf;
        vector<vector<TH1D*>> hist_other;//

		bool dataset_isMuon;
		bool isData;
		bool isDY;
		bool isTTbar;
		bool isWW;
		bool ttbar_reweight;
		bool isFake_e;
		bool isFake_mu;
		bool useSYS;
		bool usePDF;
		string year;
		string InputFile;

		//IIHENtuples* my_iihe;
};
