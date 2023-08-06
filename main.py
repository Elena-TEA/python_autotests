import requests

token = 'a989ca876fe29f1c5981c0d6dce92d3a'

'''response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "TTT",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response.text)
'''




'''response_changename = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "5946",
    "name": "NewTTT",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_changename.text)
'''



response_inpokebol = requests.post('https://api.pokemonbattle.me:9104//trainers/add_pokeball', json = {
    "pokemon_id": "5946"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_inpokebol.text)