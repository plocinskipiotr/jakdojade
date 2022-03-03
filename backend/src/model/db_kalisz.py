from backend.src.model.db_model import Routes, StopTimes, Stops, Trips


class KaliszRoutes(Routes):
    __tablename__ = 'kalisz_routes'


class KaliszStopTimes(StopTimes):
    __tablename__ = 'kalisz_stop_times'


class KaliszStops(Stops):
    __tablename__ = 'kalisz_stops'


class KaliszTrips(Trips):
    __tablename__ = 'kalisz_trips'
