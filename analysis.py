
import numpy as np

def health_index(capacity, initial_capacity):
    return (capacity / initial_capacity) * 100

def degradation_rate(capacities, times):
    if len(capacities) < 2:
        return 0.0
    coeff = np.polyfit(times, capacities, 1)
    return coeff[0]

import numpy as np

def estimate_eol(capacities, times, eol_threshold=0.8):
    rate = np.polyfit(times, capacities, 1)
    if rate[0] >= 0:
        return None
    return (eol_threshold - rate[1]) / rate[0]

def capacity_fade(initial, current):
    return ((initial - current) / initial) * 100
