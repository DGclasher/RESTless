import requests
import json

endpoint = "http://localhost:8000/api/quotes/"

session = requests.Session()
response = requests.get(endpoint)

data = json.loads(response.text)

print(data)
