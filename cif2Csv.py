#!/usr/bin/python

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

    inPath, fmtFile, outCsv = argv[1:4]
    fmtStrList=fmt.getStrFmtList(fmtFile)

    if inPath[-1] == '/':
        inPath = inPath[:-1]#removing trailing '/'

    with open(outCsv, 'w') as f:
        if outCsv == "-":
            f = sys.stdout

        for cRoute in fnd.yieldCifRoute(inPath):
            block = fmt.getBlock(cRoute)
            evalList=[misc.myEval(e, block) for e in fmtStrList]

            try:
                csvStr = ", ".join(evalList)
            except:
                sys.stderr.write("error: %s is None\n" %(cRoute))
                if '-l' in myOptDict:
                    with open(myOptDict['-l'][0], 'a') as lF:
                        lF.write("error: %s is None\n" %(cRoute))

            f.write(csvStr+'\n')
            if '--tee' in myOptDict:
                print(csvStr)

if __name__ == "__main__":
    main(sys.argv)
