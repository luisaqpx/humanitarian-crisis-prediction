import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    ConfusionMatrixDisplay
)

# Load prediction dataset
df = pd.read_csv(
    "data/processed/prediction_dataset.csv",
    parse_dates=["month", "target_month"]
)

# Define input features and target
features = ["severity_score", "severity_category"]
target = "target_severity"

# Chronological data split
train = df[df["target_month"] < "2026-07-01"]

validation = df[
    df["target_month"] == "2026-07-01"
]

test = df[
    df["target_month"] == "2026-10-01"
]

# Prepare features and labels
X_train = train[features]
y_train = train[target]

X_val = validation[features]
y_val = validation[target]

X_test = test[features]
y_test = test[target]

# Display split sizes
print("Training samples:", len(train))
print("Validation samples:", len(validation))
print("Testing samples:", len(test))

# Initialize Decision Tree
model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Generate predictions
val_predictions = model.predict(X_val)
test_predictions = model.predict(X_test)

# Persistence baseline
persistence_predictions = (
    test["severity_category"].astype(int)
)

# Evaluation function
def evaluate(name, actual, predicted):
    accuracy = accuracy_score(actual, predicted)

    macro_f1 = f1_score(
        actual,
        predicted,
        average="macro",
        zero_division=0
    )

    reward = np.mean(
        1 - np.abs(
            np.asarray(actual) - np.asarray(predicted)
        ) / 4
    )

    print(f"\n{name}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Macro F1: {macro_f1:.4f}")
    print(f"Average Reward: {reward:.4f}")

# Evaluate models
evaluate(
    "Decision Tree - Validation",
    y_val,
    val_predictions
)

evaluate(
    "Decision Tree - Test",
    y_test,
    test_predictions
)

evaluate(
    "Persistence Baseline - Test",
    y_test,
    persistence_predictions
)

# Create results directory
results_path = Path("results")
results_path.mkdir(exist_ok=True)

# Generate confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test,
    test_predictions,
    labels=[1, 2, 3, 4, 5],
    display_labels=[
        "Very Low", "Low", "Medium",
        "High", "Very High"
    ],
    cmap="Blues",
    xticks_rotation=45
)

plt.title("Decision Tree - Confusion Matrix")
plt.tight_layout()

plt.savefig(
    results_path / "confusion_matrix.png",
    dpi=300
)

plt.close()

# Generate target class distribution
counts = df["target_severity"].value_counts()
counts = counts.reindex(
    [1, 2, 3, 4, 5],
    fill_value=0
)

plt.figure(figsize=(8, 5))

plt.bar(
    ["Very Low", "Low", "Medium", "High", "Very High"],
    counts.values
)

plt.title("Target Severity Distribution")
plt.xlabel("Severity Category")
plt.ylabel("Number of Observations")
plt.tight_layout()

plt.savefig(
    results_path / "severity_distribution.png",
    dpi=300
)

plt.close()

# Compare individual predictions
print(
    "\nDifferent predictions from persistence:",
    np.sum(
        test_predictions != persistence_predictions.to_numpy()
    )
)

print("\nEvaluation figures saved successfully.")