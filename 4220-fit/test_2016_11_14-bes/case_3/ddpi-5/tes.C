#include "stdio.h"
#include "TMinuit.h"
#include "Riostream.h"
#include "TLorentzVector.h"
#include "TGenPhaseSpace.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TGraph.h"
#include "TGraphAsymmErrors.h"
#include "math.h"
#include "TF1.h"
#include "Math/WrappedTF1.h"
#include "Math/GaussIntegrator.h"
#include "TMath.h"
//void tt(*Double_t x, Double_t y);
static Double_t pi = 3.1415926;

static bool Use_Scan_Data = true ;

static Int_t nlines_hc = 0;
static Int_t nlines_omega = 0;
static Int_t nlines_jpsi = 0;
static Int_t nlines_ddpi = 0;
static Int_t nlines_hc_scan = 0;
static Int_t nlines_omega_scan = 0;
static Int_t nlines_jpsi_scan = 0;
static Int_t nlines_ddpi_scan = 0;
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
static  Double_t data_hc_yeh[100] = {0};
static  Double_t data_hc_yel[100] = {0};

static  Double_t data_omega_x[100] = {0};
static  Double_t data_omega_y[100] = {0};
static  Double_t data_omega_xe[100] = {0};
static  Double_t data_omega_yeh[100] = {0};
static  Double_t data_omega_yel[100] = {0};

static  Double_t data_jpsi_x[100] = {0};
static  Double_t data_jpsi_y[100] = {0};
static  Double_t data_jpsi_xe[100] = {0};
static  Double_t data_jpsi_yeh[100] = {0};
static  Double_t data_jpsi_yel[100] = {0};

static  Double_t data_ddpi_x[100] = {0};
static  Double_t data_ddpi_y[100] = {0};
static  Double_t data_ddpi_xe[100] = {0};
static  Double_t data_ddpi_yeh[100] = {0};
static  Double_t data_ddpi_yel[100] = {0};
//scan
static  Double_t data_scan_hc_x[1000] = {0};
static  Double_t data_scan_hc_y[1000] = {0};
static  Double_t data_scan_hc_xe[1000] = {0};
static  Double_t data_scan_hc_yeh[1000] = {0};
static  Double_t data_scan_hc_yel[1000] = {0};

/*
static  Double_t data_scan_omega_x[1000] = {0};
static  Double_t data_scan_omega_y[1000] = {0};
static  Double_t data_scan_omega_xe[1000] = {0};
static  Double_t data_scan_omega_yeh[1000] = {0};
static  Double_t data_scan_omega_yel[1000] = {0};
*/
static  Double_t data_scan_jpsi_x[1000] = {0};
static  Double_t data_scan_jpsi_y[1000] = {0};
static  Double_t data_scan_jpsi_xe[1000] = {0};
static  Double_t data_scan_jpsi_yeh[1000] = {0};
static  Double_t data_scan_jpsi_yel[1000] = {0};

static  Double_t data_scan_ddpi_x[1000] = {0};
static  Double_t data_scan_ddpi_y[1000] = {0};
static  Double_t data_scan_ddpi_xe[1000] = {0};
static  Double_t data_scan_ddpi_yeh[1000] = {0};
static  Double_t data_scan_ddpi_yel[1000] = {0};

static Double_t crossSection_hc_part1;
static Double_t crossSection_hc_part2;
static Double_t crossSection_hc_part3;

static Double_t crossSection_omega_part1;
static Double_t crossSection_omega_part2;

static Double_t crossSection_jpsi_part1;
static Double_t crossSection_jpsi_part2;
static Double_t crossSection_jpsi_part3;

static Double_t crossSection_ddpi_part1;
static Double_t crossSection_ddpi_part2;
static Double_t crossSection_ddpi_part3;
static Double_t crossSection_ddpi_part4;


void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag);
Double_t my_cs_hc(Double_t mass, Double_t *par_list, bool my_write);
Double_t my_cs_omega(Double_t mass, Double_t *par_list, bool my_write);
Double_t my_cs_jpsi(Double_t mass, Double_t *par_list, bool my_write);
Double_t my_cs_ddpi(Double_t mass, Double_t *par_list, bool my_write);
void my_BW(Double_t mass, Double_t M, Double_t width, Double_t gaB, Double_t PS_mass, Double_t PS_M, Double_t &re, Double_t &im);
Double_t ps3(Double_t mass, Double_t m1, Double_t m2, Double_t m3);
Double_t ps2(Double_t mass, Double_t m1, Double_t m2);
void my_plot_hc(Double_t *par_list);
void my_plot_omega(Double_t *par_list);
void my_plot_jpsi(Double_t *par_list);
void my_plot_ddpi(Double_t *par_list);

void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag)
{
   Double_t par_list[30];
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
   par_list[10] = par[10];
   par_list[11] = par[11];
   par_list[12] = par[12];
   par_list[13] = par[13];
   par_list[14] = par[14];
   par_list[15] = par[15];
   par_list[16] = par[16];
   par_list[17] = par[17];
   par_list[18] = par[18];
   par_list[19] = par[19];
   par_list[20] = par[20];
   par_list[21] = par[21];
   par_list[22] = par[22];
   par_list[23] = par[23];
   par_list[24] = par[24];
   par_list[25] = par[25];
   par_list[26] = par[26];
   par_list[27] = par[27];

   Double_t likelihood = 0.0;
   Double_t likelihood_1 = 0.0;
   Double_t likelihood_2 = 0.0;
   Double_t likelihood_3 = 0.0;
   Double_t likelihood_4 = 0.0;
   Int_t i = 0;
   
   for(i=0;data_hc_x[i]>0;i++)
   {
      //printf("i = %d , data_hc_x[i] = %f\n",i,data_hc_x[i] );
      Double_t my_cs = my_cs_hc(data_hc_x[i],par_list,false);
      Double_t my_target_cs = data_hc_y[i];
      Double_t my_error;
      if(my_cs >= my_target_cs)
      {
         my_error = data_hc_yeh[i];
      }
      else
      {
         my_error = data_hc_yel[i];
      }
      Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      likelihood_1 += my_value;
   }
   for(i=0;data_omega_x[i]>0;i++)
   {
      Double_t my_cs = my_cs_omega(data_omega_x[i],par_list,false);
      Double_t my_target_cs = data_omega_y[i];
      Double_t my_error;
      if(my_cs >= my_target_cs)
      {
         my_error = data_omega_yeh[i];
      }
      else
      {
         my_error = data_omega_yel[i];
      }
      Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      likelihood_2 += my_value;
   }
   for(i=0;data_jpsi_x[i]>0;i++)
   {
      Double_t my_cs = my_cs_jpsi(data_jpsi_x[i],par_list,false);
      Double_t my_target_cs = data_jpsi_y[i];
      Double_t my_error;
      if(my_cs >= my_target_cs)
      {
         my_error = data_jpsi_yeh[i];
      }
      else
      {
         my_error = data_jpsi_yel[i];
      }
      Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      likelihood_3 += my_value;
   }
   for(i=0;data_ddpi_x[i]>0;i++)
   {
      Double_t my_cs = my_cs_ddpi(data_ddpi_x[i],par_list,false);
      Double_t my_target_cs = data_ddpi_y[i];
      Double_t my_error;
      if(my_cs >= my_target_cs)
      {
         my_error = data_ddpi_yeh[i];
      }
      else
      {
         my_error = data_ddpi_yel[i];
      }
      Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      likelihood_4 += my_value;
   }
   //~~~~~~  Scan Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   if(Use_Scan_Data)
   {
   		for(i=0;data_scan_hc_x[i]>0;i++)
   		{
      		//printf("i = %d , data_scan_hc_x[i] = %f\n",i,data_scan_hc_x[i] );
      		Double_t my_cs = my_cs_hc(data_scan_hc_x[i],par_list,false);
      		Double_t my_target_cs = data_scan_hc_y[i];
      		Double_t my_error;
      		if(my_cs >= my_target_cs)
      		{
         		my_error = data_scan_hc_yeh[i];
      		}
      		else
      		{
         		my_error = data_scan_hc_yel[i];
      		}
      		Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      		likelihood_1 += my_value;
   		}/*
   		for(i=0;data_scan_omega_x[i]>0;i++)
   		{
      		Double_t my_cs = my_cs_omega(data_scan_omega_x[i],par_list,false);
      		Double_t my_target_cs = data_scan_omega_y[i];
      		Double_t my_error;
      		if(my_cs >= my_target_cs)
      		{
         		my_error = data_scan_omega_yeh[i];
      		}
      		else
      		{
         		my_error = data_scan_omega_yel[i];
      		}
      		Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      		likelihood_2 += my_value;
   		}*/
   		for(i=0;data_scan_jpsi_x[i]>0;i++)
   		{
      		Double_t my_cs = my_cs_jpsi(data_scan_jpsi_x[i],par_list,false);
      		Double_t my_target_cs = data_scan_jpsi_y[i];
      		Double_t my_error;
      		if(my_cs >= my_target_cs)
      		{
         		my_error = data_scan_jpsi_yeh[i];
      		}
      		else
      		{
         		my_error = data_scan_jpsi_yel[i];
      		}
      		Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      		likelihood_3 += my_value;
   		}
   		for(i=0;data_scan_ddpi_x[i]>0;i++)
   		{
      		Double_t my_cs = my_cs_ddpi(data_scan_ddpi_x[i],par_list,false);
      		Double_t my_target_cs = data_scan_ddpi_y[i];
      		Double_t my_error;
      		if(my_cs >= my_target_cs)
      		{
         		my_error = data_scan_ddpi_yeh[i];
      		}
      		else
      		{
         		my_error = data_scan_ddpi_yel[i];
      		}
      		Double_t my_value = ((my_cs-my_target_cs)*(my_cs-my_target_cs))/(my_error*my_error);
      		likelihood_4 += my_value;
   		}
   }
   likelihood = likelihood_1 + likelihood_2 + likelihood_3 + likelihood_4;
//   if(min_li > likelihood)
//   {
//      print likelihood;
//      min_li = likelihood;
//  }
   printf("**** ChiSqr: %f\n",likelihood );
   f = likelihood;
}

