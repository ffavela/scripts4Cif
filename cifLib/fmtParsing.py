from gemmi import cif
from cifLib.super_split import super_split #Fermin's code

def getBlock(cifFName):
    """Gets a single block from a given cif file"""
    doc = cif.read_file(cifFName)
    if len(doc) == 0:
        return None
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
    """A really simple parser just returns the string in question"""
    with open(fmtPath) as f:
        V=f.readlines()

    for v in V:
        s=v.rstrip().lstrip()
        if '#' in s or s == '':
            continue
        return s

def getStrFmtList1(fmtPath):
    """A really newer parser still need 2 improve"""
    with open(fmtPath) as f:
        V=f.readlines()

    for v in V:
        s=v.rstrip().lstrip()
        if '#' in s or s == '':
            continue
        #Using Fermin's code
        return super_split(s)
