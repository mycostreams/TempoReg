from data_structs.images import SingleImage
from data_structs.registration import ColumnRegistration


def register_column(
        column: list[SingleImage],
) -> ColumnRegistration:
    """
    Function to perform registration on a single column. Will return a ColumnRegistration object containing the registration deltas for each time point in the column.

    Args:
        column (SingleColumn): SingleColumn object containing the images and metadata for a single grid position.

    Returns:
        ColumnRegistration: ColumnRegistration object containing the registration deltas for each time point in the column.
    """
    pass