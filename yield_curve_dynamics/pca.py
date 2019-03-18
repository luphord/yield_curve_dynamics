import numpy as np
from sklearn.decomposition import PCA


def shifted_log_diff(rates, shift=2.0):
    return np.log(rates + shift).diff(axis=0).iloc[1:]


def perform_pca(rate_changes):
    pca = PCA()
    pca.fit(rate_changes)
    return pca