Double_t my_cs_hc(Double_t mass, Double_t *par_list, bool my_write)
{
   Double_t M1          = par_list[0];
   Double_t width1      = par_list[1];
   Double_t gaB1        = par_list[2];
   Double_t M2          = par_list[3];
   Double_t width2      = par_list[4];
   Double_t gaB2        = par_list[5];
   Double_t phase       = par_list[6];
   Double_t CC          = par_list[7];
   Double_t phi         = par_list[8];
   Double_t gaB3        = par_list[9];
   Double_t M5          = par_list[10];
   Double_t width5      = par_list[11];
   Double_t gaB5        = par_list[12];
   Double_t M6          = par_list[13];
   Double_t width6      = par_list[14];
   Double_t gaB6        = par_list[15];
   Double_t gaB4        = par_list[16];
   Double_t phase_4     = par_list[17];
   Double_t phase_6     = par_list[18];
   Double_t CC_ddpi     = par_list[19];
   Double_t gaB7        = par_list[20];
   Double_t gaB8        = par_list[21];
   Double_t phase_7     = par_list[22];
   Double_t phase_8     = par_list[23];

   Double_t gaB9        = par_list[24];//4320 in hc
   Double_t phase_9     = par_list[25];//4320 in hc


   Double_t m1=0.13957018;
   Double_t m2=0.13957018;
   Double_t m3=3.52538;

   Double_t re, im, crossSection;
   Double_t re1, im1;
   Double_t re2, im2;
   Double_t re6, im6;

   Double_t ps3_mass = ps3(mass,m1,m2,m3);
   Double_t ps3_M1 = ps3(M1,m1,m2,m3);
   Double_t ps3_M2 = ps3(M2,m1,m2,m3);
   Double_t ps3_M6 = ps3(M6,m1,m2,m3);
   //ps3_mass = 1;
   //ps3_M1 = 1;
   //ps3_M2 = 1;
   //printf("PS_mass : %f ; PS_M1 : %f ; PS_M2 : %f\n",ps3_mass,ps3_M1,ps3_M2 );
   my_BW(mass,M1,width1,gaB1,ps3_mass,ps3_M1, re1, im1);
   my_BW(mass,M2,width2,gaB2,ps3_mass,ps3_M2, re2, im2);
   my_BW(mass,M6,width6,gaB9,ps3_mass,ps3_M6, re6, im6);

   re=re1+re2*cos(phase)-im2*sin(phase)+re6*cos(phase_9)-im6*sin(phase_9);
   im=im1+im2*cos(phase)+re2*sin(phase)+im6*cos(phase_9)+re6*sin(phase_9);
   crossSection=(pow(re,2)+pow(im,2))*(0.389379*10);

   if(my_write)
   {
      crossSection_hc_part1 = (pow(re1,2)+pow(im1,2))*(0.389379*10);
      crossSection_hc_part2 = (pow(re2,2)+pow(im2,2))*(0.389379*10);
      crossSection_hc_part3 = (pow(re6,2)+pow(im6,2))*(0.389379*10);
   }
   return crossSection;
}

Double_t my_cs_omega(Double_t mass, Double_t *par_list, bool my_write)
{
   Double_t M1          = par_list[0];
   Double_t width1      = par_list[1];
   Double_t gaB1        = par_list[2];
   Double_t M2          = par_list[3];
   Double_t width2      = par_list[4];
   Double_t gaB2        = par_list[5];
   Double_t phase       = par_list[6];
   Double_t CC          = par_list[7];
   Double_t phi         = par_list[8];
   Double_t gaB3        = par_list[9];
   Double_t M5          = par_list[10];
   Double_t width5      = par_list[11];
   Double_t gaB5        = par_list[12];
   Double_t M6          = par_list[13];
   Double_t width6      = par_list[14];
   Double_t gaB6        = par_list[15];
   Double_t gaB4        = par_list[16];
   Double_t phase_45    = par_list[17];
   Double_t phase_46    = par_list[18];

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
   crossSection=(pow(re,2)+pow(im,2))*(0.389379*10.0);

   if(my_write)
   {
      crossSection_omega_part1 = (pow(tt,2))*(0.389379*10);
      crossSection_omega_part2 = (pow(re3,2)+pow(im3,2))*(0.389379*10);
   }
   return crossSection;
}


