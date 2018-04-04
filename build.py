import yaml
import json
import os
import requests

languages_url = 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml'

replace_names = {
    'C++': 'cpp',
    'C#': 'C Sharp'
}


r =  requests.get(languages_url)
colors = yaml.load(r.text)
colors = dict((replace_names.get(name, name), color['color']) for name, color in colors.items() if 'color' in color)

with open('colors.json', 'w') as f:
    json.dump(colors, f, indent=4, sort_keys=True, separators=(',', ': '))
