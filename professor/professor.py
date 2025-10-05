import random

def main():
    level = get_level()
    running = True
    tries = 0
    score = 0
    num = 0
    while running:
        X, Y = generate_integer(level)
        answer = X + Y
        while True:

            if tries == 3:
                num += 1
                print(f'{X} + {Y} = {answer}')
                tries = 0
                break
            elif num == 10:
                print (f'Score: {score}')
                running = False
                break

            print(f'{X} + {Y} = ', end='')
            ask = input('')
            try:
                if ask.isdigit and int(ask) == answer:
                    score += 1
                    num += 1
                    break
                else:
                    print('EEE')
                    tries += 1

            except ValueError:
                    print('EEE')
                    tries += 1


def get_level():

    while True:
        lvl = input('Level: ').strip()
        try:
            if int(lvl) == 1 or int(lvl) == 2 or int(lvl) == 3:
                return int(lvl)
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):

    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    else:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)

    return X, Y

if __name__ == "__main__":
    main()
