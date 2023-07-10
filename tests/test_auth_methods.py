import random
import requests
from decouple import config

ENDPOINT = "http://127.0.0.1:8000/api"

username = config("TEST_USER")
password = config("TEST_PASS")

response = requests.post(
    ENDPOINT + "/auth/", json={"username": username, "password": password})
token = response.json()["token"]
header = {"Authorization": f"Token {token}"}


def get_random_quote_for_testing():
    response = requests.get("https://quote-garden.onrender.com/api/v3/quotes")
    data = response.json()["data"]
    quote = random.choice(data)
    author = quote["quoteAuthor"]
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": author})
    if "Author doesn't exist" in response.text:
        return 14, "unknown", quote["quoteText"]
    id = response.json()["id"]
    return id, author, quote["quoteText"]


def create_test_quote(quote, author_name, id):
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
    name = "test author"
    response = requests.post(ENDPOINT + "/create/author/",
                             json={"name": name}, headers=header)
    assert response.status_code == 201


def test_can_update_author():
    new_name = "test author"
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": new_name})
    author_id = response.json()["id"]
    response = requests.put(
        ENDPOINT + f"/update/author/{author_id}", json={"name": new_name}, headers=header)
    assert response.status_code == 200


def test_can_delete_quote():
    quote = "this is a test quote"
    author = "test author"
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": author})
    author_id = response.json()["id"]
    create_test_quote(quote, author, author_id)
    response = requests.get(ENDPOINT+"/fetch/author/",
                            params={"id": author_id})
    data = random.choice(response.json()["quotes"])
    quote_id = data["id"]
    response = requests.delete(
        ENDPOINT + f"/delete/quote/{quote_id}", headers=header)
    assert response.status_code == 200


def test_can_delete_author():
    response = requests.get(ENDPOINT + "/fetch/author/",
                            params={"name": "test author"})
    id = response.json()["id"]
    response = requests.delete(
        ENDPOINT + f"/delete/author/{id}", headers=header)
    assert response.status_code == 200