Double_t my_cs_jpsi(Double_t mass, Double_t *par_list, bool my_write)
{
   Double_t M1          = par_list[0];
   Double_t width1      = par_list[1];
   Double_t gaB1        = par_list[2];
   Double_t M2          = par_list[3];
   Double_t width2      = par_list[4];
   Double_t gaB2        = par_list[5];
   Double_t phase       = par_list[6];
   Double_t CC          = par_list[7];
   Double_t phi         = par_list[8];
   Double_t gaB3        = par_list[9];
   Double_t M5          = par_list[10];
   Double_t width5      = par_list[11];
   Double_t gaB5        = par_list[12];
   Double_t M6          = par_list[13];
   Double_t width6      = par_list[14];
   Double_t gaB6        = par_list[15];
   Double_t gaB4        = par_list[16];
   Double_t phase_4     = par_list[17];
   Double_t phase_6     = par_list[18];

   Double_t m1=0.13957018;
   Double_t m2=0.13957018;
   Double_t m3=3.0969;

   Double_t re, im, crossSection;
   Double_t re4, im4;
   Double_t re5, im5;
   Double_t re6, im6;

   //printf("mass : %f\n",mass );
   //printf("M1 : %f\n",M1 );
   //printf("M5 : %f\n",M5 );
   //printf("M6 : %f\n",M6 );
   Double_t ps3_mass = ps3(mass,m1,m2,m3);
   Double_t ps3_M1 = ps3(M1,m1,m2,m3);//4220
   Double_t ps3_M5 = ps3(M5,m1,m2,m3);//4008
   Double_t ps3_M6 = ps3(M6,m1,m2,m3);//4320

   //ps3_mass = 1;
   //ps3_M1 = 1;
   //ps3_M2 = 1;
   //printf("PS_mass : %f ; PS_M1 : %f ; PS_M5 : %f\n",ps3_mass,ps3_M1,ps3_M5 );

   my_BW(mass,M1,width1,gaB4,ps3_mass,ps3_M1, re4, im4);// 4: Y(4220)
   my_BW(mass,M5,width5,gaB5,ps3_mass,ps3_M5, re5, im5);// 5: Y(4008)
   my_BW(mass,M6,width6,gaB6,ps3_mass,ps3_M6, re6, im6);// 6: Y(4320)
   re=re5+re4*cos(phase_4)-im4*sin(phase_4)+re6*cos(phase_6)-im6*sin(phase_6);
   im=im5+im4*cos(phase_4)+re4*sin(phase_4)+im6*cos(phase_6)+re6*sin(phase_6);

   crossSection=(pow(re,2)+pow(im,2))*(0.389379*10);
 
   if(my_write)
   {
      crossSection_jpsi_part1 = (pow(re4,2)+pow(im4,2))*(0.389379*10);
      crossSection_jpsi_part2 = (pow(re5,2)+pow(im5,2))*(0.389379*10);
      crossSection_jpsi_part3 = (pow(re6,2)+pow(im6,2))*(0.389379*10);
   }
   return crossSection;
}


Double_t my_cs_ddpi(Double_t mass, Double_t *par_list, bool my_write)
{
   Double_t M1          = par_list[0];
   Double_t width1      = par_list[1];
   Double_t gaB1        = par_list[2];
   Double_t M2          = par_list[3];
   Double_t width2      = par_list[4];
   Double_t gaB2        = par_list[5];
   Double_t phase       = par_list[6];
   Double_t CC          = par_list[7];
   Double_t phi         = par_list[8];
   Double_t gaB3        = par_list[9];
   Double_t M5          = par_list[10];
   Double_t width5      = par_list[11];
   Double_t gaB5        = par_list[12];
   Double_t M6          = par_list[13];
   Double_t width6      = par_list[14];
   Double_t gaB6        = par_list[15];
   Double_t gaB4        = par_list[16];
   Double_t phase_4     = par_list[17];
   Double_t phase_6     = par_list[18];
   Double_t CC_ddpi     = par_list[19];
   Double_t gaB7        = par_list[20];
   Double_t gaB8        = par_list[21];
   Double_t phase_7     = par_list[22];
   Double_t phase_8     = par_list[23];
   Double_t gaB9        = par_list[24];//4320 in hc
   Double_t phase_9     = par_list[25];//4320 in hc
   Double_t gaB10        = par_list[26];//4320 in ddpi
   Double_t phase_10     = par_list[27];//4320 in ddpi

   Double_t m1=0.13957018;
   Double_t m2=1.86483;
   Double_t m3=2.01026;

   Double_t re, im, tt, crossSection;
   Double_t re7, im7;
   Double_t re8, im8;
   Double_t re10, im10;

   //printf("gaB7 : %f\n",gaB7 );
   //printf("gaB8 : %f\n",gaB8 );
   //printf("*************************\n");
   Double_t ps3_mass = ps3(mass,m1,m2,m3);
   Double_t ps3_M1 = ps3(M1,m1,m2,m3);//4220
   Double_t ps3_M2 = ps3(M2,m1,m2,m3);//4390
   Double_t ps3_M6 = ps3(M6,m1,m2,m3);//4390

   //ps3_mass = 1;
   //ps3_M1 = 1;
   //ps3_M2 = 1;
   //printf("PS_mass : %f ; PS_M1 : %f ; PS_M5 : %f\n",ps3_mass,ps3_M1,ps3_M5 );
   my_BW(mass,M1,width1,gaB7,ps3_mass,ps3_M1, re7, im7);// 4: Y(4220)
   my_BW(mass,M2,width2,gaB8,ps3_mass,ps3_M2, re8, im8);// 5: Y(4390)
   my_BW(mass,M6,width6,gaB10,ps3_mass,ps3_M2, re10, im10);// 5: Y(4390)

   tt = CC_ddpi*sqrt(ps3_mass);
   re=tt+re7*cos(phase_7)-im7*sin(phase_7)+re8*cos(phase_8)-im8*sin(phase_8)+re10*cos(phase_10)-im10*sin(phase_10);
   im=   im7*cos(phase_7)+re7*sin(phase_7)+im8*cos(phase_8)+re8*sin(phase_8)+im10*cos(phase_10)+re10*sin(phase_10);

   crossSection=(pow(re,2)+pow(im,2))*(0.389379*10);
 
   if(my_write)
   {
      crossSection_ddpi_part1 = (pow(tt,2))*(0.389379*10);
      crossSection_ddpi_part2 = (pow(re7,2)+pow(im7,2))*(0.389379*10);
      crossSection_ddpi_part3 = (pow(re8,2)+pow(im8,2))*(0.389379*10);
      crossSection_ddpi_part4 = (pow(re10,2)+pow(im10,2))*(0.389379*10);
   }
   return crossSection;
}

void my_BW(Double_t mass, Double_t M, Double_t width, Double_t gaB, Double_t PS_mass, Double_t PS_M, Double_t &re, Double_t &im)
{
   Double_t s, f;
   s = mass*mass;
   f=12*pi*gaB*width*PS_mass/PS_M;
   //printf("gaB: %f\n",gaB );
   //printf("width : %f\n",width );
   //printf("PS_mass: %f\n",PS_mass );
   //printf("PS_M: %f\n",PS_M );
   //printf("P /P: %f\n",PS_mass/PS_M);
   //printf("Before F: %f\n",f);

   f=sqrt(f);
   //printf("f: %f\n",f );

   re=f*(s-M*M)/(pow(s-M*M,2)+pow(M*width,2));
   im=f*M*width*(-1.0)/(pow(s-M*M,2)+pow(M*width,2));
}


Double_t ps3(Double_t mass, Double_t m1, Double_t m2, Double_t m3)
{

   TF1 f("PS3 Function", "sqrt((1-pow(([1]+x)/[0],2)) * (1-pow(([1]-x)/[0],2)) * (1-pow(([2]+[3])/x,2)) * (1-pow(([2]-[3])/x,2)))*x/3.1415926",(m3),(mass));
   f.SetParameters(mass, m1, m2, m3);
   //f.Draw();

   ROOT::Math::WrappedTF1 wf1(f);
   
   ROOT::Math::GaussIntegrator ig;
   
   ig.SetFunction(wf1);
   ig.SetRelTolerance(0.01);
   //ig.SetNumberPoints(20);
   
   Double_t ps3_factor;
   ps3_factor = ig.Integral((m2+m3),(mass-m1));
   ps3_factor = ps3_factor / (pow(8*pi,2));
   
   return ps3_factor;

}

Double_t ps2(Double_t mass, Double_t m1, Double_t m2)
{
   Double_t t1, t2, ps_value;
   t1=1.0-(pow((m1+m2)/mass,2));
   t2=1.0-(pow((m1-m2)/mass,2));
   //printf("t1 ; %f ; t2 : %f\n",t1,t2 );

   ps_value=sqrt(t1*t2);
   ps_value=ps_value/(8*pi);
   return ps_value;
}

