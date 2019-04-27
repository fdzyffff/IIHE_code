#rm data_2017E_DoubleEG.root
mkdir output
rm output/*.root


hadd -f output/fkm_DYToLL_all.root	 		batchmc/fkm_2017_MC*_DYToLL_*_nor_*.root
hadd -f output/fkm_ttbar2l2u_all.root			batchmc/fkm_2017_MC*_ttbar2l2u_*_nor_*.root
hadd -f output/fkm_ST.root 				batchmc/fkm_2017_MC*_ST_*_nor_*.root
hadd -f output/fkm_WW.root 				batchmc/fkm_2017_MC*_WW_*_nor_*.root
hadd -f output/fkm_WZ.root				batchmc/fkm_2017_MC*_WZ_*_nor_*.root
hadd -f output/fkm_ZZ.root 				batchmc/fkm_2017_MC*_ZZ_*_nor_*.root

#hadd -f output/fke_DYToLL_all_muptu.root	 	batchmc/fke_2017_MC*_DYToLL_*_muptu_*.root
#hadd -f output/fke_ttbar2l2u_all_muptu.root		batchmc/fke_2017_MC*_ttbar2l2u_*_muptu_*.root
#hadd -f output/fke_ST_muptu.root 			batchmc/fke_2017_MC*_ST_*_muptu_*.root
#hadd -f output/fke_WW_muptu.root 			batchmc/fke_2017_MC*_WW_*_muptu_*.root
#hadd -f output/fke_WZ_muptu.root			batchmc/fke_2017_MC*_WZ_*_muptu_*.root
#hadd -f output/fke_ZZ_muptu.root 			batchmc/fke_2017_MC*_ZZ_*_muptu_*.root
#
#hadd -f output/fke_DYToLL_all_muresu.root	 	batchmc/fke_2017_MC*_DYToLL_*_muresu_*.root
#hadd -f output/fke_ttbar2l2u_all_muresu.root		batchmc/fke_2017_MC*_ttbar2l2u_*_muresu_*.root
#hadd -f output/fke_ST_muresu.root 			batchmc/fke_2017_MC*_ST_*_muresu_*.root
#hadd -f output/fke_WW_muresu.root 			batchmc/fke_2017_MC*_WW_*_muresu_*.root
#hadd -f output/fke_WZ_muresu.root			batchmc/fke_2017_MC*_WZ_*_muresu_*.root
#hadd -f output/fke_ZZ_muresu.root 			batchmc/fke_2017_MC*_ZZ_*_muresu_*.root
#
#hadd -f output/fke_DYToLL_all_eletu.root	 	batchmc/fke_2017_MC*_DYToLL_*_eletu_*.root
#hadd -f output/fke_ttbar2l2u_all_eletu.root		batchmc/fke_2017_MC*_ttbar2l2u_*_eletu_*.root
#hadd -f output/fke_ST_eletu.root 			batchmc/fke_2017_MC*_ST_*_eletu_*.root
#hadd -f output/fke_WW_eletu.root 			batchmc/fke_2017_MC*_WW_*_eletu_*.root
#hadd -f output/fke_WZ_eletu.root			batchmc/fke_2017_MC*_WZ_*_eletu_*.root
#hadd -f output/fke_ZZ_eletu.root 			batchmc/fke_2017_MC*_ZZ_*_eletu_*.root

#hadd -f output/ZPrime_M1000.root 	batchmc/2017_MC*_ZPrime_M1000_*
#hadd -f output/QBH_n4_M1000.root	batchmc/2017_MC*_QBH_n4_M1000_*
#hadd -f output/RPV_M1000.root	 	batchmc/2017_MC*_RPV_M1000_*
