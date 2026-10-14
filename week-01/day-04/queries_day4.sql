-- W1D4: SQL Subqueries & CTEs
-- Database: sales table
-- Columns: sale_id, sale_date, region, category, qty, unit_price, discount_pct

-- Query 1: Non-correlated subquery
-- Find sales whose net amount is above the average sale amount.
SELECT sale_id, sale_date, region,
       qty * unit_price * (1 - discount_pct / 100.0) AS net_sale
FROM sales
WHERE qty * unit_price * (1 - discount_pct / 100.0) >
      (SELECT AVG(qty * unit_price * (1 - discount_pct / 100.0))
       FROM sales);

-- Query 2: Correlated subquery
-- Find the highest-value sale in each region.
SELECT s.sale_id, s.sale_date, s.region,
       s.qty * s.unit_price * (1 - s.discount_pct / 100.0) AS net_sale
FROM sales s
WHERE s.qty * s.unit_price * (1 - s.discount_pct / 100.0) =
      (SELECT MAX(t.qty * t.unit_price * (1 - t.discount_pct / 100.0))
       FROM sales t
       WHERE t.region = s.region);

-- Query 3: Rewrite a nested subquery using a CTE.
WITH sale_amounts AS (
    SELECT sale_id, sale_date, region,
           qty * unit_price * (1 - discount_pct / 100.0) AS net_sale
    FROM sales
)
SELECT *
FROM sale_amounts
WHERE net_sale > (SELECT AVG(net_sale) FROM sale_amounts);

-- Query 4: Chain two CTEs.
WITH sale_amounts AS (
    SELECT sale_id, sale_date, region, category, qty,
           qty * unit_price * (1 - discount_pct / 100.0) AS net_sale
    FROM sales
),
region_totals AS (
    SELECT region, SUM(net_sale) AS total_revenue,
           SUM(qty) AS units_sold
    FROM sale_amounts
    GROUP BY region
)
SELECT region, total_revenue, units_sold
FROM region_totals
ORDER BY total_revenue DESC;