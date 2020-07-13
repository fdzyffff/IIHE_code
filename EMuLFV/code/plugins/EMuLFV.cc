// change done 7 July 2018 -- add >= 1 bjets requirement
#include "EMuLFV.h"
//#include "LHAPDF/LHAPDF.h"

using namespace std;
using namespace LHAPDF;

EMuLFV::EMuLFV(const edm::ParameterSet& iConfig)

{
	dataset_isMuon = iConfig.getParameter<bool>("dataset_isMuon");
	isData = iConfig.getParameter<bool>("isData");
	isDY = iConfig.getParameter<bool>("isDY");
	isTTbar = iConfig.getParameter<bool>("isTTbar");
	isWW = iConfig.getParameter<bool>("isWW");
	ttbar_reweight = iConfig.getParameter<bool>("ttbar_reweight");
	isFake_e = iConfig.getParameter<bool>("isFake_e");
	isFake_mu = iConfig.getParameter<bool>("isFake_mu");
	year = iConfig.getParameter<string>("year");
	InputFile = iConfig.getParameter<string>("InputFile"); 
	useSYS = iConfig.getParameter<bool>("useSYS");
	usePDF = iConfig.getParameter<bool>("usePDF");
}


EMuLFV::~EMuLFV()
{

	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)

}


//
// member functions
//
// ------------ method called once each job just before starting event loop  ------------


void 
EMuLFV::beginJob()
{
	std::cout<<"InputFile::"<<InputFile<< std::endl;

	//outTree = fs->make<TTree>("outTree", "outTree");
 
	//for(unsigned int i = 0; i < 101 ; i++ ) array_sumweights[i] = 0;
	//for(unsigned int i = 0; i < 4 ; i++ ) array_scaleweights[i] = 0;

	h_nominal_name.push_back("nominal");
	if (!(isFake_e || isFake_mu) && !isData && useSYS) {
		h_nominal_name.push_back("top_w_up");
		h_nominal_name.push_back("top_w_down");
		h_nominal_name.push_back("top_pdf_up");
		h_nominal_name.push_back("top_pdf_down");
		h_nominal_name.push_back("top_qs_up");
		h_nominal_name.push_back("top_qs_down");
		h_nominal_name.push_back("pu_w_up");
		h_nominal_name.push_back("pu_w_down");
		h_nominal_name.push_back("mu_trig_up");
		h_nominal_name.push_back("mu_trig_down");
		h_nominal_name.push_back("mu_id_up");
		h_nominal_name.push_back("mu_id_down");
		h_nominal_name.push_back("mu_iso_up");
		h_nominal_name.push_back("mu_iso_down");
		h_nominal_name.push_back("ele_id_up");
		h_nominal_name.push_back("ele_id_down");
		h_nominal_name.push_back("ele_reco_up");
		h_nominal_name.push_back("ele_reco_down");

		h_other_name.push_back("mu_pt_scale_up");
		//h_other_name.push_back("mu_pt_scale_down");
		h_other_name.push_back("mu_pt_res_up");
		h_other_name.push_back("ele_et_scale_up");
		h_other_name.push_back("ele_et_scale_down");
		h_other_name.push_back("ele_et_res_up");
	}
	if (!isData && usePDF) {
		for(int in = 0; in < 101; in++){
			//pdf.push_back(LHAPDF::mkPDF("NNPDF31_nnlo_hessian_pdfas", in));//NNPDF23_lo_as_0130_qed", in )) ;//NNPDF30_lo_as_0130", in)) ;
			pdf.push_back(LHAPDF::mkPDF("NNPDF30_nlo_as_0118", in));
			h_pdf_name.push_back("pdf"+to_string(in));
			//std::cout<<"h_pdf_name:: "<< "pdf"+to_string(in) << std::endl;
		}
	}

	hist_name.push_back("ele_pt");
	hist_name.push_back("ele_eta");
	hist_name.push_back("ele_phi");
	hist_name.push_back("mu_pt");
	hist_name.push_back("mu_eta");
	hist_name.push_back("mu_phi");
	hist_name.push_back("M_emu");
	hist_name.push_back("M_emu_Ml");
	hist_name.push_back("pv_n");
	hist_name.push_back("sumOfWeights");

	for (unsigned int iHisto = 0; iHisto<hist_name.size(); ++iHisto) {
		std::cout<<"HistoName:: "<< hist_name[iHisto] << std::endl;
	}
	for(unsigned int j = 0; j <h_nominal_name.size(); j++){  
		hist_nominal.push_back(make_histo(h_nominal_name.at(j)));
	}
	for(unsigned int j = 0; j <h_other_name.size(); j++){  
		hist_other.push_back(make_histo(h_other_name.at(j)));
	}
	for(unsigned int j = 0; j <h_pdf_name.size(); j++){  
		hist_pdf.push_back(make_histo(h_pdf_name.at(j)));
	}

	for(unsigned int j = 0; j <h_nominal_name.size(); j++){ 
		std::cout<<"~~("<<hist_nominal.at(j).size()<<")~~HistoType:: "<< h_nominal_name.at(j) << std::endl;
	}
	for(unsigned int j = 0; j <h_other_name.size(); j++){  
		std::cout<<"~~("<<hist_other.at(j).size()<<")~~HistoType:: "<< h_other_name.at(j) << std::endl;
	}
	for(unsigned int j = 0; j <h_pdf_name.size(); j++){  
		std::cout<<"~~("<<hist_pdf.at(j).size()<<")~~HistoType:: "<< h_pdf_name.at(j) << std::endl;
	}
}

