from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.extractor import (
    extract_text_from_pdf,
    extract_text_from_image
)

app = FastAPI(
    title="Social Media Content Analyzer",
    description="Analyze social media content and provide insights.",
    version="1.0.0"
)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/extract")
async def extract_content(file: UploadFile = File(...)):

    allowed_types = {
        "application/pdf",
        "image/png",
        "image/jpeg",
        "image/jpg"
    }

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, PNG and JPEG files are supported."
        )

    file_bytes = await file.read()

    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file_bytes)
    else:
        text = extract_text_from_image(file_bytes)

    return {
        "filename": file.filename,
        "text": text,
        "character_count": len(text)
    }