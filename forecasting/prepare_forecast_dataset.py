import pandas as pd


def prepare_forecast_dataset(timeseries, forecast_horizon, lag_features, lead_time=0):
    x = pd.concat({f'lag_{lag}': timeseries.shift(lag + lead_time)
                   for lag in range(1, lag_features+1)},
                  axis=1)
    y = pd.concat({f'step_{steps}': timeseries.shift(-steps)
                   for steps in range(0, forecast_horizon)},
                  axis=1)
    return x, y