// ------------ method called for each event  ------------
void
EMuLFV::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

	using namespace edm;

	std::cout<<"datafile::"<<InputFile<<std::endl;
	TFile *file_in=TFile::Open(InputFile.c_str(),"READ");


	TTree* treePtr = (TTree*) file_in->Get("IIHEAnalysis"); 
	IIHENtuples* my_iihe = new IIHENtuples();
	my_iihe->fChain = treePtr ;
	my_iihe->isData = isData ;
	my_iihe->isDY = isDY ;
	my_iihe->isTTbar = isTTbar ;
	my_iihe->isWW = isWW ;
	my_iihe->runNo1 = 0 ;
	my_iihe->runNo2 = 999999 ;
	my_iihe->No_print = 0 ;
	my_iihe->mc_str = "none" ;
	my_iihe->sys_str = "sys_str" ;
	my_iihe->triggerVersion = 0 ;
	my_iihe->year = year;
	my_iihe->ttbar_reweight = ttbar_reweight;
	my_iihe->WW_shape = false;
	my_iihe->isFake_e = isFake_e;
	my_iihe->isFake_mu = isFake_mu;
	my_iihe->sys_mu_pt_scale_up = false;
	my_iihe->sys_mu_pt_scale_down = false;
	my_iihe->sys_mu_pt_res_up = false;
	my_iihe->sys_ele_et_res_up = false;
	my_iihe->sys_ele_et_scale_up = false;
	my_iihe->sys_ele_et_scale_down = false;

	my_iihe->Init();

	std::cout << "useSYS : "<< useSYS << std::endl;
	std::cout << "usePDF : "<< usePDF << std::endl;
	SFs my_sf;
	std::cout << "entries in tree : "<< my_iihe->GetEntries() << std::endl;
	//bool print_tmp = true;
	for (int iEntry = 0; iEntry < my_iihe->GetEntries(); iEntry++)
	{
		my_iihe->GetEntry(iEntry);

		vector<float> pdfweights;
		if (usePDF) {
			//std::cout<<"ids : " << my_iihe->mc_id_first << " : "<< my_iihe->mc_x_first <<" : "<< my_iihe->mc_scalePDF <<" : "<< my_iihe->mc_id_second <<" : "<< my_iihe->mc_x_second << std::endl;
			float xfx1_3 = pdf.at(0)->xfxQ(my_iihe->mc_id_first,  my_iihe->mc_x_first, my_iihe->mc_scalePDF);
			float xfx2_3 = pdf.at(0)->xfxQ(my_iihe->mc_id_second,  my_iihe->mc_x_second, my_iihe->mc_scalePDF);
			//std::cout<< "first : "<<xfx1_3 << "second : " << xfx2_3 << std::endl;
			float w03 = xfx1_3*xfx2_3;
			float lhaweight3 = 0.0;
			for(unsigned int i = 0; i < pdf.size(); i++){
				float      xfx_1_3 = pdf.at(i)->xfxQ(my_iihe->mc_id_first, my_iihe->mc_x_first, my_iihe->mc_scalePDF);
				float      xfx_2_3 = pdf.at(i)->xfxQ(my_iihe->mc_id_second, my_iihe->mc_x_second, my_iihe->mc_scalePDF);
				float w_new3 = xfx_1_3*xfx_2_3;
				lhaweight3  = w_new3/w03;
	
				//std::cout<< "lhaweight: "<<lhaweight3 << ":" << "w_new : "<< w_new3 << "w0 : " << w03 << std::endl;
				pdfweights.push_back(lhaweight3);
				//if (print_tmp){cout<<"pdfweights "<<i<< ": "<<pdfweights.at(i);}
			}
		}
		//print_tmp = false;

		// normalization and factorization scale 
		vector<float> scale_weights;
		if (usePDF) {
			scale_weights.clear();
			double const scaleVarFactor = 2.;
			double scale= my_iihe->mc_scalePDF;
			double const alphaSNominal = AlphaS(scale);
			float w_scale_1 = std::pow(AlphaS(scale * scaleVarFactor) / alphaSNominal, 2) ;
			float w_scale_2 = std::pow(AlphaS(scale / scaleVarFactor) / alphaSNominal, 2);
	
			double const pdfNominal = pdf.at(0)->xfxQ(my_iihe->mc_id_first,  my_iihe->mc_x_first, my_iihe->mc_scalePDF) * pdf.at(0)->xfxQ(my_iihe->mc_id_second,  my_iihe->mc_x_second, my_iihe->mc_scalePDF) ;
			float w_scale_3 =  pdf.at(0)->xfxQ(my_iihe->mc_id_first,  my_iihe->mc_x_first, my_iihe->mc_scalePDF * scaleVarFactor) * pdf.at(0)->xfxQ(my_iihe->mc_id_second,  my_iihe->mc_x_second, my_iihe->mc_scalePDF * scaleVarFactor)/ pdfNominal;
	
			float w_scale_4 = pdf.at(0)->xfxQ(my_iihe->mc_id_first,  my_iihe->mc_x_first, my_iihe->mc_scalePDF/scaleVarFactor) * pdf.at(0)->xfxQ(my_iihe->mc_id_second,  my_iihe->mc_x_second, my_iihe->mc_scalePDF / scaleVarFactor) / pdfNominal;
	
			scale_weights.push_back(w_scale_1);
			scale_weights.push_back(w_scale_2);
			scale_weights.push_back(w_scale_3);
			scale_weights.push_back(w_scale_4);
			
			//if(!isdata) h_control[4]->Fill(Mass,my_iihe->mc_w_sign);
		}

		bool trigger_fired= false;
		bool muon_trigger_fired= false;
		if (isData){
			if (year == "2016"){
				if (dataset_isMuon) {
					trigger_fired =  my_iihe->Muon50_trig_fire || my_iihe->TkMu50_trig_fire;
				} else {
					trigger_fired =  !(my_iihe->Muon50_trig_fire || my_iihe->TkMu50_trig_fire) && my_iihe->Photon175_trig_fire;
				}
			}
		} else {
			if (year == "2016"){
				trigger_fired =  my_iihe->Muon50_trig_fire || my_iihe->TkMu50_trig_fire || my_iihe->Photon175_trig_fire;
				muon_trigger_fired = my_iihe->Muon50_trig_fire || my_iihe->TkMu50_trig_fire;
			}
		}

		if(!trigger_fired) continue;

		//~~~~~~~~~~~~~~~~~~~~ run 1 event ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		if (!my_iihe->Loop()) continue;
		my_iihe->displayProgress(iEntry, my_iihe->GetEntries());
		//~~~~~~~~~~~~~~~~~~~~ Scale Factor && weight, will be override by next step ~~~~~~~~~~~~~~~~~~~~~~~~~~~
		float sf_weight = 1.0;
		float event_weight = 1.0;
		float final_weight = 1.0;
		//~~~~~~~~~~~~~~~~~~~~ Fill nominal and common sys ~~~~~~~~~~~~~~~~~~~~~~~~~~~
		for(unsigned int j = 0; j <h_nominal_name.size(); j++){

			if (h_nominal_name.at(j) == "nominal") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "top_w_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_ts1_up * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "top_w_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_ts1_down * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "top_pdf_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_top_PDF_up * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "top_pdf_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_top_PDF_down * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "top_qs_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_top_Qscale_up * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "top_qs_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_top_Qscale_down * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "pu_w_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_up_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "pu_w_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "ele_reco_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "up", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "ele_reco_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "down", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "ele_id_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "up", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "ele_id_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "down", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "mu_trig_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "up", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "mu_trig_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "down", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "mu_id_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "up", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "mu_id_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "down", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "mu_iso_up") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "up", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
			if (h_nominal_name.at(j) == "mu_iso_down") {
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "down", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_nominal[j], final_weight, my_iihe);
			}
		}

		//~~~~~~~~~~~~~~~~~~~~ Fill other sys ~~~~~~~~~~~~~~~~~~~~~~~~~~~
		for(unsigned int j = 0; j <h_other_name.size(); j++){
			if (h_other_name.at(j) == "mu_pt_scale_up") {
				my_iihe->sys_mu_pt_scale_up = true;
				my_iihe->sys_mu_pt_scale_down = false;
				my_iihe->sys_mu_pt_res_up = false;
				my_iihe->sys_ele_et_scale_up = false;
				my_iihe->sys_ele_et_scale_down = false;
				my_iihe->sys_ele_et_res_up = false;
				my_iihe->Loop();
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_other[j], final_weight, my_iihe);
			}
			if (h_other_name.at(j) == "mu_pt_scale_down") {
				my_iihe->sys_mu_pt_scale_up = false;
				my_iihe->sys_mu_pt_scale_down = true;
				my_iihe->sys_mu_pt_res_up = false;
				my_iihe->sys_ele_et_scale_up = false;
				my_iihe->sys_ele_et_scale_down = false;
				my_iihe->sys_ele_et_res_up = false;
				my_iihe->Loop();
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_other[j], final_weight, my_iihe);
			}
			if (h_other_name.at(j) == "mu_pt_res_up") {
				my_iihe->sys_mu_pt_scale_up = false;
				my_iihe->sys_mu_pt_scale_down = false;
				my_iihe->sys_mu_pt_res_up = true;
				my_iihe->sys_ele_et_scale_up = false;
				my_iihe->sys_ele_et_scale_down = false;
				my_iihe->sys_ele_et_res_up = false;
				my_iihe->Loop();
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_other[j], final_weight, my_iihe);
			}
			if (h_other_name.at(j) == "ele_et_scale_up") {
				my_iihe->sys_mu_pt_scale_up = false;
				my_iihe->sys_mu_pt_scale_down = false;
				my_iihe->sys_mu_pt_res_up = false;
				my_iihe->sys_ele_et_scale_up = true;
				my_iihe->sys_ele_et_scale_down = false;
				my_iihe->sys_ele_et_res_up = false;
				my_iihe->Loop();
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_other[j], final_weight, my_iihe);
			}
			if (h_other_name.at(j) == "ele_et_scale_down") {
				my_iihe->sys_mu_pt_scale_up = false;
				my_iihe->sys_mu_pt_scale_down = false;
				my_iihe->sys_mu_pt_res_up = false;
				my_iihe->sys_ele_et_scale_up = false;
				my_iihe->sys_ele_et_scale_down = true;
				my_iihe->sys_ele_et_res_up = false;
				my_iihe->Loop();
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_other[j], final_weight, my_iihe);
			}
			if (h_other_name.at(j) == "ele_et_res_up") {
				my_iihe->sys_mu_pt_scale_up = false;
				my_iihe->sys_mu_pt_scale_down = false;
				my_iihe->sys_mu_pt_res_up = false;
				my_iihe->sys_ele_et_scale_up = false;
				my_iihe->sys_ele_et_scale_down = false;
				my_iihe->sys_ele_et_res_up = true;
				my_iihe->Loop();
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight;
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_other[j], final_weight, my_iihe);
			}
		}

		//~~~~~~~~~~~~~~~~~~~~ Fill pdf sys ~~~~~~~~~~~~~~~~~~~~~~~~~~~
		if (usePDF) {
			for(unsigned int j = 0; j <h_pdf_name.size(); j++){
				if (!isData) {
					sf_weight = my_sf.get_ele_reco_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_ele_ID_sf(year, "nominal", my_iihe->ele_Et_out, my_iihe->ele_eta_out) *
								my_sf.get_mu_Trigger_sf(muon_trigger_fired, year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_ID_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_mu_Iso_sf(year, "nominal", my_iihe->muon_pt, my_iihe->muon_eta_out) *
								my_sf.get_NNPDF_sf(year, my_iihe->M_emu, ttbar_reweight);
					event_weight = my_iihe->w_PU_down_out * my_iihe->w_fake * my_iihe->w_top * my_iihe->w_other;
					final_weight = sf_weight * event_weight * pdfweights.at(j);
				} else {
					final_weight = my_iihe->w_fake;
				}
				Fill_histo(hist_pdf[j], final_weight, my_iihe);
			}
		}
	}
