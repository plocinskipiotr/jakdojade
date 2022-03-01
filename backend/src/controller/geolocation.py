from math import cos, sqrt


class GeoPoint():

    def __init__(self, coords: dict):
        self.latitude = coords['lat']
        self.longitude = coords['long']

    def calc_distance(self, other: 'GeoPoint'):
        x = 69.1 * (self.latitude - other.latitude)
        y = 69.1 * (self.longitude - other.longitude) * cos(self.latitude / 57.3)
        result = sqrt(x * x + y * y)
        return self._change_to_kilometers(result)

    @staticmethod
    def _change_to_kilometers(val: float):
        return val / 0.62137
