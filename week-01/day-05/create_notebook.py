import nbformat
from pathlib import Path

folder = Path("week-01/day-05")
notebook = nbformat.v4.new_notebook()
cells = []

cells.append(nbformat.v4.new_markdown_cell("""# Week 1 Day 5 — Python for Data: Pandas Basics

## Objective
Load, inspect, filter, clean, group, and export sales data using Pandas.

Dataset: `sales_data.csv`
"""))

cells.append(nbformat.v4.new_code_cell("""import pandas as pd

df = pd.read_csv("sales_data.csv")
df.head()
"""))

cells.append(nbformat.v4.new_markdown_cell("## 1. Inspect the dataset"))
cells.append(nbformat.v4.new_code_cell("""print("Shape:", df.shape)
df.info()
"""))

cells.append(nbformat.v4.new_code_cell("df.describe()"))
cells.append(nbformat.v4.new_code_cell('df["category"].value_counts()'))

cells.append(nbformat.v4.new_markdown_cell("## 2. Filter rows and select columns"))
cells.append(nbformat.v4.new_code_cell("""df.loc[df["amount"] > 5000, ["customer_name", "product", "amount"]]
"""))

cells.append(nbformat.v4.new_markdown_cell("## 3. Check and handle missing values"))
cells.append(nbformat.v4.new_code_cell("""print(df.isnull().sum())

# Exercise assumption: treat missing discounts as zero.
df["discount"] = df["discount"].fillna(0)

print("\\nMissing values after cleaning:")
print(df.isnull().sum())
"""))

cells.append(nbformat.v4.new_markdown_cell("## 4. Group and aggregate"))
cells.append(nbformat.v4.new_code_cell("""df.groupby("region")["amount"].agg(["count", "sum", "mean"])
"""))

cells.append(nbformat.v4.new_markdown_cell("## 5. Export cleaned data"))
cells.append(nbformat.v4.new_code_cell("""df.to_csv("cleaned_sales_data.csv", index=False)
print("Exported cleaned_sales_data.csv")
"""))

cells.append(nbformat.v4.new_markdown_cell("""## Key findings

- The dataset contains 10 sales records.
- Electronics is the most frequent category, with 5 records.
- South has the highest total sales amount in this dataset.
- Three discount values were missing before cleaning.
- Missing discounts were filled with zero as an exercise assumption.

## Viva revision

- **DataFrame:** A labelled two-dimensional table of rows and columns.
- **groupby():** Splits data into groups so calculations can be performed for each group.
- **loc vs iloc:** `loc` selects by labels or conditions; `iloc` selects by integer positions.
"""))

notebook.cells = cells
notebook.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    }
}

path = folder / "analysis_day5.ipynb"
nbformat.write(notebook, path)
print(f"Created: {path}")
