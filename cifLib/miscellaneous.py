import re
import math

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

def getSublattice(block):
    sL = ['P', 'I', 'F', 'C']
    thing = block.find_pair("_symmetry_space_group_name_Hall")[1]
    if thing != None:
        for sl in sL:
            if sl in thing:
                return sl
    return None

def get_atom_number_old(block):
    atom_number = len(block.find("_atom_site_label"))
    return atom_number

def extract_number(cadena):
    match = re.match(r"([0-9.]+)", cadena)
    if match:
        return float(match.group(1))
    else:
        try:
            return float(cadena)
        except:
            return None

def count_atoms(block):
    # Get occupancies and multiplicities, in case they don't exist
    # place a None
    try: # For occupancy
        occupancies = block.find_loop('_atom_site_occupancy')
    except KeyError:
        occupancies = None

    try:
        multiplicities = block.find_loop('_atom_site_symmetry_multiplicity')
    except KeyError:
        multiplicities = None

    labels = block.find_loop('_atom_site_label')

    number_of_atoms = 0

    for i in range(len(labels)):
        # If the occupancy was found use it, else use 1.
        if occupancies:
            occupancy = extract_number(occupancies[i])
        else:
            occupancy = 1 # Asumir occupancy 1 si no se especifica
        # If the multipliticy was found use it, else use 1.
        if multiplicities:
            multiplicity = int(multiplicities[i])
        else:
            multiplicity = 1
        number_of_atoms += occupancy * multiplicity

    return number_of_atoms

def formula_cell_volume(a, b, c, alpha, beta, gamma):
    # Convert the angles from degrees to radians
    alpha_rad = math.radians(alpha)
    beta_rad = math.radians(beta)
    gamma_rad = math.radians(gamma)

    # Calculate the cosines of the angles
    cos_alpha = math.cos(alpha_rad)
    cos_beta = math.cos(beta_rad)
    cos_gamma = math.cos(gamma_rad)

    # Calculate the term 1 - cos^2(alpha) - cos^2(beta) - cos^2(gamma)
    term1 = 1 - cos_alpha**2 - cos_beta**2 - cos_gamma**2

    # Calculate the term 2 * cos(alpha) * cos(beta) * cos(gamma)
    term2 = 2 * cos_alpha * cos_beta * cos_gamma

    # Calculate the square root of the sum of the terms
    sqrt_term = math.sqrt(term1 + term2)

    # Calculate the cell volume
    volume = a * b * c * sqrt_term

    return volume

def get_bravais_cell_volume(block):
    # Get the cell lengths and angles
    a = block.find_pair('_cell_length_a')[1]
    b = block.find_pair('_cell_length_b')[1]
    c = block.find_pair('_cell_length_c')[1]
    alpha = block.find_pair('_cell_angle_alpha')[1]
    beta = block.find_pair('_cell_angle_beta')[1]
    gamma = block.find_pair('_cell_angle_gamma')[1]
    # Remove uncertainty info from values.
    a = extract_number(a)
    b = extract_number(b)
    c = extract_number(c)
    alpha = extract_number(alpha)
    beta = extract_number(beta)
    gamma = extract_number(gamma)
    # Calculate the cell volume using the formula_volume function
    volume = formula_cell_volume(a, b, c, alpha, beta, gamma)
    return volume

def get_bravais(block):
    # Get the cell lengths and angles
    a = block.find_pair('_cell_length_a')[1]
    b = block.find_pair('_cell_length_b')[1]
    c = block.find_pair('_cell_length_c')[1]
    alpha = block.find_pair('_cell_angle_alpha')[1]
    beta = block.find_pair('_cell_angle_beta')[1]
    gamma = block.find_pair('_cell_angle_gamma')[1]
    # Remove uncertainty info from values.
    a = extract_number(a)
    b = extract_number(b)
    c = extract_number(c)
    alpha = extract_number(alpha)
    beta = extract_number(beta)
    gamma = extract_number(gamma)
    result = None
    # Content
    if math.isclose(a, b) and math.isclose(b, c) and math.isclose(alpha, beta)\
       and math.isclose(beta, gamma) and math.isclose(gamma, 90):
        result = "cubic"
    elif math.isclose(a, b) and b != c and math.isclose(alpha, beta)\
         and math.isclose(beta, gamma) and math.isclose(gamma, 90):
        result = "tetragonal"
    elif a != b and b != c and a != c and math.isclose(alpha, beta)\
         and math.isclose(beta, gamma) and math.isclose(gamma, 90):
        result = "orthorhombic"
    elif math.isclose(a, b) and b != c and math.isclose(alpha, beta)\
         and math.isclose(beta, 90) and math.isclose(gamma, 120):
        result = "hexagonal"
    elif math.isclose(a, b) and math.isclose(b, c) and math.isclose(alpha, beta)\
         and math.isclose(beta, gamma) and gamma != 90:
        result = "trigonal"
    elif a != b and b != c and a != c and math.isclose(alpha, gamma)\
         and beta != 120 and math.isclose(gamma, 90):
        result = "monoclinic"
    elif a != b and b != c and a != c and alpha != beta and beta != gamma \
         and gamma != 90:
        result = "triclinic"
    return result

def get_form_sum(block):
    form_sum = block.find_pair('_chemical_formula_sum')[1]
    return form_sum

def get_presence(block):
    form_sum = get_form_sum(block)
    clean = re.sub(r'\.?\d+(\.\d+)?', '', form_sum)
    clean = re.sub(r'\bD\b', 'H', clean) #Deuterium case
    return clean

