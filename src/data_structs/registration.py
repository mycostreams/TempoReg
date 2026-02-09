from dataclasses import dataclass
from enum import Enum

class RegistrationType(Enum):
    AFFINE = "affine"
    TRANSLATION = "translation"

class StaticRegDelta:
    reference: int | tuple[int, int]
    target: int | tuple[int, int]
    delta_x: float
    delta_y: float
    delta_theta: float
    confidence: float

class TranslationRegDelta:
    reference: int | tuple[int, int]
    target: int | tuple[int, int]
    delta_x: float
    delta_y: float
    confidence: float

@dataclass
class ColumnRegistration:
    """
    class representing the output of registration performed on a full column.
    Registration can either be affine (including rotatio, no scale) or translation-only.

    Will contain methods to evaluate its own result, so that outliers can be handled later.
    """
    registration_type: RegistrationType
    grid_position: tuple[int, int]
    neighbor_deltas: list[StaticRegDelta | TranslationRegDelta]

@dataclass
class PlateRegistration:
    """
    class to represent the output of an entire plate stitching. Will only hold the registration deltas, no solution yet.
    """
    time_index:int
    plate_deltas: list[StaticRegDelta | TranslationRegDelta]