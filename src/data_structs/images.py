from dataclasses import dataclass
import datetime
from pathlib import Path


@dataclass
class SingleImage:
    """
    Class representing a single image within a grid position and time point.
    """
    grid_pos: tuple[int, int]
    time_index: int
    time_stamp: datetime.datetime
    image_path: Path