fruits = {"Apple":130,
    "Avocado":50,
    "Banana":110,
    "Grapefruit":60,
    "Cantaloupe":50,
    "Grapes":90,
    "Honeydew Melon":50,
    "Kiwifruit":90,
    "Lime":15,
    "Nectarine":60,
    "Orange":80,
    "Peach":60,
    "Pear":100,
    "Tangerine":50,
    "Watermelon":80,
    "Pineapple":50,
    "Sweet Cherries":100,
    "Strawberries":50,
    "Plums":70}


asked = input("Item: ").title()

if asked in fruits:
    print("Calories:", fruits.get(asked))
