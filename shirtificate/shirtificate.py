from fpdf import FPDF
from PIL import Image

def main():
    user_input = input('Name: ')
    shirtificate(user_input)

def shirtificate(inpt):

    with Image.open("shirtificate.png") as shirt:
        img_width, img_hight = shirt.size
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_margin(0)
        x = pdf.w / 20
        y = pdf.h / 4.3

        pdf.image("shirtificate.png", x=x, y=y, w=img_width/3.1, h=img_hight/3.1)


        pdf.set_font("helvetica", size=45)
        pdf.cell(pdf.w, 75, "CS50 Shirtificate", align='C')
        pdf.set_y(pdf.w - 80)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("helvetica", size=20)
        pdf.cell(pdf.w, 10, inpt + ' took CS50', align='C')
        pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()
