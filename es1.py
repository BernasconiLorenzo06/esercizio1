
from flask import Flask,render_template,request
app = Flask(__name__)

import datetime

@app.route('/')
def home():
    return render_template('esercizio1.html')

@app.route('/login2', methods = ['GET'])
def login():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    sesso = request.args.get('sesso')
    if sesso == "uomo" :
        saluto = "benvenuto"
    else:
        saluto = "benvenuta"
    return render_template('saluto.html',saluto = saluto,nome=nome)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)