import sqlite3
import pandas as pd

db_path = "week-01/day-01/data/sales.db"
csv_path = "week-01/day-05/sales_data.csv"

with sqlite3.connect(db_path) as conn:
    df = pd.read_sql_query("SELECT * FROM sales", conn)

df.to_csv(csv_path, index=False)
print(f"Exported {len(df)} rows to {csv_path}")
print(df.head())
