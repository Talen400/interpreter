def is_digit(arg):
    return (arg >= '0' and arg <= '9')

def is_name(arg):
     return(arg >= 'a' and arg <= 'z' or
            arg >= 'A' and arg <= 'Z')


def lex(input):
    input = input
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
             out.append({"type": "identifier", "value": arg})
        elif arg == '+':
             out.append({"type": "operator", "value": arg})
        elif arg == '(':
             out.append({"type": "left parenthesis", "value": arg})
        elif arg == ')':
             out.append({"type": "right parenthesis", "value": arg})
        elif arg == '-':
             out.append({"type": "operator", "value": arg})
        elif arg == '*':
             out.append({"type": "operator", "value": arg})
        elif arg == '/':
             out.append({"type": "operator", "value": arg})
        elif arg == ' ':
             pass
        
        else:
             print("Error lexic: '" + arg + "' Unexpected")
             exit(1)

        pointer += 1
    return out

def parse(input):
     for dic in input:
          match dic["type"]:
               case "identifier":
                    return dic
               case "number":
                    return dic
               case "=":
                    pass
               case ";":
                    pass
               case tpy :
                    print("Systax Error: unexpected" + tpy + ".")
                    exit(1)

def read_file(path):
    file = open(path, "r")
    input = file.read()
    return input

def main():
    input = read_file("program1.lisp")
    tokens = lex(input)
    print(tokens)
    tree = parse(tokens)
    
main()