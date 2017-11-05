from flask import Flask, render_template
import requests, json

import libraries.aviacao as aviacao

app = Flask(__name__)

# Import files from current dir
import sys, os
print 
sys.path.append(os.getcwd()+'/libraries/aviacao_brasil.py')


@app.route('/')
def display():
    return "Opendata AIG Brazil - Ocorrências Aeronáuticas na Aviação Civil Brasileira"

@app.route('/aeronaves')
def getAeronaves():
   return aviacao.get_aeronaves()

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)