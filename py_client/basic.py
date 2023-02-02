import requests
import json

endpoint = "http://localhost:8000/api/quotes/quote"
auth_endpoint = "http://localhost:8000/api/quotes/author/"
post_endpoint = "http://localhost:8000/api/quotes/post/"
author_post = "http://localhost:8000/api/quotes/post/author/"
author_info = "http://localhost:8000/quotes/details/author/1"
session = requests.Session()
# response = requests.post(post_endpoint, json={"id":69,"quote":"don't bow down","author":1})

response = requests.post(post_endpoint, json={"quote":"here we go again", "author_id": {"id" : 1, "name":"Thomas Edison"} })

# response = requests.get(author_info)

data = json.loads(response.text)

print(data)
