class Animal:
    def __init__(self, nombre, peso, edad):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    def hacer_sonido(self):
        pass

    def tipo(self):
        return self.__class__.__name__

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

class Huron(Animal):
    def hacer_sonido(self):
        return "Eeek Eeek!"

class Boa(Animal):
    def hacer_sonido(self):
        return "Tsss!"