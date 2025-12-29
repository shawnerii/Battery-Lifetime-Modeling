
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

import numpy as np
from scipy.optimize import curve_fit

class ExponentialModel:
    def __init__(self):
        self.params = None

    def _func(self, t, a, b, c):
        return a * np.exp(b * t) + c

    def fit(self, times, capacities):
        try:
            self.params, _ = curve_fit(self._func, times, capacities, p0=[1, -0.001, 0], maxfev=5000)
        except Exception:
            self.params = [1, -0.001, 0]
        return self

    def predict(self, t):
        return self._func(t, *self.params)

import numpy as np
from models import LinearModel, ExponentialModel

class EnsembleModel:
    def __init__(self):
        self.models = [LinearModel(), ExponentialModel()]
        self.weights = [0.5, 0.5]

    def fit(self, times, capacities):
        for m in self.models:
            m.fit(times, capacities)
        return self

    def predict(self, t):
        preds = [m.predict(t) for m in self.models]
        return np.average(preds, weights=self.weights)

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

import numpy as np
from scipy.optimize import curve_fit

class ExponentialModel:
    def __init__(self):
        self.params = None

    def _func(self, t, a, b, c):
        return a * np.exp(b * t) + c

    def fit(self, times, capacities):
        try:
            self.params, _ = curve_fit(self._func, times, capacities, p0=[1, -0.001, 0], maxfev=5000)
        except Exception:
            self.params = [1, -0.001, 0]
        return self

    def predict(self, t):
        return self._func(t, *self.params)
