import pandas as pd


def summarize_density_by_building(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Simple grouped summary to support spatial analysis stage."""
    return (
        df_clean.groupby("building", dropna=False)["Density"]
        .agg(["count", "mean", "median", "std"])
        .reset_index()
    )
