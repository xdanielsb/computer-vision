"""
    Tracking over images, this project
    track and object in movement
"""
from enum import Enum

class Matcher(Enum):
    ORB = 1
    SIFT = 2
    SURF  = 3
