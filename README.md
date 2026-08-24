# Social Media Content Analyzer

A web application that allows users to upload PDF documents and image files and extract text from them.

## Features

- PDF upload
- JPEG/PNG image upload
- Drag-and-drop and file picker
- PDF text extraction using PyMuPDF
- OCR for images using Tesseract
- Loading indicator
- Basic error handling
- Responsive web interface

## Technologies

- Python
- FastAPI
- HTML, CSS, JavaScript
- PyMuPDF
- Pillow
- Pytesseract
- Tesseract OCR
- Docker
- Railway

## Approach

I developed a web-based Social Media Content Analyzer using FastAPI for the backend and HTML, CSS, and JavaScript for the frontend. The application provides a simple drag-and-drop and file-picker interface for uploading PDF and image files.

For PDF documents, I used PyMuPDF to extract available text. For scanned documents and image files such as JPEG and PNG, I implemented OCR using Tesseract and Pytesseract to convert image content into readable text.

The frontend sends uploaded files to the FastAPI `/extract` endpoint using a multipart form request. The backend validates the file type, processes the file using the appropriate extraction method, and returns the extracted text and character count.

Basic error handling was implemented for unsupported file types and processing failures. A loading indicator provides feedback while the file is being processed.

The application is containerized using Docker, including Tesseract installation, and deployed on Railway. The source code and documentation are maintained in this public GitHub repository.

## Live Application

https://social-media-content-analyzer-production-e032.up.railway.app/
