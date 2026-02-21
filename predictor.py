import json
import numpy as np
from sklearn.linear_model import LogisticRegression


def load_dna_history():
    try:
        with open("dna_history.json", "r") as file:
            return json.load(file)
    except:
        return []


def prepare_dataset(history):
    X = []
    y = []

    error_mapping = {
        "Exception": 0,
        "TimeoutError": 1,
        "MemoryError": 2
    }

    for entry in history:
        X.append([
            error_mapping.get(entry["error_type"], 0),
            entry["cpu_usage"],
            entry["memory_usage"],
            entry["severity"]
        ])

        # Label = 1 if severity high else 0
        y.append(1 if entry["severity"] > 0.7 else 0)

    return np.array(X), np.array(y)


def train_model():
    history = load_dna_history()

    if len(history) < 5:
        return None

    X, y = prepare_dataset(history)

    model = LogisticRegression()
    model.fit(X, y)

    return model


def predict_risk(model, dna):
    error_mapping = {
        "Exception": 0,
        "TimeoutError": 1,
        "MemoryError": 2
    }

    input_data = np.array([[
        error_mapping.get(dna["error_type"], 0),
        dna["cpu_usage"],
        dna["memory_usage"],
        dna["severity"]
    ]])

    probability = model.predict_proba(input_data)[0][1]
    return round(float(probability), 2)


def explain_risk(dna):
    reasons = []

    if dna["memory_usage"] > 80:
        reasons.append("High memory usage")

    if dna["cpu_usage"] > 75:
        reasons.append("High CPU usage")

    if dna["severity"] > 0.7:
        reasons.append("High severity score")

    if not reasons:
        return "Normal operating conditions"

    return " + ".join(reasons)
