from pdf2docx import Converter 
# We import the library that will help us convert the PDF file to a docx data type file.

def pdf_to_docx(pdf_file, docx_file): # Defining the attributes pdf_file and docx_file
   # Create the PDF converter object
   cv = Converter(pdf_file)

   # Convert from PDF to word
   cv.convert(docx_file, start=0, end=None) # You can specify page range from start/end
   cv.close()
   print(f"Converted {pdf_file} to {docx_file}")

# Test usage - I'm going to give an UI later.
pdf_to_docx("Introduccion a la algoritmia - Diagramas de flujo, tarea.pdf", "Introduccion a la algoritmia - Diagramas de flujo, tarea.docx")