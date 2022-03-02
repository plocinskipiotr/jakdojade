from backend.src.controller.gps_coordinates import GPS_Coordinates


class GPSCoordinatesBuilder():

    def __init__(self):
        self.gps_coordinates = GPS_Coordinates()

    def with_latitude(self, latitude: float):
        self.gps_coordinates.latitude = latitude
        return self

    def with_longitude(self, longitude: float):
        self.gps_coordinates.longitude = longitude
        return self

    def get_result(self) -> GPS_Coordinates:
        return self.gps_coordinates


class GPSCoordinatesDirector():

    @staticmethod
    def construct(latitude: float, longitude: float):
        return GPSCoordinatesBuilder() \
            .with_latitude(latitude) \
            .with_longitude(longitude) \
            .get_result()
