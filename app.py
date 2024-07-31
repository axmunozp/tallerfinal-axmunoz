from flask import Flask, render_template
from controller import obtener_sonido_animal, obtener_animales

app = Flask(__name__)

@app.route('/animal/<string:nombre>/sonido', methods=['GET'])
def sonido_animal(nombre):
    return obtener_sonido_animal(nombre)

@app.route('/')
def index():
    return render_template('index.html', animales=obtener_animales())

if __name__ == '__main__':
    app.run(debug=True)