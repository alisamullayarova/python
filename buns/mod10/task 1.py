import requests
import json

output = {}

def get_object_info(url):
    response = requests.get(url)
    data = json.loads(response.content)
    return data

def get_starships_info(url):
    starships = get_object_info(url)['results']
    return starships

def get_planet_info(url):
    planet = get_object_info(url)
    return planet

def find_Millennuim_Falcon(starships):
    for starship in starships:
        if starship['name'] == 'Millennium Falcon':
            return starship
        
def print_starship_info(starship):
    print('name: ', starship['name'])
    print('starship_class: ', starship['starship_class'])
    print('max_atmosphering_speed: ', starship['max_atmosphering_speed'])
    output['name'] = starship['name']
    output['starship_class'] = starship['starship_class']
    output['max_atmosphering_speed'] = starship['max_atmosphering_speed']
    print_pilots_info(starship['pilots'])

def print_pilots_info(starship_pilots):
    output['pilots'] = []
    print('pilots: ')
    for pilot in starship_pilots:
            info = get_object_info(pilot)
            pilot_info = {}
            planet_name = get_planet_info(info['homeworld'])['name']
            print('\tname: ', info['name'])
            print('\theight: ', info['height'])
            print('\tmass: ', info['mass'])
            print('\thomeworld: ', planet_name)
            print('\thomeworld_url: ', info['homeworld'])
            print()
            pilot_info['name'] = info['name']
            pilot_info['height'] = info['height']
            pilot_info['mass'] = info['mass']
            pilot_info['homeworld'] = planet_name
            pilot_info['homeworld_url'] = info['homeworld']
            output['pilots'].append(pilot_info)

def save_json():
    with open('task1_Mullayarova.json', 'w') as outfile:
        json.dump(output, outfile, indent = 2)

def main():
    starships = get_starships_info('https://swapi.dev/api/starships/')
    Millennium_Falcon = find_Millennuim_Falcon(starships)
    print_starship_info(Millennium_Falcon)
    save_json()

if __name__ == '__main__':
    main()

