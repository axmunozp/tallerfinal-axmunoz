from flask import jsonify
from model import Perro, Gato, Hurón, BoaConstrictor

animales = [
    Perro("Maxi", 10, 5),
    Gato("Nala", 4, 3),
    Hurón("Tito", 2, 2),
    BoaConstrictor("Boo", 15, 8)
]

def obtener_sonido_animal(nombre):
    for animal in animales:
        if animal._nombre.lower() == nombre.lower():
            return jsonify({"nombre": animal._nombre, "sonido": animal.hacer_sonido()}), 200
    return jsonify({"error": "Animal no encontrado"}), 404

def obtener_animales():
    return animales