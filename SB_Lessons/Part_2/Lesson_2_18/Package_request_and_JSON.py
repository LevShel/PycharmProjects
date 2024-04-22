import requests
import json

my_req = requests.get('https://swapi.dev/api/people/3/')
print(my_req.text)

data = json.loads(my_req.text)
data['name'] = 'R10-D10'
print(data['name'])

with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4) # сериализация JSON

with open('my_test.json', 'r') as file:
    data = json.load(file)
print(data)
