import pandas as pd
from pathlib import Path

DATA_PATH = Path("week-05/day-01/data/superstore.csv")
ERROR_LOG = Path("week-05/day-01/evidence/failed_queries.log")

df = pd.read_csv(DATA_PATH, encoding="cp1252")

print(f"Dataset loaded: {len(df)} rows, {len(df.columns)} columns")
print("PandasAI is installed and ready.")

# PandasAI natural-language queries require a configured LLM API key.
# The query workflow will be added after the LLM is configured.
