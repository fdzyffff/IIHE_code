#include "stdio.h"
#include "TMinuit.h"
#include "Riostream.h"
#include "TLorentzVector.h"
#include "TGenPhaseSpace"
#include "TH1.h"
#include "TCanvas"
#include "TGraph"
#include "TGraphErrors"
#include "math.h"
#include "TF1.h"
#include "Math/WrappedTF1.h"
#include "Math/GaussIntegrator.h"
#include "TMath.h"
//void tt(*Double_t x, Double_t y);
static Double_t pi = 3.1415926;

/*static ofstream out_hc("plot_hc_out.txt","w");
static ofstream out_hc_part_1("plot_hc_part1_out.txt","w");
static ofstream out_hc_part_2("plot_hc_part2_out.txt","w");

static ofstream out_omega("plot_omega_out.txt","w");
static ofstream out_omega_part_1("plot_omega_part1_out.txt","w");
static ofstream out_omega_part_2("plot_omega_part2_out.txt","w");
*/

static  Double_t data_hc_x[100] = {0};
static  Double_t data_hc_y[100] = {0};
static  Double_t data_hc_xe[100] = {0};
static  Double_t data_hc_ye[100] = {0};


static  Double_t data_omega_x[100] = {0};
static  Double_t data_omega_y[100] = {0};
static  Double_t data_omega_xe[100] = {0};
static  Double_t data_omega_ye[100] = {0};

void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag);
Double_t my_cs_hc(Double_t mass, Double_t *par_list, bool my_write);
Double_t my_cs_omega(Double_t mass, Double_t *par_list, bool my_write);
void my_BW(Double_t mass, Double_t M, Double_t width, Double_t gaB, Double_t PS_mass, Double_t PS_M, Double_t &re, Double_t &im);
Double_t ps3(Double_t mass, Double_t m1, Double_t m2, Double_t m3);
Double_t ps2(Double_t mass, Double_t m1, Double_t m2);
void my_plot_hc(Double_t *par_list, Int_t nlines_hc, Double_t *data_hc_x, Double_t *data_hc_y, Double_t *data_hc_xe, Double_t *data_hc_ye);
void my_plot_omega(Double_t *par_list, Int_t nlines_omega, Double_t *data_omega_x, Double_t *data_omega_y, Double_t *data_omega_xe, Double_t *data_omega_ye);

void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag)
{
   Double_t par_list[10];
   par_list[0] = par[0];
   par_list[1] = par[1];
   par_list[2] = par[2];
   par_list[3] = par[3];
   par_list[4] = par[4];
   par_list[5] = par[5];
   par_list[6] = par[6];
   par_list[7] = par[7];
   par_list[8] = par[8];
   par_list[9] = par[9];
   Double_t likelihood = 0.0;
   Double_t likelihood_1 = 0.0;
   Double_t likelihood_2 = 0.0;
   Int_t i = 0;
   for(i=0;data_hc_x[i]>0;i++)
   {
      //printf("i = %d , data_hc_x[i] = %f\n",i,data_hc_x[i] );
      Double_t my_cs = my_cs_hc(data_hc_x[i],par_list,false);
      Double_t my_target_cs = data_hc_y[i];
      Double_t my_error = data_hc_ye[i];
      Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      likelihood_1 += my_value;
   }
   for(i=0;data_omega_x[i]>0;i++)
   {
      Double_t my_cs = my_cs_omega(data_omega_x[i],par_list,false);
      Double_t my_target_cs = data_omega_y[i];
      Double_t my_error = data_omega_ye[i];
      Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      likelihood_2 += my_value;
   }
   likelihood = likelihood_1 + likelihood_2;
//   if(min_li > likelihood)
//   {
//      print likelihood;
//      min_li = likelihood;
//  }
   printf("****likelihood: %f\n",likelihood );
   f = likelihood;
}

