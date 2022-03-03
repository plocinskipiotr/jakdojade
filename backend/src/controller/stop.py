from backend.src.controller.gpscoordinates import GPSCoordinates


class Stop:

    def __init__(self):
        self.ID: int = 0
        self.name: str = ''
        self.gps_coordinates: GPSCoordinates = GPSCoordinates()

    def __eq__(self, other):
        return self.ID == other.ID

    def __ne__(self, other):
        return self.ID != other.ID

    def serialize(self):
        return {'stop': {'id': self.ID,
                         'name': self.name,
                         'gps_coordinates': self.gps_coordinates.serialize()}
                }
