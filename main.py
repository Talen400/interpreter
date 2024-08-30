import sys

def lex(token):
    i = 0
    while i < len(token):
        arg = token[i]["list"].split()
        pointer = 0
        while pointer < len(arg):
            
            pointer += 1
        i += 1
            

    return token    

def lines(file):
    lines = []
    value = 0
    i = 0
    while i < len(file):
        lines.append({"type": "line", "value": value, "list": file[i]})
        i += 1
        value += 1
        pass
    return lines

def main():
    program_file_path = sys.argv[1]
    program = []
    with open(program_file_path, 'r') as program_file:
        program = lines([line for line in program_file])
    lex(program)
    print(program)
main()