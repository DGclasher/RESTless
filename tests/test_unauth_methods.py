import random
import requests

ENDPOINT = "http://127.0.0.1:8000/api"

def test_can_fetch_quote():
    response = requests.get(ENDPOINT + "/fetch/quote/")
    assert response.status_code == 200

def test_can_fetch_author_by_id():
    methods = {"id": 3, "name": "unknown"}
    key, val = random.choice(list(methods.items()))
    response = requests.get(ENDPOINT + "/fetch/author/", params={key: val})
    assert response.status_code == 200

def test_can_fetch_all_authors():
    response = requests.get(ENDPOINT + "/fetch/author/all/")
    assert response.status_code == 200

