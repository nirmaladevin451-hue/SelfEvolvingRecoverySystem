import random
import psutil
import json
from datetime import datetime


def generate_dna(error_type):
    dna = {
        "error_type": error_type,
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "severity": round(random.uniform(0.3, 1.0), 2),
        "timestamp": str(datetime.now())
    }
    return dna


def store_dna(dna):
    try:
        with open("dna_history.json", "r") as file:
            history = json.load(file)
    except:
        history = []

    history.append(dna)

    with open("dna_history.json", "w") as file:
        json.dump(history, file, indent=4)
