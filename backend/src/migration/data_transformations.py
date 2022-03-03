POL_TO_ENG = {ord('ł'): ord('l'),
              ord('ą'): ord('a'),
              ord('ć'): ord('c'),
              ord('ę'): ord('e'),
              ord('ń'): ord('n'),
              ord('ó'): ord('o'),
              ord('ź'): ord('z'),
              ord('ż'): ord('z'),
              ord('ś'): ord('s')
              }


def route_trans() -> callable:
    return lambda x: {'route_id': x[0], 'route_short_name': x[2], 'route_desc': x[4]}


def city_trans() -> callable:
    return lambda x: {'city_id': x[0], 'city_name': x[1].translate(POL_TO_ENG).lower()}


def stop_times_trans() -> callable:
    return lambda x: {'trip_id': x[0], 'arrival_time': x[1], 'departure_time': x[2], 'stop_id': x[3]}


def stop_trans() -> callable:
    return lambda x: {'stop_id': x[0], 'stop_name': x[2], 'stop_lat': x[3], 'stop_lon': x[4]}


def trips_trans() -> callable:
    return lambda x: {'route_id': x[0], 'trip_id': x[2], 'trip_headsign': x[3], 'direction_id': x[4]}
