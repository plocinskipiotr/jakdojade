from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.user import User
from backend.src.controller.user_builder import UserDirector


class TestUser:

    def test_user(self):
        u = UserDirector.construct(51.09193846, 17.04004368, 25)
        assert isinstance(u, User)
        assert u.gps_coordinates == GPSCoordinatesDirector.construct(51.09193846, 17.04004368)
        assert u.age == 25
