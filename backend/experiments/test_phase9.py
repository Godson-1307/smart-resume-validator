from app.db.database import (
    initialize_database
)

from app.db.resume_repository import (
    create_resume_record,
    save_extracted_text,
    save_validation_result,
    save_score_result,
    save_ai_analysis,
    save_career_analysis,
    get_resume
)


RESUME_ID = "test_phase9_001"


print("=" * 60)
print("PHASE 9 PERSISTENCE TEST")
print("=" * 60)


# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

initialize_database()

print(
    "Database initialized."
)


# ---------------------------------------------------------
# CREATE RECORD
# ---------------------------------------------------------

try:

    create_resume_record(
        resume_id=RESUME_ID,
        original_filename="test_resume.pdf",
        saved_filename="test_phase9_001.pdf",
        file_type="pdf",
        file_path="uploads/test_phase9_001.pdf"
    )

except Exception:

    print(
        "Test record already exists."
    )


# ---------------------------------------------------------
# SAVE TEXT
# ---------------------------------------------------------

save_extracted_text(
    RESUME_ID,
    "Godson Nadar Python Machine Learning SQL"
)


# ---------------------------------------------------------
# SAVE VALIDATION
# ---------------------------------------------------------

save_validation_result(
    RESUME_ID,
    {
        "is_resume": True,
        "confidence": 90,
        "reasons": [
            "Email detected",
            "Education detected",
            "Skills detected"
        ]
    }
)


# ---------------------------------------------------------
# SAVE SCORE
# ---------------------------------------------------------

score_result = {
    "score": 80,

    "breakdown": {
        "skills": {
            "score": 15,
            "max_score": 15
        }
    },

    "improvements": [
        "Improve project descriptions."
    ]
}

recommendations = [
    {
        "priority": "Medium",
        "area": "Projects",
        "message": (
            "Add measurable project outcomes."
        )
    }
]


save_score_result(
    RESUME_ID,
    score_result,
    recommendations
)


# ---------------------------------------------------------
# SAVE AI ANALYSIS
# ---------------------------------------------------------

save_ai_analysis(
    RESUME_ID,
    {
        "name": "Godson Nadar",
        "skills": [
            "Python",
            "Machine Learning"
        ]
    }
)


# ---------------------------------------------------------
# SAVE CAREER ANALYSIS
# ---------------------------------------------------------

save_career_analysis(
    RESUME_ID,
    {
        "target_role": "Machine Learning Engineer",
        "matching_skills": [
            "Python"
        ],
        "missing_skills": [
            "PyTorch"
        ],
        "coverage_percentage": 50
    }
)


# ---------------------------------------------------------
# RETRIEVE
# ---------------------------------------------------------

resume = get_resume(
    RESUME_ID
)


print(
    "\nRetrieved record:"
)


if resume:

    print(
        "Resume ID:",
        resume["resume_id"]
    )

    print(
        "Score:",
        resume["score"]
    )

    print(
        "Validation:",
        resume["is_resume"]
    )

    print(
        "AI analysis:",
        resume["ai_analysis"]
    )

    print(
        "Career analysis:",
        resume["career_analysis"]
    )


# ---------------------------------------------------------
# RESULT
# ---------------------------------------------------------

if (
    resume
    and resume["resume_id"] == RESUME_ID
    and resume["score"] == 80
    and resume["is_resume"] == 1
    and resume["ai_analysis"] is not None
    and resume["career_analysis"] is not None
):

    print(
        "\nTEST PASSED"
    )

else:

    print(
        "\nTEST FAILED"
    )


print("=" * 60)