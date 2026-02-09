import pandas as pd
from pathlib import Path

def index_plate_grid(path: Path) -> pd.DataFrame:
    """
    Reads all relevant metadata for a plate dataset,
    returns a dataframe with each row corresponding to an image.

    Args:
        path (Path): Input path for data

    Returns:
        pd.DataFrame: Dataframe containing image metadata

    """
    pass