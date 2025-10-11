import pandas as pd
import numpy as np


def ops_rolling_rank(input_path: str, window: int = 20) -> np.ndarray:
    df = pd.read_parquet(input_path)

    def rolling_dense_rank(series):
        def rank_window(window_data):
            if len(window_data) == 0:
                return np.nan
            return window_data.rank(method='dense', ascending=False).iloc[-1]

        return series.rolling(window=window, min_periods=1).apply(
            rank_window, raw=False
        )

    ranks = df.groupby('symbol', group_keys=False)['Close'].apply(
        rolling_dense_rank
    )

    res = ranks.values.astype(np.float32)
    return res[:, None] # must be [N, 1]

