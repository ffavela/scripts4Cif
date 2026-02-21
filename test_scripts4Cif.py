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

    # Doing all this hassle to avoid race contitions
    anotherL = sorted([line.split(',') for line in lines],
                      key = lambda x: x[0])
    # Yeah very unoptimized but the list is not that long
    anotherL = [a[:-1]+[a[-1].strip()] for a in anotherL]
    genCsvL = []
    for cRoute in fnd.yieldCifRoute(inPath):
        block = fmt.getBlock(cRoute)
        evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
        genCsvL.append(evalList)

    genSorted = sorted(genCsvL, key = lambda x: x[0])

    for aL, gS in zip(anotherL, genSorted):
        assert aL == gS

