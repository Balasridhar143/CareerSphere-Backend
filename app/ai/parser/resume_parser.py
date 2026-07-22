import fitz
from docx import Document


def extract_resume_text(file_path: str):
    """
    Extract text from a PDF or DOCX resume.
    """

    if file_path.endswith(".pdf"):
        text = ""
        doc = fitz.open(file_path)

        for page in doc:
            text += page.get_text()

        doc.close()
        return text

    elif file_path.endswith(".docx"):
        doc = Document(file_path)

        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX.")