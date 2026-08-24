# Social Media Content Analyzer

A web application that allows users to upload PDF documents and image files and extract text from them.

## Features

- Upload PDF files
- Upload JPG/JPEG and PNG images
- Drag-and-drop file upload
- PDF text extraction
- OCR-based text extraction from images
- Loading indicator during processing
- Basic error handling
- Simple and responsive user interface

## Technologies Used

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- PyMuPDF
- Tesseract OCR
- Pytesseract

## How It Works

1. User selects or drags a PDF or image into the upload area.
2. The frontend sends the file to the FastAPI backend.
3. For PDFs, text is extracted using PyMuPDF.
4. For images, Tesseract OCR extracts the text.
5. The extracted content is returned to the frontend and displayed to the user.

## Running Locally

Activate the virtual environment:

    source venv/bin/activate

Start the FastAPI server:

    uvicorn app.main:app --reload

Open:

    http://127.0.0.1:8000