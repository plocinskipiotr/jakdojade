from backend.src.endpoints_queries import get_stops, get_trips
from backend.src.user import User

if __name__ == '__main__':
    user_latitude = 51.11218871
    user_longitude = 17.06335752
    age = 25
    city = 'wroclaw'
    stops = get_stops(city, User(user_latitude, user_longitude, age), stop_limit=1)
    stop = stops[0]
    res = get_trips(city, stop)
