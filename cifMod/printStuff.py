import cifLib.helpL as hlp
import sys
import os

"""Handles signals from libraries and does the printing and exiting"""

def handleSignal(argv, pSignal):
    """From cliP getParsedSignals"""
    pName = os.path.basename(argv[0])
    if pSignal == 100:
        hlp.printUsage(pName, True)
        sys.exit()
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
        sys.stderr.write("error: outCsv has to end with .csv or a '-'\n")
        hlp.printUsage(pName)
        sys.exit()

    if pSignal == 1000:
        print("#Sample format string, put this in a file")
        print('block.name, cleanNum(block.find_pair("_cell_length_a")[1]), cleanNum(block.find_pair("_cell_length_b")[1]), cleanNum(block.find_pair("_cell_length_c")[1])')
        print("#Try, for example; cif2Csv --sampleFmt > sampleFmt.txt")
        print("#Then use it!")
        print("#Note that python's eval is being used ==> there are serious SECURITY ISSUES!!")
        print("#NEVER EVER USE A fmtFile WITHOUT READING IT FIRST!!")
        sys.exit()

    if pSignal == 200:
        sys.stderr.write("error: --log needs exactly 1 argument\n")
        sys.exit()
