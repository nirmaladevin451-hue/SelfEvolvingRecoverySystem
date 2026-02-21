import random

def run_system():
    error = random.choice(["none", "crash", "timeout", "memory"])

    if error == "crash":
        raise Exception("Application Crash")
    elif error == "timeout":
        raise TimeoutError("Request Timeout")
    elif error == "memory":
        raise MemoryError("Memory Overflow")

    return "System Running Successfully"
