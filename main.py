"""
Talen | 27/08/2024 | dd/mm/yyyy

"""
import sys
import lib_interptreter as lib

# Tokening

program_filepath = sys.argv[1]

program_file = []
program_line = []

with open(program_filepath, 'r') as program_file:
    program_file = [line for line in program_file.readlines() ]


program = []

for step in range(len(program_file)):
        program_line = [ word for word in program_file[step]]
        program_command = []
        
        #print(program_line)

        i = 0

        while program_line[i] != ":" :
              if program_line[i] != ' ':
                   program_command.append(program_line[i])
              i += 1

        then_two_points = []

        while program_line[i] != ';':
              if program_line[i] != ' ' and program_line[i] != ':':
                    then_two_points.append(program_line[i])
              i += 1
        program.append(''.join(program_command))
        program.append(then_two_points)
        
i = 0
for arg in program:
      i += 1
      if arg == "/sum":
            numbers = lib.is_num(program[i])
            print(sum(numbers))