"""cif seeker

This script allows the user to get each CIF file (.cif) path from the database
into a list. With the help of the list information is searched within each file.
Subsequently the search results are stored within csv files.

The structure of the directories and subdirectories of the database must be previously
ordered with the help of an auxiliary program external to this script.

This structure consists of a directory with 9 subdirectories. Each subdirectory
contains CIF files that start with the number of each subdirectory they belong to.

This script requires that 'pandas', 'pymatgen', 'tqdm' and 'PyCifRW' be
installed within the Python environment that is running this script in.

"""

import os
import time


# from tqdm import tqdm # Module to show progress bar.

# from CifFile import ReadCif # Library for reading cif files.
# import pymatgen as pmg #Python library for material analysis.

# import pandas as pd # Library to manage database.

class Directions:
    """
    A class used to create the path list of each file in the database location.
    It could be the whole database or just one of the main folders.

    ...

    Attributes
    ----------
    path : str
        A string that contains the database (or one of the main folders) location path.
        It can be the whole database path or just one of the 9 principal files path.

    Methods
    -------
    get_directions(combine = False, print_info = True)
        Get a list with directions of each file in the database input path.

    """

    def __init__(self, path):
        """
        Parameters
        ----------
        path : str
            The path of where database is located. It can be the whole database
            or just one of the 9 main folders.

        """
        self.path = path
        self.__database_path()  # Checks if path exists.

    def get_directions(self, combine=False, print_info=True):
        """
        Gets a list of directions of the input path where database is located.

        * If the path is for the whole database, by default, it will return a list
        of 9 lists, each of one containing the path for their respective CIF files.
        It can be merged in one list using 'combine' parameter.

        * If its one of the 9 files, it will return one list containing the CIF file
        paths.

        Parameters
        ----------
        combine : bool
            Joins elements of multiple list inside only one list. Multiple list
            occurs if the database path is the general directory (default is False).
        print_info : bool
            Whether to print output list information (default is True).

        Returns
        -------
        list
            A list of the directions to the database files.

        """
        ti = time.time()  # start

        # Get the directions
        list_paths = self.__gen_path_list()

        # Combine parameter
        final_list = list()
        if combine:
            # Check if the first element is a list or not.
            if type(list_paths[0]) == list:
                for path_list in list_paths:
                    final_list += path_list
            else:
                final_list = list_paths

        elif not combine:
            final_list = list_paths

        tf = time.time()  # stop
        dt = tf - ti
        print("Run time:", dt, "s")

        # Print info parameter
        if print_info:
            self.__get_info(final_list)

        return final_list

    def __database_path(self):
        """
        Check if the database path is valid to register. If the algorithm can
        detect the error it will correct it with __correct_path() function and
        try it again.

        Raises
        ------
        NotImplementedError
            If the path does not exists or is not a valid folder.

        """
        path_found = os.path.isdir(self.path)

        if path_found:
            os.chdir(self.path)
            print("Successful. Path [", self.path, "] registered.")
        elif not path_found:
            new_path = self.__correct_path()
            new_path_found = os.path.isdir(new_path)

            if new_path_found:
                os.chdir(new_path)
                print("Successful. Path [", new_path, "] registered.")
            elif not new_path_found:
                raise NotImplementedError("Verify that the input path exists or it's a valid folder")

    def __gen_path_list(self):
        """
        Gets the list of files inside a specific path.

        This function is optimized to run in a COD database specific construction.
        This database construction ensures that every file is a "CIF file".

        There are two available options. A path containing a directory containing
        subdirectories, or a path that is a sub directory.

        Raises
        ------
        NotImplementedError
            If path that is not a subfolder is inside the database structure.
            It occurs when the database is not well structured.

        Returns
        -------
        list
            A list containing all the directions of the input path.

        """
        is_directory = os.path.isdir(self.path)
        list_p = list()

        # Tries if the path is correct.
        if is_directory:
            list_p = os.listdir(self.path)
        elif not is_directory:
            # Tries to fix it.
            self.path = self.__correct_path()
            list_p = os.listdir(self.path)

        # Gets first element in list_p to check if it has subdirectories.
        first_element_list_p = os.path.join(self.path, list_p[0])

        # If it has subdirectories.
        if os.path.isdir(first_element_list_p):
            # so the other elements must be a directory.
            list_paths = []

            for sub_directory in list_p:
                sub_directory_path = os.path.join(self.path, sub_directory)

                # Check if sub_directory_path is a directory to prevent errors.
                if os.path.isdir(sub_directory_path):
                    list_paths.append(os.listdir(sub_directory_path))
                else:
                    raise NotImplementedError("A path was found that is not a subfolder within the database folder.")
        else:
            # If list_p has no subdirectories.
            list_paths = list_p

        return list_paths

    def __correct_path(self):
        """
        Attempts to fix a path with incorrect end syntax.

        Example: cif\3 (is bad)
                 cif\\3 (is good)

                 If it ends with 8 or 9 is good both ways.

        Returns
        -------
        string
            New path if it can be fixed or the same path if it cannot correct it.

        """
        correction = str
        error = self.path[-1]
        error_ = error.split()
        flag = 0
        for i in range(1, 10):
            char = chr(i)
            if error_ == [char]:
                correction = f"\\{i}"
                flag = 1  # Successful error found.
                break

        if flag == 1:
            upper_folder = self.path.split(error)[0]
            new_path = upper_folder + correction
            return new_path
        else:
            return self.path

    @staticmethod
    def __get_info(data):
        """
        Prints length and structure of the elements inside the list
        generated by get_directions.

        """
        pl = data
        print("\n- - - List info - - -")
        print("List length:", len(pl))

        if type(pl[0]) == list:
            print("General format for elements in list: ", pl[0][0])
            count = 0
            for i in range(0, len(pl)):
                print(f"Sub list {i + 1} length:", len(pl[i]))
                count += len(pl[i])

            print("Total:", count, "files.")

        else:
            print("General format for elements in list: ", pl[0])
