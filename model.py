class Animal:
    def __init__(self, nombre, peso, edad):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

class Hurón(Animal):
    def hacer_sonido(self):
        return "Eeek Eeek!"

class BoaConstrictor(Animal):
    def hacer_sonido(self):
        return "Tsss!"