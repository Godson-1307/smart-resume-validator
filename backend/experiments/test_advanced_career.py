from pathlib import Path

from app.services.document_service import (
    extract_text,
    clean_text
)

from app.services.advanced_career_service import (
    generate_advanced_career_recommendations
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
# OPTIONAL JOB DESCRIPTION
# =========================================================

job_description = """
Machine Learning Engineer Intern

We are looking for candidates with Python,
machine learning, deep learning, PyTorch,
scikit-learn, Pandas, NumPy and SQL.

Experience with Git, Docker and cloud computing
is preferred.

Responsibilities include developing machine
learning solutions, testing models, analyzing
datasets and documenting project results.
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
# EXTRACT TEXT
# =========================================================

resume_text = extract_text(
    file_path
)

resume_text = clean_text(
    resume_text
)


# =========================================================
# GENERATE RECOMMENDATIONS
# =========================================================

result = generate_advanced_career_recommendations(
    resume_text=resume_text,
    target_role="Machine Learning Engineer",
    expected_package="10 LPA",
    industry="AI / Technology",
    experience_level="Fresher",
    job_description=job_description
)


# =========================================================
# OUTPUT
# =========================================================

print("=" * 60)
print("PHASE 13 - ADVANCED CAREER RECOMMENDATIONS")
print("=" * 60)


print(
    "\nGoal:"
)

print(
    result["goal"]
)


print(
    "\nMatched role:",
    result["matched_role"]
)


print(
    "\nCurrent skills:"
)

print(
    result["current_skills"]
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
    "\nSkill coverage:",
    result["skill_coverage_percentage"],
    "%"
)


print(
    "\nLearning priorities:"
)

for item in result[
    "learning_priorities"
]:

    print(
        "-",
        item["skill"],
        "|",
        item["priority"]
    )


print(
    "\nRecommended projects:"
)

for project in result[
    "recommended_projects"
]:

    print(
        "-",
        project
    )


print(
    "\nProfile actions:"
)

for action in result[
    "profile_actions"
]:

    print(
        "-",
        action
    )


print(
    "\nRelated roles:"
)

for role in result[
    "related_roles"
]:

    print(
        "-",
        role["role"],
        "|",
        role["skill_overlap_percentage"],
        "%"
    )


if result["job_match"]:

    print(
        "\nJob description match:",
        result["job_match"][
            "overall_match_percentage"
        ],
        "%"
    )

print(
    "\n" + "=" * 60
)

print(
    "TEST PASSED"
)

print("=" * 60)