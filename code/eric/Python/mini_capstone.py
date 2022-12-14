# MINI CAPSTONE - I created a program to search a PDF and extract the pages 
# into a new PDF that contain the searched term.

import re
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file = open('tesla_10k.pdf','rb')
pdfReader = PdfFileReader(pdf_file)
pdfWriter = PdfFileWriter()

information = pdfReader.getDocumentInfo()
number_of_pages = int(pdfReader.numPages)

print('The author is: ', information.author)
print(f'The PDF has', number_of_pages, 'pages.')

# search the PDF for the search word
results = []
def search():
    results = []
    search_word = input('Input a word to search: ')
    for x in range(0, number_of_pages): 
        page = pdfReader.getPage(x)
        page_content = page.extractText()
        if re.search(search_word.lower(), page_content.lower()):
            print(f"Found '{search_word}' on page {x}")
            results.append(x)
    print(f'The search term is found on the following {len(results)} pages: {results}')
search()

# create a new PDF with the pages where the search word is found
output = PdfFileWriter()

print_pdf = input('Would you like to print these pages to a new PDF (yes/no)?: ')
if print_pdf == 'yes':
    for x in results:
        output.addPage(pdfReader.getPage(x))
    with open("search_results.pdf", "wb") as output_stream:
        output.write(output_stream)
search_again = input('Would you like to search again (yes/no)?:')
if search_again == 'yes':
    search()
if print_pdf == 'no':
    search_again = input('Would you like to search again (yes/no)?:')
    if search_again == 'yes':
        search()
    