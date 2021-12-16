#!/usr/bin/python

import sys
import cifLib.helpL as hlp
import cifLib.cliParsing as cliP
import cifMod.printStuff as pS
import cifMod.processing as proc
import cifLib.cifFinder as fnd

def main(argv):
    myOptDict = cliP.getMyOptDict1(argv)

    pSignal = cliP.getParsedSignals(argv, myOptDict)
    pS.handleSignal(argv, pSignal)

    inPath, fmtFile, outCsv = argv[1:4]
    for e in fnd.yieldCifRoute(inPath):
        print(e)


if __name__ == "__main__":
    main(sys.argv)
