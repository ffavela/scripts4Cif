import re
import math

"""Just a set of miscellaneous functions"""

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
    return numStr[:numStr.find('(')]

def rmTrailSlash(strPath):
    if strPath[-1] == '/':
        strPath = strPath[:-1]#removing trailing '/'
    return strPath

def rmSN(strVal):
    """Removes the semicolons on a string & \n"""
    return strVal.replace(';', '').replace('\n', '')

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
