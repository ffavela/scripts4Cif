"""Just a set of miscellaneous functions"""
import cifLib.lattice_volume as latt
from cifLib.get_bravais_lattice_type import *

def isFloat(myStr):
    try:
        float(myStr)
    except ValueError:
        return False
    return True

def myEval(myStr, block):
    try:
        return eval(myStr)
    except:
        return None

def cleanNum(numStr):
    """Removes the parenthesis, simple implementation"""
    return numStr[:numStr.find('(')]

def rmTrailSlash(strPath):
    if strPath[-1] == '/':
        strPath = strPath[:-1]#removing trailing '/'
    return strPath

def rmSN(strVal):
    """Removes the semicolons on a string & \n"""
    return strVal.replace(';', '').replace('\n', '')
    
def simpleOperation(intVal):
    return intVal + 1000
