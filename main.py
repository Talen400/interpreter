from TokenType import TokenType

def error(line, message):
    print(line + " " + message)

def report(line, where, message):
    print("[line " + line + "] Error" + where + ": " + message)

def main():
    f = open("program.lisp", "r", encoding="utf=8")
    long = f.read()
    print(f)
    print(long)
    print("Hi :>")
    print(TokenType.LEFT_PAREN);
    while (True):
        text = input("> ")
        print("sua saida: " + text)

if __name__ == "__main__":
    main()
