months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").title()
        if "," in date:
            month, day, year = date.strip(",").split()
            if int(day)>31 or int(day)<1:
                pass
            else:
                dmonth = months.index(month) + 1
                print(f"{year}-{dmonth:02}-{day:02}")
                break
        elif "/" in date:
            month, day, year = date.split("/")
            if int(day)>31 or int(day)<1 or int(month)>12 or int(month)<1:
                pass
            else:
                print(f"{year}-{month:02}-{day:02}")
                break
    except Exception:
        pass



