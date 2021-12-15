import cifLib.helpL as hlp
import sys
import os

"""Handles signals from libraries and does the printing and exiting"""

def handleSignal(argv, pSignal):
    """From cliP getParsedSignals"""
    pName = os.path.basename(argv[0])
    if pSignal == 1:
        hlp.printUsage(pName)
        sys.exit()

    if pSignal == 2:
        sys.stderr.write("error: 3 filenames are needed as arguments\n")
        hlp.printUsage(pName)
        sys.exit()

    if pSignal == 3:
        sys.stderr.write("error: inPath has to exist\n")
        hlp.printUsage(pName)
        sys.exit()

    if pSignal == 4:
        sys.stderr.write("error: fmtFile has to exist\n")
        hlp.printUsage(pName)
        sys.exit()

    if pSignal == 5:
        sys.stderr.write("error: fmtFile has to be a regular file\n")
        hlp.printUsage(pName)
        sys.exit()

    if pSignal == 6:
        sys.stderr.write("error: outCsv has to end with .csv\n")
        hlp.printUsage(pName)
        sys.exit()

    if pSignal == 1000:
        print("REPLACING THIS WITH SAMPLE FMT TEXT")
        sys.exit()
