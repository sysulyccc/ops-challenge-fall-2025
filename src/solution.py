# test 111
import polars as pl
import numpy as np

class ops:
    @staticmethod
    def rolling_regbeta(col_x_or_expr, col_y_or_expr, window: int) -> pl.Expr:
        if isinstance(col_x_or_expr, str):
            expr_x = pl.col(col_x_or_expr)
        else:
            expr_x = col_x_or_expr

        if isinstance(col_y_or_expr, str):
            expr_y = pl.col(col_y_or_expr)
        else:
            expr_y = col_y_or_expr

        cov_xy = pl.rolling_cov(expr_x, expr_y, window_size=window, ddof=1, min_samples=2) # ddof=1
        var_x = expr_x.rolling_var(window_size=window, ddof=1, min_samples=2)

        # Must use the same var_x threshold
        # When var_x is close to 0, beta = 0
        return pl.when(var_x < 1e-6).then(0.0).otherwise(cov_xy / var_x).alias("rolling_regbeta")


def ops_rolling_regbeta(input_path: str, window: int = 20) -> np.ndarray:
    res = (
        pl.scan_parquet(input_path)
        .with_columns([
            pl.col("Close"),
            pl.col("Low")
        ])
        .select(
            ops.rolling_regbeta("Low", "Close", window).over("symbol")
        )
    ).collect()
    return res.to_numpy()
