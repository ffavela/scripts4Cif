Hola, esto es una entrada

# Cloning (you probably already did this)

cif2Csv is an utility for creating csv files from a given path where
the cif files are located.

You may clone the repository with:

git clone git@github.com:ffavela/scripts4Cif.git

If that fails just do it with HTTPS via:

git clone https://github.com/ffavela/scripts4Cif.git

# General usage

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

## About the inPath

It should only be a route for finding cif files, it can be directly a
single cif file. If you want to obtain a bunch of cif files, you can
download them from the crystallography open database:

http://www.nanocrystallography.org/

## About the fmtFile

First of all just be careful in what you put here, I'm using python's
eval. That means that whatever is placed there it will try to execute
it. The intention it to always use a simple to read file.

The format file should contain a line with comma separated commands,
these commands will normally include the "block" object. This object
is obtained from the cif file and the gemmi library. A sole block is
obtained from each cif file.

Lines starting with \# are ignored. A sample content for a fmtFile is:

block.name, block.find_pair("_journal_year")[1]

The scope of available functions, outside the gemmi library, are given
in the cLib/miscellaneous.py library.

In case an operation fails for any reason, then the corresponding
value will be 'None'. Correspondingly a message will be printed to
stderr. If the '--log' option is used then the cif paths with None
values will be logged.

Remember that it is good practive to test the fmFile with a single cif
file and not with a path that may contain tenths of thousands.

# About the outCsv

A csv (comma separated value) file, created from the cif files in the
inPath and the fmtFile. If an '-' is used then the output csv are
printed to stdout.

Look at the develop (comming soon) branch for the latest commits.
