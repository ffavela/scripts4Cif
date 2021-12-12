"""Just a set of miscellaneous functions"""

def isFloat(myStr):
    try:
        float(myStr)
    except ValueError:
        return False
    return True
