from pymatgen.core.structure import Structure

from atoms_counter import get_num_atoms
from lattice_volume import get_lattice_class_and_volume
import get_directions as gd


def get_cif_name(cif_path):
    """
    The cif number of the path file.

    Parameters
    ----------
    cif_path : str
        Contains the cif file path.

    Returns
    -------
    int
        Numero de siete digitos.

    """
    name = int(cif_path[-11:].split(".")[0])
    return name


def analyzer(cif_path, file_struct):
    """
    Obtains the data of interest from the cif file in a list and reports with an "error" string those that could not
    be extracted.

    Parameters
    ----------
    cif_path : str
        Path of the cif file.
    file_struct : pymatgen Structure
        Structure of the cif file.

    Returns
    -------
    list[str, list]
        The first list item is just the string that labels the results as: success or failure ("s" or "f").The second
        list item is a list containing the results of the analysis sorted as follows:

        [cif_num, num_atoms]

    """
    results = []
    
    # 1.Gets the cif ID number.
    cif_name = get_cif_name(cif_path)
    results.append(cif_name)
    
    # 2.Gets the number of atoms in the sample.
    try:
        num_atoms = get_num_atoms(file_struct)
        results.append(num_atoms)
    except:
        results.append("error")
    
    # 3.Gets the volume of the unit cell
    try:
        volume = get_lattice_class_and_volume(file_struct)
        results.append(volume)
    except:
        results.append("error")
    
    # - - - - - - - - - - - - - - - - - - - - - - - -
    # Success or failure
    if "error" in results:
        # If there are "errors" strings, then the data extraction was a failure.
        # "f" stands for failure.
        data = ("f", results)
    else:
        # So, there are no "errors" strings, then the data extraction was successful.
        # "s" stands for success.
        data = ("s", results)

    return data


def analyze_cif(cif_path):
    """
    It extracts the data from the cif and returns it in a list. If it has no structure it records the cif number and
    returns it in a list.

    Parameters
    ----------
    data : list(str, bool)
        The first element is the path to the cif file, the second is a boolean indicating whether to clear the elements.
    clean_elem : bool, default=False
        Decide whether or not to clean up the Wyckoff site elements. Default is False.

    Returns
    -------
    list
        Depending on the case, it contains the data obtained with success or partial success or the cif number if it
        has no structure.
    """

    try:
        # General filter. If it hasn't Structure, this line won't run.
        file_struct = Structure.from_file(cif_path)
        analyzed_data = analyzer(cif_path, file_struct)

        return analyzed_data
    
    except:
        cif_num = get_cif_name(cif_path)
        
        return (cif_num, "NoStructure")