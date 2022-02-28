from backend.src.stop import Stop
from backend.src.endpoints_queries import get_stops
from backend.src.user import User

if __name__ == '__main__':
    user_latitude = 51.14232537
    user_longitude = 17.127874
    age = 25
    city = 'wroclaw'
    user_stop_ids = get_stops(city, User(user_latitude, user_longitude, age), stop_limit=1)

    end_latitude = 51.13788049
    end_longitude = 17.07363454
    end_stop_ids = get_stops(city, User(end_latitude, end_longitude), stop_limit=1)
    # 3881   #611
    user_stops = [Stop(city, user_stop_id) for user_stop_id in user_stop_ids]
    end_stops = [Stop(city, end_stop_id) for end_stop_id in end_stop_ids]

    user_stops = user_stops[0]
    end_stops = end_stops[0]

    x = user_stops.next_departure(end_stops)

    y = 'BREAK'
