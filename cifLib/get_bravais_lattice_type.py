#from cifLib.miscellaneous import cleanNum

def cleanNum(numStr):
    """Removes the parenthesis, simple implementation"""
    return numStr[:numStr.find('(')]


def get_bravais_lattice_type(block):
    a = float(cleanNum(block.find_pair("_cell_length_a")[1]))
    b = float(cleanNum(block.find_pair("_cell_length_b")[1]))
    c = float(cleanNum(block.find_pair("_cell_length_c")[1]))
    alpha = float(cleanNum(block.find_pair("_cell_angle_alpha")[1]))
    beta = float(cleanNum(block.find_pair("_cell_angle_beta")[1]))
    gamma = float(cleanNum(block.find_pair("_cell_angle_gamma")[1]))

    if alpha == gamma == 90.0 and beta != 90.0 and a != c:
        red = "monoclinic"

    elif alpha == gamma == beta == 90.0 and a != b != c:
        red = "orthorhombic"

    elif alpha == gamma == beta == 90.0 and a == b != c:
        red = "tetragonal"

    elif alpha == beta == gamma != 90.0 and a == b == c:
        red = "rhombohedral"

    elif alpha == beta == 90.0 and gamma == 120.0 and a == b:
        red = "hexagonal"

    elif alpha == beta == gamma == 90.0 and a == b == c:
        red = "cubic"

    else:
        red = "triclinic"

    return red
