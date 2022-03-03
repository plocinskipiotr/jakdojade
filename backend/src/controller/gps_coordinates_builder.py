"""Contains builder for GPS coordinates class"""
from backend.src.controller.gpscoordinates import GPSCoordinates


class GPSCoordinatesBuilder:
    """Builder for GPS coordinates class"""

    def __init__(self):
        self.gps_coordinates = GPSCoordinates()

    def with_latitude(self, latitude: float):
        self.gps_coordinates.latitude = latitude
        return self

    def with_longitude(self, longitude: float):
        self.gps_coordinates.longitude = longitude
        return self

    def get_result(self) -> GPSCoordinates:
        return self.gps_coordinates


class GPSCoordinatesDirector:

    @staticmethod
    def construct(latitude: float, longitude: float) -> GPSCoordinates:
        """Construct builder method"""
        return GPSCoordinatesBuilder() \
            .with_latitude(latitude) \
            .with_longitude(longitude) \
            .get_result()
