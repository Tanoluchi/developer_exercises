import random
"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

def create_array():
    """ Se genera una matriz 5x5 con numeros enteros entre 0 y 1 para poder encontrar mas facilmente
    una secuencia de numeros consecutivos."""
    array = [[random.randint(0, 1) for i in range(0, 5)] for j in range(0, 5)]
    return array

def consecutive_numbers(array):
    """ Se busca secuencias de 4 numeros consecutivos de manera horizontal y vertical,
    si se encuentra mostramos por pantalla la posición inicial y final de esta secuencia.
    
    >>> array = [[0, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0],]
    >>> consecutive_numbers(array)
    Buscando de manera vertical
    Se encontro una sucuencia, empieza en el indice [1, 0] y termina en el [4, 0]
    Se encontro una sucuencia, empieza en el indice [0, 1] y termina en el [3, 1]
    Se encontro una sucuencia, empieza en el indice [0, 4] y termina en el [3, 4]
    Buscando de manera horizontal
    Se encontro una secuencia, empieza en el indice [0, 0] y termina en el [0, 3]
    Se encontro una secuencia, empieza en el indice [4, 1] y termina en el [4, 4]
    """
    #Columna x Filas
    is_vertical_sequence = False
    print("Buscando de manera vertical")
    for column in range(len(array)):
        for row in range(len(array[column])):
            count = 0
            pi = []
            pf = []
            n = array[row][column]
            for i in range(len(array[column])):
                # Se verifica si es igual al valor en n y si el contador es 0, sumamos 1 y asignamos la posicion inicial
                if array[i][column] == n and count == 0:
                    count += 1
                    pi = [i, column]
                # Se verifica si es igual al valor en n y si el contador es 3, sumamos 1 y asignamos la posicion final. Se encontro una secuencia de 4 numeros consecutivos.
                elif array[i][column] == n and count == 3:
                    count += 1
                    pf = [i, column]
                    break
                # Se verifica si es igual valor en n y si mientras el contador es distinto a 4, sumamos 1 y continuamos.
                elif array[i][column] == n and count != 4:
                    count += 1
                # Si no se ha encontrado ninguna coincidencia entonces el contador se reinicia a 0.
                else:
                    count = 0
            if count == 4:
                print(f"Se encontro una sucuencia, empieza en el indice {pi} y termina en el {pf}")
                is_vertical_sequence = True
                break
    #Filas x Columna
    print("Buscando de manera horizontal")
    is_horizontal_sequence = False
    for row in range(len(array)):
        for column in range(len(array[row])):
            count = 0
            pi = []
            pf = []
            n = array[row][column]
            for i in range(len(array[row])):
                if array[row][i] == n and count == 0:
                    count += 1
                    if count == 1:
                        pi = [row, i]
                elif array[row][i] == n and count == 3:
                    count += 1
                    pf = [row, i]
                    break
                elif array[row][i] == n and count != 4:
                    count += 1
                else:
                    count = 0
            if count == 4:
                print(f"Se encontro una secuencia, empieza en el indice {pi} y termina en el {pf}")
                is_horizontal_sequence = True
                break
            
    if is_vertical_sequence == False:
        print("\nNo se ha encontrado una secuencia de manera vertical.")
    if is_horizontal_sequence == False:
        print("\nNo se ha encontrado una secuencia de manera horizontal")

#print(consecutive_numbers(create_array()))
consecutive_numbers(create_array())

"""
Ejecuta doctest automaticamente.
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()