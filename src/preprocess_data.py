import pandas as pd
from pathlib import Path

data_path = Path("data/raw")
files = sorted(data_path.glob("*.xlsx"))

datasets = []

for file in files:

    # Extract the month from the filename
    month = pd.to_datetime(file.name[:6], format="%Y%m")

    # Load severity data
    severity = pd.read_excel(
        file,
        sheet_name="INFORM Severity - all crises",
        header=None
    )

    severity = severity.iloc[4:, [0, 1, 2, 3, 4, 5, 6]].copy()

    severity.columns = [
        "crisis",
        "crisis_id",
        "country",
        "iso3",
        "drivers",
        "severity_score",
        "severity_category"
    ]

    # Convert severity values to numeric
    severity["severity_score"] = pd.to_numeric(
        severity["severity_score"], errors="coerce"
    )

    severity["severity_category"] = pd.to_numeric(
        severity["severity_category"], errors="coerce"
    )

    # Remove invalid rows
    severity = severity.dropna(
        subset=["crisis_id", "severity_category"]
    )

    severity = severity[
        severity["severity_category"].isin([1, 2, 3, 4, 5])
    ]

    # Add the observation month
    severity["month"] = month

    datasets.append(severity)

    print(f"{month:%Y-%m}: {len(severity)} records")

# Combine all monthly datasets
df = pd.concat(datasets, ignore_index=True)

df = df.sort_values(["crisis_id", "month"])

# Display initial results
print("\nCombined dataset:")
print(df.head(10))

print("\nDataset dimensions:")
print(df.shape)

print("\nSeverity distribution:")
print(df["severity_category"].value_counts().sort_index())

print("\nMissing values:")
print(df.isna().sum())

# Save combined data
output_path = Path("data/processed")
output_path.mkdir(parents=True, exist_ok=True)

df.to_csv(
    output_path / "severity_combined.csv",
    index=False
)

print("\nDataset saved successfully.")