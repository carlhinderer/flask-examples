import os
import requests


BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')


def test_hello_route():
    url = f'{BASE_URL}/hobbies'
    r = requests.get(url)
    
    assert r.status_code == 200

    json = r.json()
    assert 'swimming' in json
    assert 'diving' in json
    assert 'jogging' in json
    assert 'dancing' in json
    assert 'cooking' in json
