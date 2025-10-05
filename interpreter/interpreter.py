expr = input("Expression: ").strip().split(" ")

x, y, z = expr

def calcul():
    if y == "+":
        return int(x) + int(z)
    elif y == "-":
        return int(x) - int(z)
    elif y == "/" and z !="0":
        return int(x) / int(z)
    elif y == "*":
        return int(x) * int(z)


Result = float(calcul())

print(Result)

