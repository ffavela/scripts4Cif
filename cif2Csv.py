#!/usr/bin/python

import sys
import cifLib.helpL as hlp
import cifLib.cliParsing as cliP
import cifMod.printStuff as pS
import cifMod.processing as proc

def main(argv):
    # proc.printDeepTxt("a/b/c/d/test.txt")
    # proc.printDeepTxt(argv[1])
    # sys.exit()
    myOptDict = cliP.getMyOptDict1(argv)
    # proc.printDeepTxt()
    pSignal = cliP.getParsedSignals(argv, myOptDict)
    pS.handleSignal(argv, pSignal)
    if '-h' in myOptDict:
        hlp.printUsage()
        sys.exit()

    # print(argv)
    inPath, fmtFile, outCsv = argv[1:4]
    # print(inPath, fmtFile, outCsv)
    i=0
    # for e in proc.deepCif2Csv(inPath):
    print("Doing the printing using deepCif")
    # proc.deepCif2Csv(inPath)
    # for e in proc.deepCif2Csv(inPath):
    #     print(e)
    proc.processFiles(inPath, fmtFile, outCsv)

if __name__ == "__main__":
    main(sys.argv)
