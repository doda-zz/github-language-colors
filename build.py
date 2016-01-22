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
    color_strings = ('.. image:: http://www.placehold.it/150/%s/ffffff&text=%s' % (v[1:].lower(), k) for k, v in colors.items())
    f.write('\n'.join(sorted(color_strings)))
