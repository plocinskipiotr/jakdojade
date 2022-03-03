"""Contains User class which represents application user"""

from backend.src.controller.gps_coordinates_builder import GPSCoordinates


class User:
    """Represents application user"""

    def __init__(self):
        self.age: int = 0
        self.gps_coordinates: GPSCoordinates = GPSCoordinates()
