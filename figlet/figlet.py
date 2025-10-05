import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

if 1 > len(sys.argv) > 3:
    sys.exit('Invalid usage')


elif len(sys.argv) == 1:
    txt = input('Input: ')
    fnt = random.choice(fonts)
    ftxt = figlet.setFont(font=fnt)
    print(figlet.renderText(txt))



elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font' and sys.argv[2] in fonts:

        txt = input('Input: ')
        fnt = sys.argv[2]
        ftxt = figlet.setFont(font=fnt)
        print(figlet.renderText(txt))

    else:
        sys.exit('Invalid usage')
