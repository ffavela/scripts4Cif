import os

def yieldCifRoute(path="./"):
    """Given a path it will yield all the files that end with .cif"""
    if os.path.isfile(path) and path.endswith(".cif"):
        yield os.getcwd()+path#should try to build a string instead
        return

    os.chdir(path)
    for e in os.listdir():
        yield from yieldCifRoute(e)

    os.chdir("../")
