import numpy as np


def shifted_log_diff(rates, shift=2.0):
    return np.log(rates + shift).diff(axis=0).iloc[1:]
