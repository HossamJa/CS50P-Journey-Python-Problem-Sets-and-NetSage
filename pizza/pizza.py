import sys
import csv
from tabulate import tabulate



def main():
    print(table_version())

def table_version():

    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    elif not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')

    else:
        try:
            with open(sys.argv[1], 'r') as menu:
                menu_header = csv.DictReader(menu)
                dic_menu = csv.reader(menu)
                return tabulate(dic_menu, menu_header.fieldnames, tablefmt="grid")


        except FileNotFoundError:
            sys.exit('File does not exist')



if __name__ == "__main__":
    main()
