"""
Contains class DataExtractor which can be used to extract data
from different file formats

Example:
    extractor  = DataExtractor(path)
    data = extractor.extract_data()

Todo:
    * Add _extract_json implementation
    * Add _extract_xml implementation
"""

import logging
from csv import reader, Sniffer
from validate_path import validate_path_file


class DataExtractor():
    """This class can be used to extract data from different file formats

    arguments:
        path (str): path to extraction file

    note:
        currently supported formats:
        csv

    """

    def __init__(self, path: str):
        self.path = validate_path_file(path)

    def extract_data(self, **kwargs) -> list[list] | dict:
        """Extracts data from source file

        arguments:
            optional kwargs supported

        returns:
            data in format list[rows] or dict
        """
        extract_func = self._find_extract_func()
        return extract_func(**kwargs)

    def _find_extract_func(self) -> callable:
        """Chooses adequate extract function based on file extension

        Returns:
            data in format list or dict

        Raises:
            ValueError: If file extension is not supported

        """
        if self.path[-3:] == 'csv':
            return self._extract_csv
        if self.path[-3:] == 'txt':
            logging.warning('input data with .txt extension ' + str(self._extract_csv) + ' extractor chosen')
            return self._extract_csv
        elif self.path[-4:] == 'json':
            return self._extract_json
        elif self.path[-3:] == 'xml':
            return self._extract_xml
        else:
            raise ValueError('unknown file extension ' + self.path)

    def _extract_csv(self, **kwargs) -> list[list]:
        """Extracts CSV format

        Returns:
            data in format list[list]
        """
        with open(self.path, mode='r', newline='') as csvfile:
            dialect = Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            has_header = Sniffer().has_header(csvfile.read(1024))
            csvfile.seek(0)
            data = list(reader(csvfile, dialect, **kwargs))
        return data[1:] if has_header else data

    def _extract_json(path: str, **kwargs):
        """Extracts JSON format

        TODO:
            * Implementation
        """
        raise NotImplementedError('Extract json not implemented yet')

    def _extract_xml(path: str, **kwargs):
        """Extract XML format

        TODO:
            * Implementation
        """
        raise NotImplementedError('Extract xml not implemented yet')
