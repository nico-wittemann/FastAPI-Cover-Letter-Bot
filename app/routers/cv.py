from fastapi import APIRouter, HTTPException, Query
from app.services.cv import extract_text_from_pdf_file

router = APIRouter()

@router.get("/extract-by-name", summary="Read a CV PDF from /uploads and return plain text")
def extract_by_name(filename: str = Query(..., description="Filename in /uploads")):
    try:
        text = extract_text_from_pdf_file(filename)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"cv_text": text}

