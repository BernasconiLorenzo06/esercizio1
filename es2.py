
from flask import Flask,render_template,request
app = Flask(__name__)

import datetime

@app.route('/')
def home():
    return render_template('esercizio2.html')

@app.route('/login2', methods = ['GET'])
def login():
    peso = int(request.args.get('peso'))
    altezza = int(request.args.get('altezza')) / 100
    IMC = peso / (altezza * altezza)
    if IMC < 20:
        immagine = "static/images/mc.jpg"
        esito = "sei sottopeso"
    elif IMC > 24:
        immagine = "static/images/insalta.jpg"
        esito = "sei sovrappeso"
    else:
        immagine = "static/images/pollice.jpg"
        esito = "normopeso"


    return render_template('IMC.html',altezza = altezza,peso=peso,IMC = IMC,esito = esito,immagini=immagine)
   


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
