def main():

    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    short = []
    for char in word:
        if char in ["a", "A", "e", "E", "I", "i", "O", "o", "U", "u"]:
            continue
        else:
            short.append(char)
    return ''.join(short)


if __name__ == "__main__":
    main()
