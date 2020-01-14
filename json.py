import json

with open('file_name.json', encoding='utf8') as file:
    data = json.load(file)

# do some things
some_data = {
    'Teun': 'edu@teunvg.nl',
    'Joska': 'J.deLangen@uu.nl'
}

with open('file_name.json', 'w', encoding='utf8') as file:
    json.dump(some_data, file)