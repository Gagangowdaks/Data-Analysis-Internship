import pandas as pd
import duckdb
import polars as pl
import math

path = "week-05/day-03/data/superstore_100k.csv"

pdf = pd.read_csv(path)
pandas_totals = pdf[["Sales", "Profit"]].sum()

con = duckdb.connect()
duckdb_totals = con.execute(
    "SELECT SUM(Sales), SUM(Profit) FROM read_csv_auto(?)",
    [path]
).fetchone()

pldf = pl.read_csv(path)
polars_totals = pldf.select(
    pl.col("Sales").sum(),
    pl.col("Profit").sum()
).row(0)

assert len(pdf) == 100000
assert math.isclose(pandas_totals["Sales"], duckdb_totals[0], rel_tol=1e-9)
assert math.isclose(pandas_totals["Profit"], duckdb_totals[1], rel_tol=1e-9)
assert math.isclose(pandas_totals["Sales"], polars_totals[0], rel_tol=1e-9)
assert math.isclose(pandas_totals["Profit"], polars_totals[1], rel_tol=1e-9)

print("PASS: Dataset contains 100,000 rows")
print("PASS: Pandas, DuckDB and Polars totals match")
print("Total Sales:", round(pandas_totals["Sales"], 2))
print("Total Profit:", round(pandas_totals["Profit"], 2))

con.close()
