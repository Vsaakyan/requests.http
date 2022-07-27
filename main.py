import requests
import json


url = 'https://akabab.github.io/superhero-api/api/all.json'

resp = requests.get(url)
response = resp.text
data = json.loads(response)

intelligence_dict = {}

my_heroes = ['Hulk', 'Captain America', 'Thanos']


def get_most_intelligence_hero():
    for hero in data:
        if hero['name'] in my_heroes:
            intelligence_dict[hero['name']] = hero['powerstats']['intelligence']
    print(f'Самый умный супергерой - {max(intelligence_dict.keys())} - {max(intelligence_dict.values())}')


get_most_intelligence_hero()






