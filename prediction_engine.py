import json
import numpy as np
from sklearn.linear_model import LogisticRegression

def encode_error(error_type):
    mapping = {
        "Exception": 0,
        "TimeoutError": 1,
        "MemoryError": 2
    }
    return mapping.get(error_type, -1)

def train_model():
    with open("dna_history.json", "r") as file:
        data = json.load(file)

    if len(data) < 5:
        return None

    X = []
    y = []

    for entry in data:
        encoded_error = encode_error(entry["error_type"])
        cpu = entry["cpu_usage"]
        memory = entry["memory_usage"]
        severity = entry["severity"]

        # Simple rule: assume high severity more likely failure
        label = 1 if severity > 0.75 else 0

        X.append([encoded_error, cpu, memory, severity])
        y.append(label)

    model = LogisticRegression()
    model.fit(X, y)

    return model

def predict_risk(model, dna):
    encoded_error = encode_error(dna["error_type"])
    features = np.array([[encoded_error, dna["cpu_usage"], dna["memory_usage"], dna["severity"]]])

    probability = model.predict_proba(features)[0][1]
    return round(probability, 2)
