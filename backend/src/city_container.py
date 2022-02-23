"""
Contains class CityContainer and Singleton
"""

from constants import CITIES_FILE
from db_model import Routes
from validate_path import validate_path_file
from data_extractor import DataExtractor


class Singleton(type):
    """Standard singleton design pattern implementation in Python"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CityContainer(metaclass=Singleton):
    """ Class contains classes created from citites.txt file

        argument:
            path to cities.txt file

        attributes:
            POL_TO_ENG (dict): needed in translation polish special characters to english
            cities (dict): contains (table_name, class_name) pairs

        This class creates and stores classes for every city used in application.
        It is used with every load to db function (load needs the corresponding class in
        pair class-table. This is SQLAlchemy requirement.)

        Dynamically creating new types for every city eliminates the need to define new classes
        in db_model for every city

        This class can be seen as anti pattern, but I do not know how to avoid creating it.

    """
    POL_TO_ENG = {
        ord('ł'): ord('l'), ord('ą'): ord('a'), ord('ć'): ord('c'),
        ord('ę'): ord('e'), ord('ń'): ord('n'), ord('ó'): ord('o'),
        ord('ź'): ord('z'), ord('ż'): ord('z'), ord('ś'): ord('s')
    }

    def __init__(self, path=CITIES_FILE):
        self.path = validate_path_file(path)
        self.extractor = DataExtractor(path)
        self.cities = self.load_cities()

    def load_cities(self) -> dict:
        """creates new type for every city from input file

            Returns:
                dict(table_name : class_name)
        """
        csv_data = self.extractor.extract_data()
        data = dict()

        for row in csv_data:
            city_name = row[1].translate(self.POL_TO_ENG).lower()
            data[city_name] = self._add_city_class(city_name)

        return data

    def _add_city_class(self, name: str, base_cls=Routes) -> type:
        """creates new type based on Routes (db_model) abstract class"""
        return type(name.title(), (base_cls,), {'__tablename__': name.lower()})