void my_plot_hc(Double_t *par_list)
{
   TCanvas *c1 = new TCanvas("c1", "test_hc" , 200,10,700,500);
   c1->SetLeftMargin(0.15);
   c1->SetBottomMargin(0.14);
   TGraphAsymmErrors *gr_hc_data = new TGraphAsymmErrors(nlines_hc, data_hc_x, data_hc_y, data_hc_xe, data_hc_xe, data_hc_yel, data_hc_yeh);
   gr_hc_data->SetTitle("");
   gr_hc_data->SetMarkerColor(1);
   gr_hc_data->SetLineColor(kBlack);
   gr_hc_data->SetLineStyle(1);
   gr_hc_data->SetLineWidth(2);
   gr_hc_data->SetMarkerStyle(20);
   gr_hc_data->SetMarkerSize(1.0);
   gr_hc_data->GetXaxis()->SetTitle("M(#pi^{+}#pi^{-}h_{c}) (GeV/c^{2})");
   gr_hc_data->GetXaxis()->SetLabelSize(0.06);
   gr_hc_data->GetXaxis()->SetTitleSize(0.07);
   gr_hc_data->GetXaxis()->SetTitleOffset(0.85);
   gr_hc_data->GetXaxis()->SetNdivisions(505);
   gr_hc_data->GetYaxis()->SetLabelSize(0.06);
   gr_hc_data->GetYaxis()->SetTitle("#sigma (e^{+}e^{-}->#pi^{+}#pi^{-}h_{c}) (pb)");
   gr_hc_data->GetYaxis()->SetTitleSize(0.075);
   gr_hc_data->GetYaxis()->SetTitleOffset(0.8);
   gr_hc_data->GetYaxis()->SetRangeUser(-50,210);
   gr_hc_data->Draw("AP");
   TGraphAsymmErrors *gr_hc_data_scan = new TGraphAsymmErrors(nlines_hc_scan, data_scan_hc_x, data_scan_hc_y, data_scan_hc_xe, data_scan_hc_xe, data_scan_hc_yel, data_scan_hc_yeh);
   gr_hc_data_scan->SetMarkerColor(6);
   gr_hc_data_scan->SetLineColor(6);
   gr_hc_data_scan->SetLineStyle(1);
   gr_hc_data_scan->SetLineWidth(1);
   gr_hc_data_scan->SetMarkerStyle(22);
   gr_hc_data_scan->SetMarkerSize(1.0);
   gr_hc_data_scan->Draw("P");
   c1->Update();

   TGraph *gr_hc_fit = new TGraph();
   TGraph *gr_hc_fit_part1 = new TGraph();
   TGraph *gr_hc_fit_part2 = new TGraph();
   TGraph *gr_hc_fit_part3 = new TGraph();
   Int_t i=1;
   Double_t mass;
   for(mass = 3.9; mass < 4.8; mass+= 0.001)
   {
      Double_t my_cs = my_cs_hc(mass,par_list,true);
      gr_hc_fit->SetPoint(i,mass,my_cs);
      gr_hc_fit_part1->SetPoint(i,mass,crossSection_hc_part1);
      gr_hc_fit_part2->SetPoint(i,mass,crossSection_hc_part2);
      gr_hc_fit_part3->SetPoint(i,mass,crossSection_hc_part3);
      i+=1;
   }
   gr_hc_fit->SetMarkerColor(4);
   gr_hc_fit->SetLineColor(kPink);
   gr_hc_fit->SetLineStyle(1);
   gr_hc_fit->SetLineWidth(3);
   gr_hc_fit->Draw("C");
   gr_hc_fit_part1->SetMarkerColor(2);
   gr_hc_fit_part1->SetLineColor(kBlue);
   gr_hc_fit_part1->SetLineStyle(2);
   gr_hc_fit_part1->SetLineWidth(3);
   gr_hc_fit_part1->Draw("C");
   gr_hc_fit_part2->SetMarkerColor(2);
   gr_hc_fit_part2->SetLineColor(kBlue);
   gr_hc_fit_part2->SetLineStyle(2);
   gr_hc_fit_part2->SetLineWidth(3);
   gr_hc_fit_part2->Draw("C");
   gr_hc_fit_part3->SetMarkerColor(2);
   gr_hc_fit_part3->SetLineColor(kBlue);
   gr_hc_fit_part3->SetLineStyle(2);
   gr_hc_fit_part3->SetLineWidth(3);
   gr_hc_fit_part3->Draw("C");
   c1->Update();

   TLegend* legend = new TLegend(0.17, 0.60, 0.35, 0.88) ;
   legend->SetFillColor(kWhite) ;
   legend->SetBorderSize(0) ;
   legend->SetShadowColor(0) ;
   legend->SetTextSize(0.07);
   //legend->AddEntry(H_divide,"efficience of HLT_Ele20WP60_Ele8_Mass55_v1 ","l");
   legend->AddEntry(gr_hc_data,			"XYZ data ","lp");
   legend->AddEntry(gr_hc_data_scan,	"Scan data ","lp");
   legend->AddEntry(gr_hc_fit,			"Best fit ","lp");
   //NameAxes(eff, "Number of pile up)", "Efficience");
   legend->Draw();
   c1->Update();

   c1->Print("4220-hc.png");
   c1->Print("4220-hc.eps");
}

void my_plot_omega(Double_t *par_list)
{
   TCanvas *c2 = new TCanvas( "c2", "test_omega" , 200, 10, 700, 500 );
   c2->SetLeftMargin(0.15);
   c2->SetBottomMargin(0.14);
   TGraphAsymmErrors *gr_omega_data = new TGraphAsymmErrors(nlines_omega, data_omega_x, data_omega_y, data_omega_xe, data_omega_xe, data_omega_yel, data_omega_yeh);
   gr_omega_data->SetTitle("");
   gr_omega_data->SetMarkerColor(1);
   gr_omega_data->SetLineColor(kBlack);
   gr_omega_data->SetLineStyle(1);
   gr_omega_data->SetLineWidth(2);
   gr_omega_data->SetMarkerStyle(20);
   gr_omega_data->SetMarkerSize(1.0);
   gr_omega_data->GetXaxis()->SetTitle("M(#omega#chi_{c0}) (GeV/c^{2})");
   gr_omega_data->GetXaxis()->SetLabelSize(0.06);
   gr_omega_data->GetXaxis()->SetTitleSize(0.07);
   gr_omega_data->GetXaxis()->SetTitleOffset(0.85);
   gr_omega_data->GetXaxis()->SetNdivisions(505);
   gr_omega_data->GetXaxis()->SetRangeUser(4.2,4.7);
   gr_omega_data->GetYaxis()->SetLabelSize(0.06);
   gr_omega_data->GetYaxis()->SetTitle("#sigma (e^{+}e^{-}->#omega#chi_{c0}) (pb)");
   gr_omega_data->GetYaxis()->SetTitleSize(0.075);
   gr_omega_data->GetYaxis()->SetTitleOffset(0.8);
   gr_omega_data->Draw("AP");
   TGraph *gr_omega_fit = new TGraph();
   TGraph *gr_omega_fit_part1 = new TGraph();
   TGraph *gr_omega_fit_part2 = new TGraph();
   Int_t i=1;
   Double_t mass;
   for(mass = 4.2; mass < 4.8; mass+= 0.001)
   {
      Double_t my_cs = my_cs_omega(mass,par_list,true);
      gr_omega_fit->SetPoint(i,mass,my_cs);
      gr_omega_fit_part1->SetPoint(i,mass,crossSection_omega_part1);
      gr_omega_fit_part2->SetPoint(i,mass,crossSection_omega_part2);
      i+=1;
      //out_omega << "%f\t%f\n";
   }
   gr_omega_fit->SetMarkerColor(4);
   gr_omega_fit->SetLineColor(kPink);
   gr_omega_fit->SetLineStyle(1);
   gr_omega_fit->SetLineWidth(3);
   gr_omega_fit->Draw("C");
   gr_omega_fit_part1->SetMarkerColor(2);
   gr_omega_fit_part1->SetLineColor(kBlue);
   gr_omega_fit_part1->SetLineStyle(2);
   gr_omega_fit_part1->SetLineWidth(3);
   gr_omega_fit_part1->Draw("C");
   gr_omega_fit_part2->SetMarkerColor(2);
   gr_omega_fit_part2->SetLineColor(kBlue);
   gr_omega_fit_part2->SetLineStyle(2);
   gr_omega_fit_part2->SetLineWidth(3);
   gr_omega_fit_part2->Draw("C");
   c2->Update();

   TLegend* legend = new TLegend(0.57, 0.7, 0.85, 0.88) ;
   legend->SetFillColor(kWhite) ;
   legend->SetBorderSize(0) ;
   legend->SetShadowColor(0) ;
   legend->SetTextSize(0.07);
   //legend->AddEntry(H_divide,"efficience of HLT_Ele20WP60_Ele8_Mass55_v1 ","l");
   legend->AddEntry(gr_omega_data,	"XYZ data ","lp");
   legend->AddEntry(gr_omega_fit,	"Best fit ","lp");
   //NameAxes(eff, "Number of pile up)", "Efficience");
   legend->Draw();
   c2->Update();

   c2->Print("4220-omega.png");
   c2->Print("4220-omega.eps");
}

