# MINI CAPSTONE - I created a program to search a PDF and extract the pages
# into a new PDF that contain the searched term.

import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
pdf_file = open('/Users/erichewitt/code-guild/Labs/Python/tesla_10k.pdf', 'rb') # the path to the PDF goes here
pdfReader = PdfFileReader(pdf_file)

information = pdfReader.getDocumentInfo()
number_of_pages = int(pdfReader.numPages)

print('The author is: ', information.author)
print(f'The PDF has', number_of_pages, 'pages.')

results = []

# search the PDF for the search word
def search_pdf():
    search_word = input('Input a word to search: ')
    for x in range(0, number_of_pages):
        page = pdfReader.getPage(x)
        page_content = page.extractText()
        if re.search(search_word.lower(), page_content.lower()):
            print(f"Found '{search_word}' on page {x}")
            results.append(x)
    print(f'The search term is found on the following {len(results)} pages: {results}')

# create a new PDF with the pages where the search word is found
def print_pdf():
    output = PdfFileWriter()
    print_pdf_yn = input('Would you like to print these pages to a new PDF (yes/no)?: ')
    if print_pdf_yn == 'yes':
        for x in results:
            output.addPage(pdfReader.getPage(x))
        with open(f"search_results_{moment}.pdf", "wb") as output_stream:
            output.write(output_stream)

search_pdf()
print_pdf()