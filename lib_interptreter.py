def error(num):
    try:
        float(num)
        return True
    except:
        return False
        
def analisy(args):
    a = []
    for i in range(len(args)):
        value = args[i]
        if error(value):
            a.append(int(value))
    return a

def is_num(args):

    new_args = []

    if error(args) :
        for i in args:
            new_arg = int(args[i])
            new_args.append(new_arg)      
        return new_args
    else:
        return "Error unexpected"