from pathlib import Path

from app.services.document_service import (
    extract_text,
    clean_text
)

from app.services.qwen_analysis_service import (
    analyze_resume_semantically
)


# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

UPLOAD_DIR = BASE_DIR / "uploads"

RESUME_ID = "res_b2017714"


# ---------------------------------------------------------
# FIND RESUME
# ---------------------------------------------------------

matching_files = list(
    UPLOAD_DIR.glob(
        f"{RESUME_ID}.*"
    )
)

if not matching_files:

    raise FileNotFoundError(
        "Resume file not found."
    )

file_path = matching_files[0]


# ---------------------------------------------------------
# EXTRACT TEXT
# ---------------------------------------------------------

text = extract_text(
    file_path
)

text = clean_text(
    text
)


# ---------------------------------------------------------
# QWEN ANALYSIS
# ---------------------------------------------------------

print(
    "Running Qwen semantic analysis..."
)

result = analyze_resume_semantically(
    text
)


# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL SEMANTIC RESULT")
print("=" * 60)

print(result)

print("=" * 60)