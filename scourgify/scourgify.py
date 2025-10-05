import sys
import csv

def main():
    print(table_version())

def table_version():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    else:
        try:
            with open(sys.argv[1], 'r') as list_before, open(sys.argv[2], 'w') as sys.argv[2]:
                read = csv.DictReader(list_before)
                write = csv.DictWriter(sys.argv[2], fieldnames=['first', 'last', 'house'])
                write.writeheader()

                for row in read:
                    last_name, fisr_name = row['name'].split(',')
                    write.writerow(
                        {
                           'first': fisr_name.lstrip(),
                           'last': last_name,
                           'house': row['house']
                        }
                    )

        except FileNotFoundError:
            sys.exit(f'Could not read {sys.argv[1]}')



if __name__ == "__main__":
    main()
