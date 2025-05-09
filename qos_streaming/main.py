from data_simulator import simulate_viewer_data
from sentiment_analysis import analyze_sentiment
from satisfaction_model import train_dummy_model
from qos_manager import qos_adjustment
import numpy as np

# Load DNN model
model = train_dummy_model()

# Start streaming simulation
stream = simulate_viewer_data()
print("⏳ Starting QoS Manager...\n")

for _ in range(10):  # Limit to 10 entries for demo
    data = next(stream)
    sentiment_label, sentiment_score = analyze_sentiment(data['message'])

    # Prepare input features
    input_features = np.array([[data['bitrate'], data['buffering_time'], data['fps']]])
    satisfaction_prob = model.predict(input_features)[0][0]
    decision = qos_adjustment(satisfaction_prob)

    print(f"👤 Viewer {data['viewer_id']} | Sentiment: {sentiment_label} ({sentiment_score:.2f}) | "
          f"Satisfaction Score: {satisfaction_prob:.2f} => 🛠️ Action: {decision}")