/*	if (usePDF) {
		for(unsigned int j = 0; j <h_pdf_name.size(); j++){
			for (unsigned int i_name = 0; i_name < hist_name.size(); i_name++){
				cout<<"histpdf: "<<hist_pdf[j].at(i_name)->GetName()<<"  : "<<hist_pdf[j].at(i_name)->Integral()<<endl;
			}
		}
	}*/
	delete treePtr;
	delete my_iihe;
	//delete my_sf;
	file_in->Close();

}

// ------------ method called once each job just after ending the event loop  ------------
void 
EMuLFV::endJob() 
{
	;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
EMuLFV::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

vector<TH1D*> EMuLFV::make_histo(TString histoName) {
	vector<TH1D*> tmp_hist;
	float lep_pt[34] = {0};
	for (unsigned int i_bin = 31; i_bin<65; ++i_bin) {
		lep_pt[i_bin-31] = pow(1.12, i_bin);
	}
	float lep_m[41] = {50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600,
						680, 760, 820, 880, 940, 1000, 1150, 1300, 1450, 1600, 1850, 2100, 2600, 3100, 3600, 4100, 4700, 5500,
						6600, 8000};
	for (unsigned int i_name = 0; i_name < hist_name.size(); ++i_name) {
		if (hist_name.at(i_name) == "ele_pt") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 33, lep_pt));
		}
		if (hist_name.at(i_name) == "ele_eta") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 55, -2.75, 2.75));
		}
		if (hist_name.at(i_name) == "ele_phi") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 35, -3.5, 3.5));
		}
		if (hist_name.at(i_name) == "mu_pt") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 33, lep_pt));
		}
		if (hist_name.at(i_name) == "mu_eta") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 55, -2.75, 2.75));
		}
		if (hist_name.at(i_name) == "mu_phi") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 35, -3.5, 3.5));
		}
		if (hist_name.at(i_name) == "M_emu") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 40, lep_m));
		}
		if (hist_name.at(i_name) == "M_emu_Ml") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 80, 50, 4500));
		}
		if (hist_name.at(i_name) == "pv_n") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 100, 0, 100));
		}
		if (hist_name.at(i_name) == "sumOfWeights") {
			tmp_hist.push_back(fs->make<TH1D>(histoName+"_"+hist_name.at(i_name), histoName+"_"+hist_name.at(i_name) , 10, 0, 10));
		}
	}

	for (unsigned int i_name = 0; i_name<hist_name.size(); ++i_name) {
		tmp_hist.at(i_name)->Sumw2();
	}
	return tmp_hist;
}

