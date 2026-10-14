-- Cynaris W1D2: SQL Joins
-- Database: data/joins.db

-- 1. INNER JOIN: only customers with matching orders
SELECT c.customer_name, o.order_id, o.amount
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY c.customer_id, o.order_id;

-- 2. LEFT JOIN: all customers, including those without orders
SELECT c.customer_name, o.order_id, o.amount
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY c.customer_id, o.order_id;

-- 3. RIGHT JOIN: all orders, including orders without a matching customer
SELECT c.customer_name, o.order_id, o.amount
FROM customers AS c
RIGHT JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY o.order_id;

-- 4. FULL OUTER JOIN: all customers and all orders
SELECT c.customer_name, o.order_id, o.amount
FROM customers AS c
FULL OUTER JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY o.order_id;

-- 5. Duplicate rows: one customer can have multiple orders.
-- This returns one row per customer with orders, not one row per customer.
SELECT c.customer_id, c.customer_name, o.order_id
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY c.customer_id, o.order_id;

-- Fix: aggregate orders first to get one row per customer.
SELECT c.customer_id, c.customer_name,
       COALESCE(t.total_amount, 0) AS total_amount
FROM customers AS c
LEFT JOIN (
    SELECT customer_id, SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
) AS t
    ON c.customer_id = t.customer_id
ORDER BY c.customer_id;

-- 6. SELF JOIN: show each employee and their manager.
SELECT e.employee_name AS employee,
       m.employee_name AS manager
FROM employees AS e
LEFT JOIN employees AS m
    ON e.manager_id = m.employee_id
ORDER BY e.employee_id;
