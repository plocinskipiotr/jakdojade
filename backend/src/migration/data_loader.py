"""
Contains class DataLoader which can be used to load data
to database

Warning:
    only data in format list[list] is acceptable

Example:
    loader = DataLoader(db,'wroclaw')
    loader.load_data(data)
"""

from backend.src.model.db_service import DBService
from backend.src.model.db_table_to_class import TableToClass


class DataLoader():
    """This class can be used to load data to database

    arguments:
        db (DBService): DB management object
        table_name (str): target table name
    attributes:
        db (DBService): DB management object
        table_cls (class) : class connected to adequate table in db
    note:
        this class check implicitly if adequate sqlalchemy class bound to table
        exists, the table MUST be present in database schema.
    """

    def __init__(self, db: DBService, table_name: str):
        self.db = db
        self.table_cls = self.find_table_class(table_name)

    def load_data(self, data: list[list]):
        """loads data to database

        arguments:
            data in format list[list]

        """
        Session = self.db.get_sessionmaker()
        with Session.begin() as session:
            for item in data:
                el = self.table_cls(**item)
                session.add(el)

    def find_table_class(self, table_name: str):
        """finding corresponding class to table_name

        arguments:
            table_name (str): name of the table

        note:
            table_name and corresponding must be in
            TableToClassParser.table_class
        """
        return TableToClass.parse(table_name)