void EMuLFV::Fill_histo(vector<TH1D*> histo_vector, float final_weight, IIHENtuples* my_iihe){
	for (unsigned int i_name = 0; i_name < hist_name.size(); i_name++){
		if (hist_name.at(i_name) == "ele_pt") {
			histo_vector.at(i_name)->Fill(my_iihe->ele_Et_out ,final_weight);
		}
		if (hist_name.at(i_name) == "ele_eta") {
			histo_vector.at(i_name)->Fill(my_iihe->ele_eta_out ,final_weight);
		}
		if (hist_name.at(i_name) == "ele_phi") {
			histo_vector.at(i_name)->Fill(my_iihe->ele_phi_out ,final_weight);
		}
		if (hist_name.at(i_name) == "mu_pt") {
			histo_vector.at(i_name)->Fill(my_iihe->muon_pt ,final_weight);
		}
		if (hist_name.at(i_name) == "mu_eta") {
			histo_vector.at(i_name)->Fill(my_iihe->muon_eta_out ,final_weight);
		}
		if (hist_name.at(i_name) == "mu_phi") {
			histo_vector.at(i_name)->Fill(my_iihe->muon_phi_out ,final_weight);
		}
		if (hist_name.at(i_name) == "M_emu") {
			histo_vector.at(i_name)->Fill(my_iihe->M_emu ,final_weight*get_bin_width(histo_vector.at(i_name), my_iihe->M_emu));
		}
		if (hist_name.at(i_name) == "M_emu_Ml") {
			histo_vector.at(i_name)->Fill(my_iihe->M_emu ,final_weight);
		}
		if (hist_name.at(i_name) == "pv_n") {
			histo_vector.at(i_name)->Fill(my_iihe->pv_n ,final_weight);
		}
		if (hist_name.at(i_name) == "sumOfWeights") {
			histo_vector.at(i_name)->Fill(final_weight);
		}
	}
}

double EMuLFV::get_bin_width(TH1D* h1, float value) 
{
    TAxis *Xaxis = h1->GetXaxis();
    double weight = 1.0;
    int NbinsX = Xaxis->GetNbins();
    float x_min = Xaxis->GetBinLowEdge(1);
    float x_max = Xaxis->GetBinLowEdge(NbinsX) + Xaxis->GetBinWidth(NbinsX);
    if(x_min < value && value < x_max) {
        weight = 1.0 / Xaxis->GetBinWidth( Xaxis->FindBin(value) );
    }
    return weight;
}

double EMuLFV::AlphaS(double scale)
{
	double const alpha0 = 0.118;//4;
	double const mZ = 91.199997; //91.1876;
	unsigned const nf = 5;//4;

	double const b0 = (33 - 2 * nf) / (12 * M_PI);
	return alpha0 / (1 + alpha0 * b0 * 2 * std::log(scale / mZ));
}

DEFINE_FWK_MODULE(EMuLFV);
