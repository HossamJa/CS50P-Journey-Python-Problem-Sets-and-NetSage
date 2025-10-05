import sys

def main():
    print(line_number())

def line_number():
    ask = sys.argv
    if len(ask) < 2:
        sys.exit('Too few command-line arguments')
    elif len(ask) > 2:
        sys.exit('Too many command-line arguments')
    elif not ask[1].endswith('.py'):
        sys.exit('Not a Python file')
    else:
        try:
            with open(sys.argv[1]) as lines:

                cod_lines = 0
                for line in lines:
                    if line.lstrip() != '' and not line.lstrip().startswith('#'):
                        cod_lines += 1
                return cod_lines

        except FileNotFoundError:
            sys.exit('File does not exist')



if __name__ == "__main__":
    main()

