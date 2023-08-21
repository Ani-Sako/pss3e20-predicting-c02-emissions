import pandas as pd


def prepare_forecast_dataset(timeseries, forecast_horizon, lag_features, lead_time=0):
    x = pd.concat({f'step_{steps}': timeseries.shift(steps + lead_time)
                   for steps in range(1, lag_features)},
                  axis=1)
    y = pd.concat({f'step_{steps}': timeseries.shift(-steps)
                   for steps in range(0, forecast_horizon-1)},
                  axis=1)
    return x, y
