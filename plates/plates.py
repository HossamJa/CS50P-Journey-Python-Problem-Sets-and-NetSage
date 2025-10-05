def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 < int(len(s)) < 7:
        return False
    elif not s.isalnum():
        return False
    elif not s[:2].isalpha():
        return False

    elif s[2:].isdigit():
        if not int(s[2]) > 0:
            return False
        return True

    elif s[3:].isdigit():
        if not int(s[3]) > 0:
            return False
        return True

    elif s[4:].isdigit():
        if not int(s[4]) > 0:
            return False
        return True

    elif not s[2:].isalpha():
         return False

    else:
       return True
main()
