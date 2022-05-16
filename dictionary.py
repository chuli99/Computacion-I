# AGREGAR UNA LISTA COMO VALUE DE UNA KEY EN UN DICCIONARIO

# list of values = clave

def dict1(dict, key, list_of_values):
    # si la clave no esta en el dicc, convierte su valor en lista
    if key not in dict:
        dict[key] = list()
    # agrego una lista como valor con la funcion 'extend()'
    dict[key].extend(list_of_values)
    return dict

word_freq = {'example': [1, 3, 4, 8, 10],
             'for': [3, 10, 15, 7, 9],
             'this': [5, 3, 7, 8, 1],
             'tutorial': [2, 3, 5, 6, 11],
             'python': [10, 3, 9, 8, 12]}

# igualo al diccionario a la llamada de la funcion 'dict1'
word_freq = dict1(word_freq, 'tutorial', [20, 21, 22])
print(word_freq)