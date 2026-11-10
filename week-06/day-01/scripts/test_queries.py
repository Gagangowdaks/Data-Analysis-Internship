from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore

class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

vn = MyVanna(config={"model": "qwen2.5:3b"})
vn.connect_to_sqlite("data/sales.db")

questions = [
    "Show all sales",
    "How many sales records are there?",
    "What is the total quantity sold?",
    "Show the number of sales in each region",
    "Calculate total revenue by category",
    "Which region has the highest number of sales?",
    "Show average unit price by category",
    "Find the highest unit price",
    "Show total quantity sold by region",
    "List sales where the discount is greater than 5 percent"
]

for i, question in enumerate(questions, 1):
    print(f"\nQUESTION {i}: {question}")
    try:
        sql = vn.generate_sql(question=question)
        print("GENERATED SQL:", sql)
        if sql and "SELECT" in sql.upper():
            result = vn.run_sql(sql)
            print("RESULT:")
            print(result)
        else:
            print("SQL NOT GENERATED")
    except Exception as error:
        print("ERROR:", error)

print("\n10_QUERY_TEST_COMPLETED")
