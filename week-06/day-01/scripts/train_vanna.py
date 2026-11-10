from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore

class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

vn = MyVanna(config={"model": "qwen2.5:3b"})
vn.connect_to_sqlite("data/sales.db")
vn.train(documentation="discount_pct stores whole percentage values: 5.0 means 5 percent. Divide by 100 when calculating discounted amounts.")

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
    ("Calculate total revenue by category", "SELECT category, SUM(qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)) AS total_revenue FROM sales GROUP BY category;"),
    ("Show all sales", "SELECT * FROM sales;"),
    ("Count total sales", "SELECT COUNT(*) AS total_sales FROM sales;"),
    ("Show sales by region", "SELECT region, COUNT(*) AS sales_count FROM sales GROUP BY region;"),
    ("Calculate total quantity sold", "SELECT SUM(qty) AS total_quantity FROM sales;"),
    ("Find total sales amount by category", "SELECT category, SUM(qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)) AS total_amount FROM sales GROUP BY category;")
]

for question, sql in examples:
    vn.train(question=question, sql=sql)
    print("Trained:", question)

print("VANNA_TRAINING_SUCCESS")


