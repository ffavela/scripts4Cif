"""Just a set of miscellaneous functions"""
import numpy as np
import cifLib.lattice_volume as latt
from math import radians
from cifLib.get_bravais_lattice_type import *
import gemmi 

def isFloat(myStr):
    try:
        float(myStr)
    except ValueError:
        return False
    return True

def myEval(myStr, block):
    try:
        return eval(myStr)
    except:
        return None
        
def cleanNum(numStr): 
     """Removes the parenthesis, simple implementation""" 
     if numStr.find('(') != -1:       
         return numStr[:numStr.find('(')] 
     return numStr

def cleanJournal(Str): 
     """Removes the ; and ' (simple implementation)""" 
     Str = Str.replace(";","")
     Str = Str.replace("'","")
     Str = Str.replace("\n","")
     Str = Str.lstrip()
     Str = Str.rstrip()
     Str = Str.upper()
     return Str

def rmTrailSlash(strPath):
    if strPath[-1] == '/':
        strPath = strPath[:-1]#removing trailing '/'
    return strPath

def rmSN(strVal):
    """Removes the semicolons on a string & \n"""
    return strVal.replace(';', '').replace('\n', '')
    
def simpleOperation(intVal):
    return intVal + 1000
    
def get_lattice_volume(block):
    """
    The function requires the pymatgen file_struct structure.
    According to the 6 parameters obtained from lattice, it will give us the type of network and the network volume

    Parameters
    ----------
    file_struct: pymatgen structure


    Return
    ------
    tuple: (str, float)
        A tuple with the first element "the type of net" and the second element the calculated volume

    """


    a = float(cleanNum(block.find_pair("_cell_length_a")[1]))
    b = float(cleanNum(block.find_pair("_cell_length_b")[1]))
    c = float(cleanNum(block.find_pair("_cell_length_c")[1]))
    alpha = float(cleanNum(block.find_pair("_cell_angle_alpha")[1]))
    beta = float(cleanNum(block.find_pair("_cell_angle_beta")[1]))
    gamma = float(cleanNum(block.find_pair("_cell_angle_gamma")[1]))


    if alpha == gamma == 90.0 and beta != 90.0 and a != c:
#        red = "monoclinic"
        volumen = a*b*c*np.sin(radians(beta))

    elif alpha == gamma == beta == 90.0 and a != b != c:
#        red = "orthorhombic"
        volumen = a*b*c

    elif alpha == gamma == beta == 90.0 and a == b != c:
#        red = "tetragonal"
        volumen = (a**2)*c

    elif alpha == beta == gamma != 90.0 and a == b == c:
#        red = "rhombohedral"
        s1 = 3*(np.cos(radians(alpha))**2)
        s2 = 2*(np.cos(radians(alpha))**3)
        volumen = (a**3)*np.sqrt(1-s1+s2)

    elif alpha == beta == 90.0 and gamma == 120.0 and a == b:
#        red = "hexagonal"
        volumen = (np.sqrt(3)/2)*(a**2)*c

    elif alpha == beta == gamma == 90.0 and a == b == c:
#        red = "cubic"
        volumen = a**3

    else:
#        red = "triclinic"
        s1 = np.cos(radians(alpha))**2
        s2 = np.cos(radians(beta))**2
        s3 = np.cos(radians(gamma))**2
        s4 = 2*np.cos(radians(alpha))*np.cos(radians(beta))*np.cos(radians(gamma))
        
        volumen = a*b*c*(np.sqrt(1-s1-s2-s3+s4))

    return volumen

def get_atom_count(formulaBlock):
    elements = gemmi.make_small_structure_from_block(formulaBlock)
    return len(elements.sites)

def get_element_count(formulaString):
    elements = gemmi.make_small_structure_from_block(formulaBlock)
    return [elements.sites[i].label for i in range(len(elements.sites))]