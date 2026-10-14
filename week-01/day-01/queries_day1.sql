
-- Cynaris W1D1: SQL Fundamentals
-- Dataset: Synthetic sales data in data/sales.db

-- 1. Display all sales records
SELECT * FROM sales;

-- 2. Select specific columns
SELECT customer_name, product, amount
FROM sales;

-- 3. WHERE with AND
SELECT * FROM sales
WHERE region = 'South' AND amount > 5000;

-- 4. WHERE with OR
SELECT * FROM sales
WHERE region = 'North' OR region = 'East';

-- 5. WHERE with NOT
SELECT * FROM sales
WHERE NOT category = 'Furniture';

-- 6. LIKE: find products containing "book"
SELECT * FROM sales
WHERE product LIKE '%book%';

-- 7. IN: select multiple regions
SELECT * FROM sales
WHERE region IN ('South', 'East');

-- 8. BETWEEN: filter amounts from 2000 to 18000
SELECT * FROM sales
WHERE amount BETWEEN 2000 AND 18000;

-- 9. IS NULL: find missing discounts
SELECT * FROM sales
WHERE discount IS NULL;

-- 10. Comparison operators: sales above 10000
SELECT customer_name, product, amount
FROM sales
WHERE amount >= 10000;