Double_t my_cs_hc(Double_t mass, Double_t *par_list, bool my_write)
{
   Double_t M1     = par_list[0];
   Double_t width1 = par_list[1];
   Double_t gaB1   = par_list[2];
   Double_t M2     = par_list[3];
   Double_t width2 = par_list[4];
   Double_t gaB2   = par_list[5];
   Double_t phase  = par_list[6];
   Double_t CC     = par_list[7];
   Double_t phi    = par_list[8];
   Double_t gaB3   = par_list[9];

   Double_t m1=0.13957018;
   Double_t m2=0.13957018;
   Double_t m3=3.52538;

   Double_t re, im, crossSection;
   Double_t re1, im1;
   Double_t re2, im2;

   Double_t ps3_mass = ps3(mass,m1,m2,m3);
   Double_t ps3_M1 = ps3(M1,m1,m2,m3);
   Double_t ps3_M2 = ps3(M2,m1,m2,m3);
   //ps3_mass = 1;
   //ps3_M1 = 1;
   //ps3_M2 = 1;
   //printf("PS_mass : %f ; PS_M1 : %f ; PS_M2 : %f\n",ps3_mass,ps3_M1,ps3_M2 );
   my_BW(mass,M1,width1,gaB1,ps3_mass,ps3_M1, re1, im1);
   my_BW(mass,M2,width2,gaB2,ps3_mass,ps3_M2, re2, im2);
   //my_BW(mass,M1,width1,gaB1,1,1, re1, im1);
   //my_BW(mass,M2,width2,gaB2,1,1, re2, im2);
   re=re1+re2*cos(phase)-im2*sin(phase);
   im=im1+im2*cos(phase)+re2*sin(phase);
   crossSection=(re**2+im**2)*(0.389379*10);
   return crossSection;
}

Double_t my_cs_omega(Double_t mass, Double_t *par_list, bool my_write)
{
   Double_t M1     = par_list[0];
   Double_t width1 = par_list[1];
   Double_t gaB1   = par_list[2];
   Double_t M2     = par_list[3];
   Double_t width2 = par_list[4];
   Double_t gaB2   = par_list[5];
   Double_t phase  = par_list[6];
   Double_t CC     = par_list[7];
   Double_t phi    = par_list[8];
   Double_t gaB3   = par_list[9];

   Double_t m1=3.41475;
   Double_t m2=0.782;

   Double_t re, im, crossSection, tt;
   Double_t re3 = 0;
   Double_t im3 = 0;
   Double_t ps2_mass = ps2(mass,m1,m2);
   Double_t ps2_M1 = ps2(M1,m1,m2);
   //printf("mass : %f\n",mass );
   my_BW(mass,M1,width1,gaB3,ps2_mass,ps2_M1, re3, im3);
   //printf("after bw : %f  ; %f\n",re3, im3 );
   tt = CC*sqrt(ps2_mass);
   //tt = 0;
   re=tt+re3*cos(phi)-im3*sin(phi);
   im=im3*cos(phi)+re3*sin(phi);
   crossSection=(re**2+im**2)*(0.389379*10.0);
   return crossSection;
}

void my_BW(Double_t mass, Double_t M, Double_t width, Double_t gaB, Double_t PS_mass, Double_t PS_M, Double_t &re, Double_t &im)
{
   Double_t s, f;
   s = mass*mass;
   f=sqrt((12*pi*gaB*width*PS_mass/(PS_M)));
   //printf("f: %f\n",f );
   //printf("gaB: %f\n",gaB );
   re=f*(s-M**2)/((s-M**2)**2+(M*width)**2);
   im=f*M*width*(-1.0)/((s-M**2)**2+(M*width)**2);
}


Double_t ps3(Double_t mass, Double_t m1, Double_t m2, Double_t m3)
{
/*   if (!gROOT->GetClass("TGenPhaseSpace")) gSystem->Load("libPhysics");

   Double_t masses[3] = {m3,m2,m1};

   TLorentzVector M(0.0, 0.0, 0.0,mass);
   //printf("###################%f\n",M->M() );

   TGenPhaseSpace event;
   event.SetDecay(M,3,masses);
   //return event.GetWtMax();
   return 1/mass;
*/
   TF1 f("PS3 Function", "sqrt((1-(([1]+x)/[0])**2) * (1-(([1]-x)/[0])**2) * (1-(([2]+[3])/x)**2) * (1-(([2]-[3])/x)**2))*x",(m3),(mass));
   f.SetParameters(mass, m1, m2, m3);
   //f.Draw();

   ROOT::Math::WrappedTF1 wf1(f);
   
   ROOT::Math::GaussIntegrator ig;
   
   ig.SetFunction(wf1);
   ig.SetRelTolerance(0.01);
   //ig.SetNumberPoints(20);
   
   Double_t ps3_factor;
   ps3_factor = ig.Integral((m2+m3),(mass-m1));
   
   return ps3_factor;

}

