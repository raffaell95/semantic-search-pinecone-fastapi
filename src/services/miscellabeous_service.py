from typing import List

from PyPDF2 import PdfReader
from fastapi import UploadFile
from io import BytesIO


def extract_text_from_pdf(pdf_file: UploadFile) -> str:
    pdf_byte = pdf_file.file.read()
    pdf_stream = BytesIO(pdf_byte)

    reader_pdf = PdfReader(pdf_stream)
    return "".join(page.extract_text() for page in reader_pdf.pages)

def slip_text_into_chunks(text: str, chunk_size=1000, overlap=200) -> List[str]:
    chunks = [text[i:i + chunk_size]
              for i in range(0, len(text), chunk_size - overlap)]
    return chunks