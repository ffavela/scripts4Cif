#!/usr/bin/python

import sys
import cifLib.helpL as hlp
import cifLib.cliParsing as cliP
import cifLib.cifFinder as fnd
import cifLib.fmtParsing as fmt
import cifMod.printStuff as pS
import cifMod.processing as proc

from gemmi import cif
import os

def main(argv):
    myOptDict = cliP.getMyOptDict1(argv)

    pSignal = cliP.getParsedSignals(argv, myOptDict)
    pS.handleSignal(argv, pSignal)

    inPath, fmtFile, outCsv = argv[1:4]
    fmtStrList=fmt.getStrFmtList(fmtFile)
    if os.path.isfile(inPath) and inPath.endswith(".cif"):
        block = fmt.getBlock(inPath)
        print(inPath)
        print("block.name = ", block.name)
    else:
        for cRoute in fnd.yieldCifRoute(inPath):
            print(cRoute)
            block = fmt.getBlock(cRoute)
            print("block.name = ", block.name)

if __name__ == "__main__":
    main(sys.argv)
