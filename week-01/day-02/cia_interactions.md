# Cynaris W1D2 — CIA Interaction Evidence

## Interaction 1: LEFT JOIN vs INNER JOIN

**Question asked:**

Explain the difference between LEFT JOIN and INNER JOIN with a business reporting example.

**Key learnings from the actual CIA response:**

- `INNER JOIN` returns only records that match in both tables.
- `LEFT JOIN` keeps every record from the left table and returns NULL for unmatched right-side records.
- Example: an INNER JOIN can show customers who purchased, while a LEFT JOIN can include customers with zero purchases.
- `COUNT(right_table.id)` does not count NULL values, making it useful for customer-wise sales reports.
- Choose the join based on the business requirement and verify results.
- Join performance depends on the data, query plan, indexes, and database optimizer.

## Interaction 2: JOIN Order and Query Performance

**Research question asked:**

How does JOIN order affect SQL query performance?

**Key learnings from the actual CIA response:**

- Large intermediate result sets can increase processing time and memory usage.
- Filtering data early can reduce the number of rows processed by later joins.
- Suitable indexes on join and filter columns can improve performance.
- Database optimizers choose join orders and algorithms using statistics and estimates.
- Use `EXPLAIN` or `EXPLAIN ANALYZE`, where supported, to inspect query execution.
- Keep database statistics updated and compare query plans before claiming performance improvements.
- A CTE or subquery can make filtering logic clearer, but does not guarantee materialization or a faster query.

## Evidence status

**Status:** Both CIA responses received and reviewed.

**Evidence source:** Actual CIA responses pasted into the ChatGPT conversation on 14 October 2026.

**Related practical work:** W1D2 SQL Joins — 7 of 7 queries passed in the local test.

**Important note:** Performance improvements mentioned in CIA examples are illustrative unless independently measured in our project.
