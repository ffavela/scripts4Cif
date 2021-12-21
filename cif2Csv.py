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
    print(fmtStrList)

    if inPath[-1] == '/':
        inPath = inPath[:-1]#removing trailing '/'

    for cRoute in fnd.yieldCifRoute(inPath):
        print(cRoute)
        # proc.simpleProcess(inPath, fmtStrList)
        block = fmt.getBlock(cRoute)
        print(block.name, misc.cleanNum(block.find_pair("_cell_length_a")[1]))


if __name__ == "__main__":
    main(sys.argv)
