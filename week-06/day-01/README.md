# Week 6 Day 1 – Vanna Setup: NL to SQL

## Objective
Build a Natural Language to SQL workflow using Vanna, Ollama, and SQLite.

## Environment
- Python 3.11
- Vanna 0.7.9
- Ollama model: qwen2.5:3b
- Vector store: ChromaDB
- Database: data/sales.db
- Table: sales

## Implementation
1. Connected Vanna to the SQLite sales database.
2. Trained Vanna using database schema, documentation, and six example question-SQL pairs.
3. Tested ten natural-language questions.
4. Executed generated SQL against SQLite and reviewed the results.

## Discount Rule
The discount_pct column stores whole percentage values. For example, 5.0 means 5%. Discounted revenue is calculated using:

`qty * unit_price * (1 - COALESCE(discount_pct, 0) / 100.0)`

## Evidence
- `evidence/query_test_output.txt`
- `evidence/query_05_revenue.md`

## Scripts
- `scripts/test_vanna.py`
- `scripts/train_vanna.py`
- `scripts/test_queries.py`

