from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.stop_builder import StopStandardDirector

STOP_3144 = StopStandardDirector.construct(3144, 'KOSZAROWA (Szpital)',
                                           GPSCoordinatesDirector.construct(51.14166292, 17.06477615))
STOP_4517 = StopStandardDirector.construct(4517, 'Ogród Botaniczny',
                                           GPSCoordinatesDirector.construct(51.1161181, 17.05107322))
STOP_4588 = StopStandardDirector.construct(4588, 'Bierutowska 75',
                                           GPSCoordinatesDirector.construct(51.1361181, 17.05507322))
