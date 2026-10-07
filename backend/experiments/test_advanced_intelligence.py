from pathlib import Path

from app.services.document_service import (
    extract_text,
    clean_text
)

from app.services.advanced_resume_intelligence import (
    analyze_advanced_resume_intelligence
)


# =========================================================
# CONFIGURATION
# =========================================================

BASE_DIR = Path(
    __file__
).resolve().parents[2]

UPLOAD_DIR = BASE_DIR / "uploads"

RESUME_ID = "res_32a15717"


# =========================================================
# FIND RESUME
# =========================================================

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


# =========================================================
# EXTRACT TEXT
# =========================================================

text = extract_text(
    file_path
)

text = clean_text(
    text
)


# =========================================================
# ANALYZE
# =========================================================

result = analyze_advanced_resume_intelligence(
    text
)


# =========================================================
# OUTPUT
# =========================================================

print("=" * 60)
print("PHASE 11 - ADVANCED RESUME INTELLIGENCE")
print("=" * 60)


print("\nCONTACT ANALYSIS")
print(
    result["contact_analysis"]
)


print("\nEXPERIENCE ANALYSIS")
print(
    result["experience_analysis"]
)


print("\nACHIEVEMENT ANALYSIS")
print(
    result["achievement_analysis"]
)


print("\nSKILL ANALYSIS")
print(
    result["skill_analysis"]
)


print("\nEDUCATION ANALYSIS")
print(
    result["education_analysis"]
)


print("\nPROJECT ANALYSIS")
print(
    result["project_analysis"]
)


print("\nSTRUCTURE ANALYSIS")
print(
    result["structure_analysis"]
)


print("\nQUALITY FLAGS")

for flag in result[
    "quality_flags"
]:

    print(
        "-",
        flag
    )


print("\nSTRENGTHS")

for strength in result[
    "strengths"
]:

    print(
        "-",
        strength
    )


print("\nADVANCED IMPROVEMENTS")

for improvement in result[
    "advanced_improvements"
]:

    print(
        "-",
        improvement
    )


print("\n" + "=" * 60)
print("TEST PASSED")
print("=" * 60)