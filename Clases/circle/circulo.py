import math

"""Clase para manejar una excepcion. Si el usuario ingresa el 0 o un numero negativo lanzamos 
de forma intencional una excepcion, donde manejamos este error.
"""
class ZeroOrNegativeError(Exception):
    pass

class Circulo:
    """ Se crea una clase circulo que recibe un radio, contiene un metodo que devuelve el area y otro metodo que devuelve el perimetro.
    """
    
    # Constructor
    def __init__(self, radio):
        self.__setRadio(radio)
    
    """Setter"""
    def __setRadio(self, p_radio):
        self.radio = p_radio
        
    """Getters"""
    def getRadio(self):
        return self.radio
    
    def getArea(self):
        return round(math.pi * (self.getRadio() ** 2), 2)
    
    def getPerimeter(self):
        return round(2 * (math.pi * self.getRadio()), 2)
    
    """Metodo para modificar el radio, recibe un radio y setea el atributo."""
    def modifyRadius(self, p_radio):
        self.__setRadio(p_radio)
        
    """Metodo para imprimir las caracteristicas del circulo."""
    def __str__(self):
        return f"Caracteristicas del circulo:\nRadio: {self.getRadio()}  Area: {self.getArea()}  Perimetro: {self.getPerimeter()}"
    
    """Metodo para multiplicar el radio de 2 objetos.
    Retorna un nuevo objeto con el producto del radio de los 2 objetos pasados por parametro.
    """
    def __mul__(self, obj):
        newObj = self.getRadio() * obj.getRadio()
        return Circulo(newObj)