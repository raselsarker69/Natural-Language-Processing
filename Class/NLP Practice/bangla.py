from pdf2image import convert_from_path, exceptions
import pytesseract
import os

# Path to the PDF and the output text file
pdf_path = r'bangla.pdf'
output_file = 'bangla.txt'

try:
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file '{pdf_path}' does not exist.")
    
    # Convert PDF to images
    pages = convert_from_path(pdf_path)
    
    # Extract text from the single page
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, page in enumerate(pages, start=1):
            text = pytesseract.image_to_string(page, lang='ben')
            f.write(f"Page {i}:\n")
            f.write(text + '\n\n')
    
    print(f"Text extracted and saved to {output_file}")
    
except FileNotFoundError as e:
    print(f"Error: {e}")
except exceptions.PDFInfoNotInstalledError:
    print("Error: Poppler is not installed. Please install it to process PDFs.")
except exceptions.PDFPageCountError:
    print(f"Error: Unable to get page count for the file: '{pdf_path}'. Check if the file is corrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")