import string

def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greet = greeting.strip().lower()
    first = greet.split()[0].strip(string.punctuation)
    chara = first[0]
    if first == "hello":
        return 0
    elif chara == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
