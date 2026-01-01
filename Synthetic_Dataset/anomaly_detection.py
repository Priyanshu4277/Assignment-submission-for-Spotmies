import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("processed_features.csv")

scaler = StandardScaler()
X = scaler.fit_transform(df)

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

df["anomaly"] = model.fit_predict(X)
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

df.to_csv("anomaly_results.csv", index=False)
df[df["anomaly"] == 1].head()
