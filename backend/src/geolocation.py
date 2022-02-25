from math import cos, sqrt


class GeoPoint():

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def calc_distance(self, other: 'GeoPoint'):
        x = 69.1 * (self.latitude - other.latitude)
        y = 69.1 * (self.longitude - other.longitude) * cos(self.latitude / 57.3)
        return sqrt(x * x + y * y)
