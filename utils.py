
import numpy as np

def normalize(data):
    mn, mx = np.min(data), np.max(data)
    if mx == mn:
        return np.zeros_like(data)
    return (data - mn) / (mx - mn)

def zscore(data):
    mu, sigma = np.mean(data), np.std(data)
    if sigma == 0:
        return np.zeros_like(data)
    return (data - mu) / sigma
