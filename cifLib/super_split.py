"""
Fermin Martinez
This package contains the `super_split(string)` function.
Function that separates a word by commas.

If there are words with parentheses and inside these there are commas,
the function ignores them, and does not separate them.

Example:
[In] : super_split('block.name, f(a,b,c), g(x,y,d), h(a), (a,b)')
[Out] : ['block.name', 'f(a,b,c)', 'g(x,y,d)', 'h(a)', '(a,b)']
"""


def search_comas(string):
    """
    Gets the commas within a sentence and returns their positions in a list.
    """
    lst = []
    for pos, char in enumerate(string):
        if(char == ','):
            lst.append(pos)
    return lst

def search_parentesis(string):
    """
    Gets the parentheses within a sentence and returns their positions in a list.
    """
    lst = []
    for pos, char in enumerate(string):
        if(char == '('):
            lst.append(pos)
        elif(char == ')'):
            lst.append(pos)
    return lst

def comas_para_separar(string):
    """
    Returns the position of commas that are not inside a parenthesis of an input string.
    """
    comas_position = search_comas(string)
    parentesis_position = search_parentesis(string)

    n = len(parentesis_position)
    k = 0
    comas_seleccionadas = [e for e in comas_position]

    while k <= n-2:
        # Selects parenthesis.
        par1 = parentesis_position[k]
        par2 = parentesis_position[k+1]
        for j in range(len(comas_position)):
            coma = comas_position[j]
            if coma >= par1 and coma <= par2:
                comas_seleccionadas.remove(coma)  # Removes the comma from the comma list.
        k += 2

    return comas_seleccionadas

def super_split(string):
    """
    Function that separates a word by commas.
    If there are words with parentheses and inside them there are commas, the
    function ignores them, and does not separate them.

    Example:
    [In] : super_split('block.name, f(a,b,c), g(x,y,d), h(a), (a,b)')
    [Out] : ['block.name', 'f(a,b,c)', 'g(x,y,d)', 'h(a)', '(a,b)']

    Parameters
    ----------
    `string` : `str`
        Input word for the analysis.

    Returns
    -------
    list
        Returns a list containing strings.
    """
    # Gets the specific position of commas separating only functions.
    posicion_comas = comas_para_separar(string)

    # Here the found functions are stored
    set_splits = []

    # Number of commas in the word
    n = len(posicion_comas)
    # Counting for split analysis at zero.
    k = 0

    while k <= n and n > 0:
        if k == 0:
            # String start
            coma = posicion_comas[k]
            word = string[:coma].strip()
        elif k > 0 and k < n:
            # Intermediate parts of the string
            coma_ant = posicion_comas[k-1]
            coma_post = posicion_comas[k]
            word = string[coma_ant+1:coma_post].strip()
        elif k == n and n > 0:
            # Final part of the string
            coma = posicion_comas[k-1]
            word = string[coma+1:].strip()

        # The variable is saved.
        if word != '':
            # We do not want to keep empty spaces if there are commas together in the string as: "a,,,"
            set_splits.append(word)

        k += 1

    if n == 0:
        # That is, there are no commas, so it just returns the word.
        set_splits.append(string)

    return set_splits
