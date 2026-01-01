# AWS / CloudWatch Traffic Anomaly Detection using ELK & Machine Learning

## Overview

This project demonstrates an **end-to-end security analytics pipeline** to detect anomalous network and application traffic using **machine learning** and **ELK Stack (Elasticsearch & Kibana)**.  
Two complementary approaches are implemented:

1. **Synthetic AWS VPC Flow Logs–based detection**
    
2. **Real CloudWatch / security traffic CSV–based detection**
    

Both approaches simulate **SOC-style workflows** for threat detection, investigation, and visualization.

---

## Architecture

                   Traffic Logs (Synthetic / CSV)
                                ↓
                  Python ETL & Feature Engineering
                                ↓
              ML Anomaly Detection (Isolation Forest)
                                ↓
                     Elasticsearch Indexing         
                                ↓
                     Kibana Lens Dashboards`

---

## Tools & Technologies

- Python 3
    
- pandas, scikit-learn
    
- Elasticsearch 7.17.x
    
- Kibana 7.17.x
    
- AWS VPC Flow Logs (synthetic format)
    
- CloudWatch / Security traffic CSV logs
    

---

## Approach 1: Synthetic AWS VPC Flow Logs

### Purpose

This approach simulates **real AWS VPC Flow Logs** when a live AWS account is unavailable.  
It helps demonstrate:

- Cloud network traffic behavior
    
- SOC-style anomaly detection
    
- ELK-based visualization
    

### Data Source

Synthetic logs are generated in **AWS VPC Flow Log format**, including:

- Source & destination IPs
    
- Ports (22, 80, 443, 3389, etc.)
    
- Protocols (TCP/UDP)
    
- Packets and bytes
    
- ACCEPT / REJECT actions
    

### Processing Steps

1. Generate synthetic VPC Flow Logs using Python
    
2. Parse and preprocess logs (ETL)
    
3. Extract numeric traffic features:
    
    - src_port
        
    - dst_port
        
    - bytes
        
    - packets
        
    - duration
        
4. Apply **Isolation Forest** for unsupervised anomaly detection
    
5. Index results into Elasticsearch
    
6. Visualize anomalies in Kibana using Lens
    

### Outcome

- Identification of abnormal ports and traffic volumes
    
- Detection of suspicious SSH/RDP-like behavior
    
- SOC-style dashboard for cloud network monitoring
    

---

## Approach 2: CloudWatch / Security Traffic CSV (Realistic Logs)

### Purpose

This approach works with **realistic CloudWatch / security analytics CSV data**, closer to production SOC environments.  
It focuses on **application-layer and security-event anomalies** rather than raw network flows.

### Data Source

CSV logs include rich security context such as:

- bytes_in / bytes_out
    
- source and destination IPs
    
- destination ports
    
- protocol
    
- response codes
    
- rule names
    
- detection types
    
- timestamps
    
Link: https://www.kaggle.com/datasets/jancsg/cybersecurity-suspicious-web-threat-interactions

### Feature Engineering (ML)

Only **behavior-driven numeric fields** are used for ML:

- dst_port
    
- bytes_in
    
- bytes_out
    

Other fields are retained for **contextual investigation**, not ML training.

### Processing Steps

1. Load CloudWatch CSV logs
    
2. Select relevant numeric features
    
3. Normalize data using StandardScaler
    
4. Apply **Isolation Forest** (≈5% contamination)
    
5. Add an `anomaly` flag to the dataset
    
6. Index enriched data into Elasticsearch
    
7. Analyze anomalies in Kibana
    

### Outcome

- Detection of unusual traffic volumes
    
- Identification of suspicious destination ports
    
- Correlation with WAF rules, response codes, and detection types
    
- SOC investigation–ready dashboards
    

---

## Why Two Approaches?

|Aspect|Synthetic Logs|CSV Logs|
|---|---|---|
|AWS account required|No|No|
|Realism|Network-level|Security/application-level|
|Use case|Cloud networking & SOC simulation|Cloud security & WAF analysis|
|ML complexity|Moderate|Low–Moderate|
|SOC relevance|High|Very High|

Together, both approaches demonstrate **adaptability**, **security engineering thinking**, and **real-world SOC workflows**.

---

## Machine Learning Model

- **Algorithm:** Isolation Forest
    
- **Type:** Unsupervised anomaly detection
    
- **Reason for choice:**
    
    - No labeled data required
        
    - Works well with traffic patterns
        
    - Commonly used in security analytics
        

The model identifies traffic that **deviates significantly from normal behavior**, rather than relying on predefined attack signatures.

---

## Kibana Dashboards

Dashboards are created using **Kibana Lens**, including:

- Anomalous traffic by destination port
    
- Total anomalous bytes transferred
    
- Detailed tables for SOC investigation
    
- Filters using `anomaly = 1`
    

These dashboards enable **visual threat hunting and incident analysis**.

---

## How to Run (High-Level)

1. Generate or load logs (synthetic or CSV)
    
2. Run Python preprocessing and ML scripts
    
3. Index output into Elasticsearch
    
4. Create index patterns in Kibana
    
5. Build Lens visualizations and dashboards
    

---

## Key Learning Outcomes

- Cloud security log analysis
    
- Feature engineering for security ML
    
- Unsupervised anomaly detection
    
- Elasticsearch indexing and querying
    
- Kibana Lens for SOC dashboards
    
- Real-world troubleshooting and pipeline design
    

---

## Conclusion

This project demonstrates a **practical, SOC-aligned approach** to cloud traffic anomaly detection using machine learning and the ELK stack.  
By implementing both **synthetic** and **realistic CSV-based** approaches, the solution showcases flexibility, strong security fundamentals, and readiness for real-world Cyber Security Analyst roles.
