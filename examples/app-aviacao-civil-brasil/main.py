from flask import Flask, render_template

import requests, json
import libraries.aviacao as aviacao

app = Flask(__name__) # Create Flask singleton


@app.route('/')
def display():
    return render_template('home.html')

@app.route('/aeronaves')
def getAeronaves():
    aeronaves = aviacao.getAeronaves().values()
    return render_template('aeronaves.html', aeronaves=aeronaves)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)