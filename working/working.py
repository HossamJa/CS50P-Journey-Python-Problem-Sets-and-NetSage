import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    Conversion_Table = {
        '12:00 AM' : '00:00',
        '1:00 AM' : '01:00',
        '2:00 AM' : '02:00',
        '3:00 AM':'03:00',
        '4:00 AM':'04:00',
        '5:00 AM':'05:00',
        '6:00 AM':'06:00',
        '7:00 AM':'07:00',
        '8:00 AM':'08:00',
        '9:00 AM':'09:00',
        '10:00 AM':'10:00',
        '11:00 AM':'11:00',
        '12:00 PM':'12:00',
        '1:00 PM':'13:00',
        '2:00 PM':'14:00',
        '3:00 PM':'15:00',
        '4:00 PM':'16:00',
        '5:00 PM':'17:00',
        '6:00 PM':'18:00',
        '7:00 PM':'19:00',
        '8:00 PM':'20:00',
        '9:00 PM':'21:00',
        '10:00 PM':'22:00',
        '11:00 PM':'23:00',
        '12:00 AM':'00:00',
    }

    form = r'(?P<h1>\d+)(?P<min1>:\d+)?(?P<frm1>.+) to (?P<h2>\d+)(?P<min2>:\d+)?(?P<frm2>.+)'
    time = re.search(form, s)

    try:
        time1 = Conversion_Table[f'{time.group('h1')}:00{time.group('frm1')}']
        time2 = Conversion_Table[f'{time.group('h2')}:00{time.group('frm2')}']

        if time.group('min1') and time.group('min2'):
            if int(time.group('min1').strip(':')) > 59 or 0 > int(time.group('min1').strip(':')) or int(time.group('min2').strip(':')) > 59 or 0 > int(time.group('min2').strip(':')):
                raise ValueError
            else:
                return f'{time1.replace(':00', time.group('min1'))} to {time2.replace(':00', time.group('min2'))}'

        elif time.group('min1'):
            if int(time.group('min1').strip(':')) > 59 or 0 > int(time.group('min1').strip(':')):
                raise ValueError
            else:
                return f'{time1.replace(':00', time.group('min1'))} to {time2}'

        elif time.group('min2'):
            if int(time.group('min2').strip(':')) > 59 or 0 > int(time.group('min2').strip(':')):
                raise ValueError
            else:

                return f'{time1} to {time2.replace(':00', time.group('min2'))}'
        else:
            return f'{time1} to {time2}'


    except:
        raise ValueError



if __name__ == "__main__":
    main()
