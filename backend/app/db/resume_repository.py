import json

from app.db.database import (
    get_connection,
    update_timestamp
)


# =========================================================
# JSON HELPER
# =========================================================

def serialize(value):
    """
    Convert Python data into JSON text for SQLite storage.
    """

    if value is None:
        return None

    return json.dumps(
        value,
        ensure_ascii=False
    )


def deserialize(value):
    """
    Convert JSON text from SQLite back into Python data.
    """

    if value is None:
        return None

    try:
        return json.loads(value)

    except (
        json.JSONDecodeError,
        TypeError
    ):
        return value


# =========================================================
# CREATE RESUME RECORD
# =========================================================

def create_resume_record(
    resume_id: str,
    original_filename: str,
    saved_filename: str,
    file_type: str,
    file_path: str
):
    """
    Create a new resume record.
    """

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO resumes (
            resume_id,
            original_filename,
            saved_filename,
            file_type,
            file_path
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            resume_id,
            original_filename,
            saved_filename,
            file_type,
            file_path
        )
    )

    connection.commit()

    connection.close()


# =========================================================
# SAVE EXTRACTED TEXT
# =========================================================

def save_extracted_text(
    resume_id: str,
    extracted_text: str
):
    """
    Save extracted resume text.
    """

    connection = get_connection()

    connection.execute(
        """
        UPDATE resumes
        SET extracted_text = ?
        WHERE resume_id = ?
        """,
        (
            extracted_text,
            resume_id
        )
    )

    update_timestamp(
        connection,
        resume_id
    )

    connection.commit()

    connection.close()


# =========================================================
# SAVE VALIDATION
# =========================================================

def save_validation_result(
    resume_id: str,
    validation: dict
):
    """
    Save resume validation result.
    """

    connection = get_connection()

    connection.execute(
        """
        UPDATE resumes
        SET
            is_resume = ?,
            validation_confidence = ?,
            validation_reasons = ?
        WHERE resume_id = ?
        """,
        (
            int(
                validation.get(
                    "is_resume",
                    False
                )
            ),

            validation.get(
                "confidence",
                0
            ),

            serialize(
                validation.get(
                    "reasons",
                    []
                )
            ),

            resume_id
        )
    )

    update_timestamp(
        connection,
        resume_id
    )

    connection.commit()

    connection.close()


# =========================================================
# SAVE SCORE
# =========================================================

def save_score_result(
    resume_id: str,
    score_result: dict,
    recommendations: list
):
    """
    Save rule-based score and recommendations.
    """

    connection = get_connection()

    connection.execute(
        """
        UPDATE resumes
        SET
            score = ?,
            score_breakdown = ?,
            rule_based_improvements = ?,
            recommendations = ?
        WHERE resume_id = ?
        """,
        (
            score_result.get(
                "score"
            ),

            serialize(
                score_result.get(
                    "breakdown",
                    {}
                )
            ),

            serialize(
                score_result.get(
                    "improvements",
                    []
                )
            ),

            serialize(
                recommendations
            ),

            resume_id
        )
    )

    update_timestamp(
        connection,
        resume_id
    )

    connection.commit()

    connection.close()


# =========================================================
# SAVE AI ANALYSIS
# =========================================================

def save_ai_analysis(
    resume_id: str,
    ai_analysis: dict
):
    """
    Save Qwen resume extraction result.
    """

    connection = get_connection()

    connection.execute(
        """
        UPDATE resumes
        SET ai_analysis = ?
        WHERE resume_id = ?
        """,
        (
            serialize(
                ai_analysis
            ),
            resume_id
        )
    )

    update_timestamp(
        connection,
        resume_id
    )

    connection.commit()

    connection.close()


# =========================================================
# SAVE CAREER ANALYSIS
# =========================================================

def save_career_analysis(
    resume_id: str,
    career_analysis: dict
):
    """
    Save target-role and career analysis.
    """

    connection = get_connection()

    connection.execute(
        """
        UPDATE resumes
        SET career_analysis = ?
        WHERE resume_id = ?
        """,
        (
            serialize(
                career_analysis
            ),
            resume_id
        )
    )

    update_timestamp(
        connection,
        resume_id
    )

    connection.commit()

    connection.close()


# =========================================================
# GET ONE RESUME
# =========================================================

def get_resume(
    resume_id: str
):
    """
    Retrieve one complete resume record.
    """

    connection = get_connection()

    row = connection.execute(
        """
        SELECT *
        FROM resumes
        WHERE resume_id = ?
        """,
        (resume_id,)
    ).fetchone()

    connection.close()

    if row is None:
        return None

    data = dict(row)

    # Deserialize JSON columns
    for field in [
        "validation_reasons",
        "score_breakdown",
        "rule_based_improvements",
        "recommendations",
        "ai_analysis",
        "career_analysis"
        "career_recommendations",
        "job_match_analysis",
    ]:

        data[field] = deserialize(
            data[field]
        )

    return data


# =========================================================
# GET ALL RESUMES
# =========================================================

def get_all_resumes():
    """
    Return resume history ordered by newest first.
    """

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT
            resume_id,
            original_filename,
            file_type,
            is_resume,
            validation_confidence,
            score,
            created_at,
            updated_at
        FROM resumes
        ORDER BY created_at DESC
        """
    ).fetchall()

    connection.close()

    return [
        dict(row)
        for row in rows
    ]

def save_job_match(
    resume_id: str,
    job_description: str,
    job_match_analysis: dict
):
    """
    Save job description matching results.
    """

    connection = get_connection()

    connection.execute(
        """
        UPDATE resumes
        SET
            job_description = ?,
            job_match_analysis = ?
        WHERE resume_id = ?
        """,
        (
            job_description,
            serialize(
                job_match_analysis
            ),
            resume_id
        )
    )

    update_timestamp(
        connection,
        resume_id
    )

    connection.commit()

    connection.close()

def save_career_recommendations(
    resume_id: str,
    recommendations: dict
):
    """
    Save advanced career recommendations.
    """

    connection = get_connection()

    connection.execute(
        """
        UPDATE resumes
        SET career_recommendations = ?
        WHERE resume_id = ?
        """,
        (
            serialize(
                recommendations
            ),
            resume_id
        )
    )

    update_timestamp(
        connection,
        resume_id
    )

    connection.commit()

    connection.close()    