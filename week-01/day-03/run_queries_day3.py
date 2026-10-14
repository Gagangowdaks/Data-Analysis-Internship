import sqlite3
from pathlib import Path

db_path = Path("data/sales.db")
sql_path = Path("week-01/day-03/queries_day3.sql")

conn = sqlite3.connect(db_path)
sql_text = sql_path.read_text(encoding="utf-8")

# Split the SQL file into individual statements.
statements = [
    statement.strip()
    for statement in sql_text.split(";")
    if statement.strip()
]

passed = 0

for number, statement in enumerate(statements, start=1):
    try:
        cursor = conn.execute(statement)
        rows = cursor.fetchall()

        print(f"\nQuery {number}: PASS — {len(rows)} rows returned")
        for row in rows[:5]:
            print(" ", row)

        passed += 1

    except sqlite3.Error as error:
        print(f"\nQuery {number}: FAIL — {error}")

conn.close()
print(f"\nTotal queries verified: {passed}/{len(statements)}")