import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()
#defines merger as a PdfFileMerger object

for file in os.listdir(os.curdir):
#lists all files in the current directory
    if file.endswith(".pdf"):
    #checks if the file is a pdf
        merger.append(file)
        #appends the file to the merger object
        
merger.write("merged.pdf")
#writes the merger object to a new pdf file
merger.close()
#closes the merger object