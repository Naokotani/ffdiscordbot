import json

charName = input('Character Name? ')

f = open(charName, 'r')

char = json.load(f)

print(char)
print('\n\n')
skills = char['Skills']
general = skills['General']

print(general)

print('\n\n')

print(general['Charm'])

