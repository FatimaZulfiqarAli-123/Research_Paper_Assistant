import fitz  # PyMuPDF

def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text("text")

    return text