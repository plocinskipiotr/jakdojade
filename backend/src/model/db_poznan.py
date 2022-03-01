from backend.src.model.db_base import Routes, StopTimes, Stops, Trips


class PoznanRoutes(Routes):
    __tablename__ = 'poznan_routes'


class PoznanStopTimes(StopTimes):
    __tablename__ = 'poznan_stop_times'


class PoznanStops(Stops):
    __tablename__ = 'poznan_stops'


class PoznanTrips(Trips):
    __tablename__ = 'poznan_trips'