Double_t ps2(Double_t mass, Double_t m1, Double_t m2)
{
   Double_t t1, t2, ps_value;
   t1=1.0-(((m1+m2)/mass)**2);
   t2=1.0-(((m1-m2)/mass)**2);
   //printf("t1 ; %f ; t2 : %f\n",t1,t2 );

   ps_value=sqrt(t1*t2);
   ps_value=ps_value/(8*pi);
   return ps_value;
}

void my_plot_hc(Double_t *par_list, Int_t nlines_hc, Double_t *data_hc_x, Double_t *data_hc_y, Double_t *data_hc_xe, Double_t *data_hc_ye)
{
   TCanvas *c1 = new TCanvas("c1", "test_hc" , 200,10,700,500);
   TGraphErrors *gr_hc_data = new TGraphErrors(nlines_hc,data_hc_x,data_hc_y,data_hc_xe,data_hc_ye);
   //printf("n :%d",nlines_hc);
   gr_hc_data->Draw("AP");
   c1->Update();

   gr_hc_fit = new TGraph();
   Int_t i=1;
   Double_t mass;
   for(mass = 3.9; mass < 4.8; mass+= 0.001)
   {
      Double_t my_cs = my_cs_hc(mass,par_list,true);
      gr_hc_fit->SetPoint(i,mass,my_cs);
      i+=1;
   }
   gr_hc_fit->Draw("PC");
   c1->Update();
}

void my_plot_omega(Double_t *par_list, Int_t nlines_omega, Double_t *data_omega_x, Double_t *data_omega_y, Double_t *data_omega_xe, Double_t *data_omega_ye)
{
   TCanvas *c2 = new TCanvas( "c2", "test_omega" , 200, 10, 700, 500 );
   TGraphErrors *gr_omega_data = new TGraphErrors(nlines_omega,data_omega_x,data_omega_y,data_omega_xe,data_omega_ye);
   gr_omega_data->Draw("AP");
   TGraph *gr_omega_fit = new TGraph();
   Int_t i=1;
   Double_t mass;
   for(mass = 4.2; mass < 4.8; mass+= 0.001)
   {
      Double_t my_cs = my_cs_omega(mass,par_list,true);
      gr_omega_fit->SetPoint(i,mass,my_cs);
      i+=1;
      //out_omega << "%f\t%f\n";
   }
   //fclose(out_omega);
   //fclose(out_omega_part_1);
   //fclose(out_omega_part_2);
   gr_omega_fit->Draw("PC");
   c2->Update();
}

void my_plot_ps3()
{
   TCanvas *c3 = new TCanvas("c3", "test_ps3" , 200,10,700,500);

   gr_hc_fit = new TGraph();
   Int_t i=1;
   Double_t mass;
   Double_t m1=0.13957018;
   Double_t m2=0.13957018;
   Double_t m3=3.52538;

   for(mass = 3.9; mass < 5.4; mass+= 0.1)
   {
      Double_t my_cs = ps3(mass,m1,m2,m3);
      gr_hc_fit->SetPoint(i,mass,my_cs);
      i+=1;
   }
   gr_hc_fit->Draw("APC");
   c3->Update();
}

