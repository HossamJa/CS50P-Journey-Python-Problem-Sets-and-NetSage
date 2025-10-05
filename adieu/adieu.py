import sys
import inflect
p = inflect.engine()
names = list()
while True:
    try:
        name = input('Name: ').strip().capitalize()
        names.append(name)
    except EOFError:
            print('')
            break

print('Adieu, adieu, to ' + p.join(names))

sys.exit(0)
