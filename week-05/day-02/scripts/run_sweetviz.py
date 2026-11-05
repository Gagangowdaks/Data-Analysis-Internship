import pandas as pd
import sweetviz as sv
from pathlib import Path

BASE = Path("week-05/day-02")
DATA = BASE / "data" / "superstore.csv"
REPORTS = BASE / "reports"

df = pd.read_csv(DATA, encoding="cp1252")

report = sv.analyze(df)
output = REPORTS / "sweetviz_report.html"
report.show_html(filepath=str(output), open_browser=False)

print("SweetViz report generated:", output)