void tes()
{
   ifstream in1;
   ifstream in2;
   in1.open("4220_sigma_hc_new.dat");
   //in1.open("4220_sigma_hc.dat");
   in2.open("4220_sigma_omega_new.dat");
   

//input hc data
   Int_t nlines_hc = 0;
   Int_t ii=0;
   for(ii=0;1;ii++)
   {
      in1 >> data_hc_x[ii] >> data_hc_y[ii] >> data_hc_ye[ii] ;
      if(!in1.good())break;
      nlines_hc += 1;
   }
   in1.close();
   printf("hc data total lines : %d \n",nlines_hc);
//input omega data
   Int_t nlines_omega = 0;
   for(ii=0;1;ii++)
   {      
      in2 >> data_omega_x[ii] >> data_omega_y[ii] >> data_omega_ye[ii] ;
      if(!in2.good())break;
      nlines_omega += 1;
      printf("%d :%f\n",ii, data_omega_x[ii] );
   }
   printf("omega data total lines : %d \n",nlines_omega);
   in2.close();
//read input over

//start minuit
   TMinuit *gMinuit = new TMinuit(10);
   gMinuit->SetFCN( fcn );

   Int_t ierflg = 0;


 // Set starting values and step sizes for parameters
   Double_t para[10] = {4.213, 0.081, 0.68, 4.38, 0.142, 1.5, 3.5, 0.0, 0.2, 0.5};//new data result 2
   //Double_t para[10] = {4.2, 0.08, 0.5, 4.39, 0.12, 1.2, 3.1, 0.0, 0.0, 0.3};//new data result 1
   //Double_t para[10] = {4.23, 0.03, 0.02, 4.29, 0.2, 1.4, -0.6, 0.0, 0.2, 0.25};//old data result 2
   Double_t para_step[10] = {0.001, 0.001, 0.01, 0.001, 0.001, 0.01, 0.001, 0.01, 0.1, 0.01};

   gMinuit->mnparm( 0, "M1"      , para[0], para_step[0], 4.2, 4.3, ierflg);//4220
   gMinuit->mnparm( 1, "width1"  , para[1], para_step[1], 0, 0, ierflg);
   gMinuit->mnparm( 2, "gaB1"    , para[2], para_step[2], 0, 10, ierflg);
   gMinuit->mnparm( 3, "M2"      , para[3], para_step[3], 0, 0, ierflg);//4390 in pipihc 
   gMinuit->mnparm( 4, "width2"  , para[4], para_step[4], 0, 0, ierflg);
   gMinuit->mnparm( 5, "gaB2"    , para[5], para_step[5], 0, 10, ierflg);
   gMinuit->mnparm( 6, "phase"   , para[6], para_step[6], 0, 0, ierflg);
   gMinuit->mnparm( 7, "CC"      , para[7], para_step[7], 0, 0, ierflg);
   gMinuit->mnparm( 8, "phi"     , para[8], para_step[8], 0, 0, ierflg);
   gMinuit->mnparm( 9, "gaB3"    , para[9], para_step[9], 0, 10, ierflg);

   /*gMinuit->FixParameter(2);
   gMinuit->FixParameter(3);
   gMinuit->FixParameter(4);
   gMinuit->FixParameter(5);
   gMinuit->FixParameter(6);*/
   gMinuit->mncomd( "SET ERR 0.5", ierflg);
   gMinuit->mncomd( "SET PRI 0.0", ierflg );
   //gMinuit->mncomd( "SET EPS 1e-9", ierflg );
   Double_t arglist[10] = {0};
   arglist[0] = 10000;
   arglist[1] = 0.05;
   gMinuit->mnexcm( "MIGRAD", arglist, 2, ierflg );
   gMinuit->mncomd( "SHOW COV", ierflg );
   gMinuit->mncomd( "RETURN", ierflg );

   Double_t out_par_list[10] = {0};
   Double_t out_par_err_list[10] = {0};

   gMinuit->GetParameter(0,out_par_list[0],out_par_err_list[0]);
   gMinuit->GetParameter(1,out_par_list[1],out_par_err_list[1]);
   gMinuit->GetParameter(2,out_par_list[2],out_par_err_list[2]);
   gMinuit->GetParameter(3,out_par_list[3],out_par_err_list[3]);
   gMinuit->GetParameter(4,out_par_list[4],out_par_err_list[4]);
   gMinuit->GetParameter(5,out_par_list[5],out_par_err_list[5]);
   gMinuit->GetParameter(6,out_par_list[6],out_par_err_list[6]);
   gMinuit->GetParameter(7,out_par_list[7],out_par_err_list[7]);
   gMinuit->GetParameter(8,out_par_list[8],out_par_err_list[8]);
   gMinuit->GetParameter(9,out_par_list[9],out_par_err_list[9]);


   my_plot_hc(out_par_list, nlines_hc, data_hc_x, data_hc_y, data_hc_xe, data_hc_ye);
   my_plot_omega(out_par_list, nlines_omega, data_omega_x, data_omega_y, data_omega_xe, data_omega_ye);

   my_plot_ps3();


}