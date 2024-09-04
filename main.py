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
        elif arg == ' ':
             pass
        
        else:
             print("Error lexic: '" + arg + "' Unexpected")
             exit(1)

        pointer += 1
    return out

def pick_type_pop(input, num):
     pick = input.pop(num)
     return pick["type"]

def empty(input):
     return len(input) == 0

def parse(input, inner):

     res = []

     while len(input) > 0:

          arg = input[0]
          current = pick_type_pop(input, 0)

          if current == 'left parenthesis':
               res.append(parse(input, True))
          elif current == 'right parenthesis':
               if inner:
                    return res
               else:
                    print("Systan error: unclosed expression")
                    return None
          else:
               res.append(arg)
     
     if inner:
          print("Unmatched expression")
     else:
          return res

     
     return parse(input, False)

def evaluator ():
     pass

def read_file(path):
    file = open(path, "r")
    input = file.read()
    return input

def main():
    input = read_file("program1.lisp")
    tokens = lex(input)
    tree = parse(tokens, False)
    print(tree)
    
main()