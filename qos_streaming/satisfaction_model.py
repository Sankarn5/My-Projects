from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Simple DNN for satisfaction classification
def build_satisfaction_model():
    model = Sequential([
        Dense(32, input_dim=3, activation='relu'),
        Dense(16, activation='relu'),
        Dense(1, activation='sigmoid')  # 0 = dissatisfied, 1 = satisfied
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Dummy training for illustration
def train_dummy_model():
    model = build_satisfaction_model()
    X = np.random.rand(1000, 3) * [6000, 5, 60]  # bitrate, buffer, fps
    y = np.random.randint(0, 2, 1000)
    model.fit(X, y, epochs=5, verbose=0)
    return model