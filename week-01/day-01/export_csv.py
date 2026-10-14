import sqlite3
import csv
from pathlib import Path

folder = Path(__file__).parent
database = folder / "data" / "sales.db"
output_file = folder / "exports" / "high_value_sales.csv"

query = """
SELECT customer_name, product, amount, region
FROM sales
WHERE amount >= 10000
ORDER BY amount DESC
"""

with sqlite3.connect(database) as connection:
    cursor = connection.execute(query)
    rows = cursor.fetchall()
    headers = [column[0] for column in cursor.description]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"CSV exported successfully: {output_file}")
print(f"Rows exported: {len(rows)}")
