from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data" / "indian_retail_sales.csv"

df = pd.read_csv(DATA)

checks = {
    "Dataset has 100,000 rows": len(df) == 100000,
    "Dataset has 25 columns": len(df.columns) == 25,
    "No missing values": not df.isnull().any().any(),
    "No duplicate rows": not df.duplicated().any(),
    "All records are from India": set(df["Country"]) == {"India"},
    "Three charts exist": len(list((BASE / "charts").glob("*.png"))) == 3,
    "Sweetviz report exists": (BASE / "reports" / "sweetviz_eda_report.html").exists(),
    "Business insights exist": (BASE / "evidence" / "business_insights.txt").exists(),
    "AI-assisted insights exist": (BASE / "evidence" / "ai_assisted_insights.md").exists(),
    "Data quality evidence exists": (BASE / "evidence" / "data_quality.txt").exists(),
}

for name, passed in checks.items():
    print(f"{'PASS' if passed else 'FAIL'}: {name}")

print(f"\nResult: {sum(checks.values())}/{len(checks)} checks passed")

if not all(checks.values()):
    raise SystemExit(1)
