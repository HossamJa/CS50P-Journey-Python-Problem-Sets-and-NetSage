def main():
    time = input("What time is it? ").strip()
    Time = float(convert(time))
    if 7 <= Time <= 8:
        print("Breakfast time")
    elif 12 <= Time <= 13:
        print("Lunch time")
    elif 18 <= Time <= 19:
        print("Dinner time")


def convert(b):
    hours, minutes = b.split(":")
    if minutes == "0":
        return hours + ".0"
    elif minutes != "0":
        return int(hours) + int(minutes)/60



if __name__ == "__main__":
    main()

