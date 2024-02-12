import PyPDF2

with open('/input/input.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    for page_number in range(reader.numPages):
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(reader.getPage(page_number))
        output_filename = f'output_page_{page_number + 1}.pdf'
        with open(output_filename, 'wb') as output_file:
            writer.write(output_file)