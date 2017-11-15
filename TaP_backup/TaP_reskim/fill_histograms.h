//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Dec 10 13:36:52 2015 by ROOT version 6.02/05
// from TTree tap/Streamlined tag and probe
// found on file: ZToEE.root
//////////////////////////////////////////////////////////

#ifndef fill_histograms_h
#define fill_histograms_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class fill_histograms {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Float_t         mee;
   Int_t           OS;
   Int_t           pv_n;
   Int_t           PU_true;
   Float_t         w_PU_golden;
   Float_t         w_PU_silver;
   Float_t         w_PU_silver_down;
   Float_t         w_PU_silver_up;
   Float_t         w_PU_combined;
   
   Int_t           HLT_Ele27;
   Float_t         p_Et;
   Float_t         p_eta;
   Float_t         p_phi;
   Float_t         p_Et35;
   Float_t         p_Et20;
   Int_t           p_charge;
   Int_t           p_region;
   Int_t           p_ID_tag;
   Int_t           p_ID_noDEtaIn;
   Int_t           p_ID_EcalDriven;
   Int_t           p_ID_noIsolation;
   Int_t           p_ID_nominal;
   Int_t           p_truthmatched;
   
   Float_t         t_Et;
   Float_t         t_eta;
   Float_t         t_phi;
   Float_t         t_Et35;
   Float_t         t_Et20;
   Int_t           t_charge;
   Int_t           t_region;
   Int_t           t_ID_tag;
   Int_t           t_ID_noDEtaIn;
   Int_t           t_ID_EcalDriven;
   Int_t           t_ID_noIsolation;
   Int_t           t_ID_nominal;
   Int_t           t_truthmatched;
   
   Float_t w_PU[5] ;

   // List of branches
   TBranch        *b_mee;   //!
   TBranch        *b_OS;   //!
   TBranch        *b_pv_n;   //!
   TBranch        *b_PU_true;   //!
   
   TBranch        *b_w_PU_golden;   //!
   TBranch        *b_w_PU_silver;   //!
   TBranch        *b_w_PU_silver_down;   //!
   TBranch        *b_w_PU_silver_up;   //!
   TBranch        *b_w_PU_combined;   //!
   
   TBranch        *b_HLT_Ele27;   //!
   TBranch        *b_p_Et;   //!
   TBranch        *b_p_eta;   //!
   TBranch        *b_p_phi;   //!
   TBranch        *b_p_Et35;   //!
   TBranch        *b_p_Et20;   //!
   TBranch        *b_p_charge;   //!
   TBranch        *b_p_region;   //!
   TBranch        *b_p_ID_tag;   //!
   TBranch        *b_p_ID_noDEtaIn;   //!
   TBranch        *b_p_ID_EcalDriven;   //!
   TBranch        *b_p_ID_noIsolation;   //!
   TBranch        *b_p_ID_nominal;   //!
   TBranch        *b_p_truthmatched;   //!
   
   TBranch        *b_t_Et;   //!
   TBranch        *b_t_eta;   //!
   TBranch        *b_t_phi;   //!
   TBranch        *b_t_Et35;   //!
   TBranch        *b_t_Et20;   //!
   TBranch        *b_t_charge;   //!
   TBranch        *b_t_region;   //!
   TBranch        *b_t_ID_tag;   //!
   TBranch        *b_t_ID_noDEtaIn;   //!
   TBranch        *b_t_ID_EcalDriven;   //!
   TBranch        *b_t_ID_noIsolation;   //!
   TBranch        *b_t_ID_nominal;   //!
   TBranch        *b_t_truthmatched;   //!

   fill_histograms(TTree *tree=0);
   virtual ~fill_histograms();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TString);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef fill_histograms_cxx
fill_histograms::fill_histograms(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("ZToEE.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("ZToEE.root");
      }
      f->GetObject("tap",tree);

   }
   Init(tree);
}

