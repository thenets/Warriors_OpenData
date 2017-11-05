from flask import Flask, render_template

import requests, json

app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

@app.route('/<id>')
def getPk(id):
    with requests.Session() as session:
        tries=0
        while (tries < 5):
            try:
                r = session.get('https://apps.thenets.org/pokemon_api/?id=' + id)
                pokemon = r.json()
                return render_template('home.html', pokemon=pokemon)
            except:
                tries+=1

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
