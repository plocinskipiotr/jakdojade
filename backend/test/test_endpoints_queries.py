from backend.src.endpoints_queries import get_stops
from backend.src.user import User


class TestEndpointsQueries:

    def test_get_stops(self):
        city = 'wroclaw'
        user = User(51.17569451, 16.99376387, 20)
        x = get_stops(city,user)
        assert x == [3539, 3538, 3770, 679, 3761]



    #
    # def get_stops(city: str, user: User, stop_limit=5):
    #     stop_list = session.query(TableToClass.parse(city + '_stops')).all()
    #     result = find_closest_stops(user, stop_list, stop_limit)
    #     return result