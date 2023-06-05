## MQTTServer

Este é um projeto Flask que demonstra a integração do Flask com MQTT para receber mensagens MQTT e processá-las. Você pode por exemplo instalar o aplicativo MQTT Bash no seu celular e enviar mensagens para o servidor.

### Configuração
Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Flask
- Flask-MQTT
- Cliente MQTT (opcional, se você deseja publicar mensagens para o servidor MQTT)  

### Executando o Projeto
Para executar o projeto, siga estas etapas:  

-  Inicie o servidor Mosquitto
- Certifique-se de que o arquivo mqtt.conf esteja configurado corretamente com as opções desejadas.
- Em outro terminal, execute o seguinte comando para iniciar o servidor Flask:

> python app.py

O servidor Flask será iniciado e estará ouvindo em http://127.0.0.1:5000/. Certifique-se de que o servidor esteja em execução antes de prosseguir.  

Agora você pode enviar mensagens MQTT para o servidor Flask. Você pode usar um cliente MQTT como o MQTT.fx ou até mesmo outro código Python para publicar mensagens no tópico desejado. Certifique-se de configurar o endereço do servidor MQTT no arquivo app.py de acordo com sua configuração.  

O servidor Flask receberá as mensagens MQTT e as processará de acordo. Você pode personalizar o código em app.py para realizar as ações desejadas com as mensagens recebidas.  

### Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Você pode abrir um problema para relatar bugs ou sugerir novos recursos. Além disso, pull requests são bem-vindos!

### Licença
Este projeto está licenciado sob a MIT License.
