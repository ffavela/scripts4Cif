"""Just the help functions"""

def printUsage(sName="cif2Csv", extended = False):
    """Just a synopsis"""
    print(sName+" [[-h|--help] | --sampleFmt]")
    print(sName+" <inPath> [-c | --count]")
    print(sName+" <inPath> <fmtFile> <outCsv> [options]")

    if extended:
        print()
        print("inPath;\t\ta path to cif files")
        print("fmtFile;\ta file that defines the fields")
        print("\t\tfor creating the outCsv file")
        print("\t\tsee the --sampleFmt option")
        print("outCsv;\t\tthe resulting csv file")
        print()
        print("NOTE: if outCsv is '-' then the csv is written to stdout")
        print()
        print("options:\n")
        print("\t-h | --help\t\tprints the extended options")
        print("\t--sampleFmt\t\toutputs a sample format")
        print("\t\t\t\tfor creating a csv file")
        print("\t--tee\t\t\twill print the output to")
        print("\t\t\t\tstdout in addition to outCsv,")
        print("\t\t\t\tdon't use when outCsv is '-'")
        print("\t\t\t\tthat's weird!!")
        print("\t-l | --log logFile\tlogging errors into the logFile")
        print("\t\t\t\tlog messages will be appended here")
        print("\t-c | --count\t\twill count all the cif files in the")
        print("\t\t\t\tinPath both fmtFile and outCsv can")
        print("\t\t\t\tbe '-' or omitted")
