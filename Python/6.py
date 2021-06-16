import json

input_path = input('input: ')
output_path = input('output: ')
dictionary = {}
with open(input_path) as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    dictionary[line] = json.loads(line)['id']

dictionary = list(sorted(dictionary.items(), key=lambda item: item[1]))

f = open(output_path, 'w')
for key in dictionary:
    f.write(key + '\n')
