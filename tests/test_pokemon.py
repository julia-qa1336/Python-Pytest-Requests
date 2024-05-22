import requests
import pytest

URL = ''
TOKEN = ''
HEADER1 = {'Content Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = ''

def test_pokemon():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200