from pathlib import Path
import time
import polars as pl

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
EVIDENCE = BASE / "evidence"

source = DATA / "superstore.csv"
utf8_file = DATA / "superstore_utf8.csv"

# Convert Windows-1252 CSV to UTF-8 for lazy scanning
utf8_file.write_text(
    source.read_bytes().decode("cp1252").replace("\r\n", "\n"),
    encoding="utf-8"
)

# Lazy CSV loading
lf = pl.scan_csv(utf8_file, infer_schema_length=10000)

print("Polars LazyFrame created.")
print("Dataset rows:", lf.select(pl.len()).collect().item())

queries = {
    "01_sales_profit": lf.select(
        pl.col("Sales").sum().alias("Total Sales"),
        pl.col("Profit").sum().alias("Total Profit")
    ),

    "02_category_sales": lf.group_by("Category").agg(
        pl.col("Sales").sum().alias("Total Sales")
    ).sort("Total Sales", descending=True),

    "03_region_profit": lf.group_by("Region").agg(
        pl.col("Profit").sum().alias("Total Profit")
    ).sort("Total Profit", descending=True),

    "04_top_products": lf.group_by("Product Name").agg(
        pl.col("Sales").sum().alias("Total Sales")
    ).sort("Total Sales", descending=True).head(5),

    "05_discount_analysis": (
        lf.with_columns(
            pl.when(pl.col("Discount") >= 0.2)
            .then(pl.lit("High"))
            .otherwise(pl.lit("Low"))
            .alias("Discount Level")
        )
        .group_by("Discount Level")
        .agg(
            pl.len().alias("Order Count"),
            pl.col("Sales").mean().alias("Average Sales"),
            pl.col("Profit").mean().alias("Average Profit")
        )
        .sort("Discount Level")
    )
}

start = time.perf_counter()

for name, query in queries.items():
    result = query.collect()
    result.write_csv(EVIDENCE / f"{name}.csv")
    print(f"\n{name}")
    print(result)

elapsed = time.perf_counter() - start

# Save query optimization plan
plan = queries["05_discount_analysis"].explain()
(EVIDENCE / "lazy_query_plan.txt").write_text(plan, encoding="utf-8")

# Save execution evidence
evidence = f"""
W5D4 - Polars High-Performance Operations

Polars version: {pl.__version__}
Dataset rows: {lf.select(pl.len()).collect().item()}
Dataset columns: {len(pl.read_csv(utf8_file, n_rows=1).columns)}

Operations completed:
1. Total sales and profit
2. Sales grouped by category
3. Profit grouped by region
4. Top 5 products by sales
5. Discount classification and aggregation

Features used:
- LazyFrame and scan_csv
- Expressions and filtering logic
- Grouping and aggregation
- Sorting and top-N
- Query optimization plan

Total execution time for five queries: {elapsed:.6f} seconds
"""

(EVIDENCE / "execution_evidence.txt").write_text(
    evidence, encoding="utf-8"
)

print("\nSUCCESS: All five Polars operations completed.")
print("Execution time:", round(elapsed, 6), "seconds")