void my_plot_jpsi(Double_t *par_list)
{
   TCanvas *c3 = new TCanvas( "c3", "test_jpsi" , 200, 10, 700, 500 );
   c3->SetLeftMargin(0.15);
   c3->SetBottomMargin(0.14);
   TGraphAsymmErrors *gr_jpsi_data = new TGraphAsymmErrors(nlines_jpsi, data_jpsi_x, data_jpsi_y, data_jpsi_xe, data_jpsi_xe, data_jpsi_yel, data_jpsi_yeh);
   gr_jpsi_data->SetTitle("");
   gr_jpsi_data->SetMarkerColor(1);
   gr_jpsi_data->SetLineColor(kBlack);
   gr_jpsi_data->SetLineStyle(1);
   gr_jpsi_data->SetLineWidth(2);
   gr_jpsi_data->SetMarkerStyle(20);
   gr_jpsi_data->SetMarkerSize(1.0);
   gr_jpsi_data->GetXaxis()->SetTitle("M(#pi^{+}#pi^{-}J/#psi) (GeV/c^{2})");
   gr_jpsi_data->GetXaxis()->SetLabelSize(0.06);
   gr_jpsi_data->GetXaxis()->SetTitleSize(0.07);
   gr_jpsi_data->GetXaxis()->SetTitleOffset(0.85);
   gr_jpsi_data->GetXaxis()->SetNdivisions(505);
   gr_jpsi_data->GetYaxis()->SetLabelSize(0.06);
   gr_jpsi_data->GetYaxis()->SetTitle("#sigma (e^{+}e^{-}->#pi^{+}#pi^{-}J/#psi) (pb)");
   gr_jpsi_data->GetYaxis()->SetTitleSize(0.075);
   gr_jpsi_data->GetYaxis()->SetTitleOffset(0.9);
   gr_jpsi_data->GetYaxis()->SetRangeUser(-10,150);

   gr_jpsi_data->Draw("AP");
   TGraphAsymmErrors *gr_jpsi_data_scan = new TGraphAsymmErrors(nlines_jpsi_scan, data_scan_jpsi_x, data_scan_jpsi_y, data_scan_jpsi_xe, data_scan_jpsi_xe, data_scan_jpsi_yel, data_scan_jpsi_yeh);
   gr_jpsi_data_scan->SetMarkerColor(6);
   gr_jpsi_data_scan->SetLineColor(6);
   gr_jpsi_data_scan->SetLineStyle(1);
   gr_jpsi_data_scan->SetLineWidth(1);
   gr_jpsi_data_scan->SetMarkerStyle(22);
   gr_jpsi_data_scan->SetMarkerSize(1.0);
   gr_jpsi_data_scan->Draw("P");
   TGraph *gr_jpsi_fit = new TGraph();
   TGraph *gr_jpsi_fit_part1 = new TGraph();
   TGraph *gr_jpsi_fit_part2 = new TGraph();
   TGraph *gr_jpsi_fit_part3 = new TGraph();
   Int_t i=1;
   Double_t mass;
   for(mass = 3.6; mass < 4.8; mass+= 0.001)
   {
      Double_t my_cs = my_cs_jpsi(mass,par_list,true);
      gr_jpsi_fit->SetPoint(i,mass,my_cs);
      gr_jpsi_fit_part1->SetPoint(i,mass,crossSection_jpsi_part1);
      gr_jpsi_fit_part2->SetPoint(i,mass,crossSection_jpsi_part2);
      gr_jpsi_fit_part3->SetPoint(i,mass,crossSection_jpsi_part3);
      i+=1;
      //out_jpsi << "%f\t%f\n";
   }
   gr_jpsi_fit->SetMarkerColor(4);
   gr_jpsi_fit->SetLineColor(kPink);
   gr_jpsi_fit->SetLineStyle(1);
   gr_jpsi_fit->SetLineWidth(3);
   gr_jpsi_fit->Draw("C");
   gr_jpsi_fit_part1->SetMarkerColor(2);
   gr_jpsi_fit_part1->SetLineColor(kBlue);
   gr_jpsi_fit_part1->SetLineStyle(2);
   gr_jpsi_fit_part1->SetLineWidth(3);
   gr_jpsi_fit_part1->Draw("C");
   gr_jpsi_fit_part2->SetMarkerColor(2);
   gr_jpsi_fit_part2->SetLineColor(kBlue);
   gr_jpsi_fit_part2->SetLineStyle(2);
   gr_jpsi_fit_part2->SetLineWidth(3);
   gr_jpsi_fit_part2->Draw("C");
   gr_jpsi_fit_part3->SetMarkerColor(2);
   gr_jpsi_fit_part3->SetLineColor(kBlue);
   gr_jpsi_fit_part3->SetLineStyle(2);
   gr_jpsi_fit_part3->SetLineWidth(3);
   gr_jpsi_fit_part3->Draw("C");
   c3->Update();
   TLegend* legend = new TLegend(0.17, 0.60, 0.35, 0.88) ;
   legend->SetFillColor(kWhite) ;
   legend->SetBorderSize(0) ;
   legend->SetShadowColor(0) ;
   legend->SetTextSize(0.07);
   //legend->AddEntry(H_divide,"efficience of HLT_Ele20WP60_Ele8_Mass55_v1 ","l");
   legend->AddEntry(gr_jpsi_data,		"XYZ data ","lp");
   legend->AddEntry(gr_jpsi_data_scan,	"Scan data ","lp");
   legend->AddEntry(gr_jpsi_fit,		"Best fit ","lp");
   //NameAxes(eff, "Number of pile up)", "Efficience");
   legend->Draw();
   c3->Update();

   c3->Print("4220-jpsi.png");
   c3->Print("4220-jpsi.eps");
}

