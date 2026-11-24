import pandas as pd
from pathlib import Path

# Locate the raw datasets
data_path = Path("data/raw")

# Find all Excel files
files = sorted(data_path.glob("*.xlsx"))

print(f"Total datasets: {len(files)}")

# Inspect each dataset
for file in files:
    print(f"\nFile: {file.name}")

    workbook = pd.ExcelFile(file)

    print("Available sheets:")
    print(workbook.sheet_names)

# Explore the latest dataset
latest_file = files[-1]

sheets = [
    "INFORM Severity - all crises",
    "Core Indicators",
    "Crisis Indicator Data"
]

for sheet in sheets:
    df = pd.read_excel(
        latest_file,
        sheet_name=sheet,
        header=None
    )

    print(f"\nSheet: {sheet}")
    print(f"Dimensions: {df.shape}")
    print(df.iloc[:12, :15].to_string(index=False))