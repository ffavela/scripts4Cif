import cifLib.cifFinder as fnd  # type: ignore
import cifLib.fmtParsing as fmt
import cifLib.miscellaneous as misc

def test_countTest():
    """Testing the cif counting"""

    expCount = 100
    assert expCount == fnd.getCifCount('dir4Tests/cifs4Tests')

def test_sample0():
    fname = 'dir4Tests/sampleTests/sample1.csv'
    fmtFile = 'sampleFormats/sample1.fmt'
    inPath = 'dir4Tests/cifs4Tests'
    fmtStrList=fmt.getStrFmtList(fmtFile)
    with open(fname, 'r') as file:
        lines = file.readlines()
    i = 0
    for cRoute in fnd.yieldCifRoute(inPath):
        block = fmt.getBlock(cRoute)
        evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
        csvStr = ", ".join(evalList) + '\n'
        assert lines[i] == csvStr
        i += 1

