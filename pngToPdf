from fpdf import FPDF
from PIL import Image
import os

def makePdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) + ".png")
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".png", 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")

#Read PNG image screenshot
filelist=os.listdir(os.getcwd())

listPages=[]
for file in filelist:

    if file.endswith('.png'):
        listPages.append(file.rstrip('.png'))

print(listPages)

listPages=['Quality Inn Santa Clara Convention Center']
makePdf('Quality Inn Santa Clara Convention Center',listPages)
