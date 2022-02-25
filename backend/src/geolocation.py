from math import cos, sqrt


class Stop():

    def __init__(self, id, name, lat, lon):
        self.stop_id = id
        self.name = name
        self.geopoint = GeoPoint(lat, lon)


class GeoPoint():

    def __init__(self, latitude: float, longitude: float):
        self.longitude = longitude
        self.latitude = latitude

    def calc_distance(self, other: 'GeoPoint'):
        x = 69.1 * (self.latitude - other.latitude)
        y = 69.1 * (self.longitude - other.longitude) * cos(self.latitude / 57.3)
        return sqrt(x * x + y * y)
