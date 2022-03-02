from backend.src.controller.trip import Trip
from backend.src.controller.gps_coordinates import GPS_Coordinates


class Stop():

    def __init__(self):
        self.city: str = ''
        self.id: int = 0
        self.gps_coordinates: GPS_Coordinates = GPS_Coordinates()
        self.trips: set[Trip] = set()

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id
