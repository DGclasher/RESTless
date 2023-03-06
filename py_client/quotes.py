import requests
import sys
import json
from decouple import config
from getpass import getpass

base_url = "http://localhost:8000/api/"
token_url = "http://localhost:8000/api/auth/"
login_url = "http://localhost:8000/users/login/"


# Fetch Class

class Fetch:
    def fetch_quote(self):
        response = requests.get(base_url+"fetch/quote/")
        return response.text

    def fetch_author(self, id, val):
        response = requests.get(base_url+"fetch/author/", params={id: val})
        return response.text

    def fetch_author_all(self):
        response = requests.get(base_url+"fetch/author/all/")
        return response.text


class AuthClasses:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.auth = requests.post(
            token_url, json={"username": username, "password": password})
        if self.auth.status_code != 200:
            print("Authorization failed")
            sys.exit()
        self.token = self.auth.json()['token']
        self.header = {"Authorization": f"Token {self.token}"}

    # Create Methods

    def create_author(self, name):
        response = requests.get(
            base_url+"create/author/", json={"name": name}, headers=self.header)
        return response.text

    def create_quote(self, quote, author_id, author):
        json_data = {
            "quote": quote,
            "author_id": author_id,
            "author": {
                "id": author_id,
                "name": author
            }
        }
        response = requests.post(base_url+"create/quote/",
                                     json=json_data, headers=self.header)
        return response.text

    # Update Methods

    def update_author(self, id, name):
        response = requests.put(
            base_url+"update/author/"+str(id), json={"name": name}, headers=self.header)
        return response.text

    # Delete Methods

    def delete_author(self, id):
        response = requests.delete(
            base_url+"delete/author/"+str(id), headers=self.header)
        return response.text


username = config('TEST_USER')
password = config('TEST_PASS')

auth_obj = AuthClasses(username, password)
fetch_obj = Fetch()

# password = getpass()

# Fetch
response = fetch_obj.fetch_author("name", "Lucas")
# response = fetch_obj.fetch_quote()

# Create
# response = auth_obj.create_author("jack")
# response = auth_obj.create_quote("doing from client", 109, ath_name)
# response = auth_obj.create_author("django")

# Update

# Delete
# response = auth_obj.delete_author(109)

data = json.loads(response)
print(data)
