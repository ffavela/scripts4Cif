"""Just the help functions"""

def printUsage(sName="cif2Csv", extended = False):
    """Just a synopsis"""
    print(sName+" [[-h|--help] | --sampleFmt]")
    print(sName+" <inPath> <fmtFile> <outCsv> [options]")

    if extended:
        print()
        print("NOTE: if outCsv is - then the csv is written to stdout")
        print()
        print("\t-h | --help\t\tprints the extended options")
        print("\t--sampleFmt\t\toutputs a sample format")
        print("\t\t\t\tfor creating a csv file")
        print("\t--tee\t\t\twill print the output to")
        print("\t\t\t\tstdout in addition to outCsv")
