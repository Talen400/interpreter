"""
Talen | 27/08/2024 | dd/mm/yyyy

"""
import sys
import lib_interptreter as lib

# Tokening

program_filepath = sys.argv[1]

program_file = []

with open(program_filepath, 'r') as program_file:
    program_file = [line for line in program_file.readline() ]

print(program_file)

program = []
indice = 0


for line in program_file:

    two_points = 0
    string_word = ""

    if line == ' ':
        continue

    if line == ':' :
        two_points = program_file.index(line);
        string_word = ''.join((program_file[:two_points])).strip()
        program.append(string_word)
        indice += 1
    
    if string_word == '/sum':
        numbers = lib.analisy(program_file[two_points:])
        program.append(numbers)
        indice += 1

for word in program:
    if word == "/sum":
        print(sum(program[1]))