import random

from error_simulator import simulate_error
from dna_mapper import generate_dna, store_dna
from recovery_engine import recovery_action, update_fitness
from predictor import train_model, predict_risk, explain_risk
from pattern_engine import detect_repeated_error, detect_severity_trend


def main():
    try:
        simulate_error()
        print("✅ System Running Successfully")

    except Exception as e:
        error_type = type(e).__name__
        print("⚠ Error Detected:", error_type)

        # 🧬 DNA Mapping
        dna = generate_dna(error_type)
        print("🧬 Error DNA:", dna)

        store_dna(dna)

        # 🔍 Pattern Detection Layer
        repeat_flag, repeated_error = detect_repeated_error()
        trend_flag = detect_severity_trend()

        if repeat_flag:
            print("🚨 Pattern Detected: Repeated Error ->", repeated_error)

        if trend_flag:
            print("📈 Pattern Detected: Increasing Severity Trend")

        # 🤖 ML Prediction Layer
        model = train_model()
        risk = None

        if model:
            risk = predict_risk(model, dna)
            print("📊 Predicted Failure Risk:", risk)

            reason = explain_risk(dna)
            print("🔍 Risk Reason:", reason)

        # 🔧 Recovery Layer with Pattern Escalation
        if repeat_flag:
            action = "🚨 Pattern Escalation: Forced Full System Restart"

        elif trend_flag:
            action = "📈 Trend Escalation: Preventive Full System Restart"

        else:
            action = recovery_action(error_type, risk)

        print("🔧 Recovery Action Selected:", action)

        success = random.choice([True, False])

        if success:
            print("✅ Recovery Successful")
        else:
            print("❌ Recovery Failed")

        update_fitness(error_type, success)


if __name__ == "__main__":
    main()
