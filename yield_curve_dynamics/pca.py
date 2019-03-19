import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def shifted_log_diff(rates, shift=2.0):
    return np.log(rates + shift).diff(axis=0).iloc[1:]


def perform_pca(rate_changes):
    pca = PCA()
    pca.fit(rate_changes)
    return pca


def plot_pca1(pca):
    fig, ax = plt.subplots(figsize=(12, 8))
    normalized_sv = pca.singular_values_ / pca.singular_values_.sum()
    ax.bar(range(len(normalized_sv)), normalized_sv)
    ax.plot(np.cumsum(normalized_sv), 'r')
    return fig, ax


def plot_pca2(pca):
    fig, ax = plt.subplots(figsize=(12, 8))
    normalized_sv = pca.explained_variance_ratio_
    ax.bar(range(len(normalized_sv)), normalized_sv)
    ax.plot(np.cumsum(normalized_sv), 'r')
    return fig, ax


def plot_pca_components(pca):
    plt.plot(pca.components_[:3, :].T)
    plt.legend(['first', 'second', 'third'])
