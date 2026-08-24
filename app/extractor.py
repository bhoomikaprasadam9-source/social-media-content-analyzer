import io
import fitz
import pytesseract

from PIL import Image


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from a PDF, using OCR when necessary."""

    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    extracted_text = []

    for page in pdf:
        text = page.get_text().strip()

        if text:
            extracted_text.append(text)
        else:
            # Convert scanned PDF page to an image
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            image_bytes = pix.tobytes("png")

            image = Image.open(io.BytesIO(image_bytes))
            ocr_text = pytesseract.image_to_string(image)

            extracted_text.append(ocr_text)

    pdf.close()

    return "\n".join(extracted_text).strip()


def extract_text_from_image(file_bytes: bytes) -> str:
    """Extract text from an image using Tesseract OCR."""

    image = Image.open(io.BytesIO(file_bytes))

    return pytesseract.image_to_string(image).strip()