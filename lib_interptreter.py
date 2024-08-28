def error(num):
    try:       
        return int(num)
    except:
        return error_file()
        
def analisy(args):
    a = []
    for i in range(len(args)):
        value = args[i]
        if error(value):
            a.append(int(value))
    return a

def is_num(args):

    new_args = []

    for arg in args :
        new_args.append(error(arg))
    
    return new_args

def error_file():
    print("Unexpected Error")
    exit(1)