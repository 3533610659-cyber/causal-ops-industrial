import numpy as np

def load_baseline_data():
    return np.zeros(100)

def generate_test_data():
    dcs = np.random.randn(100)
    vibration = np.random.randn(100)
    thermal = np.random.randn(100)
    return dcs, vibration, thermal