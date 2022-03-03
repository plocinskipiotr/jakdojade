from math import cos, sqrt


class GPS_Coordinates():

    def __init__(self):
        self.latitude: int = 0
        self.longitude: int = 0

    def calc_distance(self, other: 'GPS_Coordinates'):
        x = 69.1 * (self.latitude - other.latitude)
        y = 69.1 * (self.longitude - other.longitude) * cos(self.latitude / 57.3)
        result = sqrt(x * x + y * y)
        return self._change_to_kilometers(result)

    def serialize(self):
        return {'latitude': self.latitude,
                'longitude': self.longitude
                }

    def __eq__(self, other):
        return self.latitude == other.latitude and \
               self.longitude == other.longitude

    def __ne__(self, other):
        return self.latitude != other.latitude and \
               self.longitude != other.longitude

    @staticmethod
    def _change_to_kilometers(val: float):
        return val / 0.62137
