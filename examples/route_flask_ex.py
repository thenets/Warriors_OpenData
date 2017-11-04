import requests, json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

@app.route('/<id>')
def getPk(id):
    r = requests.get('http://pokeapi.co/api/v2/pokemon/' + str(id))
    pokemon = r.json()
    return 'Pokemon name: ' +  pokemon['name']

if __name__=='__main__':
    app.run(debug=True, port=3134)
