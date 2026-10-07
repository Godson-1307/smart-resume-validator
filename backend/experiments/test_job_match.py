from pathlib import Path

from app.services.document_service import (
    extract_text,
    clean_text
)

from app.services.job_match_service import (
    match_resume_to_job
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
# JOB DESCRIPTION
# =========================================================

job_description = """
Machine Learning Engineer Intern

We are looking for a Machine Learning Engineer Intern
with knowledge of Python, machine learning, deep learning,
PyTorch, scikit-learn, pandas, NumPy and SQL.

The candidate should have experience building machine
learning projects and working with data preprocessing.

Knowledge of Git, Docker and cloud computing is preferred.

Good problem solving, communication and teamwork skills
are expected.

Responsibilities include developing machine learning
solutions, testing models, analyzing datasets and
documenting project results.
"""


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
# EXTRACT RESUME
# =========================================================

resume_text = extract_text(
    file_path
)

resume_text = clean_text(
    resume_text
)


# =========================================================
# MATCH
# =========================================================

result = match_resume_to_job(
    resume_text=resume_text,
    job_description=job_description,
    job_title="Machine Learning Engineer Intern",
    company="Example Company"
)


# =========================================================
# OUTPUT
# =========================================================

print("=" * 60)
print("PHASE 12 - JOB DESCRIPTION MATCHING")
print("=" * 60)

print(
    "\nJob title:",
    result["job_title"]
)

print(
    "\nResume skills:"
)

print(
    result["resume_skills"]
)

print(
    "\nJD skills:"
)

print(
    result["job_description_skills"]
)

print(
    "\nMatching skills:"
)

print(
    result["matching_skills"]
)

print(
    "\nMissing skills:"
)

print(
    result["missing_skills"]
)

print(
    "\nAdditional resume skills:"
)

print(
    result["additional_resume_skills"]
)

print(
    "\nSkill match:",
    result["skill_match_percentage"],
    "%"
)

print(
    "\nKeyword match:",
    result["keyword_match_percentage"],
    "%"
)

print(
    "\nOverall match:",
    result["overall_match_percentage"],
    "%"
)

print(
    "\nTailoring suggestions:"
)

for suggestion in result[
    "tailoring_suggestions"
]:

    print(
        "-",
        suggestion
    )


print("\n" + "=" * 60)
print("TEST PASSED")
print("=" * 60)