import numpy as np
from math import radians
from pymatgen.core.structure import Structure


# Network parameters
def get_lattice(file_struct):
    """
    Obtiene en una lista los parametros de la red.

    Return
    ------
    list
        A list with the next elements

        [a, b, c, alfa, beta, gama]

    """
    # Sides
    a = float(file_struct.lattice.a)
    b = float(file_struct.lattice.b)
    c = float(file_struct.lattice.c)

    # Angles
    angulos = file_struct.lattice.angles  # tuple type

    alfa = float(angulos[0])
    beta = float(angulos[1])
    gama = float(angulos[2])

    values = [a, b, c, alfa, beta, gama]
    return values


# Network type and volume
def get_lattice_class_and_volume(file_struct):
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
    lattice_parameters = get_lattice(file_struct)


    a = lattice_parameters[0]
    b = lattice_parameters[1]
    c = lattice_parameters[2]
    alpha = lattice_parameters[3]
    beta = lattice_parameters[4]
    gamma = lattice_parameters[5]


    if alpha == gamma == 90.0 and beta != 90.0 and a != c:
        red = "monoclinic"
        volumen = a*b*c*np.sin(radians(beta))

    elif alpha == gamma == beta == 90.0 and a != b != c:
        red = "orthorhombic"
        volumen = a*b*c

    elif alpha == gamma == beta == 90.0 and a == b != c:
        red = "tetragonal"
        volumen = (a**2)*c

    elif alpha == beta == gamma != 90.0 and a == b == c:
        red = "rhombohedral"
        s1 = 3*(np.cos(radians(alpha))**2)
        s2 = 2*(np.cos(radians(alpha))**3)
        volumen = (a**3)*np.sqrt(1-s1+s2)

    elif alpha == beta == 90.0 and gamma == 120.0 and a == b:
        red = "hexagonal"
        volumen = (np.sqrt(3)/2)*(a**2)*c

    elif alpha == beta == gamma == 90.0 and a == b == c:
        red = "cubic"
        volumen = a**3

    else:
        red = "triclinic"
        s1 = np.cos(radians(alpha))**2
        s2 = np.cos(radians(beta))**2
        s3 = np.cos(radians(gamma))**2
        s4 = 2*np.cos(radians(alpha))*np.cos(radians(beta))*np.cos(radians(gamma))
        # Condition when the root is negative.
        if (1-s1-s2-s3+s4)<0:
            volumen = 'Nan'
        else: # Normal condition.
            volumen = a*b*c*(np.sqrt(1-s1-s2-s3+s4))

    return red, volumen
