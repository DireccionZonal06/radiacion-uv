from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['*'])

@app.route('/')
def saludo():
    return '<p><b>Bienvenido</b></p>'

if __name__=='__main__':
    app.run()