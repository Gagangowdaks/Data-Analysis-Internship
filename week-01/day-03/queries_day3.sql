-- W1D3: SQL Aggregations — GROUP BY & HAVING
-- Sample schema: sale_id, sale_date, region, category,
--                 qty, unit_price, discount_pct
-- Net sale amount = qty * unit_price * (1 - discount_pct / 100.0)

-- Query 1: Count transactions
SELECT COUNT(*) AS total_transactions
FROM sales;

-- Query 2: Calculate gross revenue
SELECT SUM(qty * unit_price) AS gross_revenue
FROM sales;

-- Query 3: Calculate net revenue
SELECT SUM(qty * unit_price * (1 - discount_pct / 100.0)) AS net_revenue
FROM sales;

-- Query 4: Calculate average transaction value
SELECT AVG(qty * unit_price * (1 - discount_pct / 100.0)) AS average_order_value
FROM sales;

-- Query 5: Find minimum and maximum transaction amounts
SELECT
    MIN(qty * unit_price * (1 - discount_pct / 100.0)) AS minimum_sale,
    MAX(qty * unit_price * (1 - discount_pct / 100.0)) AS maximum_sale
FROM sales;

-- Query 6: Summarise revenue by region
SELECT
    region,
    SUM(qty * unit_price * (1 - discount_pct / 100.0)) AS net_revenue
FROM sales
GROUP BY region;

-- Query 7: Summarise units sold by category
SELECT
    category,
    SUM(qty) AS units_sold
FROM sales
GROUP BY category;

-- Query 8: Calculate monthly revenue and filter using HAVING
SELECT
    strftime('%Y-%m', sale_date) AS sales_month,
    SUM(qty * unit_price * (1 - discount_pct / 100.0)) AS monthly_revenue
FROM sales
GROUP BY strftime('%Y-%m', sale_date)
HAVING SUM(qty * unit_price * (1 - discount_pct / 100.0)) > 0;

-- Window function: Calculate running revenue by region
SELECT
    sale_id,
    sale_date,
    region,
    qty * unit_price * (1 - discount_pct / 100.0) AS net_sale,
    SUM(qty * unit_price * (1 - discount_pct / 100.0))
        OVER (
            PARTITION BY region
            ORDER BY sale_date, sale_id
        ) AS running_revenue
FROM sales;
