import pandas as pd
from data_structs.images import SingleImage
from src.io.read_grid import index_plate_grid
from pathlib import Path

class Dataset:
    """
    Overarching class representing a full plate dataset. Contains data on all temporal layers, as well as general metadata.
    Will be used to get other objects which are subsets of internal data.
    """
    def __init__(self, path: Path):
        """
        Initializes the Plate object by reading data from the specified path.

        Args:
            path (Path): The file path to the plate dataset.
        """
        self.plate_frame = index_plate_grid(path)

    def time_index(self, time_index: int):
        return SinglePlate(self.plate_frame[self.plate_frame['time_index'] == time_index].reset_index(drop=True))
    
class SinglePlate:
    """
    Class representing a single plate at a specific time point. Contains data for all spatial layers at that time point.
    """
    def __init__(self, plate_frame: pd.DataFrame):
        self.plate_frame = plate_frame

        # check if the plate_frame contains only one time point
        if len(self.plate_frame['time_index'].unique()) > 1:
            raise ValueError("The provided plate_frame contains multiple time points. Please provide a plate_frame with only one time point.")

class SingleColumn:
    """
    Class representing a single grid position with temporal data. 
    """
    def __init__(self, plate_frame: pd.DataFrame):
        self.plate_frame = plate_frame
        self.plate_frame = plate_frame.sort_values(by='time_index').reset_index(drop=True)
        self.images = unpack_dataframe(plate_frame)

        # check if the plate_frame contains only one grid position
        if len(self.plate_frame['grid_position'].unique()) > 1:
            raise ValueError("The provided plate_frame contains multiple grid positions. Please provide a plate_frame with only one grid position.")
    def register(self):
        pass



def unpack_dataframe(frame: pd.DataFrame) -> list[SingleImage]:
    """
    Unpacks a dataframe containing metadata for a single grid position and time point into a list of SingleImage objects.

    Args:
        frame (pd.DataFrame): Dataframe containing metadata for a single grid position and time point.

    Returns:
        list[SingleImage]: List of SingleImage objects representing the images in the dataframe.
    """
    images = []
    for _, row in frame.iterrows():
        image = SingleImage(
            grid_pos=row['grid_position'],
            time_index=row['time_index'],
            time_stamp=row['time_stamp'],
            image_path=row['image_path']
        )
        images.append(image)
    return images