
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

import numpy as np

def rolling_mean(data, window=10):
    return np.convolve(data, np.ones(window)/window, mode='valid')

def cycle_stats(df):
    return {
        'mean_voltage': df['voltage'].mean(),
        'std_voltage': df['voltage'].std(),
        'capacity': df['discharge_ah'].max() - df['discharge_ah'].min()
    }

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

import numpy as np

def rolling_mean(data, window=10):
    return np.convolve(data, np.ones(window)/window, mode='valid')

def cycle_stats(df):
    return {
        'mean_voltage': df['voltage'].mean(),
        'std_voltage': df['voltage'].std(),
        'capacity': df['discharge_ah'].max() - df['discharge_ah'].min()
    }

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
