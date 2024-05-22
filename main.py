import requests
import pytest


URL = ''
TOKEN = ''
HEADER = {'Content Type' : 'application/json'}
HEADER1 = {'Content Type' : 'application/json', 'trainer_token' : TOKEN}

body_pok = {
    "name": "Покемон1",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

body_change = {
    "pokemon_id": "28019",
    "name": "Покемон2",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}

body_add_pokeball = {
    "pokemon_id": ""
}


response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER1, json = body_pok)
print (response_create.text) ##создание покемона


response_change = requests.put(url= f'{URL}/pokemons', headers= HEADER1,json= body_change) 
print (response_change.text) ##смена имени, картинки

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER1, json = body_add_pokeball)
print (response_add_pokeball.text) ##поймать в покебол
