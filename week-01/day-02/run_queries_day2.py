import sqlite3
from pathlib import Path

folder = Path(__file__).parent
db_path = folder / "data" / "joins.db"
sql_path = folder / "queries_day2.sql"

def remove_comments(statement):
    return "\n".join(
        line for line in statement.splitlines()
        if not line.strip().startswith("--")
    ).strip()

with sqlite3.connect(db_path) as con:
    sql_text = sql_path.read_text(encoding="utf-8-sig")
    statements = [
        remove_comments(part)
        for part in sql_text.split(";")
        if remove_comments(part)
    ]

    passed = 0
    for number, statement in enumerate(statements, start=1):
        try:
            cursor = con.execute(statement)
            rows = cursor.fetchall()
            print(f"Query {number}: PASS - {len(rows)} rows returned")
            passed += 1
        except sqlite3.Error as error:
            print(f"Query {number}: FAIL - {error}")
            raise

print(f"\nTotal queries verified: {passed}/{len(statements)}")
