import nbformat

nb = nbformat.v4.new_notebook()
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    }
}

cells = [
    nbformat.v4.new_markdown_cell("""# Week 2 Day 5: NumPy for Data

## Learning objectives
- Create and manipulate 1D, 2D, and 3D arrays.
- Use vectorised calculations, broadcasting, and array indexing.
- Calculate statistical measures and correlation.
- Compare NumPy with Python loops on one million values."""),
    nbformat.v4.new_code_cell("""import numpy as np
import time

np.set_printoptions(precision=3, suppress=True)
print("NumPy version:", np.__version__)"""),
    nbformat.v4.new_markdown_cell("## 1. Create 1D, 2D, and 3D arrays"),
    nbformat.v4.new_code_cell("""array_1d = np.array([10, 20, 30, 40, 50])
array_2d = np.array([[10, 20, 30], [40, 50, 60]])
array_3d = np.arange(24).reshape(2, 3, 4)

print("1D array:", array_1d)
print("1D shape:", array_1d.shape)
print("\\n2D array:\\n", array_2d)
print("2D shape:", array_2d.shape)
print("\\n3D array shape:", array_3d.shape)
print(array_3d)"""),
    nbformat.v4.new_markdown_cell("## 2. Vectorised operations and aggregation across axes"),
    nbformat.v4.new_code_cell("""prices = np.array([100, 200, 300, 400])
quantities = np.array([2, 3, 1, 4])

print("Add:", prices + quantities)
print("Multiply:", prices * quantities)
print("Total sales value:", np.sum(prices * quantities))

sales = np.array([[100, 200, 300], [150, 250, 350]])
print("Column totals (axis=0):", np.sum(sales, axis=0))
print("Row totals (axis=1):", np.sum(sales, axis=1))
print("Overall mean:", np.mean(sales))"""),
    nbformat.v4.new_markdown_cell("## 3. Broadcasting"),
    nbformat.v4.new_code_cell("""# Apply a different monthly adjustment to each column.
monthly_sales = np.array([[100, 200, 300], [150, 250, 350]])
adjustments = np.array([1.0, 1.1, 1.2])

adjusted_sales = monthly_sales * adjustments
print("Original sales:\\n", monthly_sales)
print("Adjustment factors:", adjustments)
print("Adjusted sales:\\n", adjusted_sales)"""),
    nbformat.v4.new_markdown_cell("## 4. Boolean masking and fancy indexing"),
    nbformat.v4.new_code_cell("""amounts = np.array([1200, 4500, 800, 7200, 3000, 9500])
high_value = amounts[amounts >= 3000]
selected_positions = amounts[[0, 3, 5]]

print("Amounts at least 3000:", high_value)
print("Values at positions 0, 3, and 5:", selected_positions)
print("Values between 1000 and 5000:", amounts[(amounts >= 1000) & (amounts <= 5000)])"""),
    nbformat.v4.new_markdown_cell("## 5. Statistical measures and correlation"),
    nbformat.v4.new_code_cell("""amounts = np.array([1200, 4500, 800, 7200, 3000, 9500], dtype=float)
discounts = np.array([5, 10, 2, 15, 8, 18], dtype=float)

print("Mean:", np.mean(amounts))
print("Median:", np.median(amounts))
print("Standard deviation:", np.std(amounts))
print("75th percentile:", np.percentile(amounts, 75))
print("Amount-discount correlation:", np.corrcoef(amounts, discounts)[0, 1])"""),
    nbformat.v4.new_markdown_cell("## 6. Performance benchmark: one million values"),
    nbformat.v4.new_code_cell("""n = 1_000_000
values = list(range(n))
array_values = np.arange(n)

start = time.perf_counter()
python_result = [value * 2 + 1 for value in values]
python_seconds = time.perf_counter() - start

start = time.perf_counter()
numpy_result = array_values * 2 + 1
numpy_seconds = time.perf_counter() - start

print(f"Rows processed: {n:,}")
print(f"Python list-comprehension time: {python_seconds:.6f} seconds")
print(f"NumPy vectorised time: {numpy_seconds:.6f} seconds")
if numpy_seconds > 0:
    print(f"Measured speed ratio (Python / NumPy): {python_seconds / numpy_seconds:.2f}x")
print("Results match:", np.array_equal(np.array(python_result), numpy_result))"""),
    nbformat.v4.new_markdown_cell("""## Key takeaways

- **Vectorisation** applies operations to entire arrays without writing an explicit Python loop.
- **Broadcasting** lets compatible arrays of different shapes participate in calculations.
- **Boolean masking** filters values using conditions; fancy indexing selects specified positions.
- NumPy provides fast numerical operations and statistical functions.
- A Pandas DataFrame is label-oriented and supports mixed column types; a NumPy array is generally designed for homogeneous, efficient numerical data.

## Viva answers

1. **What is vectorisation?** Performing operations on whole arrays instead of looping over individual elements in Python. NumPy uses efficient compiled operations.
2. **What is broadcasting?** NumPy's rules for performing operations on arrays with compatible shapes, such as multiplying each column by a different factor.
3. **How do NumPy arrays differ from Pandas DataFrames?** Arrays primarily hold values and use positional indexing; DataFrames provide labelled rows and columns and can hold different data types in different columns.""")
]

nb.cells = cells
nbformat.write(nb, "week-02/day-05/numpy_analysis.ipynb")
print("Created week-02/day-05/numpy_analysis.ipynb")
print("Cells:", len(nb.cells))
