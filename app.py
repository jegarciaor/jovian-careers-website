from flask import Flask

app = Flask(__name__)


@app.route('/')
def bienvenida_flask():
    return '<p> Hola mundo </p>'
