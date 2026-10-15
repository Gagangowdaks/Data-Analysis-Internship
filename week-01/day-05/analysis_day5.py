import pandas as pd

df = pd.read_csv("week-01/day-05/sales_data.csv")

print("\n=== 1. FIRST FIVE ROWS ===")
print(df.head())

print("\n=== 2. DATASET INFORMATION ===")
df.info()

print("\n=== 3. NUMERICAL SUMMARY ===")
print(df.describe())

print("\n=== 4. SALES BY CATEGORY ===")
print(df["category"].value_counts())

print("\n=== 5. FILTER: SALES ABOVE 5000 ===")
print(df.loc[df["amount"] > 5000, ["customer_name", "product", "amount"]])

print("\n=== 6. MISSING VALUES ===")
print(df.isnull().sum())

df["discount"] = df["discount"].fillna(0)

print("\n=== 7. REVENUE BY REGION ===")
print(df.groupby("region")["amount"].agg(["count", "sum", "mean"]))

cleaned_path = "week-01/day-05/cleaned_sales_data.csv"
df.to_csv(cleaned_path, index=False)
print(f"\nCleaned dataset exported to {cleaned_path}")
