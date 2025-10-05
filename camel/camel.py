def main():
    ask = input("name: ").strip()
    sncase = cts(ask)
    print(sncase.lower())


def cts(word):
    result = []
    curword = word[0]

    for char in word[1:]:
        if char.isupper():
            result.append(curword)
            curword = char
        else:
            curword += char
    result.append(curword)
    return "_".join(result)


main()
