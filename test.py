import requests, json
r = requests.get('http://pokeapi.co/api/v2/pokemon/1')
pokemon = r.json()
print(pokemon['name'])