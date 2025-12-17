import json
import pandas as pd

INPUT = "data/shl_catalog_raw.json"
OUTPUT = "data/shl_catalog.csv"

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Basic validation
df = df.dropna(subset=["assessment_name", "url"])
df = df.drop_duplicates(subset=["assessment_name"])

# Ensure required columns exist
if "description" not in df.columns:
    df["description"] = ""
if "test_type" not in df.columns:
    df["test_type"] = "K"
if "category" not in df.columns:
    df["category"] = "General"

df.to_csv(OUTPUT, index=False)

print("✅ shl_catalog.csv created successfully")
print("✅ Total assessments:", len(df))
