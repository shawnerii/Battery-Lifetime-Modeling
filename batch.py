
import numpy as np

def process_batch(battery_dict, func, **kwargs):
    results = {}
    for key, data in battery_dict.items():
        try:
            results[key] = func(data, **kwargs)
        except Exception as e:
            results[key] = None
    return results

from concurrent.futures import ThreadPoolExecutor
import numpy as np

def parallel_batch(battery_dict, func, max_workers=4):
    keys = list(battery_dict.keys())
    def process(k):
        return k, func(battery_dict[k])
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        results = dict(ex.map(process, keys))
    return results

import numpy as np

def process_batch(battery_dict, func, **kwargs):
    results = {}
    for key, data in battery_dict.items():
        try:
            results[key] = func(data, **kwargs)
        except Exception as e:
            results[key] = None
    return results

from concurrent.futures import ThreadPoolExecutor
import numpy as np

def parallel_batch(battery_dict, func, max_workers=4):
    keys = list(battery_dict.keys())
    def process(k):
        return k, func(battery_dict[k])
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        results = dict(ex.map(process, keys))
    return results
