# Cynaris W1D2 — CIA Interactions

## Interaction 1: LEFT JOIN vs INNER JOIN

**Question asked:**
Explain the difference between LEFT JOIN and INNER JOIN with a business reporting example.

**Key learnings:**
- INNER JOIN returns only rows with matching records in both tables.
- LEFT JOIN returns every row from the left table, even if there is no match in the right table.
- Example: INNER JOIN can report customers who placed orders.
- Example: LEFT JOIN can report all customers, including customers who have never ordered.
- LEFT JOIN is useful when a report must include records with no matching activity.

## Interaction 2: JOIN Order and Query Performance

**Research question:**
How does JOIN order affect SQL query performance?

**Key learnings:**
- JOIN performance depends on table sizes, indexes, join conditions, and the database query optimizer.
- Joining on suitable indexed columns can improve performance.
- Filter unnecessary rows early when appropriate.
- Avoid joining tables on incorrect keys because this can create unexpected duplicate rows.
- Use EXPLAIN or the database query plan to understand how a query runs.

**Status:** Notes prepared. Confirm that the questions were submitted to CIA and review its responses before marking the interactions complete.
