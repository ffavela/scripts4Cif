import cifLib.cifFinder as fnd  # type: ignore
import cifLib.fmtParsing as fmt
import cifLib.miscellaneous as misc

def test_countTest():
    """Testing the cif counting"""

    expCount = 100
    assert expCount == fnd.getCifCount('dir4Tests/cifs4Tests')


def test_sample0():
    fname = 'dir4Tests/sampleTests/sample0.csv'
    fmtFile = 'sampleFormats/sample0.fmt'
    inPath = 'dir4Tests/cifs4Tests'
    fmtStrList=fmt.getStrFmtList(fmtFile)
    with open(fname, 'r') as file:
        lines = file.readlines()

    # Doing all this hassle to avoid race contitions
    anotherL = sorted([line.split(',') for line in lines],
                      key = lambda x: x[0])
    # Yeah very unoptimized but the list is not that long
    for i, line in enumerate(anotherL):
         anotherL[i] = [a.strip() for a in line]
    genCsvL = []
    for cRoute in fnd.yieldCifRoute(inPath):
        block = fmt.getBlock(cRoute)
        evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
        genCsvL.append(evalList)

    genSorted = sorted(genCsvL, key = lambda x: x[0])

    for aL, gS in zip(anotherL, genSorted):
        assert aL[0] == gS[0]
        for av, gv in zip(aL[:1], gS[:1]):
            assert float(av) == float(gv)


def test_sample1():
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
    for i, line in enumerate(anotherL):
         anotherL[i] = [a.strip() for a in line]
    genCsvL = []
    for cRoute in fnd.yieldCifRoute(inPath):
        block = fmt.getBlock(cRoute)
        evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
        genCsvL.append(evalList)

    genSorted = sorted(genCsvL, key = lambda x: x[0])

    for aL, gS in zip(anotherL, genSorted):
        assert aL == gS


def test_sample2():
    fname = 'dir4Tests/sampleTests/sample2.csv'
    fmtFile = 'sampleFormats/sample2.fmt'
    inPath = 'dir4Tests/cifs4Tests'
    fmtStrList=fmt.getStrFmtList(fmtFile)
    with open(fname, 'r') as file:
        lines = file.readlines()

    # Doing all this hassle to avoid race contitions
    anotherL = sorted([line.split(',') for line in lines],
                      key = lambda x: x[0])
    # Yeah very unoptimized but the list is not that long
    for i, line in enumerate(anotherL):
         anotherL[i] = [a.strip() for a in line]
    genCsvL = []
    for cRoute in fnd.yieldCifRoute(inPath):
        block = fmt.getBlock(cRoute)
        evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
        genCsvL.append(evalList)

    genSorted = sorted(genCsvL, key = lambda x: x[0])

    for aL, gS in zip(anotherL, genSorted):
        assert aL == gS


def test_sample3():
    fname = 'dir4Tests/sampleTests/sample3.csv'
    fmtFile = 'sampleFormats/sample3.fmt'
    inPath = 'dir4Tests/cifs4Tests'
    fmtStrList=fmt.getStrFmtList(fmtFile)
    with open(fname, 'r') as file:
        lines = file.readlines()

    # Doing all this hassle to avoid race contitions
    anotherL = sorted([line.split(',') for line in lines],
                      key = lambda x: x[0])
    # Yeah very unoptimized but the list is not that long
    for i, line in enumerate(anotherL):
         anotherL[i] = [a.strip() for a in line]
    genCsvL = []
    for cRoute in fnd.yieldCifRoute(inPath):
        block = fmt.getBlock(cRoute)
        evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
        genCsvL.append(evalList)

    genSorted = sorted(genCsvL, key = lambda x: x[0])

    for aL, gS in zip(anotherL, genSorted):
        assert aL == gS


def test_sample4():
    fname = 'dir4Tests/sampleTests/sample4.csv'
    fmtFile = 'sampleFormats/sample4.fmt'
    inPath = 'dir4Tests/cifs4Tests'
    fmtStrList=fmt.getStrFmtList(fmtFile)
    with open(fname, 'r') as file:
        lines = file.readlines()

    # Doing all this hassle to avoid race contitions
    anotherL = sorted([line.split(',') for line in lines],
                      key = lambda x: x[0])
    # Yeah very unoptimized but the list is not that long
    for i, line in enumerate(anotherL):
         anotherL[i] = [a.strip() for a in line]
    genCsvL = []
    for cRoute in fnd.yieldCifRoute(inPath):
        block = fmt.getBlock(cRoute)
        evalList=[str(misc.myEval(e, block)) for e in fmtStrList]
        genCsvL.append(evalList)

    genSorted = sorted(genCsvL, key = lambda x: x[0])

    for aL, gS in zip(anotherL, genSorted):
        assert aL == gS

