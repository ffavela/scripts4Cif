import os

def yieldCifRoute(path="./"):
    """Given a path it will yield all the files that end with .cif"""
    if os.path.isfile(path) and path.endswith(".cif"):
        yield path
        return

    if os.path.isdir(path):
        for e in os.listdir(path):
            yield from yieldCifRoute(path+'/'+e)

def getCifCount(path="./", total=0):
    """Given a path it will count all the files that end with .cif"""
    if os.path.isfile(path) and path.endswith(".cif"):
        return 1

    if os.path.isdir(path):
        for e in os.listdir(path):
            total += getCifCount(path+'/'+e)

    return total
