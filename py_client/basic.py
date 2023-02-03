import requests
import json

base_url = "http://localhost:8000/api/"


class Fetch:
    def fetch_quote(self):
        response = requests.get(base_url+"fetch/quote/")
        return response.text

    def fetch_author(id, val):
        response = requests.get(base_url+"fetch/author/", params={id: val})
        return response.text


class Create:
    def create_author(self, name):
        response = requests.post(base_url+"create/author/", json={"name": name})
        return response.text

    def create_quote(quote, author):
        response = requests.post(base_url+"create/quote/",
                                json={"quote": quote, "author": author})
        return response.text

class Delete:
    def delete_author(self, id):
        response = requests.delete(base_url+"delete/author/"+str(id))
        return response.text

class Update:
    def update_author(self, id, name):
        response = requests.put(base_url+"update/author/"+str(id), json={"name": name})
        return response.text


update_quote = "http://localhost:8000/api/update/quote/4"

fetch_obj = Fetch()
create_obj = Create()
update_obj = Update()
delete_obj= Delete()

response = delete_obj.delete_author(111)

data = json.loads(response)

print(data)
