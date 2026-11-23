from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore


class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


vn = MyVanna(config={"model": "qwen2.5:3b"})
vn.connect_to_sqlite("data/sales.db")

vn.train(documentation="""
The sales table contains one row per sale.
discount_pct stores whole percentage values.
For example, 5.0 means 5 percent.
Calculate discounted revenue using:
qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0).
""")

vn.train(ddl="""
CREATE TABLE sales (
    sale_id INTEGER,
    sale_date TEXT,
    region TEXT,
    category TEXT,
    qty INTEGER,
    unit_price REAL,
    discount_pct REAL
);
""")

examples = [
    (
        "Show monthly sales revenue",
        """
        SELECT strftime('%Y-%m', sale_date) AS sales_month,
               SUM(qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)) AS revenue
        FROM sales
        GROUP BY strftime('%Y-%m', sale_date)
        ORDER BY sales_month;
        """
    ),
    (
        "Show revenue for each region and category",
        """
        SELECT region, category,
               SUM(qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)) AS revenue
        FROM sales
        GROUP BY region, category
        ORDER BY region, category;
        """
    ),
    (
        "Find total quantity sold by category",
        """
        SELECT category, SUM(qty) AS total_quantity
        FROM sales
        GROUP BY category
        ORDER BY total_quantity DESC;
        """
    ),
    (
        "Calculate average sale value",
        """
        SELECT AVG(qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)) AS average_sale_value
        FROM sales;
        """
    ),
    (
        "Show discounted revenue by region",
        """
        SELECT region,
               SUM(qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)) AS discounted_revenue
        FROM sales
        GROUP BY region
        ORDER BY discounted_revenue DESC;
        """
    )
]

for question, sql in examples:
    vn.train(question=question, sql=sql)
    print("Trained:", question)

print("W6D2_VANNA_TRAINING_SUCCESS")
