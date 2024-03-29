import PyPDF2
import os
from pdfnup import generateNup
from Tkinter import *

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.title("Python PDF Rotate'n'Print")

root.mainloop()
root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))

pdf_in = open(root.filename, 'rb')

print('Found PDF, executing...')
print('Step 1 of 2: Rotating')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    if pagenum % 2:
        page.rotateClockwise(180)
    pdf_writer.addPage(page)

pdf_out = open('output-rotated.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()



print('Step 2 of 2: Nupping')
generateNup("output-rotated.pdf", 2, verbose=True)


# Delete temporary pdf
print("Clearing Cache");
os.remove("output-rotated.pdf");

print("Done");
