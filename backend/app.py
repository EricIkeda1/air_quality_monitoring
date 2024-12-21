from flask import Flask, jsonify
import random

app = Flask(__name__)

LIMITES_CRITICOS = {
    "CO2": 1000,  
    "PM2.5": 35  
}

def gerar_dados():
    return {
        "CO2": random.randint(400, 1500),
        "PM2.5": random.uniform(10, 50)
    }

@app.route('/dados', methods=['GET'])
def dados():
    dados = gerar_dados()
    return jsonify(dados)

@app.route('/alertas', methods=['GET'])
def alertas():
    dados = gerar_dados()
    alertas = {k: v for k, v in dados.items() if v > LIMITES_CRITICOS[k]}
    return jsonify(alertas)

if __name__ == '__main__':
    app.run(debug=True)
