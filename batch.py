
import numpy as np

def process_batch(battery_dict, func, **kwargs):
    results = {}
    for key, data in battery_dict.items():
        try:
            results[key] = func(data, **kwargs)
        except Exception as e:
            results[key] = None
    return results
