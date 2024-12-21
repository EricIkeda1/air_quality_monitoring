import os
from flask import Flask, render_template, jsonify, request

# Caminho absoluto para as pastas templates e static, considerando que estão na raiz do projeto
app = Flask(__name__,
            template_folder=os.path.join(os.getcwd(), 'templates'),  # Caminho correto para 'templates' na raiz
            static_folder=os.path.join(os.getcwd(), 'static'))  # Caminho correto para 'static' na raiz

# Dados simulados
dados_sensores = []

@app.route('/')
def dashboard():
    return render_template('dashboard.html')  # Carrega o frontend

@app.route('/dados', methods=['GET'])
def obter_dados():
    return jsonify(dados_sensores)

@app.route('/enviar_dados', methods=['POST'])
def enviar_dados():
    global dados_sensores
    dados = request.json
    dados_sensores.append(dados)
    if len(dados_sensores) > 20:  # Limita histórico a 20 entradas
        dados_sensores.pop(0)
    return jsonify({"mensagem": "Dados recebidos com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
