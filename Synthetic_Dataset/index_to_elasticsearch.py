from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch("http://localhost:9200")
INDEX = "vpc-flow-anomalies"

df = pd.read_csv("anomaly_results.csv")

for _, row in df.iterrows():
    es.index(index=INDEX, document=row.to_dict())

print("[+] Data indexed successfully into Elasticsearch")
