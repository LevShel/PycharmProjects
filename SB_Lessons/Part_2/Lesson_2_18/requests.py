import requests
import json

my_req = requests.get('https://sqapi.dev/api/people/3/')
data = json.loads(my_req.text)
print(data['name'])
