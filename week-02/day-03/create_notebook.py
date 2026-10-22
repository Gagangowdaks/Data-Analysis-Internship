import nbformat as nbf
from pathlib import Path

folder = Path(__file__).parent
notebook = nbf.v4.new_notebook()

cells = [
    nbf.v4.new_markdown_cell("""# Week 2 — Day 3: EDA Workflow

## Objective
Explore a sales dataset, identify data-quality issues, visualize distributions and correlations, and extract five business insights.

## Workflow
1. Load and profile the dataset.
2. Check missing values and duplicates.
3. Visualize numeric distributions.
4. Explore correlations with a heatmap.
5. Generate summary statistics and business insights."""),
    nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

sns.set_theme(style="whitegrid")
df = pd.read_csv("cleaned_sales_data.csv")

print("Dataset loaded successfully")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
display(df.head())"""),
    nbf.v4.new_markdown_cell("## 1. Dataset profiling"),
    nbf.v4.new_code_cell("""print("Dataset shape:", df.shape)
print("\\\\nColumn data types:")
display(df.dtypes.to_frame("Data Type"))
print("\\\\nMissing values:")
display(df.isnull().sum().to_frame("Missing Count"))
print("\\\\nDuplicate rows:", df.duplicated().sum())
print("\\\\nUnique values per column:")
display(df.nunique().to_frame("Unique Values"))"""),
    nbf.v4.new_markdown_cell("## 2. Summary statistics"),
    nbf.v4.new_code_cell("""numeric_df = df.select_dtypes(include="number")
if numeric_df.empty:
    print("No numeric columns found.")
else:
    summary = numeric_df.describe().T
    summary["median"] = numeric_df.median()
    summary["missing"] = numeric_df.isnull().sum()
    display(summary.round(2))"""),
    nbf.v4.new_markdown_cell("## 3. Numeric distributions"),
    nbf.v4.new_code_cell("""if numeric_df.empty:
    print("No numeric columns available for distribution plots.")
else:
    for column in numeric_df.columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(data=df, x=column, kde=True)
        plt.title(f"Distribution of {column}")
        plt.tight_layout()
        plt.show()"""),
    nbf.v4.new_markdown_cell("## 4. Correlation heatmap"),
    nbf.v4.new_code_cell("""if numeric_df.shape[1] < 2:
    print("At least two numeric columns are needed for a correlation heatmap.")
else:
    correlation = numeric_df.corr()
    plt.figure(figsize=(max(7, len(correlation.columns)), 5))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f",
                vmin=-1, vmax=1)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
    display(correlation.round(2))"""),
    nbf.v4.new_markdown_cell("## 5. Outlier investigation"),
    nbf.v4.new_code_cell("""outlier_rows = []
for column in numeric_df.columns:
    values = numeric_df[column].dropna()
    if len(values) == 0:
        continue
    q1, q3 = values.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    count = ((values < lower) | (values > upper)).sum()
    outlier_rows.append({
        "Column": column, "Lower Bound": lower,
        "Upper Bound": upper, "Potential Outliers": int(count)
    })
display(pd.DataFrame(outlier_rows))"""),
    nbf.v4.new_markdown_cell("## 6. Five business insights"),
    nbf.v4.new_code_cell("""insights = []

# Insight 1: Dataset size and data quality
insights.append(
    f"1. The dataset contains {df.shape[0]} rows and {df.shape[1]} columns, "
    f"with {int(df.isnull().sum().sum())} missing cells and "
    f"{int(df.duplicated().sum())} duplicate rows."
)

# Insight 2: Numeric column averages
if not numeric_df.empty:
    means = numeric_df.mean().dropna()
    if not means.empty:
        col = means.idxmax()
        insights.append(
            f"2. Among numeric columns, '{col}' has the highest mean "
            f"({means[col]:.2f}); review its business meaning and units."
        )
    else:
        insights.append("2. Numeric columns contain no usable averages.")
else:
    insights.append("2. No numeric columns are available for average analysis.")

# Insight 3: Highest variability
if not numeric_df.empty:
    stds = numeric_df.std().dropna()
    if not stds.empty:
        col = stds.idxmax()
        insights.append(
            f"3. '{col}' has the highest standard deviation "
            f"({stds[col]:.2f}), indicating comparatively high variability."
        )
    else:
        insights.append("3. Variability could not be calculated.")
else:
    insights.append("3. Variability analysis requires numeric columns.")

# Insight 4: Strongest correlation
if numeric_df.shape[1] >= 2:
    corr = numeric_df.corr()
    pairs = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool)).stack()
    if not pairs.empty:
        pair = pairs.abs().idxmax()
        value = corr.loc[pair[0], pair[1]]
        insights.append(
            f"4. '{pair[0]}' and '{pair[1]}' have the strongest absolute "
            f"correlation ({value:.2f}). Correlation does not prove causation."
        )
    else:
        insights.append("4. No valid column pair was available for correlation.")
else:
    insights.append("4. At least two numeric columns are needed for correlation.")

# Insight 5: Most frequent category or most common numeric value
categorical = df.select_dtypes(exclude="number")
if not categorical.empty:
    col = categorical.nunique().idxmin()
    counts = df[col].value_counts(dropna=True)
    if not counts.empty:
        insights.append(
            f"5. The most frequent value in '{col}' is "
            f"'{counts.index[0]}' ({counts.iloc[0]} records). "
            "Consider whether this category dominates sales activity."
        )
    else:
        insights.append(f"5. Column '{col}' has no non-missing values.")
elif not numeric_df.empty:
    col = numeric_df.columns[0]
    insights.append(
        f"5. The median of '{col}' is {numeric_df[col].median():.2f}; "
        "compare it with the mean to assess possible skew."
    )
else:
    insights.append("5. No suitable column was found for a frequency insight.")

for insight in insights:
    print(insight)"""),
    nbf.v4.new_markdown_cell("""## 7. Conclusion and recommendations

Use the results above to:
- Investigate missing values and duplicates before further analysis.
- Review potential outliers before deciding whether they are errors or genuine events.
- Use the distribution charts to understand skew and unusual values.
- Investigate business relationships suggested by the correlation heatmap.
- Validate these findings with business context before making decisions.

**Note:** The five insights are generated from the dataset. Interpret each result using the actual column meanings before presenting it to stakeholders.""")
]

notebook.cells = cells
notebook.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    }
}

output = folder / "eda_report.ipynb"
nbf.write(notebook, output)
print(f"SUCCESS: Created {output}")
print(f"Notebook cells: {len(notebook.cells)}")
