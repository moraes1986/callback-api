from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Definindo um endpoint para o webhook
@app.route('/webhook', methods=['POST,GET,PUT,DELETE'])
def webhook():
    # Obtendo os dados enviados no corpo da requisição
    data = request.get_json()

    # Aqui você pode processar os dados como desejar
    print("Dados recebidos no webhook:", data)

    # Respondendo com status 200 e um JSON de confirmação
    return jsonify({"message": "Webhook recebido com sucesso!"}), 200

if __name__ == '__main__':
    # Rodando o servidor na porta 5000
    app.run(debug=True, port=5000)