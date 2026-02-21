from flask import Flask, render_template_string, jsonify
import json
import os
from collections import Counter

app = Flask(__name__)

LOG_FILE = "error_logs.json"


# -------------------------
# Helper: Load Logs
# -------------------------
def load_logs():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


# -------------------------
# Dashboard Route
# -------------------------
@app.route("/")
def dashboard():
    logs = load_logs()

    total_errors = len(logs)

    error_types = [log["error_type"] for log in logs]
    counts = Counter(error_types)

    memory_count = counts.get("MemoryError", 0)
    exception_count = counts.get("Exception", 0)
    timeout_count = counts.get("TimeoutError", 0)

    return render_template_string("""
    <html>
    <head>
        <title>Self Evolving Recovery System</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body style="font-family: Arial; background-color:#111; color:white; text-align:center;">
        <h1>Self Evolving Recovery System</h1>
        <h3>Total Logged Errors: {{total}}</h3>

        <canvas id="errorChart" width="400" height="200"></canvas>

        <script>
            const ctx = document.getElementById('errorChart');

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['MemoryError', 'Exception', 'TimeoutError'],
                    datasets: [{
                        label: 'Error Count',
                        data: [{{memory}}, {{exception}}, {{timeout}}],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: { beginAtZero: true }
                    }
                }
            });
        </script>
    </body>
    </html>
    """,
    total=total_errors,
    memory=memory_count,
    exception=exception_count,
    timeout=timeout_count
    )


# -------------------------
# API Endpoint (For Mobile / Future Expansion)
# -------------------------
@app.route("/api/dashboard")
def api_dashboard():
    logs = load_logs()

    total_errors = len(logs)
    error_types = [log["error_type"] for log in logs]
    counts = Counter(error_types)

    return jsonify({
        "total_errors": total_errors,
        "memory_errors": counts.get("MemoryError", 0),
        "exceptions": counts.get("Exception", 0),
        "timeouts": counts.get("TimeoutError", 0)
    })


# -------------------------
# Run Server
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
