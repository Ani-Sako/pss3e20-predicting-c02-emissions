import numpy as np
import pandas as pd


def fourier_features(time_dummy, fourier_feature_frequencies, time_dummy_frequency=1):
    time = np.array(time_dummy, dtype=np.float32)
    fourier_feature_dict = {}
    for frequency in fourier_feature_frequencies:
        theta = 2*np.pi*(frequency/time_dummy_frequency)*time
        fourier_feature_dict.update({f'sin_{frequency}': np.sin(theta),
                                     f'cos_{frequency}': np.cos(theta)})

    return pd.DataFrame(fourier_feature_dict, index=time_dummy)