import random
from operator import itemgetter
"""
Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.
Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
"""

def list_dictionary():
    """ Retorna una lista de diccionarios de 10 elementos con id y edad aleatoria entre 1 y 100. """
    list = [{'id': id, 'age': random.randint(1, 100)} for id in range(0, 10)]
    
    return list

#print(list_dictionary())

def ordered_list(list):
    """Retorna la lista de diccionarios recibida como parametro y ordena la edad de menor a mayor.

    >>> ordered_list([{'id': 0, 'age': 80}, {'id': 1, 'age': 6}, {'id': 2, 'age': 99}, {'id': 3, 'age': 60}])
    El id de la persona más vieja es 2 y su edad es 99
    El id de la persona más joven es 1 y su edad es 6
    [{'id': 2, 'age': 99}, {'id': 0, 'age': 80}, {'id': 3, 'age': 60}, {'id': 1, 'age': 6}]
    """
    sorted_list = sorted(list, key=itemgetter('age'), reverse=True)
    
    print(f"El id de la persona más vieja es {sorted_list[0]['id']} y su edad es {sorted_list[0]['age']}\nEl id de la persona más joven es {sorted_list[-1]['id']} y su edad es {sorted_list[-1]['age']}")
    
    return sorted_list

ordered_list(list_dictionary())
#print(ordered_list(list_dictionary()))
"""
Ejecuta doctest automaticamente.
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()