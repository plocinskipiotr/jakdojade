import pytest

from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.user import User
from backend.src.controller.user_builder import UserDirector


class TestUser:

    def test_user_happy_path(self):
        """Constructing user with correct arguments"""
        u = UserDirector.construct(51.09193846, 17.04004368, 25)
        assert isinstance(u, User)
        assert u.gps_coordinates == GPSCoordinatesDirector.construct(51.09193846, 17.04004368)
        assert u.age == 25

    def test_user_without_data(self):
        """Constructing user without arguments"""
        with pytest.raises(TypeError):
            u = UserDirector.construct()

    def test_user_without_age(self):
        """Constructing user without age argument"""
        with pytest.raises(TypeError):
            u = UserDirector.construct(51.09193846, 17.04004368)
