from pymatgen.core.structure import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def get_wyckoff_data(structure):
    """
    Return
    ------
    Returns a list of lists which contains the following for every site: wyckoff letter, number of times a letter repeats,
    the symbol of the element on the site and the ocupation of that element on the site.
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
    conjunto : list of lists
	Every list contains a letter, the wyckoff number assigned by pymatgen, the letter of the element on the site and
	the occupancy.

    Return
    ------
    Returns a dictionary. Every "key" is a tuple of the information contained in the list of the variable "conjunto". The associated
    "value" for every "key" it's the multiplicity for that site.
    """
    mult_dict = {}

    for e in conjunto:
        if tuple(e) not in mult_dict:
            mult_dict[tuple(e)] = 0

        mult_dict[tuple(e)] += 1

    return mult_dict


def num_atoms(diccionario):
    """
    It is obtained by multiplying the multiplicity times the occupation of the site.
    """
    suma = 0
    for e in diccionario:
        suma += e[-1] * diccionario[e]

    return suma

# - - - - - - - - - - Funcion principal - - - - - - - - - -
def get_num_atoms(file_struct):
    """
    This function uses other base functions to give the number of atoms.

    Return
    ------
    float
	Number of atoms of the sample.
    """
    conjunto = get_wyckoff_data(file_struct)

    mult_dict = get_multiplicity(conjunto)

    atoms = float(num_atoms(mult_dict))

    return atoms
