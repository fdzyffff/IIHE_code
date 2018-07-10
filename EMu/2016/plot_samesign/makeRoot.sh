#rm data_2016E_DoubleEG.root
mkdir output
rm output/*.root


#hadd data_2016E_DoubleEG.root data_2016E_DoubleEG*
hadd -f output/DYToLL.root DYToLL_*
hadd -f output/WJets.root WJets_*
hadd -f output/ttbar.root ttbar_*
hadd -f output/ttbar2l2u_0-1.root ttbar2l2u_0000.root ttbar2l2u_0001.root
hadd -f output/ttbar2l2uNosc.root ttbar2l2uNosc_*
hadd -f output/ST.root ST_*
hadd -f output/WW1.root WW1_*
hadd -f output/WW2.root WW2_*root
hadd -f output/WW3.root WW3_*root
hadd -f output/WW4.root WW4_*root
hadd -f output/WW5.root WW5_*root
hadd -f output/WZ.root WZ_*
hadd -f output/ZZ.root ZZ_*
