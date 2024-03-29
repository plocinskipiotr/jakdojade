"""Contains UserBuilder class which can be used to create and initiate
User class instances.
"""

from backend.src.controller.user import User
from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector


class UserBuilder:
    """Builder for User class"""

    def __init__(self):
        self.user = User()

    def with_age(self, age: int):
        self.user.age = age
        return self

    def with_geopoint(self, lat: float, long: float):
        self.user.gps_coordinates = GPSCoordinatesDirector.construct(lat, long)
        return self

    def get_result(self) -> User:
        return self.user


class UserDirector:

    @staticmethod
    def construct(lat: float, long: float, age) -> User:
        """Builder construction method"""
        return UserBuilder() \
            .with_geopoint(lat, long) \
            .with_age(age) \
            .get_result()
