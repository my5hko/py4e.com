import json
from icecream import ic

data = '''{
  "name": "Mykhailo",
  "phone": {
    "type": "intl",
    "number": "+380 67 505 4259"
  },
  "email": {
    "hide": "yes"
  }
}'''

info = json.loads(data)
ic(info)

print('Name:', info['name'])

print('Phone type:', info['phone']['type'])
print('Phone:', info['phone']['number'])

dogs = '''
[
    {"id": "001", "name": "Bert", "age": 5},
    {"id": "002", "name": "Archi", "age": 3}
]
'''
info = json.loads(dogs)
ic(info)
print('Dogs number:', len(dogs))

for dog in info:
    print('ID: ', dog['id'], ', Name: ', dog['name'], ', Age: ', dog['age'], sep='')