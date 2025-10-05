
def main():
    ask = input("Fraction: ")
    print(gauge(convert(ask)))


def convert(fraction):
    while True:
        try:
            num1, num2 = fraction.split("/")
            percentage = (int(num1) / int(num2)) * 100
            if percentage > 100:
                raise ValueError
            else:
                return round(percentage)

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError

def gauge(percentage):

    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        return (f"{round(percentage)}%")


if __name__ == "__main__":
    main()
