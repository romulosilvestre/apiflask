#importando o framework Flask
from flask import Flask
#importando o framework SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


#definindo a aplicação
app = Flask(__name__)
app.config.from_object('config')
#definindo um banco de dados
db = SQLAlchemy(app)


#adicionando o arquivo config.py
#app.config.from_object('config')

#definindo a rota com uma função def
@app.route("/")
def index():
    return "Olá Mundo!"

#executando a aplicação
if __name__ == "__main__":
    app.run()

