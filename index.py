from pdf2docx import Converter

def pdf_to_docx(pdf_file, docx_file):
   # Create the PDF converter object
   cv = Converter(pdf_file)

   # Convert from PDF to word
   cv.convert(docx_file, start=0, end=None) # You can specify page range from start/end
   cv.close()
   print(f"Converted {pdf_file} to {docx_file}")