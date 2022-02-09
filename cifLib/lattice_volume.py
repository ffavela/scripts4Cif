import numpy as np
from math import radians
from pymatgen.core.structure import Structure


# Parametros de red
def get_lattice(file_struct):
    """
    Obtiene en una lista los parametros de la red.
    
    Return
    ------
    list
        Una lista con los elementos siguientes
        
        [a, b, c, alfa, beta, gama]
        
    """
    # Lados
    a = float(file_struct.lattice.a)
    b = float(file_struct.lattice.b)
    c = float(file_struct.lattice.c)
    
    # Angulos
    angulos = file_struct.lattice.angles  # tipo tupla
    
    alfa = float(angulos[0])
    beta = float(angulos[1])
    gama = float(angulos[2])
    
    values = [a, b, c, alfa, beta, gama]
    return values


# Tipo de red y volumen
def get_lattice_class_and_volume(file_struct):
    """
    La función requiere de la estructura de pymatgen file_struct.
    Según los 6 parámetros que se obtienen de lattice, nos dará el tipo de red y el volumen de la misma.
    
    Parameters
    ----------
    file_struct: pymatgen structure
    
    
    Return
    ------
    tuple: (str, float)
        Una tupla con el primer elemento "el tipo de red" y el seguno el volumen calculado
        
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
        # Condición para cuando la raíz es negativa. (A veces pasa)
        if (1-s1-s2-s3+s4)<0:
            volumen = 'Nan'
        else: # Codicion normal.
            volumen = a*b*c*(np.sqrt(1-s1-s2-s3+s4))
    
    return red, volumen