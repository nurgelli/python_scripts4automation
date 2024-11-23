import PyPDF2

inp_book = open('book.pdf', 'rb')
pdf_read = PyPDF2.PdfReader(inp_book)


with open('output_book.txt', 'w', encoding='utf-8') as output_file:
    for page in range(len(pdf_read.pages)):
        book_pages = pdf_read.pages[page]
        text = book_pages.extract_text()
        output_file.write(text)
        output_file.write('\n')
        print('Converting PDF file to text file have successfully completed!')
        
inp_book.close()
