import requests, json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

@app.route('/<id>')
def getPk(id):
    with requests.Session() as session:
        print('loading:', id)
        r = session.get('http://pokeapi.co/api/v2/pokemon/' + id)
        pokemon = r.json()
        return 'Pokemon name: ' +  str(pokemon['name'])

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
