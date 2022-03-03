from backend.src.controller.trip import Trip
from backend.src.controller.gps_coordinates import GPS_Coordinates


class Stop():

    def __init__(self):
        self.id: int = 0
        self.name: str = ''
        self.gps_coordinates: GPS_Coordinates = GPS_Coordinates()
        self.trips: set[Trip] = set()

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def serialize(self):
        return {'stop': {'id': self.id,
                         'name': self.name,
                         'gps_coordinates': self.gps_coordinates.serialize()}
                }
