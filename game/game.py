import random

while True:
    n = input('Level: ')
    if n.isdigit():
        if int(n) < 1:
            continue
        else:
            break

lownum = 1
highnum = int(n)
answer = random.randint(lownum, highnum)
while True:

    geuss = input('Guess: ').strip()
    if not geuss.isdigit() or int(geuss) < 1:
        continue
    elif int(geuss) > answer:
        print('Too large!')
        continue
    elif int(geuss) < answer:
        print('Too small!')
        continue
    else:
        print('Just right!')
        break
