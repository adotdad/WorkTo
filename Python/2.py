import sys
import re

users = {}
tasks = {}
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    input_line = re.split("\s", line.rstrip())
    if input_line[0] == 'CREATE' and input_line[1] == 'USER':
        users[input_line[2]] = []
    if input_line[0] == 'CREATE' and input_line[1] == 'TASK':
        tasks[input_line[2]] = []
    if input_line[0] == 'ASSIGN':
        users[input_line[2]].append(input_line[1])
        tasks[input_line[1]].append(input_line[2])
    if input_line[0] == 'LIST' and input_line[1] == 'USER':
        print(users[input_line[2]])
    if input_line[0] == 'LIST' and input_line[1] == 'TASK':
        print(tasks[input_line[2]])
