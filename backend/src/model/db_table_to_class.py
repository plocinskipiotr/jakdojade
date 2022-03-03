from backend.src.model.db_kalisz import KaliszRoutes, KaliszStops, KaliszTrips, KaliszStopTimes
from backend.src.model.db_model import Cities
from backend.src.model.db_poznan import PoznanRoutes, PoznanStops, PoznanTrips, PoznanStopTimes
from backend.src.model.db_wroclaw import WroclawRoutes, WroclawTrips, WroclawStopTimes, WroclawStops


class TableToClass:
    table_class = {
        'cities': Cities,
        'wroclaw_routes': WroclawRoutes,
        'wroclaw_stops': WroclawStops,
        'wroclaw_trips': WroclawTrips,
        'wroclaw_stop_times': WroclawStopTimes,
        'poznan_routes': PoznanRoutes,
        'poznan_stops': PoznanStops,
        'poznan_trips': PoznanTrips,
        'poznan_stop_times': PoznanStopTimes,
        'kalisz_routes': KaliszRoutes,
        'kalisz_stops': KaliszStops,
        'kalisz_trips': KaliszTrips,
        'kalisz_stop_times': KaliszStopTimes,
    }

    @classmethod
    def parse(cls, table_name):
        try:
            return cls.table_class[table_name]
        except KeyError:
            raise KeyError('Error during parsing table name to corresponding class name,\n'
                           'table_class content: ' + str(TableToClass.table_class))
