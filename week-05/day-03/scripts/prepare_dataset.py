import pandas as pd
from pathlib import Path

source = Path("week-04/day-05/data/Sample - Superstore.csv")
output = Path("week-05/day-03/data/superstore_100k.csv")

df = pd.read_csv(source, encoding="cp1252")
repeats = (100000 // len(df)) + 1
large_df = pd.concat([df] * repeats, ignore_index=True).head(100000)

if "Row ID" in large_df.columns:
    large_df["Row ID"] = range(1, 100001)

large_df.to_csv(output, index=False)

print("Rows:", len(large_df))
print("Columns:", len(large_df.columns))
print("Saved:", output)
