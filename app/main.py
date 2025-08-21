# Start
# .\scripts\dev.ps1 -Port 8000

# Stop (if needed)
# .\scripts\stop.ps1 -Port 8000

from fastapi import FastAPI
from app.routers import cv

app = FastAPI(title="Cover Letter Bot")
app.include_router(cv.router)

# Root so, dass der Browser was sieht:
@app.get("/")
def health():
    return {"status": "healthy"}





















"""
from pydantic import BaseModel

@app.get("/")
def root():
    return {"status": "ok"}

class GenerateRequest(BaseModel):
    job_title: str
    company: str
    job_description: str
    contact_person: str | None = None
    cv_text: str | None = None  # <= NEW: optional CV snippet

@app.post("/generate")
def generate_cover_letter(req: GenerateRequest):
    person = req.contact_person or "Hiring Team"
    cv_snippet = (req.cv_text or "").strip()[:400]

    letter = (
        f"Hello {person},\n\n"
        f"For the {req.job_title} role at {req.company}, I bring relevant experience. "
        f"The posting highlights: {req.job_description[:300]}...\n\n"
        + (f"From my background: {cv_snippet}\n\n" if cv_snippet else "")
        + "Kind regards,\nNico"
    )
    return {"cover_letter": letter}"""

