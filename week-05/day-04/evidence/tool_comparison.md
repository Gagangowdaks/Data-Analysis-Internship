# W5D4: Polars High-Performance DataFrame Operations

## Tools Comparison

| Criteria | Pandas | DuckDB | Polars |
|---|---|---|---|
| Processing | Eager | SQL-based | Eager and Lazy |
| Query syntax | Python methods | SQL | Expressions |
| Performance | Good | Excellent for SQL analytics | Excellent for DataFrame operations |
| Optimization | Limited automatic query optimization | Query optimizer | Lazy query optimizer |
| Best use | General data analysis | SQL analytics on large datasets | Fast DataFrame transformations |

## Polars Features Practiced

1. Lazy CSV scanning using scan_csv().
2. Expressions using when(), then() and otherwise().
3. Grouping and aggregation.
4. Sorting and top-five product analysis.
5. Query optimization using explain().

## Results

- Dataset: 9,994 rows and 21 columns.
- Total Sales: $2,297,200 approximately.
- Total Profit: $286,397.02.
- Highest category sales: Technology.
- Highest regional profit: West.
- Five-query execution time: 0.230548 seconds.

## Conclusion

Polars provides efficient DataFrame operations and lazy query optimization.
It is useful for fast data transformations and analytical workflows.
