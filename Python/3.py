import argparse
import sys
import re

parser = argparse.ArgumentParser(description='This is a program for defining and assigning tasks to users.\n You can '
                                             'do this with with following commands:\n CREATE USER X: '
                                             'Creates a user with name X.\n CREATE TASK Y: Creates a task with name '
                                             'Y.\n ASSIGN Y X: Assigns task X to user Y. \n LIST USER X: Prints a '
                                             'list of assigned tasks to X.\n LIST TASK Y: Prints a list of assigned '
                                             'users to Y.')
parser.add_argument('-n', type=int, help='Number of lines')
args = parser.parse_args()

users = {}
tasks = {}

i = 0
for line in sys.stdin:
    i += 1
    if args.n is not None and i >= args.n:
        break
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