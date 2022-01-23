from circle.circulo import Circulo, ZeroOrNegativeError

def radius():
    """Pedimos al usuario que ingrese un radio para crear un circulo, verificamos
    si el radio no es 0 o un numero negativo.
    """
    while True:
        try:
            radio = int(input("Ingrese un radio para calcular el area y perimetro de un circulo: "))
            if radio > 0:
                break
            else:
                raise ZeroOrNegativeError("Por favor ingresa un número mayor a 0")
        except ZeroOrNegativeError as e:
            print(e)
        except ValueError:
            print("No se aceptan cadenas de texto!. Por favor ingresa un numero entero")
            
    return radio

def create_circle():
    """ Creamos una instancia de la clase Circulo, con el radio ingresado por el usuario.
    Multiplicamos el radio de los 2 circulos y obtenemos un nuevo objeto, y imprimimos por pantalla sus caracteristicas.
    También preguntamos si el usuario desea modificar el radio del circulo, si lo desea verificamos el radio que no sea 0 o un numero negativo.
    
    >>> x = Circulo(2)
    >>> y = Circulo(3)
    >>> z = x * y
    >>> print(z)
    Caracteristicas del circulo:
    Radio: 6  Area: 113.1  Perimetro: 37.7
    """
    x = Circulo(radius())
    y = Circulo(radius())
    
    print("\nSe ha creado un nuevo circulo entre la multiplicación de las 2 anteriores.\n")
    z = x * y
    print(z)
    while True:
        a = str.lower(input("¿Desea modificar el radio del circulo? (S/N): "))
        if a ==  "s":
            try:
                radio = int(input("Ingresa el nuevo radio: "))
                if radio > 0:
                    z.modifyRadius(radio)
                    print(f"\nSe ha modificado correctamente el radio.\n\n{z}")
                    break
                else:
                    raise ZeroOrNegativeError("Por favor ingresa un número mayor a 0")
            except ZeroOrNegativeError as e:
                print(e)
            except ValueError:
                print("No se aceptan cadenas de texto!. Por favor ingresa un numero entero")
        elif a == "n":
            exit()
        else:
            print("Por favor ingresa 'S' para si y 'N' para no. No se aceptan numeros!")
    
create_circle()

if __name__ == "__main__":
    import doctest
    doctest.testmod()