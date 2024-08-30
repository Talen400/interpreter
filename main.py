

def is_digit(arg):
    return (arg >= '0' and arg <= '9')

def is_name(arg):
     return(arg >= 'a' or arg <= 'z' or
            arg >= 'A' or arg <= 'Z')

def lex(input):
    input = input.split()
    pointer = 0
    out = []
    while pointer < len(input):
        arg = input[pointer]
        
        if arg == '=':
             out.append({"type": "operator", "value": arg})
        elif arg == ';':
              out.append({"type": "end", "value": arg})
        elif is_digit(arg):
              out.append({"type": "number", "value": arg})
        elif is_name(arg):
              out.append({"type": "number", "value": arg})

        pointer += 1
    return out



def read_file(path):
    file = open(path, "r")
    input = file.read()
    return input

def main():
    input = read_file("program1.lisp")
    tokens = lex(input)
    print(tokens)
    

main()