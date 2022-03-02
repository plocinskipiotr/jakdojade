from backend.src.controller.user import User
from backend.src.controller.user_builder import UserDirector


class TestUser:

    def test_user(self):
        u = UserDirector.construct(51.09193846, 17.04004368, 25)
        assert isinstance(u, User)
