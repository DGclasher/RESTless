import requests
import json

endpoint = "http://localhost:8000/api/quotes/"
auth_endpoint = "http://localhost:8000/api/author/"

session = requests.Session()
response = requests.post(auth_endpoint, params={"id":1})

data = json.loads(response.text)

print(data)
