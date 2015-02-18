import subprocess
import yaml
import json
import os

replace_names = {
    'C++': 'cpp',
    'C#': 'C Sharp'
}

subprocess.call(['wget', 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml', '-q'])

with open('languages.yml') as f:
    colors = yaml.load(f)
os.remove('languages.yml')
colors = dict((replace_names.get(name, name), color['color']) for name, color in colors.items() if 'color' in color)

with open('colors.json', 'w') as f:
    json.dump(colors, f, indent=4)

with open('README.rst', 'w') as f:
    f.write('A mapping of which colors github uses to represent different programming languages in their "Languages" tab on each repository.')
    f.write('\n\n')
    f.write('\n'.join('.. image:: http://www.placehold.it/200/%s/ffffff&text=%s' % (v[1:], k) for k, v in colors.items()))
