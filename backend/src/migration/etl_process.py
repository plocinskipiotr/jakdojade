"""
Contains ETL processes

    classes:
        SimpleETL : simple extract transform load process

"""

from backend.src.model.db_service import DBService
from backend.src.migration.data_loader import DataLoader
from backend.src.migration.data_transformer import DataTransformer
from backend.src.migration.data_extractor import DataExtractor
from backend.src.controller.validate_path import validate_path
import os


class SimpleETL:
    """This class provides ETL processes"""

    def __init__(self, extractor: DataExtractor, transformer: DataTransformer, loader: DataLoader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def execute(self) -> None:
        """Executes ETL process"""
        data = self.extractor.extract_data()
        data = self.transformer.transform(data)
        self.loader.load_data(data)

    @staticmethod
    def file(path: str, func: callable, db: DBService):
        """Creates and executes etl process using data from file"""
        filename = path.split('/')[-1].split('.')[0]
        process = SimpleETL(DataExtractor(path),
                            DataTransformer(func),
                            DataLoader(db, filename))
        process.execute()

    @staticmethod
    def directory(path: str, func: callable, db: DBService):
        """Creates and executes etl process using data from directory"""
        path = validate_path(path)

        if os.path.isdir(path):
            for file in os.listdir(path):
                SimpleETL.file(path + '/' + file, func, db)
        else:
            raise OSError('Invalid path ' + path, 'accepting only directory path')
