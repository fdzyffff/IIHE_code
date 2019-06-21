To checkout do:
git clone ssh://git@gitlab.cern.ch:7999/aidan/HEEPScaleFactorStudy.git

Then you need to make a directory to store the plots:

mkdir plots

mkdir plots/<YYYYMMDD>

Then you need to make directories for the ntuple:

mkdir ntuples

mkdir ntuples/in

mkdir ntuples/out

Then run the script:

python TagAndProbe.py