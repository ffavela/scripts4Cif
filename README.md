NOTE THAT THIS CODE DOES NOT YET HAVE BASIC FUNCTIONALITY. JUST WAIT
FOR A FEW MORE COMMITS!!!

From here on I'm going to assume that you have the program installed,
please check the INSTALL file for installation instructions.

Utilities for creating csv files from a given path where the cif files
are located. The general synopsis of cif2Csv is:

cif2Csv inPath fmtFile outFile [options]

Where the "inPath" is the path where the cif files are located, the
program will descend recursively finding the cif files for
processing. The "fmtFile" is a format file for placing the various
values of the cif files. The "outCsv" is the resulting csv
file. Options will be implemented and they are (suprise) optional.