import json


def load_knowledge():
    with open("knowledge_base.json", "r") as file:
        return json.load(file)


def save_knowledge(data):
    with open("knowledge_base.json", "w") as file:
        json.dump(data, file, indent=4)


def recovery_action(error_type, risk_score=None):
    actions = {
        "Exception": "Restart Application",
        "TimeoutError": "Retry Request",
        "MemoryError": "Clear Memory Cache"
    }

    base_action = actions.get(error_type, "Manual Intervention Required")

    # Risk-based adaptive strategy
    if risk_score is not None:
        if risk_score > 0.7:
            return "⚠ High Risk Strategy: Full System Restart"
        elif risk_score > 0.4:
            return base_action
        else:
            return "🟢 Light Recovery: Log and Monitor"

    return base_action


def update_fitness(error_type, success=True):
    data = load_knowledge()

    if success:
        data[error_type]["success"] += 1
        data[error_type]["fitness"] += 0.2
    else:
        data[error_type]["failure"] += 1
        data[error_type]["fitness"] -= 0.1

    save_knowledge(data)
