import os
import requests


BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')


def test_hello_route():
    url = f'{BASE_URL}/'
    r = requests.get(url)
    
    assert r.status_code == 200
    assert r.text == 'Hello World!'
