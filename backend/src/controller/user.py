from backend.src.controller.geolocation import GeoPoint


class User():

    def __init__(self, coords: dict, age=17):
        self.age = age
        self.geopoint = GeoPoint(coords)
