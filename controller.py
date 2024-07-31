from flask import jsonify
from model import Perro, Gato, Huron, Boa

animales = [
    Perro("Maxi", 10, 5),
    Gato("Nala", 4, 3),
    Huron("Tito", 2, 2),
    Boa("Boo", 15, 8)
]

def obtener_sonido_animal(nombre):
    for animal in animales:
        if animal.tipo().lower() == nombre.lower():
            return jsonify({"nombre":animal._nombre,"tipo": animal.tipo(), "sonido": animal.hacer_sonido()}), 200
    return jsonify({"error": "Animal no encontrado"}), 404

def obtener_animales():
    return animales