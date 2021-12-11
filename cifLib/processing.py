import os

def printDeepTxt(path="./"):
    """A simple recursive function that looks for all the existing .txt
files from a given path prints the file name and it's content

    """
    os.chdir(path)

    print(os.getcwd())
    for e in os.listdir():
        if os.path.isdir(e):
            printDeepTxt(e)

        if os.path.isfile(e):
            if e.endswith(".txt"):

                print(e)
                with open(e) as f:
                    print(f.read())

    os.chdir("../")

def deepCif2Csv(path="./"):
    os.chdir(path)

    for e in os.listdir():
        if os.path.isdir(e):
            deepCif2Csv(e)

        if os.path.isfile(e):
            if e.endswith(".cif"):

                print(e)
                #Do the pymatgen stuff here (populate the csv)
                with open(e) as f:
                    print(f.read())

    os.chdir("../")
