from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore

class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

vn = MyVanna(config={"model": "qwen2.5:3b"})
vn.connect_to_sqlite("data/sales.db")

result = vn.run_sql("SELECT COUNT(*) AS total_rows FROM sales")
print(result)
print("VANNA_SQLITE_CONNECTION_SUCCESS")
