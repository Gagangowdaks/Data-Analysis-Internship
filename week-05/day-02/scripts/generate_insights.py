import pandas as pd
from pathlib import Path

df = pd.read_csv("week-05/day-02/data/superstore.csv", encoding="cp1252")

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
subcategory_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values()

insights = [
    f"1. Technology has the highest category sales: ${category_sales.iloc[0]:,.2f}.",
    f"2. {region_profit.index[0]} region has the highest profit: ${region_profit.iloc[0]:,.2f}.",
    f"3. {subcategory_profit.index[0]} has the lowest sub-category profit: ${subcategory_profit.iloc[0]:,.2f}."
]

output = Path("week-05/day-02/evidence/business_insights.md")
output.write_text("# Three Business Insights\n\n" + "\n\n".join(insights), encoding="utf-8")

print("\n".join(insights))
print("\nSaved:", output)
