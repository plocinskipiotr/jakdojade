from backend.src.db_model import Routes, StopTimes, Stops, Trips


class WroclawRoutes(Routes):
    __tablename__ = 'wroclaw_routes'


class WroclawStopTimes(StopTimes):
    __tablename__ = 'wroclaw_stop_times'


class WroclawStops(Stops):
    __tablename__ = 'wroclaw_stops'


class WroclawTrips(Trips):
    __tablename__ = 'wroclaw_trips'
