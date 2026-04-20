import random

def get_live_stadium_data():
    """Generates mock crowd density percentages (0-100%) for stadium zones."""
    return {
        "gates": {
            "Gate A": random.randint(20, 95),
            "Gate B": random.randint(10, 80),
            "Gate C": random.randint(5, 50)
        },
        "concessions": {
            "Food Court North": random.randint(40, 100),
            "Food Court South": random.randint(20, 70)
        },
        "restrooms": {
            "East Block": random.randint(10, 90),
            "West Block": random.randint(10, 60)
        }
    }