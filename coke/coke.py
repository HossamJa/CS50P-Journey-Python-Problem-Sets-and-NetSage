
amount = 50
result = amount

while True:
    coins = int(input("Insert Coin: "))
    if coins in [5, 10, 25]:
        last = result - coins
        result = last
        if result <= 0:
            change = result * -1
            print("Change Owed:", change)
            break
        print("Amount Due:", result)

    else:
        print("Amount Due:", result)
