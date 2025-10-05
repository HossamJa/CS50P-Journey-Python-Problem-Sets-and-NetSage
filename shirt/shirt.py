import sys
from PIL import Image
from PIL import ImageOps
from os.path import splitext



def main():
    tshirt_version()

def tshirt_version():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    elif not splitext(sys.argv[1])[1] in ['.jpg', '.jpeg', '.png']:
        sys.exit('Invalid input')
    elif not splitext(sys.argv[2])[1] in ['.jpg', '.jpeg', '.png']:
        sys.exit('Invalid output')

    elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit('Input and output have different extensions')

    else:
        try:
            with Image.open('shirt.png') as shirt, Image.open(sys.argv[1]) as img:
                size = shirt.size
                imag = ImageOps.fit(img, size)

                imag.paste(shirt, (0, 0), shirt)

                imag.save(sys.argv[2])



        except FileNotFoundError:
            sys.exit(f'Input does not exist')



if __name__ == "__main__":
    main()