void my_plot_ddpi(Double_t *par_list)
{
   TCanvas *c4 = new TCanvas( "c4", "test_ddpi" , 200, 10, 700, 500 );
   c4->SetLeftMargin(0.15);
   c4->SetBottomMargin(0.14);
   TGraphAsymmErrors *gr_ddpi_data = new TGraphAsymmErrors(nlines_ddpi, data_ddpi_x, data_ddpi_y, data_ddpi_xe, data_ddpi_xe, data_ddpi_yel, data_ddpi_yeh);
   gr_ddpi_data->SetTitle("");
   gr_ddpi_data->SetMarkerColor(1);
   gr_ddpi_data->SetLineColor(kBlack);
   gr_ddpi_data->SetLineStyle(1);
   gr_ddpi_data->SetLineWidth(2);
   gr_ddpi_data->SetMarkerStyle(20);
   gr_ddpi_data->SetMarkerSize(1.0);
   gr_ddpi_data->GetXaxis()->SetTitle("M(D^{0}D*#pi) (GeV/c^{2})");
   gr_ddpi_data->GetXaxis()->SetLabelSize(0.05);
   gr_ddpi_data->GetXaxis()->SetTitleSize(0.07);
   gr_ddpi_data->GetXaxis()->SetTitleOffset(0.85);
   gr_ddpi_data->GetXaxis()->SetNdivisions(505);
   gr_ddpi_data->GetXaxis()->SetRangeUser(4.0,4.65);
   gr_ddpi_data->GetYaxis()->SetLabelSize(0.06);
   gr_ddpi_data->GetYaxis()->SetTitle("#sigma (e^{+}e^{-}->D^{0}D*#pi) (pb)");
   gr_ddpi_data->GetYaxis()->SetTitleSize(0.08);
   gr_ddpi_data->GetYaxis()->SetTitleOffset(0.9);
   gr_ddpi_data->GetYaxis()->SetRangeUser(0,1100);

   gr_ddpi_data->Draw("AP");

   TGraphAsymmErrors *gr_ddpi_data_scan = new TGraphAsymmErrors(nlines_ddpi_scan, data_scan_ddpi_x, data_scan_ddpi_y, data_scan_ddpi_xe, data_scan_ddpi_xe, data_scan_ddpi_yel, data_scan_ddpi_yeh);
   gr_ddpi_data_scan->SetMarkerColor(6);
   gr_ddpi_data_scan->SetLineColor(6);
   gr_ddpi_data_scan->SetLineStyle(1);
   gr_ddpi_data_scan->SetLineWidth(1);
   gr_ddpi_data_scan->SetMarkerStyle(22);
   gr_ddpi_data_scan->SetMarkerSize(1.0);
   gr_ddpi_data_scan->Draw("P");
   TGraph *gr_ddpi_fit = new TGraph();
   TGraph *gr_ddpi_fit_part1 = new TGraph();
   TGraph *gr_ddpi_fit_part2 = new TGraph();
   TGraph *gr_ddpi_fit_part3 = new TGraph();
   TGraph *gr_ddpi_fit_part4 = new TGraph();
   Int_t i=1;
   Double_t mass;
   for(mass = 4.05; mass < 4.8; mass+= 0.001)
   {
      Double_t my_cs = my_cs_ddpi(mass,par_list,true);
      gr_ddpi_fit->SetPoint(i,mass,my_cs);
      gr_ddpi_fit_part1->SetPoint(i,mass,crossSection_ddpi_part1);
      gr_ddpi_fit_part2->SetPoint(i,mass,crossSection_ddpi_part2);
      gr_ddpi_fit_part3->SetPoint(i,mass,crossSection_ddpi_part3);
      gr_ddpi_fit_part4->SetPoint(i,mass,crossSection_ddpi_part4);
      i+=1;
      //out_ddpi << "%f\t%f\n";
   }
   gr_ddpi_fit->SetMarkerColor(4);
   gr_ddpi_fit->SetLineColor(kPink);
   gr_ddpi_fit->SetLineStyle(1);
   gr_ddpi_fit->SetLineWidth(3);
   gr_ddpi_fit->Draw("C");
   gr_ddpi_fit_part1->SetMarkerColor(2);
   gr_ddpi_fit_part1->SetLineColor(kBlue);
   gr_ddpi_fit_part1->SetLineStyle(2);
   gr_ddpi_fit_part1->SetLineWidth(3);
   gr_ddpi_fit_part1->Draw("C");
   gr_ddpi_fit_part2->SetMarkerColor(2);
   gr_ddpi_fit_part2->SetLineColor(kBlue);
   gr_ddpi_fit_part2->SetLineStyle(2);
   gr_ddpi_fit_part2->SetLineWidth(3);
   gr_ddpi_fit_part2->Draw("C");
   gr_ddpi_fit_part3->SetMarkerColor(2);
   gr_ddpi_fit_part3->SetLineColor(kBlue);
   gr_ddpi_fit_part3->SetLineStyle(2);
   gr_ddpi_fit_part3->SetLineWidth(3);
   gr_ddpi_fit_part3->Draw("C");
   gr_ddpi_fit_part4->SetMarkerColor(2);
   gr_ddpi_fit_part4->SetLineColor(kBlue);
   gr_ddpi_fit_part4->SetLineStyle(2);
   gr_ddpi_fit_part4->SetLineWidth(3);
   gr_ddpi_fit_part4->Draw("C");
   c4->Update();
   TLegend* legend = new TLegend(0.17, 0.60, 0.35, 0.88) ;
   legend->SetFillColor(kWhite) ;
   legend->SetBorderSize(0) ;
   legend->SetShadowColor(0) ;
   legend->SetTextSize(0.07);
   //legend->AddEntry(H_divide,"efficience of HLT_Ele20WP60_Ele8_Mass55_v1 ","l");
   legend->AddEntry(gr_ddpi_data,		"XYZ data ","lp");
   legend->AddEntry(gr_ddpi_data_scan,	"Scan data ","lp");
   legend->AddEntry(gr_ddpi_fit,		"Best fit ","lp");
   //NameAxes(eff, "Number of pile up)", "Efficience");
   legend->Draw();
   c4->Update();

   c4->Print("4220-ddpi.png");
   c4->Print("4220-ddpi.eps");
}

void my_plot_ps3()
{
   TCanvas *c10 = new TCanvas("c10", "test_ps3" , 200,10,700,500);

   TGraph *gr_hc_fit = new TGraph();
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
   c10->Update();
}

void my_plot_ps2()
{
   TCanvas *c11 = new TCanvas("c11", "test_ps2" , 200,11,700,500);

   TGraph *gr_hc_fit = new TGraph();
   Int_t i=1;
   Double_t mass;

   Double_t m1=3.41475;
   Double_t m2=0.782;

   for(mass = 4.2; mass < 5.4; mass+= 0.1)
   {
      Double_t my_cs = ps2(mass,m1,m2);
      gr_hc_fit->SetPoint(i,mass,my_cs);
      i+=1;
   }
   gr_hc_fit->Draw("APC");
   c11->Update();
}

