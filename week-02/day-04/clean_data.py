import pandas as pd
from pathlib import Path

folder = Path(__file__).parent
source = folder / "sales_data.csv"
output = folder / "cleaned_dataset.csv"
log_file = folder / "cleaning_log.md"

df = pd.read_csv(source)
original = df.copy()

# Standardise column names and text values.
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# Parse dates where applicable.
for col in df.columns:
    if "date" in col:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# Convert likely numeric columns stored as text.
for col in df.columns:
    if col not in ["sale_date"] and df[col].dtype == "object":
        converted = pd.to_numeric(df[col], errors="coerce")
        if converted.notna().sum() > 0 and converted.notna().sum() >= df[col].notna().sum() * 0.8:
            df[col] = converted

before_rows = len(df)
before_missing = int(df.isnull().sum().sum())
before_duplicates = int(df.duplicated().sum())

# Remove exact duplicate rows.
df = df.drop_duplicates().copy()
duplicates_removed = before_duplicates

# Fill missing values based on column type.
imputation_log = []
for col in df.columns:
    missing = int(df[col].isnull().sum())
    if missing == 0:
        continue

    if pd.api.types.is_numeric_dtype(df[col]):
        median = df[col].median()
        if pd.notna(median):
            df[col] = df[col].fillna(median)
            imputation_log.append(f"- `{col}`: filled {missing} missing numeric value(s) with the median ({median}).")
        else:
            df = df.dropna(subset=[col])
            imputation_log.append(f"- `{col}`: removed rows because no valid numeric value was available for imputation.")
    elif pd.api.types.is_datetime64_any_dtype(df[col]):
        df = df.dropna(subset=[col])
        imputation_log.append(f"- `{col}`: removed rows with missing or invalid dates because a safe date imputation could not be inferred.")
    else:
        mode = df[col].mode(dropna=True)
        if not mode.empty:
            df[col] = df[col].fillna(mode.iloc[0])
            imputation_log.append(f"- `{col}`: filled {missing} missing value(s) with the mode (`{mode.iloc[0]}`).")
        else:
            df = df.dropna(subset=[col])
            imputation_log.append(f"- `{col}`: removed rows because no valid category was available for imputation.")

# Cap numeric outliers using the IQR rule, excluding likely identifiers.
outlier_log = []
for col in df.select_dtypes(include="number").columns:
    if col.endswith("_id") or col == "id":
        outlier_log.append(f"- `{col}`: skipped IQR capping because it appears to be an identifier.")
        continue

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    if pd.isna(iqr) or iqr == 0:
        outlier_log.append(f"- `{col}`: no IQR capping applied because the IQR is zero or unavailable.")
        continue

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (df[col] < lower) | (df[col] > upper)
    count = int(mask.sum())
    df[col] = df[col].clip(lower=lower, upper=upper)
    outlier_log.append(
        f"- `{col}`: capped {count} value(s) to the IQR bounds [{lower:.2f}, {upper:.2f}]."
    )

# Final text normalisation and whitespace cleanup.
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].apply(
        lambda x: " ".join(x.split()) if isinstance(x, str) else x
    )

after_rows = len(df)
after_missing = int(df.isnull().sum().sum())
after_duplicates = int(df.duplicated().sum())

df.to_csv(output, index=False)

def bullets(items):
    return "\n".join(items) if items else "- No missing values required imputation."

report = f"""# Week 2 — Day 4: Data Cleaning Log

## Dataset
- Source: `sales_data.csv`
- Output: `cleaned_dataset.csv`

## Before-and-after data quality comparison

| Metric | Before cleaning | After cleaning |
|---|---:|---:|
| Rows | {before_rows} | {after_rows} |
| Columns | {len(original.columns)} | {len(df.columns)} |
| Missing cells | {before_missing} | {after_missing} |
| Duplicate rows | {before_duplicates} | {after_duplicates} |

## Cleaning decisions

### 1. Standardisation
- Trimmed whitespace from column names and text values.
- Standardised column names to lowercase with underscores.
- Parsed date columns where applicable and converted numeric-looking text columns when conversion was sufficiently reliable.

### 2. Missing values
{bullets(imputation_log)}

### 3. Duplicates
- Removed {duplicates_removed} exact duplicate row(s).

### 4. Outliers
{bullets(outlier_log)}

### 5. Validation
- Output saved as `cleaned_dataset.csv`.
- Remaining missing cells: {after_missing}.
- Remaining duplicate rows: {after_duplicates}.
- Review capped values and imputation choices with domain knowledge before using the data for business decisions.

## Summary
Cleaning was applied systematically, and the before/after metrics above record the observed changes. Imputation and outlier capping can affect analysis, so the original source file has been preserved.
"""

log_file.write_text(report, encoding="utf-8")

print("SUCCESS: Data cleaning completed.")
print("Rows before:", before_rows)
print("Rows after:", after_rows)
print("Missing cells before:", before_missing)
print("Missing cells after:", after_missing)
print("Duplicates before:", before_duplicates)
print("Duplicates after:", after_duplicates)
print("Created:", output)
print("Created:", log_file)
