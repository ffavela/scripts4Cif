#!/usr/bin/python3

import sys
import cifLib.helpL as hlp
import cifLib.cliParsing as cliP
import cifLib.cifFinder as fnd
import cifLib.fmtParsing as fmt
import cifLib.miscellaneous as misc

import cifMod.printStuff as pS
import cifMod.processing as proc

from gemmi import cif
import os

def main(argv):
    myOptDict = cliP.getMyOptDict1(argv)
    pSignal = cliP.getParsedSignals(argv, myOptDict)
    pS.handleSignal(argv, pSignal)

    myOptDict = cliP.getRefactoredOptDict(myOptDict)

    if '-c' in myOptDict:
        #The cif counting
        inPath = misc.rmTrailSlash(argv[1])
        print(fnd.getCifCount(inPath))
        sys.exit()

    if '-p' in myOptDict:
        #The cif printing
        inPath = misc.rmTrailSlash(argv[1])
        fnd.printPath(inPath, '-n' in myOptDict)
        sys.exit()

    inPath, fmtFile, outCsv = argv[1:4]
    fmtStrList=fmt.getStrFmtList(fmtFile)

    if '-H' in myOptDict:
        header='#'+fmt.getStrFmt(fmtFile)

    inPath = misc.rmTrailSlash(inPath)
    fileOp='w'
    if '-a' in myOptDict:
        fileOp='a'
    with open(outCsv, fileOp) if outCsv != '-'\
         else sys.stdout as f:
        if '-H' in myOptDict:#Just writting the header
            f.write(header+'\n')
            if '--tee' in myOptDict:
                print(header)

        for cRoute in fnd.yieldCifRoute(inPath):
            block = fmt.getBlock(cRoute)
            evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
            if 'None' in evalList:
                sys.stderr.write("warning: %s has a None\n" %(cRoute))
                if '-l' in myOptDict:
                    with open(myOptDict['-l'], 'a') as lF:
                        lF.write("warning: %s has a None\n" %(cRoute))
                if '-N' in myOptDict:
                    continue

            csvStr = ", ".join(evalList)

            f.write(csvStr+'\n')
            if '--tee' in myOptDict:
                print(csvStr)

if __name__ == "__main__":
    main(sys.argv)
