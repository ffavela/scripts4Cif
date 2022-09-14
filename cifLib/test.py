from getMultiplicity import *
from os.path import isfile


def itera(file_path: str, database_path: str):
    file = open(file_path, "r")
    text_list = file.readlines()
    new_list = []
    for e in text_list:
        string_split = e.split("/")
        cif_file: str = string_split[0] + "/" + string_split[-1].split(":")[0]
        cif_final_path = database_path + "/" + cif_file
        new_list.append(cif_final_path)
    return new_list


def get_atom_number_list(paths_list) -> list:
    atoms_number_list = []
    n = len(paths_list)
    for i in range(n):
        cif_path = paths_list[i]
        block = getBlock(cif_path)
        name = cif_path[-11:-4]
        atoms_number_list.append((name, getAtomNumber(cif_path, block)))
    return atoms_number_list


file_path = "C:/Users/PH317-52/Downloads/Telegram Desktop/sitesClean.txt"
print(isfile("C:/Users/PH317-52/Downloads/Telegram Desktop/sitesClean.txt"))
database_path = "D:/proyectos/cristales/COD_compact_database2021/cif"


una_lista = itera(file_path, database_path)
result = get_atom_number_list(una_lista)

print(result)
