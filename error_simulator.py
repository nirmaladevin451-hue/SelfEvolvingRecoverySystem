import random

def simulate_error():
    errors = [
        Exception("General Exception"),
        TimeoutError("Request Timeout"),
        MemoryError("Memory Overflow")
    ]

    # 70% chance to raise error
    if random.random() < 0.7:
        raise random.choice(errors)
