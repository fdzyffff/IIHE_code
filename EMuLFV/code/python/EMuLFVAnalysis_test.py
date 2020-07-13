import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('python')

options.register('inputFilename', 'DYJets_inc_small', #HTauTauAnalysis_1_1_Sl2.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Input file name"
)


options.register('outFilename', 'Output_default.root', #HTauTauAnalysis_1_1_Sl2.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
)

options.register('sample', 'DYinc', #HTauTauAnalysis_1_1_Sl2.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Name of sample you are running on"
)
#~~~~~~~~~~~~~~~~ my para ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
options.register('datasetisMuon', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "dataset_isMuon"
)

options.register('isData', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isData"
)

options.register('isDY', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isDY"
)

options.register('isTTbar', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isTTbar"
)

options.register('isWW', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isWW"
)

options.register('ttbarreweight', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "ttbar_reweight"
)

options.register('isFakee', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isFake_e"
)

options.register('isFakemu', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isFake_mu"
)

options.register('useSYS', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "useSYS"
)

options.register('usePDF', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "usePDF"
)

options.register('year', '2016',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "year"
)

options.register('InputFile', 'no-file',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "InputFile"
)


options.parseArguments()

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

#process.TFileService=cms.Service("TFileService",fileName=cms.string("Dec31_OUT_"+options.outFilename))

process.TFileService=cms.Service("TFileService",fileName=cms.string(options.outFilename))



process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("EmptySource")
#process.Timing = cms.Service("Timing",
#  summaryOnly = cms.untracked.bool(False),
#  useJobReport = cms.untracked.bool(True)
#)
process.tauhist = cms.EDAnalyzer('EMuLFV',
                                dataset_isMuon = cms.bool(options.datasetisMuon),
                                isData = cms.bool(options.isData),
                                isDY = cms.bool(options.isDY),
                                isTTbar = cms.bool(options.isTTbar),
                                isWW = cms.bool(options.isWW),
                                ttbar_reweight = cms.bool(options.ttbarreweight),
                                isFake_e = cms.bool(options.isFakee),
                                isFake_mu = cms.bool(options.isFakemu),
                                year = cms.string(options.year),
                                InputFile = cms.string(options.InputFile),
                                useSYS = cms.bool(options.useSYS),
                                usePDF = cms.bool(options.usePDF),
)


process.p = cms.Path(process.tauhist)
