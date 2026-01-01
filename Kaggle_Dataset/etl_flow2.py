import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# Load CSV
df = pd.read_csv("CloudWatch_Traffic_Web_Attack.csv")

# --- FEATURE SELECTION (BASED ON YOUR REAL COLUMNS) ---
FEATURE_COLUMNS = [
    "dst_port",
    "bytes_in",
    "bytes_out"
]

# Handle missing values
features_df = df[FEATURE_COLUMNS].fillna(0)

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features_df)

# Train anomaly detection model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,   # ~5% anomalies
    random_state=42
)

# Predict anomalies
df["anomaly"] = model.fit_predict(scaled_features)

# Convert output to readable format
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

# Save enriched dataset
df.to_csv("cloudwatch_with_anomalies.csv", index=False)

# Summary
print("Anomaly detection completed")
print(df["anomaly"].value_counts())
