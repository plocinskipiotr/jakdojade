from backend.src.controller.gps_coordinates_builder import GPS_Coordinates


class User():

    def __init__(self):
        self.age: int = 0
        self.gps_coordinates: GPS_Coordinates = GPS_Coordinates()
