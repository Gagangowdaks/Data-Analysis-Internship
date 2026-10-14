import sqlite3
from pathlib import Path

folder = Path(__file__).parent
database = folder / "data" / "sales.db"
sql_file = folder / "queries_day1.sql"

sql_text = sql_file.read_text(encoding="utf-8")

# Remove SQL comment lines
lines = [
    line for line in sql_text.splitlines()
    if not line.strip().startswith("--")
]
clean_sql = "\n".join(lines)

queries = [
    query.strip()
    for query in clean_sql.split(";")
    if query.strip()
]

with sqlite3.connect(database) as connection:
    for number, query in enumerate(queries, start=1):
        cursor = connection.execute(query)
        rows = cursor.fetchall()
        print(f"Query {number}: PASS — {len(rows)} rows returned")

print(f"Total queries verified: {len(queries)}")
