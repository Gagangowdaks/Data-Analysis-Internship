# W6D2 – Vanna Query Verification

## Training
- Vanna connected to the SQLite sales database.
- Trained with 5 custom question-SQL examples.
- Added table schema and discount calculation documentation.

## Query Testing

| No. | Question | Verified result |
|---|---|---|
| 1 | Revenue for each month | September: 6020.0; October: 5435.0 |
| 2 | Discounted revenue by region | North: 3425.0; South: 3220.0; West: 2980.0; East: 1830.0 |
| 3 | Category with most units sold | Grocery: 19 units |
| 4 | Average discounted value per sale | 1145.5 |
| 5 | Rank regions by discounted revenue | North: 1; South: 2; West: 3; East: 4 |
| 6 | Units by category and region | Grouped results returned successfully |
| 7 | October 2026 sales | 6 rows returned |
| 8 | Highest discounted revenue category | Electronics: 5225.0 |
| 9 | Total sales before discounts | 12000.0 |
| 10 | Total discount amount by region | East: 70.0; North: 75.0; South: 180.0; West: 220.0 |

## Verification Notes
- 10 queries were executed.
- 9 queries used valid Vanna-generated SQL.
- Query 5 generated invalid SQL and was manually corrected in the test script before execution.
- All 10 queries ultimately executed successfully.
- Discount calculations use discount_pct / 100.0 because the database stores whole percentage values.

## Evidence
See query_test_output.txt for the execution output.
