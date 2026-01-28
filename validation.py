
import numpy as np
import pandas as pd

def validate_cycle(df):
    issues = []
    if df.empty:
        issues.append('empty dataframe')
    if df['voltage'].isnull().any():
        issues.append('null voltages')
    if (df['voltage'] < 0).any():
        issues.append('negative voltages')
    return issues

def check_continuity(times):
    gaps = np.diff(times)
    return gaps.max() if len(gaps) > 0 else 0

import numpy as np
import pandas as pd

def validate_cycle(df):
    issues = []
    if df.empty:
        issues.append('empty dataframe')
    if df['voltage'].isnull().any():
        issues.append('null voltages')
    if (df['voltage'] < 0).any():
        issues.append('negative voltages')
    return issues

def check_continuity(times):
    gaps = np.diff(times)
    return gaps.max() if len(gaps) > 0 else 0
