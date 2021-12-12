#!/usr/bin/python

import sys
import cifLib.helpL as hlp
import cifLib.processing as proc
import cifLib.cliParsing as cliP
import cifMod.printStuff as pS

def main(argv):
    myOptDict = cliP.getMyOptDict1(argv)
    # proc.printDeepTxt()
    pSignal = cliP.getParsedSignals(argv, myOptDict)
    print("pSignal = ", pSignal)
    pS.handleSignal(argv, pSignal)
    # if '-h' in myOptDict:
    #     hlp.printUsage()
    #     sys.exit()

    print(sys.argv)
    
if __name__ == "__main__":
    main(sys.argv)
