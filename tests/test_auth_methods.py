import json
import random
import requests
from decouple import config


ENDPOINT = "http://127.0.0.1:8000/api"


def initialize():
    username = config("TEST_USER")
    password = config("TEST_PASS")

    response = requests.post(
        ENDPOINT + "/auth/", json={"username": username, "password": password})
    response = json.loads(response.text)
    token = response["token"]
    header = {"Authorization": f"Token {token}",
              "Content-Type": "application/json"}
    return header


def get_random_quote_for_testing():
    response = requests.get("https://quote-garden.onrender.com/api/v3/quotes")
    response = json.loads(response.text)
    data = response["data"]
    quote = random.choice(data)
    author = quote["quoteAuthor"]
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": author})
    if "Author doesn't exist" in response.text:
        return 14, "unknown", quote["quoteText"]
    response = json.loads(response.text)
    id = response["id"]
    return id, author, quote["quoteText"]


def create_test_quote(quote, author_name, id, header):
    payload = {
        "quote": quote,
        "author_id": id,
        "author": {
            "id": id,
            "name": author_name
        }
    }
    response = requests.post(ENDPOINT + "/create/quote/",
                             json=payload, headers=header)


def test_can_create_quote():
    header = initialize()
    id, author_name, quote = get_random_quote_for_testing()
    payload = {
        "quote": quote,
        "author_id": id,
        "author": {
            "id": id,
            "name": author_name
        }
    }
    response = requests.post(ENDPOINT + "/create/quote/",
                             json=payload, headers=header)
    assert response.status_code == 201


def test_can_create_author():
    header = initialize()
    name = "test author"
    response = requests.post(ENDPOINT + "/create/author/",
                             json={"name": name}, headers=header)
    assert response.status_code == 201


def test_can_update_author():
    header = initialize()
    new_name = "test author"
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": new_name})
    response = json.loads(response.text)
    author_id = response["id"]
    response = requests.put(
        ENDPOINT + f"/update/author/{author_id}", json={"name": new_name}, headers=header)
    assert response.status_code == 200


def test_can_delete_quote():
    header = initialize()
    quote = "this is a test quote"
    author = "test author"
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": author})
    response = json.loads(response.text)
    author_id = response["id"]
    create_test_quote(quote, author, author_id, header)
    response = requests.get(ENDPOINT+"/fetch/author/",
                            params={"id": author_id})
    response = json.loads(response.text)
    data = random.choice(response["quotes"])
    quote_id = data["id"]
    response = requests.delete(
        ENDPOINT + f"/delete/quote/{quote_id}", headers=header)
    assert response.status_code == 200


def test_can_delete_author():
    header = initialize()
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": "test author"})
    response = json.loads(response.text)
    id = response["id"]
    response = requests.delete(
        ENDPOINT + f"/delete/author/{id}", headers=header)
    assert response.status_code == 200
