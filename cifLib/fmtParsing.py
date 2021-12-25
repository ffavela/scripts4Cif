from gemmi import cif

def getBlock(cifFName):
    """Gets a single block from a given cif file"""
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
        return s.split(',')

def getStrFmt(fmtPath):
    """A really simple parser good enough for the moment"""
    with open(fmtPath) as f:
        V=f.readlines()

    for v in V:
        s=v.rstrip().lstrip()
        if '#' in s or s == '':
            continue
        return s
