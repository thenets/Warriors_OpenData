import requests, json
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

@app.route('/<name>')
def doJoke(name):
    joke_json = requests.get('http://api.icndb.com/jokes/random?firstName='+str(name).title()+'&amp').text
    joke_dict = json.loads(joke_json)
    return render_template('joke.html', joke=joke_dict['value']['joke'], name=str(name).title()+' Norris')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9005)

    
    