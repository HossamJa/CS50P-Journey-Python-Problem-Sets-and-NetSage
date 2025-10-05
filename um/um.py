import re


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    parts = s.split(' ')
    um = r'\b ?Um\b,?\.?'
    for part in parts:
        if  re.search(um, part, re.IGNORECASE):
            count += 1
        else:
            continue
    return count


if __name__ == "__main__":
    main()
