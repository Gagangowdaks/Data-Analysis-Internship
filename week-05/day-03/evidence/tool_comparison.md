# Pandas vs DuckDB vs Polars

| Criteria | Pandas | DuckDB | Polars |
|---|---|---|---|
| Query syntax | Python DataFrame methods | SQL queries | Python DataFrame expressions |
| Performance | Moderate | Fast | Fastest in this benchmark |
| Data handling | Loads data into memory | Queries CSV and database files directly | Efficient DataFrame processing |
| Best use | Data cleaning and analysis | SQL analytics on large files | Fast data transformations |
| Ease of use | Easy for Python users | Easy for SQL users | Requires learning Polars expressions |

## Benchmark Results

Dataset: 100,000 rows and 21 columns.

| Tool | Load Time (seconds) | Five Queries (seconds) | Total (seconds) |
|---|---:|---:|---:|
| Pandas | 0.415623 | 0.042943 | 0.458565 |
| DuckDB | 0.311626 | 0.038533 | 0.350159 |
| Polars | 0.047131 | 0.025588 | 0.072720 |

## Conclusion

Polars was the fastest in this benchmark, followed by DuckDB and Pandas. DuckDB is useful for SQL-based analytics directly on large files. Pandas is suitable for general data analysis and cleaning. Polars is useful for fast data processing and transformations.

## Dataset Note

The 100,000-row CSV was created by repeating records from the Sample Superstore dataset. It contains repeated records and does not represent 100,000 unique transactions. Timings are from one run on the local machine.
