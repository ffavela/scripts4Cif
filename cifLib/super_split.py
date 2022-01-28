"""
Fermin Martinez

Esta paquetería contiene la función `super_split(string)`.

Función que separa una palabra por comas.
Si hay palabras con paréntesis y dentro de estos hay comas, la función
las ignora, y no las separa.

Ejemplo:
[In] : super_split('block.name, f(a,b,c), g(x,y,d), h(a), (a,b)')
[Out] : ['block.name', 'f(a,b,c)', 'g(x,y,d)', 'h(a)', '(a,b)']
"""

def search_comas(string):
    """
    Obtiene las comas dentro de una oracion y regresa las posiciones de estos en una
    lista.
    """
    lst = []
    for pos, char in enumerate(string):
        if(char == ','):
            lst.append(pos)
    return lst

def search_parentesis(string):
    """
    Obtiene los parentesis dentro de una oracion y regresa las posiciones de estos en una
    lista.
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
    Regresa la posicion de las comas que no esten dentro de un paréntesis de un string ingresado.
    """
    comas_position = search_comas(string)
    parentesis_position = search_parentesis(string)

    n = len(parentesis_position)
    k = 0
    comas_seleccionadas = [e for e in comas_position]

    while k <= n-2:
        # Selecciona los paréntesis.
        par1 = parentesis_position[k]
        par2 = parentesis_position[k+1]
        for j in range(len(comas_position)):
            coma = comas_position[j]
            if coma >= par1 and coma <= par2:
                comas_seleccionadas.remove(coma) # Elimina la coma de la lista de las comas
        k += 2

    return comas_seleccionadas

def super_split(string):
    """
    Función que separa una palabra por comas.
    Si hay palabras con paréntesis y dentro de estos hay comas, la función
    las ignora, y no las separa.

    Ejemplo:
    [In] : super_split('block.name, f(a,b,c), g(x,y,d), h(a), (a,b)')
    [Out] : ['block.name', 'f(a,b,c)', 'g(x,y,d)', 'h(a)', '(a,b)']

    Parameters
    ----------
    `string` : `str`
        Palabra ingresada para analizar.

    Returns
    -------
    list
        Regresa una lista que contiene strings.
    """
    # Obtiene la posicion especifica de las comas que separan solo funciones
    posicion_comas = comas_para_separar(string)

    # Aqui se guardan las funciones encontradas
    set_splits = []

    # Cantidad de comas en la palabra
    n = len(posicion_comas)
    # Conteo para analisis de split en cero.
    k = 0

    while k <= n and n > 0:
        if k == 0:
            # Inicio del string
            coma = posicion_comas[k]
            word = string[:coma].strip()
        elif k>0 and k<n:
            # Partes intermedias del string
            coma_ant = posicion_comas[k-1]
            coma_post = posicion_comas[k]
            word = string[coma_ant+1:coma_post].strip()
        elif k==n and n>0:
            # Parte final del string
            coma = posicion_comas[k-1]
            word = string[coma+1:].strip()

        # Se guarda la variable.
        if word != '':
            # No queremos guardar espacios vacios si hay comas juntas en el string como: "a,,,"
            set_splits.append(word)

        k += 1

    if n==0:
        # Es decir, no hay comas, entonces, solo devuelve la palabra.
        set_splits.append(string)

    return set_splits
