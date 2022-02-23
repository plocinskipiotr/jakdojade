"""
Contains class DataLoader which can be used to load data
to database

Warning:
    only data in format list[list] is acceptable

Example:
    loader = DataLoader(db,'wroclaw')
    loader.load_data(data)
"""

from city_container import CityContainer
from db_service import DBService
import sys


class DataLoader():
    """This class can be used to load data to database

    arguments:
        db (DBService): DB management object
        table_name (str): target table name
    attributes:
        db (DBService): DB management object
        cities (dict): hashmap in format {city_name (str) : city_class bound with table}
        table_cls (class) : class connected to adequate table in database
    note:
        this class check implicitly if adequate sqlalchemy class bound to table
        exists, the table MUST be present in database schema, there is no way to create
        table 'on the fly'.
    """

    def __init__(self, db: DBService, table_name: str):
        self.db = db
        self.cities = CityContainer().cities
        self.table_cls = self.find_table_class(table_name)

    def load_data(self, data: list[list]):
        """loads data to database

        arguments:
            data in format list[list]

        """
        Session = self.db.get_session()
        with Session.begin() as session:
            for item in data:
                el = self.table_cls(**item)
                session.add(el)

    def find_table_class(self, table_name: str):
        """finding corresponding class to table_name

        arguments:
            table_name (str): name of the table

        notes:
            corresponding classes can be found either in dynamically typed
            (cities) or in db_model file.
        """
        if table_name in self.cities.keys():
            return self.cities[table_name]
        else:
            return getattr(sys.modules['db_model'], table_name.title())
