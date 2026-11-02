import pandas as pd
from pathlib import Path

DATA_PATH = Path("week-05/day-01/data/superstore.csv")
OUTPUT_PATH = Path("week-05/day-01/evidence/manual_comparison.txt")

df = pd.read_csv(DATA_PATH, encoding="cp1252")

results = {
    "Q1: What are total sales?": df["Sales"].sum(),
    "Q2: Which category has the highest sales?": (
        df.groupby("Category")["Sales"].sum().idxmax()
    ),
    "Q3: What is the average profit?": df["Profit"].mean(),
}

with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    for question, answer in results.items():
        file.write(f"{question}\nManual Pandas answer: {answer}\n\n")
        print(f"{question}\nManual Pandas answer: {answer}\n")

print(f"Comparison saved to: {OUTPUT_PATH}")
