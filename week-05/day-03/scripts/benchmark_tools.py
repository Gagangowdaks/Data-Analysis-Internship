import time
import pandas as pd
import duckdb
import polars as pl
from pathlib import Path

DATA = "week-05/day-03/data/superstore_100k.csv"
OUTPUT = Path("week-05/day-03/evidence/benchmark_results.csv")

results = []

# 1. Pandas
start = time.perf_counter()
pdf = pd.read_csv(DATA)
pandas_load = time.perf_counter() - start

start = time.perf_counter()
pandas_results = [
    pdf[["Sales", "Profit"]].sum(),
    pdf.groupby("Category")["Sales"].sum(),
    pdf.groupby("Region")["Profit"].sum(),
    pdf.groupby("Product Name")["Sales"].sum().nlargest(5),
    pdf.groupby("Segment")["Sales"].mean()
]
pandas_query = time.perf_counter() - start

results.append(["Pandas", pandas_load, pandas_query])

# 2. DuckDB
con = duckdb.connect()
start = time.perf_counter()
con.execute(
    "CREATE TABLE sales AS SELECT * FROM read_csv_auto(?)",
    [DATA]
)
duckdb_load = time.perf_counter() - start

queries = [
    "SELECT SUM(Sales), SUM(Profit) FROM sales",
    "SELECT Category, SUM(Sales) FROM sales GROUP BY Category",
    "SELECT Region, SUM(Profit) FROM sales GROUP BY Region",
    "SELECT \"Product Name\", SUM(Sales) AS total_sales FROM sales GROUP BY \"Product Name\" ORDER BY total_sales DESC LIMIT 5",
    "SELECT Segment, AVG(Sales) FROM sales GROUP BY Segment"
]

start = time.perf_counter()
for query in queries:
    con.execute(query).fetchall()
duckdb_query = time.perf_counter() - start

results.append(["DuckDB", duckdb_load, duckdb_query])

# 3. Polars
start = time.perf_counter()
pldf = pl.read_csv(DATA)
polars_load = time.perf_counter() - start

start = time.perf_counter()
polars_results = [
    pldf.select(["Sales", "Profit"]).sum(),
    pldf.group_by("Category").agg(pl.col("Sales").sum()),
    pldf.group_by("Region").agg(pl.col("Profit").sum()),
    pldf.group_by("Product Name").agg(pl.col("Sales").sum().alias("total_sales")).sort("total_sales", descending=True).head(5),
    pldf.group_by("Segment").agg(pl.col("Sales").mean())
]
polars_query = time.perf_counter() - start

results.append(["Polars", polars_load, polars_query])

# Save benchmark
result_df = pd.DataFrame(
    results,
    columns=["Tool", "Load_Time_Seconds", "Five_Queries_Time_Seconds"]
)
result_df["Total_Time_Seconds"] = (
    result_df["Load_Time_Seconds"] + result_df["Five_Queries_Time_Seconds"]
)

result_df.to_csv(OUTPUT, index=False)

print("\nBENCHMARK RESULTS")
print(result_df.to_string(index=False))
print("\nSaved:", OUTPUT)

con.close()
