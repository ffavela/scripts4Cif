from gemmi import cif

def getBlock(cifFName):
    doc = cif.read_file(cifFName)
    block = doc.sole_block()
    return block

def getStrFmtList(fmtPath):
    """A really simple parser good enough for the moment"""
    with open(fmtPath) as f:
        V=f.readlines()

    for v in V:
        s=v.rstrip().lstrip()
        if '#' in s or s == '':
            continue
        return v.split(',')
