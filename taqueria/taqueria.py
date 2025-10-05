
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

result = []
while True:
    try:
        item = input("Item: ").strip().title()
        price = items.get(item)
        if item in items:
            result.append(price)
            total = sum(result)
            print(f"Total: ${total:.2f}")
        else:
            pass

    except EOFError:
        print()
        break


