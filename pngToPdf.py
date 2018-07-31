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

#Give pages where the pages are in .PNG format
listPages=['page1','page2']

#Give the target filename which will be the filename of the final PDF, eg outputfile.pdf
makePdf('outputfile',listPages)
