import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'a989ca876fe29f1c5981c0d6dce92d3a'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1952})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1952})
    assert response.json()['trainer_name'] =='Meow'