
import numpy as np

def health_index(capacity, initial_capacity):
    return (capacity / initial_capacity) * 100

def degradation_rate(capacities, times):
    if len(capacities) < 2:
        return 0.0
    coeff = np.polyfit(times, capacities, 1)
    return coeff[0]
