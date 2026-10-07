from pathlib import Path
import re

import fitz
from docx import Document


def extract_pdf_text(file_path: Path) -> str:
    """
    Extract text from all pages of a PDF file.
    """

    text = []

    with fitz.open(file_path) as pdf:
        for page in pdf:
            page_text = page.get_text()

            if page_text:
                text.append(page_text)

    return "\n".join(text).strip()


def extract_docx_text(file_path: Path) -> str:
    """
    Extract text from a DOCX file.
    """

    document = Document(file_path)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text.strip())

    return "\n".join(text).strip()


def clean_text(text: str) -> str:
    """
    Clean extracted document text.
    """

    if not text:
        return ""

    # Replace multiple spaces/tabs with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove leading/trailing spaces from each line
    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines at beginning/end
    text = "\n".join(lines).strip()

    return text


def check_text_quality(text: str) -> dict:
    """
    Check whether extracted text is usable for further analysis.
    """

    cleaned_text = clean_text(text)

    character_count = len(cleaned_text)
    word_count = len(cleaned_text.split())

    if character_count == 0:
        return {
            "readable": False,
            "character_count": 0,
            "word_count": 0,
            "reason": "No text could be extracted from the document."
        }

    if word_count < 20:
        return {
            "readable": False,
            "character_count": character_count,
            "word_count": word_count,
            "reason": "The document contains too little readable text."
        }

    return {
        "readable": True,
        "character_count": character_count,
        "word_count": word_count,
        "reason": "The document contains sufficient readable text."
    }


def extract_text(file_path: Path) -> str:
    """
    Detect the file type and extract its text.
    """

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    if extension == ".docx":
        return extract_docx_text(file_path)

    raise ValueError(
        "Unsupported document type. Only PDF and DOCX are currently supported."
    )