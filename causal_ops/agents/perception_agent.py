import numpy as np
from sklearn.preprocessing import StandardScaler

class MultimodalPerceptionAgent:
    def __init__(self, baseline_model, sampling_rate=0.1):
        self.scaler = StandardScaler()
        self.baseline = baseline_model
        self.sampling_rate = sampling_rate

    def data_preprocess(self, dcs_data, vibration_data, thermal_data):
        multi_data = np.hstack([dcs_data, vibration_data, thermal_data])
        return self.scaler.fit_transform(multi_data)

    def anomaly_detection(self, real_time_data):
        deviation = np.abs(real_time_data - self.baseline)
        anomaly_nodes = np.where(deviation > 0.15)[0]
        return anomaly_nodes

    def extract_anomaly_subgraph(self, full_causal_graph, anomaly_nodes):
        subgraph = full_causal_graph.subgraph(anomaly_nodes)
        return subgraph