from pathlib import Path
from pypdf import PdfReader

# Base directory = project root (two levels up from this file: app/services -> app -> project root)
BASE_DIR = Path(__file__).resolve().parents[2]
UPLOADS_DIR = BASE_DIR / "uploads"

def extract_text_from_pdf_file(filename: str, max_chars: int = 8000) -> str:
    """
    Read a PDF from <project-root>/uploads/<filename> and return its text.
    - Only .pdf files are allowed.
    - Only files directly inside /uploads are allowed (no subfolders).
    """
    # Disallow path tricks like "../" or "subdir/file.pdf"
    if Path(filename).name != filename:
        raise ValueError("Use only the plain filename, no paths or subfolders.")

    file_path = (UPLOADS_DIR / filename).resolve()

    # Allow only PDFs
    if file_path.suffix.lower() != ".pdf":
        raise ValueError("Only .pdf files are allowed.")

    # Basic existence check
    if not file_path.is_file():
        raise ValueError(f"File not found: {file_path.name} in /uploads")

    # Read & extract
    reader = PdfReader(file_path)
    text_parts = []
    for page in reader.pages:
        txt = page.extract_text()
        if txt is None:
            txt = ""
        text_parts.append(txt)
    text = "\n".join(text_parts).strip()

    # Limit size (you can increase/decrease as needed)
    return text[:max_chars]



# test output:
# print(extract_text_from_pdf_file("CV_Nico_Wittemann_eng.pdf"))