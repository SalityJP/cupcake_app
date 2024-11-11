from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data/cupcakes.json'

# Função para carregar os cupcakes do arquivo JSON
def load_cupcakes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Função para salvar os cupcakes no arquivo JSON
def save_cupcakes(cupcakes):
    with open(DATA_FILE, 'w') as file:
        json.dump(cupcakes, file)

@app.route('/')
def index():
    cupcakes = load_cupcakes()
    return render_template('index.html', cupcakes=cupcakes)

@app.route('/add_cupcake', methods=['POST'])
def add_cupcake():
    name = request.form['name']
    ingredients = request.form['ingredients']
    price = request.form['price']
    
    cupcakes = load_cupcakes()
    cupcakes.append({"name": name, "ingredients": ingredients, "price": price})
    save_cupcakes(cupcakes)
    
    return jsonify({"message": "Cupcake adicionado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
