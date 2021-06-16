from os import walk

files = []
for (dir_path, dir_names, filenames) in walk('venv'):
    files.extend(filenames)
f = open('venv/index', 'w')
for file in files:
    f.write(file + '\n')
