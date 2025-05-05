
import numpy as np

def exponential_smoothing(data, alpha=0.3):
    result = [data[0]]
    for i in range(1, len(data)):
        result.append(alpha * data[i] + (1 - alpha) * result[-1])
    return np.array(result)

import numpy as np

def kalman_filter(data, process_noise=1e-5, measurement_noise=1e-2):
    n = len(data)
    estimates = np.zeros(n)
    P = 1.0
    x = data[0]
    for i, z in enumerate(data):
        P += process_noise
        K = P / (P + measurement_noise)
        x = x + K * (z - x)
        P = (1 - K) * P
        estimates[i] = x
    return estimates
