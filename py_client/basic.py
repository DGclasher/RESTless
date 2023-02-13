import requests
import json

base_url = "http://localhost:8000/api/"

# Fetch Class
class Fetch:
    def fetch_quote(self):
        response = requests.get(base_url+"fetch/quote/")
        return response.text

    def fetch_author(self, id, val):
        response = requests.get(base_url+"fetch/author/", params={id: val})
        return response.text

# Create Class
class Create:
    def create_author(self, name):
        response = requests.post(
            base_url+"create/author/", json={"name": name})
        return response.text

    def create_quote(self, quote, author):
        response = requests.post(base_url+"create/quote/",
                                 json={"quote": quote, "author": author})
        return response.text

# Delete Class
class Delete:
    def delete_author(self, id):
        response = requests.delete(base_url+"delete/author/"+str(id))
        return response.text

# Update Class
class Update:
    def update_author(self, id, name):
        response = requests.put(
            base_url+"update/author/"+str(id), json={"name": name})
        return response.text


update_quote = "http://localhost:8000/api/update/quote/4"

fetch_obj = Fetch()
create_obj = Create()
update_obj = Update()
delete_obj = Delete()

# response = fetch_obj.fetch_author("name", "Thomas Edison")
response = delete_obj.delete_author(104)
# response = create_obj.create_author("david")
response = update_obj.update_author(93, "Epictetus")

data = json.loads(response)

print(data)
