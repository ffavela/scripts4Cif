import os
from gemmi import cif
import cifLib.miscellaneous as misc
import cifLib.fmtParsing as fmt

def printDeepTxt(path="./"):
    """A simple recursive function that looks for all the existing .txt
files from a given path prints the file name and it's content

    """
    if os.path.isfile(path):
        if path.endswith(".txt"):
            print("A file", path)
            with open(path) as f:
                print(f.read())

            return

    os.chdir(path)

    print(os.getcwd())
    for e in os.listdir():
        printDeepTxt(e)

    os.chdir("../")

def deepCif2Csv(path="./"):
    """Given a path it will yield all the files that end with .cif"""
    if os.path.isfile(path) and path.endswith(".cif"):
        yield os.getcwd()+path
        return

    os.chdir(path)

    for e in os.listdir():
        yield from deepCif2Csv(e)

    os.chdir("../")

# A first approach in order to have a functional program, I will
# probably delete this so don't rely on this one.
def processFiles(inPath, fmtFile, outCsv):
    fmtParsing = fmt.getStrFmtList(fmtFile)
    # print(fmtParsing)
    """Doing all at once"""
    def deepProcess(path="./"):
        if os.path.isfile(path) and path.endswith(".cif"):
            block = fmt.getBlock(path)
            print("block.name = ", misc.myEval("block.name", block))
            fmtEvalList = [misc.myEval(val, block) for val in fmtParsing]
            print(fmtEvalList)
            return

        os.chdir(path)

        for e in os.listdir():
            deepProcess(e)

        os.chdir("../")

    deepProcess(inPath)
