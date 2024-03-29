"""Contains GPS coordinates class"""

from math import cos, sqrt


class GPSCoordinates:
    """Represents Global Positioning System coordinates"""

    def __init__(self):
        self.latitude: int = 0
        self.longitude: int = 0

    def calc_distance(self, other: 'GPSCoordinates') -> float:
        """calculates distance between two GPS points"""
        x = 69.1 * (self.latitude - other.latitude)
        y = 69.1 * (self.longitude - other.longitude) * cos(self.latitude / 57.3)
        result = sqrt(x * x + y * y)
        return self._change_to_kilometers(result)

    def serialize(self) -> dict:
        """serialize instance attributes to dictionary"""
        return {'latitude': self.latitude,
                'longitude': self.longitude}

    @staticmethod
    def _change_to_kilometers(val: float) -> float:
        """changing miles to kilometers"""
        return val / 0.62137

    def __eq__(self, other):
        return self.latitude == other.latitude and \
               self.longitude == other.longitude

    def __ne__(self, other):
        return self.latitude != other.latitude and \
               self.longitude != other.longitude
