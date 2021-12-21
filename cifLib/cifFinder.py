import os

def yieldCifRoute(path="./"):
    """Given a path it will yield all the files that end with .cif"""
    if os.path.isfile(path) and path.endswith(".cif"):
        yield path
        return

    for e in os.listdir(path):
        yield from yieldCifRoute(path+'/'+e)
