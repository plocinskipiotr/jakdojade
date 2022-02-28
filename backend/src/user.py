from backend.src.geolocation import GeoPoint


class User():

    def __init__(self, latitude, longitude, age=17):
        self.age = age
        self.geopoint = GeoPoint(latitude, longitude)