void tes()
{
   ifstream in1;
   ifstream in2;
   ifstream in3;
   ifstream in4;
   in1.open("4220_sigma_hc_new.dat");
   //in1.open("4220_sigma_hc.dat");
   in2.open("4220_sigma_omega_new.dat");
   in3.open("4220_sigma_jpsi_new.dat");
   in4.open("4220_sigma_ddpi_bes3.dat");

   ifstream in11;
   ifstream in12;
   ifstream in13;
   ifstream in14;
   in11.open("4220_scan_hc_new.dat");
   in13.open("4220_scan_jpsi_new.dat");
   in14.open("4220_scan_ddpi_bes3.dat");
   
   ofstream out_value;
   ofstream out_error;
   out_value.open("result_4220_fit_value.dat");
   out_error.open("result_4220_fit_error.dat");

//input hc data
   Int_t ii=0;
   for(ii=0;1;ii++)
   {
      in1 >> data_hc_x[ii] >> data_hc_y[ii] >> data_hc_yeh[ii] >> data_hc_yel[ii] ;
      if(!in1.good())break;
      nlines_hc += 1;
   }
   in1.close();
   printf("hc data total lines : %d \n",nlines_hc);

   for(ii=0;1;ii++)
   {
      in11 >> data_scan_hc_x[ii] >> data_scan_hc_y[ii] >> data_scan_hc_yeh[ii] >> data_scan_hc_yel[ii] ;
      if(!in11.good())break;
      nlines_hc_scan += 1;
   }
   in11.close();
   printf("hc data scan total lines : %d \n",nlines_hc_scan);
//input omega data
   for(ii=0;1;ii++)
   {      
      in2 >> data_omega_x[ii] >> data_omega_y[ii] >> data_omega_yeh[ii] >> data_omega_yel[ii] ;
      if(!in2.good())break;
      nlines_omega += 1;
      printf("%d :%f\n",ii, data_omega_x[ii] );
   }
   printf("omega data total lines : %d \n",nlines_omega);
   in2.close();
//input pi pi jpsi data
   for(ii=0;1;ii++)
   {      
      in3 >> data_jpsi_x[ii] >> data_jpsi_y[ii] >> data_jpsi_yeh[ii] >> data_jpsi_yel[ii] ;
      if(!in3.good())break;
      nlines_jpsi += 1;
      printf("%d :%f\n",ii, data_jpsi_x[ii] );
   }
   printf("jpsi data total lines : %d \n",nlines_jpsi);
   in3.close();

   for(ii=0;1;ii++)
   {      
      in13 >> data_scan_jpsi_x[ii] >> data_scan_jpsi_y[ii] >> data_scan_jpsi_yeh[ii] >> data_scan_jpsi_yel[ii] ;
      if(!in13.good())break;
      nlines_jpsi_scan += 1;
      printf("%d :%f ; %f + %f - %f\n",ii, data_scan_jpsi_x[ii], data_scan_jpsi_y[ii], data_scan_jpsi_yeh[ii], data_scan_jpsi_yel[ii]);
   }
   printf("jpsi data scan total lines : %d \n",nlines_jpsi_scan);
   in13.close();
//input pi pi jpsi data

   for(ii=0;1;ii++)
   {      
      in4 >> data_ddpi_x[ii] >> data_ddpi_y[ii] >> data_ddpi_yeh[ii] >> data_ddpi_yel[ii] ;
      if(!in4.good())break;
      nlines_ddpi += 1;
      printf("%d :%f\n",ii, data_ddpi_x[ii] );
   }
   printf("ddpi data total lines : %d \n",nlines_ddpi);
   in4.close();

   for(ii=0;1;ii++)
   {      
      in14 >> data_scan_ddpi_x[ii] >> data_scan_ddpi_y[ii] >> data_scan_ddpi_yeh[ii] >> data_scan_ddpi_yel[ii] ;
      if(!in14.good())break;
      nlines_ddpi_scan += 1;
      printf("%d :%f\n",ii, data_scan_ddpi_x[ii] );
   }
   printf("ddpi data scan total lines : %d \n",nlines_ddpi_scan);
   in14.close();
//read input over

//start minuit
   TMinuit *gMinuit = new TMinuit(28);
   gMinuit->SetFCN( fcn );

   Int_t ierflg = 0;


 // Set starting values and step sizes for parameters
   //             	   {  0   ,   1  ,   2  ,   3  ,   4  ,  5 ,  6 ,   7  ,   8 ,  9 ,  10 ,  11 ,  12  ,  13  ,   14  ,   15 ,   16 , 17 ,  18 ,    19 ,  20,  21 , 22 , 23};

   //Double_t para[28] = {4.22 , 0.057, 0.2, 4.38, 0.15, 0.6, 3.2, 0.0, 0.0, 0.5, 3.86, 0.36, 0.55 , 4.33 , 0.056 , 0.067 , 0.26, 0.2, 1.86, 1200.0, 0.5, 3.7, 2.0, 1.7, 0.0, 0.0, 0.8, 3.7};//Default result
   //Double_t para[28] = {4.22 , 0.057, 0.2, 4.38, 0.15, 0.6, 3.2, 0.0, 0.0, 0.5, 3.86, 0.36, 0.55 , 4.33 , 0.056 , 0.067 , 0.26, 0.2, 1.86, 2000.0, 7.2, 5.9, -2.2, 2.4,   0.0, 0.0, 0.8, 3.7};//new data ddpi result 2
   //Double_t para[28] = {4.22 , 0.057, 0.2, 4.38, 0.15, 0.6, 3.2, 0.0, 0.0, 0.5, 3.86, 0.36, 0.55 , 4.33 , 0.056 , 0.067 , 0.26, 0.2, 1.86, 2000.0, 2.9, 26.0, -2.2, 4.2,  0.0, 0.0, 0.8, 3.7};//new data ddpi result 3
   //Double_t para[28] = {4.22 , 0.057, 0.2, 4.38, 0.15, 0.6, 3.2, 0.0, 0.0, 0.5, 3.86, 0.36, 0.55 , 4.33 , 0.056 , 0.067 , 0.26, 0.2, 1.86, 2000.0, 8.4, 35.0, -1.4, 3.94, 0.0, 0.0, 0.8, 3.7};//new data ddpi result 4
   Double_t para[28] = {4.2205, 0.055, 0.2625, 4.3788, 0.147, 0.882, 2.23, 0.0, 0.0, 0.3379, 3.833, 0.359, 0.547, 4.339, 0.116, 0.68, 0.24, 0.144, 2.35, 1436.0, 0.7, 11.6, 3.1, 1.2, 0.0, 0.0, 20.4, -2.3};//new data ddpi result 5
   
   //Double_t para[28] = {4.223 , 0.057, 0.2, 4.393, 0.154, 0.6, 3.2, 0.0, 0.0, 0.5, 3.86, 0.31, 0.55 , 4.33 , 0.056 , 1.3 , 0.3, 0.9, -1.9, 2000.0, 2.5, 4.36, 3.2, 2.7,      0.0, 0.0, 0.8, 3.1};//new data jpsi result 2
   //Double_t para[28] = {4.223 , 0.057, 0.2, 4.393, 0.154, 0.6, 3.2, 0.0, 0.0, 0.5, 3.86, 0.31, 0.55 , 4.33 , 0.056 , 0.2 , 0.9 , -2.0 ,1.0, 1300.0, 2.5, 4.36, 3.2, 2.7,     0.0, 0.0, 0.6, 2.0};//new data jpsi result 3
   //Double_t para[28] = {4.223 , 0.057, 0.2, 4.393, 0.154, 0.6, 3.2, 0.0, 0.0, 0.5, 3.86, 0.31, 0.55 , 4.33 , 0.056 , 2.0 , 1.1, -0.7 ,-2.5, 2000.0, 2.5, 4.36, 3.2, 2.7,     0.0, 0.0, 0.8, -2.0};//new data jpsi result 4

   //Double_t para[28] = {4.22 , 0.057, 0.7, 4.38, 0.15, 1.6, 1.2, 0.0, 0.0, 0.5, 3.86, 0.36, 0.55 , 4.33 , 0.056 , 0.067 , 0.26, 0.2, 1.86, 1200.0, 0.5, 3.7, 2.0, 1.7, 0.0, 0.0, 0.8, 3.7};//pi pi hc result 2



   Double_t para_step[28] = {0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.1, 0.01, 0.01, 0.001, 0.001, 0.01, 0.001, 0.001, 0.01, 0.01, 0.01, 0.01, 1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01};

   gMinuit->mnparm( 0, "M(4220)"          , para[0], para_step[0], 4.2, 4.25, ierflg);//4220
   gMinuit->mnparm( 1, "width(4220)"      , para[1], para_step[1], 0, 0.15, ierflg);//4220
   gMinuit->mnparm( 2, "gaB_hc(4220)"     , para[2], para_step[2], 0, 50, ierflg);//4220
   gMinuit->mnparm( 3, "M(4390)"          , para[3], para_step[3], 4.32, 4.42, ierflg);//4390 in pipihc 
   gMinuit->mnparm( 4, "width(4390)"      , para[4], para_step[4], 0, 0.2, ierflg);//4390 in pipihc 
   gMinuit->mnparm( 5, "gaB(4390)"        , para[5], para_step[5], 0, 50, ierflg);//4390 in pipihc 
   gMinuit->mnparm( 6, "phase_(4390)"         , para[6], para_step[6], 0, 0, ierflg);//pipihc 
   gMinuit->mnparm( 7, "CC_omega_ps2"     , para[7], para_step[7], 0, 0, ierflg);//omega chi_c0
   gMinuit->mnparm( 8, "phase_omega"      , para[8], para_step[8], -5, 5, ierflg);//omega chi_c0
   gMinuit->mnparm( 9, "gaB_omega(4220)"  , para[9], para_step[9], 0, 10, ierflg);//omega chi_c0

   gMinuit->mnparm( 10, "M(4008)"         , para[10], para_step[10], 3.6, 4.2, ierflg);
   gMinuit->mnparm( 11, "width(4008)"     , para[11], para_step[11], 0.25, 0.7, ierflg);
   gMinuit->mnparm( 12, "gaB(4008)"       , para[12], para_step[12], 0, 15, ierflg);//
   gMinuit->mnparm( 13, "M(4320)"         , para[13], para_step[13], 4.2, 4.4, ierflg);//
   gMinuit->mnparm( 14, "width(4320)"     , para[14], para_step[14], 0.03, 0.25, ierflg);//
   gMinuit->mnparm( 15, "gaB(4320)"       , para[15], para_step[15], 0, 5, ierflg);//
   gMinuit->mnparm( 16, "gaB_jpsi(4220)"  , para[16], para_step[16], 0, 5, ierflg);//
   gMinuit->mnparm( 17, "phase_jpsi_(4220)"    , para[17], para_step[17], 0, 0, ierflg);//
   gMinuit->mnparm( 18, "phase_jpsi_(4320)"    , para[18], para_step[18], 0, 0, ierflg);//

   gMinuit->mnparm( 19, "CC_ddpi"               , para[19], para_step[19], 1000, 3000, ierflg);//constant for PS3 in DDpi
   gMinuit->mnparm( 20, "gaB_ddpi(4220)"        , para[20], para_step[20], 0, 150, ierflg);//
   gMinuit->mnparm( 21, "gaB_ddpi(4390)"        , para[21], para_step[21], 0, 150, ierflg);//
   gMinuit->mnparm( 22, "phase_ddpi_(4220)"     , para[22], para_step[22], 0, 0, ierflg);//
   gMinuit->mnparm( 23, "phase_ddpi_(4390)"     , para[23], para_step[23], 0, 0, ierflg);//

   gMinuit->mnparm( 24, "gaB_hc(4320)"       , para[24], para_step[24], 0, 150, ierflg);//
   gMinuit->mnparm( 25, "phase_hc(4320)"     , para[25], para_step[25], -10.0, 10.0, ierflg);//

   gMinuit->mnparm( 26, "gaB_ddpi(4320)"       , para[26], para_step[26], 0, 150, ierflg);//
   gMinuit->mnparm( 27, "phase_ddpi(4320)"     , para[27], para_step[27], 0, 0, ierflg);//
/*
   //gMinuit->FixParameter(0);
   //gMinuit->FixParameter(1);
   //gMinuit->FixParameter(2);
   //gMinuit->FixParameter(3);
   //gMinuit->FixParameter(4);
   //gMinuit->FixParameter(5);
   //gMinuit->FixParameter(6);
   //*/
   gMinuit->FixParameter(7);
   gMinuit->FixParameter(8);/*
   gMinuit->FixParameter(9);
   gMinuit->FixParameter(10);
   gMinuit->FixParameter(11);
   gMinuit->FixParameter(12);
   gMinuit->FixParameter(13);
   gMinuit->FixParameter(14);
   gMinuit->FixParameter(15);
   gMinuit->FixParameter(16);
   gMinuit->FixParameter(17);
   gMinuit->FixParameter(18);
   gMinuit->FixParameter(19);
   gMinuit->FixParameter(20);
   gMinuit->FixParameter(21);
   gMinuit->FixParameter(22);
   gMinuit->FixParameter(23);
   gMinuit->FixParameter(26);
   gMinuit->FixParameter(27);
*/
   gMinuit->FixParameter(24);
   gMinuit->FixParameter(25);

   gMinuit->mncomd( "SET ERR 1.0", ierflg);
   gMinuit->mncomd( "SET PRI 0.0", ierflg );
   gMinuit->mncomd( "SET EPS 1e-9", ierflg );
   Double_t arglist[10] = {0};
   arglist[0] = 10000;
   arglist[1] = 0.1;
   gMinuit->mnexcm( "MIGRAD", arglist, 2, ierflg );
   gMinuit->mncomd( "SHOW COV", ierflg );
   gMinuit->mncomd( "RETURN", ierflg );

   Double_t out_par_list[30] = {0};
   Double_t out_par_err_list[30] = {0};

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
   gMinuit->GetParameter(10,out_par_list[10],out_par_err_list[10]);
   gMinuit->GetParameter(11,out_par_list[11],out_par_err_list[11]);
   gMinuit->GetParameter(12,out_par_list[12],out_par_err_list[12]);
   gMinuit->GetParameter(13,out_par_list[13],out_par_err_list[13]);
   gMinuit->GetParameter(14,out_par_list[14],out_par_err_list[14]);
   gMinuit->GetParameter(15,out_par_list[15],out_par_err_list[15]);
   gMinuit->GetParameter(16,out_par_list[16],out_par_err_list[16]);
   gMinuit->GetParameter(17,out_par_list[17],out_par_err_list[17]);
   gMinuit->GetParameter(18,out_par_list[18],out_par_err_list[18]);
   gMinuit->GetParameter(19,out_par_list[19],out_par_err_list[19]);
   gMinuit->GetParameter(20,out_par_list[20],out_par_err_list[20]);
   gMinuit->GetParameter(21,out_par_list[21],out_par_err_list[21]);
   gMinuit->GetParameter(22,out_par_list[22],out_par_err_list[22]);
   gMinuit->GetParameter(23,out_par_list[23],out_par_err_list[23]);
   gMinuit->GetParameter(24,out_par_list[24],out_par_err_list[24]);
   gMinuit->GetParameter(25,out_par_list[25],out_par_err_list[25]);
   gMinuit->GetParameter(26,out_par_list[26],out_par_err_list[26]);
   gMinuit->GetParameter(27,out_par_list[27],out_par_err_list[27]);

   Int_t i = 0;
   printf("********* fit mean value *********\n");
   for(i=0;i<28;i++)
   {
        printf("%0.3f\n",out_par_list[i]);
        out_value <<out_par_list[i]<<"\n";
   }
   printf("********* fit error value *********\n");
   for(i=0;i<28;i++)
   {
        printf("%0.4f\n",out_par_err_list[i]);
        out_error <<out_par_err_list[i]<<"\n";
   }

   my_plot_hc(out_par_list);
   my_plot_omega(out_par_list);
   my_plot_jpsi(out_par_list);
   my_plot_ddpi(out_par_list);

   //my_plot_ps3();
   //my_plot_ps2();
}
