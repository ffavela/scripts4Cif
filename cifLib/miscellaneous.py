"""Just a set of miscellaneous functions"""

def isFloat(myStr):
    try:
        float(myStr)
    except ValueError:
        return False
    return True

def myEval(myStr, block):
    # print("globals() are")
    # print(globals())
    try:
        return eval(myStr)
    except:
        return None

def cleanNum(numStr):
    """Removes the parenthesis, simple implementation"""
    return numStr[:numStr.find('(')]
