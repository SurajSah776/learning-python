'''
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities.

# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
'''
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

path = input(
    "Enter absolute path of the files ('.' for current directory) : ")
files = os.listdir(path)
# print(files)

pdfFiles = [file for file in files if file.endswith(".pdf")]

print()
print(f"All the pdf files present in the location '{path}' :  ")
print(pdfFiles)
