import pandas as pd
from pathlib import Path
from autoviz import AutoViz_Class

BASE = Path("week-05/day-02")
DATA = BASE / "data" / "superstore.csv"
REPORTS = BASE / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA, encoding="cp1252")

AV = AutoViz_Class()
AV.AutoViz(
    filename="",
    sep=",",
    depVar="",
    dfte=df,
    header=0,
    verbose=1,
    lowess=False,
    chart_format="html",
    save_plot_dir=str(REPORTS)
)

print("AutoViz analysis completed.")
print("Reports folder:", REPORTS.resolve())
