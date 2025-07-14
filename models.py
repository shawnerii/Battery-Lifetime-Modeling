
import numpy as np

class LinearModel:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, times, capacities):
        coeff = np.polyfit(times, capacities, 1)
        self.slope, self.intercept = coeff
        return self

    def predict(self, t):
        return self.slope * t + self.intercept
