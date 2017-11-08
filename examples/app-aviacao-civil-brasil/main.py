from flask import Flask, render_template

import requests, json
import libraries.aviacao as aviacao

app = Flask(__name__) # Create Flask singleton

@app.route('/')
def Ocorrencias():
    return render_template('home.html', getOcorrencias=aviacao.getOcorrencias)

@app.route('/aeronaves')
def Aeronaves():
    aeronaves = aviacao.getAeronaves().values()
    return render_template('aeronaves.html', aeronaves=aeronaves)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)