from pymatgen.core.structure import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def get_wyckoff_data(structure):
    """
    Return
    ------
    Regresa una lista de listas que contienen de cada sitio: letra de wyckoff, numero de repeticiones de la letra, 
    el simbolo del elemento del sitio y la ocupación de ese elemento en el sitio.
    """
    sitios = structure.sites
    
    symmetry_data = SpacegroupAnalyzer(structure).get_symmetry_dataset()
    wyckoff_letters = symmetry_data["wyckoffs"]
    equiv_atoms = list(symmetry_data["equivalent_atoms"])
    
    conjunto = [[i,j, k.species.elements[0].symbol, k.species.num_atoms] for i, j, k in zip(wyckoff_letters, equiv_atoms, sitios)]
    
    return conjunto


def get_multiplicity(conjunto):
    """
    Parameters
    ----------
    conjunto : lista de listas
        Cada lista contiene la letra, el numero de wyckoff que otorga pymatgen, la letra del elemento en el sitio
        y la ocupancia.
        
    Return
    ------
    Regresa un diccionario. Cada "key" es una tupla de la informacion de la lista del conjunto. el "valor" asociado
    a cada "key" es la multiplicidad para ese sitio.
    """
    mult_dict = {}

    for e in conjunto:
        if tuple(e) not in mult_dict:
            mult_dict[tuple(e)] = 0

        mult_dict[tuple(e)] += 1
        
    return mult_dict


def num_atoms(diccionario):
    """
    Se obtiene de la multiplicación de la multiplicidad por la ocupación del sitio.
    """
    suma = 0
    for e in diccionario:
        suma += e[-1] * diccionario[e]
        
    return suma

# - - - - - - - - - - Funcion principal - - - - - - - - - -
def get_num_atoms(file_struct):
    """
    Funcion que utiliza funciones base para dar el numero de atomos.
    
    Return
    ------
    float
        Numero de atomos de la muestra.
    """
    conjunto = get_wyckoff_data(file_struct)
    
    mult_dict = get_multiplicity(conjunto)
    
    atoms = float(num_atoms(mult_dict))
    
    return atoms