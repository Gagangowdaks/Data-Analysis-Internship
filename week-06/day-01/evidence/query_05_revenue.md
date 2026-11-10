# Vanna NL-to-SQL Test Evidence

Model: qwen2.5:3b
Database: data/sales.db
Table: sales

## Query 5: Calculate total revenue by category

Status: PASS

Generated SQL:
SELECT category,
       SUM(qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)) AS total_revenue
FROM sales
GROUP BY category;

Verified results:
- Clothing: 4630.00
- Electronics: 5225.00
- Grocery: 1600.00

Manual verification: The discount percentage is stored as a whole number, so it must be divided by 100.
