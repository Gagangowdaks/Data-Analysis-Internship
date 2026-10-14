import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "data" / "joins.db"
db_path.parent.mkdir(parents=True, exist_ok=True)

with sqlite3.connect(db_path) as con:
    con.executescript("""
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS customers;
    DROP TABLE IF EXISTS employees;

    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        city TEXT
    );

    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount REAL NOT NULL
    );

    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        manager_id INTEGER
    );

    INSERT INTO customers VALUES
        (1, 'Asha', 'Bengaluru'),
        (2, 'Rahul', 'Chennai'),
        (3, 'Priya', 'Hyderabad'),
        (4, 'Arun', 'Mumbai');

    INSERT INTO orders VALUES
        (101, 1, 2500),
        (102, 1, 1500),
        (103, 2, 4000),
        (104, 4, 3000),
        (105, 99, 1200);

    INSERT INTO employees VALUES
        (1, 'Meera', NULL),
        (2, 'Kiran', 1),
        (3, 'Divya', 1),
        (4, 'Ravi', 2);
    """)

print(f"Database created: {db_path}")
print("Tables created: customers, orders, employees")