fill_histograms::~fill_histograms()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t fill_histograms::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t fill_histograms::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void fill_histograms::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("mee"    , &mee    , &b_mee    );
   fChain->SetBranchAddress("OS"     , &OS     , &b_OS     );
   fChain->SetBranchAddress("pv_n"   , &pv_n   , &b_pv_n   );
   fChain->SetBranchAddress("PU_true", &PU_true, &b_PU_true);
   fChain->SetBranchAddress("w_PU_golden"     , &w_PU[0], &b_w_PU_golden     );
   fChain->SetBranchAddress("w_PU_silver"     , &w_PU[1], &b_w_PU_silver     );
   fChain->SetBranchAddress("w_PU_combined"   , &w_PU[2], &b_w_PU_combined   );
   fChain->SetBranchAddress("w_PU_silver_down", &w_PU[3], &b_w_PU_silver_down);
   fChain->SetBranchAddress("w_PU_silver_up"  , &w_PU[4], &b_w_PU_silver_up  );
   
   
   fChain->SetBranchAddress("HLT_Ele27", &HLT_Ele27, &b_HLT_Ele27);
   fChain->SetBranchAddress("p_Et"     , &p_Et     , &b_p_Et     );
   fChain->SetBranchAddress("p_eta"    , &p_eta    , &b_p_eta    );
   fChain->SetBranchAddress("p_phi"    , &p_phi    , &b_p_phi    );
   fChain->SetBranchAddress("p_Et35"   , &p_Et35   , &b_p_Et35   );
   fChain->SetBranchAddress("p_Et20"   , &p_Et20   , &b_p_Et20   );
   fChain->SetBranchAddress("p_charge" , &p_charge , &b_p_charge );
   fChain->SetBranchAddress("p_region" , &p_region , &b_p_region );
   fChain->SetBranchAddress("p_ID_tag" , &p_ID_tag , &b_p_ID_tag );
   fChain->SetBranchAddress("p_ID_noDEtaIn"   , &p_ID_noDEtaIn   , &b_p_ID_noDEtaIn   );
   fChain->SetBranchAddress("p_ID_EcalDriven" , &p_ID_EcalDriven , &b_p_ID_EcalDriven );
   fChain->SetBranchAddress("p_ID_noIsolation", &p_ID_noIsolation, &b_p_ID_noIsolation);
   fChain->SetBranchAddress("p_ID_nominal"    , &p_ID_nominal    , &b_p_ID_nominal    );
   fChain->SetBranchAddress("p_truthmatched"  , &p_truthmatched  , &b_p_truthmatched  );
   
   fChain->SetBranchAddress("t_Et"     , &t_Et     , &b_t_Et     );
   fChain->SetBranchAddress("t_eta"    , &t_eta    , &b_t_eta    );
   fChain->SetBranchAddress("t_phi"    , &t_phi    , &b_t_phi    );
   fChain->SetBranchAddress("t_Et35"   , &t_Et35   , &b_t_Et35   );
   fChain->SetBranchAddress("t_Et20"   , &t_Et20   , &b_t_Et20   );
   fChain->SetBranchAddress("t_charge" , &t_charge , &b_t_charge );
   fChain->SetBranchAddress("t_region" , &t_region , &b_t_region );
   fChain->SetBranchAddress("t_ID_tag" , &t_ID_tag , &b_t_ID_tag );
   fChain->SetBranchAddress("t_ID_noDEtaIn"   , &t_ID_noDEtaIn   , &b_t_ID_noDEtaIn   );
   fChain->SetBranchAddress("t_ID_EcalDriven" , &t_ID_EcalDriven , &b_t_ID_EcalDriven );
   fChain->SetBranchAddress("t_ID_noIsolation", &t_ID_noIsolation, &b_t_ID_noIsolation);
   fChain->SetBranchAddress("t_ID_nominal"    , &t_ID_nominal    , &b_t_ID_nominal    );
   fChain->SetBranchAddress("t_truthmatched"  , &t_truthmatched  , &b_t_truthmatched  );
   
   Notify();
}

Bool_t fill_histograms::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void fill_histograms::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t fill_histograms::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef fill_histograms_cxx
