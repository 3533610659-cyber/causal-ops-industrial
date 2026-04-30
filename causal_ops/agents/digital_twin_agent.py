import numpy as np
from dtw import dtw

class DigitalTwinAgent:
    def __init__(self, model_path="hysys_model.hsc"):
        self.model_path = model_path

    def inject_fault_simulation(self, fault_chain):
        sim_curve = np.random.randn(100)
        return sim_curve

    def dtw_similarity(self, real_curve, sim_curve):
        distance, _ = dtw(real_curve, sim_curve, dist=np.linalg.norm)
        confidence_score = 1 / (1 + distance)
        return round(confidence_score, 2)