
import numpy as np

def exponential_smoothing(data, alpha=0.3):
    result = [data[0]]
    for i in range(1, len(data)):
        result.append(alpha * data[i] + (1 - alpha) * result[-1])
    return np.array(result)
