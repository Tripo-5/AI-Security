import pandas as pd

# Example: Load logs from a SIEM system
logs = pd.read_csv('path_to_siem_logs.csv')

# Extract relevant features (e.g., timestamp, event type, source IP)
logs['timestamp'] = pd.to_datetime(logs['timestamp'])
logs['event_type'] = logs['event_type'].astype('category')
logs['source_ip'] = logs['source_ip'].astype('category')
