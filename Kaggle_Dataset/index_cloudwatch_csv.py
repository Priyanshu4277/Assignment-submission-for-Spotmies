import pandas as pd
from elasticsearch import Elasticsearch

# Connect to Elasticsearch (7.17.x)
es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "cloudwatch-traffic-anomalies"

# Load enriched CSV
df = pd.read_csv("cloudwatch_with_anomalies.csv")

# Index documents
for _, row in df.iterrows():
    es.index(index=INDEX_NAME, document=row.to_dict())

print("[+] CloudWatch CSV indexed successfully")
