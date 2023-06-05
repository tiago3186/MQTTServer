from flask import Flask, request
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'localhost'  # Endereço do servidor MQTT
app.config['MQTT_BROKER_PORT'] = 1883  # Porta do servidor MQTT
app.config['MQTT_KEEPALIVE'] = 5  # Intervalo de tempo em segundos para manter a conexão MQTT
mqtt = Mqtt(app)

# Rota para receber mensagens MQTT
@app.route('/mqtt', methods=['POST'])
def receive_mqtt_message():
    topic = request.form.get('topic')
    message = request.form.get('message')
    print(f'Recebido - Tópico: {topic}, Mensagem: {message}')
    # Faça o processamento desejado com a mensagem recebida, como salvar no banco de dados

    return 'OK'

if __name__ == '__main__':
    app.run()
