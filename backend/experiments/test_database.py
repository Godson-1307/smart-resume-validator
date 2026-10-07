from app.db.database import (
    initialize_database,
    DATABASE_PATH,
    get_connection
)


print("=" * 60)
print("PHASE 9 DATABASE TEST")
print("=" * 60)


initialize_database()

print(
    "Database:",
    DATABASE_PATH
)


connection = get_connection()

cursor = connection.cursor()


cursor.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name='resumes'
    """
)

table = cursor.fetchone()


if table:

    print(
        "resumes table: FOUND"
    )

else:

    print(
        "resumes table: NOT FOUND"
    )


cursor.execute(
    "PRAGMA table_info(resumes)"
)

columns = cursor.fetchall()


print(
    "\nColumns:"
)

for column in columns:

    print(
        "-",
        column["name"]
    )


connection.close()


if table and columns:

    print(
        "\nTEST PASSED"
    )

else:

    print(
        "\nTEST FAILED"
    )


print("=" * 60)