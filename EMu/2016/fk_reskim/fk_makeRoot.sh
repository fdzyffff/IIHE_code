#rm data_2016E_DoubleEG.root
mkdir output
rm output/*.root


#hadd data_2016E_DoubleEG.root data_2016E_DoubleEG*
hadd -f output/fk_DYToLL_all.root	batchmc/fk_2016_MC*_DYToLL_all_*
hadd -f output/fk_DYToLL_1.root	 	batchmc/fk_2016_MC*_DYToLL_1_*
hadd -f output/fk_DYToLL_2.root	 	batchmc/fk_2016_MC*_DYToLL_2_*
hadd -f output/fk_DYToLL_3.root	 	batchmc/fk_2016_MC*_DYToLL_3_*
hadd -f output/fk_DYToLL_4.root	 	batchmc/fk_2016_MC*_DYToLL_4_*
hadd -f output/fk_DYToLL_5.root	 	batchmc/fk_2016_MC*_DYToLL_5_*
hadd -f output/fk_DYToLL_6.root	 	batchmc/fk_2016_MC*_DYToLL_6_*
hadd -f output/fk_DYToLL_7.root	 	batchmc/fk_2016_MC*_DYToLL_7_*
hadd -f output/fk_DYToLL_8.root	 	batchmc/fk_2016_MC*_DYToLL_8_*
hadd -f output/fk_DYToLL_9.root	 	batchmc/fk_2016_MC*_DYToLL_9_*
hadd -f output/fk_WJets.root 		batchmc/fk_2016_MC*_WJets_*
hadd -f output/fk_ttbar.root 		batchmc/fk_2016_MC*_ttbar_*
hadd -f output/fk_ttbar2l2u_1.root 	batchmc/fk_2016_MC*_ttbar2l2u_1_*
hadd -f output/fk_ttbar2l2u_2.root 	batchmc/fk_2016_MC*_ttbar2l2u_2_*
hadd -f output/fk_ttbar2l2u_3.root 	batchmc/fk_2016_MC*_ttbar2l2u_3_*
hadd -f output/fk_ttbar2l2u_4.root 	batchmc/fk_2016_MC*_ttbar2l2u_4_*
hadd -f output/fk_ttbar2l2u_5.root 	batchmc/fk_2016_MC*_ttbar2l2u_5_*
hadd -f output/fk_ST.root 		batchmc/fk_2016_MC*_ST_*
hadd -f output/fk_WW_all.root 		batchmc/fk_2016_MC*_WW_all_*
hadd -f output/fk_WW1.root 		batchmc/fk_2016_MC*_WW1_*
hadd -f output/fk_WW2.root 		batchmc/fk_2016_MC*_WW2_*root
hadd -f output/fk_WW3.root 		batchmc/fk_2016_MC*_WW3_*root
hadd -f output/fk_WW4.root 		batchmc/fk_2016_MC*_WW4_*root
hadd -f output/fk_WW5.root 		batchmc/fk_2016_MC*_WW5_*root
hadd -f output/fk_WZ.root		batchmc/fk_2016_MC*_WZ_*
hadd -f output/fk_ZZ.root 		batchmc/fk_2016_MC*_ZZ_*
