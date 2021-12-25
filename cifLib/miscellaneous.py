"""Just a set of miscellaneous functions"""

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
        inPath = strPath[:-1]#removing trailing '/'
    return strPath
