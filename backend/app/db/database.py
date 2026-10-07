import sqlite3
from pathlib import Path


# =========================================================
# DATABASE LOCATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DATABASE_PATH = DATA_DIR / "smart_resume_validator.db"


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_connection():
    """
    Create a connection to the SQLite database.
    """

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


# =========================================================
# INITIAL TABLE
# =========================================================

def create_resumes_table(connection):
    """
    Create the resumes table if it does not exist.
    """

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_id TEXT UNIQUE NOT NULL,

            original_filename TEXT NOT NULL,

            saved_filename TEXT NOT NULL,

            file_type TEXT NOT NULL,

            file_path TEXT NOT NULL,

            extracted_text TEXT,

            is_resume INTEGER,

            validation_confidence INTEGER,

            validation_reasons TEXT,

            score INTEGER,

            score_breakdown TEXT,

            rule_based_improvements TEXT,

            recommendations TEXT,

            ai_analysis TEXT,

            career_analysis TEXT,

            career_recommendations TEXT,

            job_description TEXT,

            job_match_analysis TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


# =========================================================
# DATABASE MIGRATION
# =========================================================

def migrate_resumes_table(connection):
    """
    Add missing columns to an existing resumes table.

    This allows older databases to work with the
    current application schema.
    """

    cursor = connection.execute(
        "PRAGMA table_info(resumes)"
    )

    existing_columns = {
        row["name"]
        for row in cursor.fetchall()
    }

    required_columns = {
        "saved_filename": "TEXT",
        "file_type": "TEXT",
        "file_path": "TEXT",
        "extracted_text": "TEXT",
        "is_resume": "INTEGER",
        "validation_confidence": "INTEGER",
        "validation_reasons": "TEXT",
        "score": "INTEGER",
        "score_breakdown": "TEXT",
        "rule_based_improvements": "TEXT",
        "recommendations": "TEXT",
        "ai_analysis": "TEXT",
        "career_analysis": "TEXT",
        "career_recommendations": "TEXT",
        "job_description": "TEXT",
        "job_match_analysis": "TEXT",
        "created_at": "TIMESTAMP",
        "updated_at": "TIMESTAMP"
    }

    for column_name, column_type in required_columns.items():

        if column_name not in existing_columns:

            print(
                f"Adding missing database column: {column_name}"
            )

            connection.execute(
                f"""
                ALTER TABLE resumes
                ADD COLUMN {column_name} {column_type}
                """
            )


# =========================================================
# DATABASE INITIALIZATION
# =========================================================

def initialize_database():
    """
    Create and migrate the SQLite database.
    """

    connection = get_connection()

    try:

        # Create table if needed
        create_resumes_table(
            connection
        )

        # Add any columns missing from older versions
        migrate_resumes_table(
            connection
        )

        connection.commit()

        print(
            "Database initialized successfully."
        )

    finally:

        connection.close()


# =========================================================
# UPDATE TIMESTAMP
# =========================================================

def update_timestamp(
    connection,
    resume_id: str
):
    """
    Update the modification timestamp.
    """

    connection.execute(
        """
        UPDATE resumes
        SET updated_at = CURRENT_TIMESTAMP
        WHERE resume_id = ?
        """,
        (resume_id,)
    )


# =========================================================
# DIRECT EXECUTION
# =========================================================

if __name__ == "__main__":

    initialize_database()

    print(
        f"Database location: {DATABASE_PATH}"
    )