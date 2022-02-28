from backend.src.user import User


class TestUser:

    def test_user(self):
        age = 20
        latitude = 51.17569451
        longitude = 16.99376387
        user = User(latitude, longitude, age)
