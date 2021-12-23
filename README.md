cif2Csv is an utility for creating csv files from a given path where
the cif files are located.

You may clone the repository with:

git clone git@github.com:ffavela/scripts4Cif.git

From here on I'm going to assume that you have the program installed,
please check the INSTALL file for installation instructions.

A simple help is shown by running:

cif2Csv

An extended version can be seen with:

cif2Csv -h

The general synopsis of cif2Csv is:

cif2Csv inPath fmtFile outFile [options]

Where the "inPath" is the path where the cif files are located, the
program will descend recursively finding the cif files for
processing. The "fmtFile" is a format file for placing the various
values of the cif files. The "outCsv" is the resulting csv file if a
'-' is used then the table is displayed to stdout.

Options will be implemented and they are (suprise) optional.

Look at the develop (comming soon) branch for the latest commits.