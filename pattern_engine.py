import json


def load_dna_history():
    try:
        with open("dna_history.json", "r") as file:
            return json.load(file)
    except:
        return []


def detect_repeated_error(threshold=3):
    history = load_dna_history()

    if len(history) < threshold:
        return False, None

    last_errors = [entry["error_type"] for entry in history[-threshold:]]

    if all(error == last_errors[0] for error in last_errors):
        return True, last_errors[0]

    return False, None


def detect_severity_trend(threshold=3):
    history = load_dna_history()

    if len(history) < threshold:
        return False

    last_severity = [entry["severity"] for entry in history[-threshold:]]

    if last_severity == sorted(last_severity):
        return True

    return False

