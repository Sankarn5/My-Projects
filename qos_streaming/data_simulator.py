import random
import time

# Simulate viewer data stream
def simulate_viewer_data():
    messages = [
        "This stream is awesome!", "Too much lag", "Great quality!", 
        "Horrible buffering", "Loving the gameplay", "Video froze again!"
    ]
    while True:
        yield {
            "viewer_id": random.randint(1000, 9999),
            "message": random.choice(messages),
            "bitrate": random.randint(2000, 6000),  # in kbps
            "buffering_time": round(random.uniform(0, 5), 2),  # in seconds
            "fps": random.randint(20, 60)
        }
        time.sleep(1)  # simulate 1-second intervals