import sqlite3
from pathlib import Path

db_path = Path("data/aggregations.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(db_path)

conn.execute("DROP TABLE IF EXISTS sales")

conn.execute("""
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    sale_date TEXT,
    region TEXT,
    category TEXT,
    qty INTEGER,
    unit_price REAL,
    discount_pct REAL
)
""")

sales_data = [
    (1, "2026-09-01", "South", "Electronics", 2, 1000, 5),
    (2, "2026-09-02", "North", "Clothing", 3, 500, 0),
    (3, "2026-09-05", "South", "Clothing", 1, 800, 10),
    (4, "2026-09-10", "West", "Electronics", 1, 2000, 5),
    (5, "2026-10-01", "North", "Grocery", 5, 100, 0),
    (6, "2026-10-03", "South", "Grocery", 4, 150, 0),
    (7, "2026-10-05", "West", "Clothing", 2, 600, 10),
    (8, "2026-10-08", "North", "Electronics", 1, 1500, 5),
    (9, "2026-10-10", "East", "Grocery", 10, 50, 0),
    (10, "2026-10-12", "East", "Clothing", 2, 700, 5),
]

conn.executemany("""
INSERT INTO sales
(sale_id, sale_date, region, category, qty, unit_price, discount_pct)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", sales_data)

conn.commit()
print("Database created: data/sales.db")
print("Sales records inserted:", conn.execute(
    "SELECT COUNT(*) FROM sales"
).fetchone()[0])

conn.close()