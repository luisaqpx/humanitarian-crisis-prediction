import pandas as pd

# Load combined dataset
df = pd.read_csv(
    "data/processed/severity_combined.csv",
    parse_dates=["month"]
)

# Remove exact duplicate records
original_count = len(df)

df = df.drop_duplicates().copy()

print("Duplicates removed:", original_count - len(df))

# Verify unique crisis-month records
if df.duplicated(["crisis_id", "month"]).any():
    raise ValueError("Duplicate crisis-month records remain.")

# Sort observations chronologically
df = df.sort_values(["crisis_id", "month"])

# Get the next observation for each crisis
df["target_severity"] = (
    df.groupby("crisis_id")["severity_category"].shift(-1)
)

df["target_month"] = (
    df.groupby("crisis_id")["month"].shift(-1)
)

# Keep only consecutive months
expected_month = df["month"] + pd.DateOffset(months=1)

df = df[df["target_month"] == expected_month].copy()

df["target_severity"] = df["target_severity"].astype(int)

# Display results
print("Dataset dimensions:", df.shape)

print("\nTarget distribution:")
print(df["target_severity"].value_counts().sort_index())

print("\nObservations by target month:")
print(df.groupby("target_month").size())

print("\nSample records:")
print(df[[
    "crisis_id",
    "month",
    "severity_category",
    "target_month",
    "target_severity"
]].head(10))

# Save dataset
df.to_csv(
    "data/processed/prediction_dataset.csv",
    index=False
)

print("\nPrediction dataset saved successfully.")