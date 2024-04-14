import os

def convert_str_to_date(date):
    possible_formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y/%m/%d"]
    for fmt in possible_formats:
        try: return datetime.strptime(date, fmt)
        except ValueError: pass
    # If none of formats match
    raise ValueError("Unrecognized date format, valid formats 'Y-M-D H:M:S', 'Y-M-D H:M', 'Y-M-D', 'Y/M/D' ")

def remove_static_files(): # remove files before initialize database
    directories = [
        'static/admin_graphs',
        'static/images/authors',
        'static/images/books',
        'static/images/profiles',
        'static/images/sections',
        'static/pdfs'
    ]
    for directory in directories:
        default_files = set(['default.png','default.pdf'])
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root,file)
                if file not in default_files:
                    os.remove(file_path)
    return 200

import uuid
from datetime import datetime
def get_unique_filename(filename):
    # Split the filename and extension
    name, ext = os.path.splitext(filename)
    # Generate a unique filename using the current timestamp and a random string
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_string = str(uuid.uuid4().hex)[:4]  # Generate a random string of 8 characters
    unique_filename = f"{timestamp}_{random_string}{ext}"
    return unique_filename

def count_pdf_pages(pdf_path):
    import PyPDF2
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
    return num_pages

def extract_first_page_as_png(pdf_path, output_path):
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[0]
    image = page.render(scale=4).to_pil()
    image.save(output_path)
