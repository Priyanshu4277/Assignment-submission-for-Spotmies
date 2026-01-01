import pandas as pd

COLUMNS = [
    "version", "account_id", "interface_id",
    "srcaddr", "dstaddr", "dstport", "srcport",
    "protocol", "packets", "bytes",
    "start", "end", "action", "log_status"
]

df = pd.read_csv(
    r"d:\Spotmies\log\vpc_flow_logs.log",
    sep=" ",
    names=COLUMNS
)

# Keep valid traffic only
df = df[df["log_status"] == "OK"]

# Feature engineering
df["duration"] = df["end"] - df["start"]

features = df[
    ["srcport", "dstport", "protocol", "packets", "bytes", "duration"]
]

features.to_csv("processed_features.csv", index=False)

print("[+] ETL completed successfully")