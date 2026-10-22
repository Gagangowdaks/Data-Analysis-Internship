# Week 2 — Day 4: Data Cleaning Log

## Dataset
- Source: `sales_data.csv`
- Output: `cleaned_dataset.csv`

## Before-and-after data quality comparison

| Metric | Before cleaning | After cleaning |
|---|---:|---:|
| Rows | 10 | 10 |
| Columns | 8 | 8 |
| Missing cells | 3 | 0 |
| Duplicate rows | 0 | 0 |

## Cleaning decisions

### 1. Standardisation
- Trimmed whitespace from column names and text values.
- Standardised column names to lowercase with underscores.
- Parsed date columns where applicable and converted numeric-looking text columns when conversion was sufficiently reliable.

### 2. Missing values
- `discount`: filled 3 missing numeric value(s) with the median (0.05).

### 3. Duplicates
- Removed 0 exact duplicate row(s).

### 4. Outliers
- `sale_id`: skipped IQR capping because it appears to be an identifier.
- `amount`: capped 1 value(s) to the IQR bounds [-18187.50, 37312.50].
- `discount`: capped 3 value(s) to the IQR bounds [0.02, 0.11].

### 5. Validation
- Output saved as `cleaned_dataset.csv`.
- Remaining missing cells: 0.
- Remaining duplicate rows: 0.
- Review capped values and imputation choices with domain knowledge before using the data for business decisions.

## Summary
Cleaning was applied systematically, and the before/after metrics above record the observed changes. Imputation and outlier capping can affect analysis, so the original source file has been preserved.
