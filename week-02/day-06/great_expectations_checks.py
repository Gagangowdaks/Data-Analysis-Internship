from pathlib import Path
import pandas as pd

data_file = Path("week-01/day-05/sales_data.csv")
report = Path("week-02/day-06/great_expectations_report.txt")

df = pd.read_csv(data_file)
results = []

def check(name, success, error=""):
    results.append({
        "check": name,
        "success": bool(success),
        "error": error if not success else ""
    })

check("Dataset is not empty", not df.empty)
check("No duplicate rows", not df.duplicated().any(),
      f"{df.duplicated().sum()} duplicate rows found")
check("Required fields have no missing values",
      not df[["sale_id", "customer_name", "product", "category",
              "region", "amount", "sale_date"]].isnull().any().any())
check("Column names are unique", df.columns.is_unique)
check("Amounts are non-negative", (df["amount"] >= 0).all())

missing_discounts = int(df["discount"].isnull().sum())
results.append({
    "check": "Discount missing values documented",
    "success": True,
    "error": f"{missing_discounts} missing discounts; review before analysis"
})

passed = sum(item["success"] for item in results)
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(
    "\n".join(
        f"{'PASS' if item['success'] else 'FAIL'}: {item['check']}"
        + (f" — {item['error']}" if item.get("error") else "")
        for item in results
    )
    + f"\n\nSummary: {passed}/{len(results)} checks passed\n",
    encoding="utf-8",
)

print(f"Summary: {passed}/{len(results)} checks passed")
print(f"Missing discount values: {missing_discounts}")
print("Report saved:", report)
