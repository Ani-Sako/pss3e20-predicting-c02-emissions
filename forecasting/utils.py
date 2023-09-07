import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def pca_timeseries(data, num_components):
    pca = PCA(n_components=num_components)
    pca.fit(data)
    dfpca = pca.transform(data)
    return pca, pd.DataFrame(dfpca, columns=['ts'+str(i+1) for i in range(num_components)])


def remove_nulldata(x_data, y_data):
    null_indices = pd.concat([x_data, y_data], axis=1).isna().any(axis=1)
    valid_indices = null_indices[null_indices == False].index
    x_train_residual = x_data.loc[valid_indices, :]
    y_train_residual = y_data.loc[valid_indices, :]
    return  x_train_residual, y_train_residual
