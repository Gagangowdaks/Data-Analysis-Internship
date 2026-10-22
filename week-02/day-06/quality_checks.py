import pandas as pd
import numpy as np
import json
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = Path("week-01/day-05/sales_data.csv")
REPORT = ROOT / "quality_report.json"

df = pd.read_csv(SOURCE)
initial_rows = len(df)

# Six DAMA-DMBOK quality dimensions
checks = {}

# 1. Completeness: required fields are not missing
required = [c for c in ["sale_id", "amount", "sale_date"] if c in df.columns]
checks["completeness"] = {
    "passed": bool(df[required].notna().all().all()) if required else False,
    "missing_values_by_column": df.isna().sum().to_dict()
}

# 2. Accuracy: amounts should be non-negative
checks["accuracy"] = {
    "passed": bool((pd.to_numeric(df["amount"], errors="coerce") >= 0).all())
        if "amount" in df.columns else False,
    "negative_amount_rows": int(
        (pd.to_numeric(df["amount"], errors="coerce") < 0).sum()
    ) if "amount" in df.columns else None
}

# 3. Consistency: identifiers must not be null and dates must parse
checks["consistency"] = {
    "passed": bool(df["sale_id"].notna().all()) if "sale_id" in df.columns else False
}

# 4. Timeliness: report date range; freshness SLA needs ingestion timestamps
if "sale_date" in df.columns:
    dates = pd.to_datetime(df["sale_date"], errors="coerce")
    checks["timeliness"] = {
        "passed": bool(dates.notna().all()),
        "earliest_date": str(dates.min()) if dates.notna().any() else None,
        "latest_date": str(dates.max()) if dates.notna().any() else None,
        "note": "Ingestion timestamps are needed to test a 2-hour freshness SLA."
    }
else:
    checks["timeliness"] = {
        "passed": False,
        "note": "No sale_date column available."
    }

# 5. Uniqueness: sale_id should be unique
checks["uniqueness"] = {
    "passed": bool(df["sale_id"].is_unique) if "sale_id" in df.columns else False,
    "duplicate_sale_ids": int(df["sale_id"].duplicated().sum())
        if "sale_id" in df.columns else None
}

# 6. Validity: sale_date must parse and amount must be numeric
checks["validity"] = {
    "passed": bool(
        pd.to_numeric(df["amount"], errors="coerce").notna().all()
        and pd.to_datetime(df["sale_date"], errors="coerce").notna().all()
    ) if {"amount", "sale_date"}.issubset(df.columns) else False
}

result = {
    "source": str(SOURCE),
    "row_count": initial_rows,
    "columns": list(df.columns),
    "dimensions": checks,
    "overall_pass": all(item["passed"] for item in checks.values())
}

REPORT.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
print(json.dumps(result, indent=2, default=str))
print(f"\nReport saved: {REPORT}")
