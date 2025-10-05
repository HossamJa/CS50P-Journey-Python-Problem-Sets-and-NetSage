def main():
    result = round(calculat())
    if result > 100:
        calculat()
    elif result <= 1:
        print ("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result}%")

def calculat():

    while True:
        ask = input("Fraction: ")

        try:
            num1, num2 = ask.split("/")
            return (int(num1) / int(num2)) * 100

        except (ValueError, ZeroDivisionError):
            pass



main()
