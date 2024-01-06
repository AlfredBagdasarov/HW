import requests
import json


my_req = requests.get('https://swapi.dev/api/people/3/')

if my_req.status_code == 200:
    data = json.loads(my_req.text)
    data['name'] = input('Введите новое имя: ')
    with open('swap.json', 'w') as file:
        json_text = json.dump(data, file, indent=4)

    result_homeworld = requests.get(data['homeworld'])
    print(result_homeworld.text)
