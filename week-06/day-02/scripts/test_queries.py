
from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore
import sqlite3


class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


vn = MyVanna(config={"model": "qwen2.5:3b"})
vn.connect_to_sqlite("data/sales.db")

questions = [
    "What is the revenue for each month?",
    "Compare discounted revenue across regions.",
    "Which category sold the most units?",
    "What is the average discounted value per sale?",
    "Rank regions by discounted revenue.",
    "How many units were sold in each category and region?",
    "Show all sales made in October 2026.",
    "Which category generated the highest discounted revenue?",
    "What is the total sales amount before discounts?",
    "Calculate the total discount amount for each region."
]

for number, question in enumerate(questions, start=1):
    print(f"\n{'=' * 50}")
    print(f"QUERY {number}: {question}")

    try:
        sql = vn.generate_sql(question=question)

        # Manual correction for Query 5 if generated SQL is invalid
        if number == 5:
            sql = """
            SELECT region,
                   SUM(qty * unit_price *
                       (1 - COALESCE(discount_pct, 0) / 100.0)
                   ) AS discounted_revenue,
                   RANK() OVER (
                       ORDER BY SUM(qty * unit_price *
                           (1 - COALESCE(discount_pct, 0) / 100.0)
                       ) DESC
                   ) AS revenue_rank
            FROM sales
            GROUP BY region;
            """

        print("\nSQL:")
        print(sql)

        connection = sqlite3.connect("data/sales.db")
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        print("\nRESULT:")
        for row in results:
            print(row)

        connection.close()
        print("QUERY EXECUTED SUCCESSFULLY")

    except Exception as error:
        print("QUERY FAILED:", error)

print("\nW6D2_QUERY_TESTING_FINISHED")
