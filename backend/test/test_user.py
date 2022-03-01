from backend.src.controller.user import User


class TestUser:

    def test_user(self):
        age = 20
        coords = {'latitude': 51.17569451,
                  'longitude': 16.99376387}
        user = User(coords, age)
        assert isinstance(user,User)
