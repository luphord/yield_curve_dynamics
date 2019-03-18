import numpy as np
import pandas as pd


week = 1.0 / 52.0
month = 1.0 / 12.0
year = 1.0
key_tenors = np.array([0, 1*week, 2*week, 3*week,
                       1*month, 2*month, 3*month, 4*month, 5*month,
                       6*month, 7*month, 8*month, 9*month, 10*month, 11*month,
                       1*year, 2*year, 3*year, 4*year, 5*year, 7*year,
                       10*year, 15*year, 20*year, 25*year, 30*year])


def keyrates(dates_and_curves):
    return pd.DataFrame([curve(key_tenors) for dt, curve in dates_and_curves],
                        columns=np.array(key_tenors).round(2),
                        index=[dt for dt, curve in dates_and_curves])
