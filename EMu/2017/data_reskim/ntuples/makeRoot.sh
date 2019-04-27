#rm data_2017E_DoubleEG.root
mkdir output
rm output/*.root


hadd -f output/DYToLL_all.root	 	batchmc/2017_MC*_DYToLL_*_nor_*.root
hadd -f output/ttbar2l2u_all.root	batchmc/2017_MC*_ttbar2l2u_*_nor_*.root
hadd -f output/ST.root 			batchmc/2017_MC*_ST_*_nor_*.root
hadd -f output/WW.root 			batchmc/2017_MC*_WW_*_nor_*.root
hadd -f output/WZ.root			batchmc/2017_MC*_WZ_*_nor_*.root
hadd -f output/ZZ.root 			batchmc/2017_MC*_ZZ_*_nor_*.root

hadd -f output/DYToLL_all_muptu.root	 	batchmc/2017_MC*_DYToLL_*_muptu_*.root
hadd -f output/ttbar2l2u_all_muptu.root		batchmc/2017_MC*_ttbar2l2u_*_muptu_*.root
hadd -f output/ST_muptu.root 			batchmc/2017_MC*_ST_*_muptu_*.root
hadd -f output/WW_muptu.root 			batchmc/2017_MC*_WW_*_muptu_*.root
hadd -f output/WZ_muptu.root			batchmc/2017_MC*_WZ_*_muptu_*.root
hadd -f output/ZZ_muptu.root 			batchmc/2017_MC*_ZZ_*_muptu_*.root

hadd -f output/DYToLL_all_muresu.root	 	batchmc/2017_MC*_DYToLL_*_muresu_*.root
hadd -f output/ttbar2l2u_all_muresu.root	batchmc/2017_MC*_ttbar2l2u_*_muresu_*.root
hadd -f output/ST_muresu.root 			batchmc/2017_MC*_ST_*_muresu_*.root
hadd -f output/WW_muresu.root 			batchmc/2017_MC*_WW_*_muresu_*.root
hadd -f output/WZ_muresu.root			batchmc/2017_MC*_WZ_*_muresu_*.root
hadd -f output/ZZ_muresu.root 			batchmc/2017_MC*_ZZ_*_muresu_*.root

hadd -f output/DYToLL_all_eletu.root	 	batchmc/2017_MC*_DYToLL_*_eletu_*.root
hadd -f output/ttbar2l2u_all_eletu.root		batchmc/2017_MC*_ttbar2l2u_*_eletu_*.root
hadd -f output/ST_eletu.root 			batchmc/2017_MC*_ST_*_eletu_*.root
hadd -f output/WW_eletu.root 			batchmc/2017_MC*_WW_*_eletu_*.root
hadd -f output/WZ_eletu.root			batchmc/2017_MC*_WZ_*_eletu_*.root
hadd -f output/ZZ_eletu.root 			batchmc/2017_MC*_ZZ_*_eletu_*.root

hadd -f output/DYToLL_all_eletd.root	 	batchmc/2017_MC*_DYToLL_*_eletd_*.root
hadd -f output/ttbar2l2u_all_eletd.root		batchmc/2017_MC*_ttbar2l2u_*_eletd_*.root
hadd -f output/ST_eletd.root 			batchmc/2017_MC*_ST_*_eletd_*.root
hadd -f output/WW_eletd.root 			batchmc/2017_MC*_WW_*_eletd_*.root
hadd -f output/WZ_eletd.root			batchmc/2017_MC*_WZ_*_eletd_*.root
hadd -f output/ZZ_eletd.root 			batchmc/2017_MC*_ZZ_*_eletd_*.root

#hadd -f output/ZPrime_M1000.root 	batchmc/2017_MC*_ZPrime_M1000_*
#hadd -f output/ZPrime_M1000.root 	batchmc/2017_MC*_ZPrime_M1000_*
#hadd -f output/QBH_n4_M1000.root	batchmc/2017_MC*_QBH_n4_M1000_*
#hadd -f output/RPV_M1000.root	 	batchmc/2017_MC*_RPV_M1000_*
