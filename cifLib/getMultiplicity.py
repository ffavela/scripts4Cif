import gemmi
from gemmi import cif
from numpy import zeros,asarray,dot

cifRoute = '/home/carlos/Documents/Cristales/cif/9/01/47/9014752.cif'

def getBlock(cifRoute):
    """Gets a single block from a given cif file"""
    doc = cif.read_file(cifRoute)
    if len(doc) == 0:
        return None
    block = doc.sole_block()
    return block

block = getBlock(cifRoute)

def getOccupancies(cifRoute):
    structure = gemmi.read_small_structure(cifRoute)
    
    listOcc = zeros(len(structure.sites))
    
    for i in range(0,len(structure.sites)):
    	listOcc[i] = structure.sites[i].occ
    
    return listOcc

def getMultiplicity(cifRoute,block):
    listMult = block.find_loop('_atom_site_symmetry_multiplicity')

    return listMult

def getAtomNumber(cifRoute,block):
    listOcc_arr = asarray(getOccupancies(cifRoute))
    listMult_arr = asarray(getMultiplicity(cifRoute,block), float)

    return dot(listOcc_arr,listMult_arr)


print(getAtomNumber(cifRoute,block))
