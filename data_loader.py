from pathlib import Path

import geopandas as gpd
import pandas as pd


def load_penguin_data(filepath: str) -> pd.DataFrame:
    """Reads the CSV and handles standard pandas cleaning."""
    data_dir = Path("data")
    data = data_dir / filepath
    return pd.read_csv(data)


def convert_to_gdf(
    df: pd.DataFrame,
    lon_col: str = "longitude",
    lat_col: str = "latitude",
    target_crs: int = 3031,
) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df[lon_col], df[lat_col]), crs=4326
    ).to_crs(target_crs)
