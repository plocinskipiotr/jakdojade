"""
Contains class Datatransformer which can be used to transform data

Warning:
    only data in format list[list] is acceptable

Example:
    transformer = DataTransformer(lambda x: {'route_id': x[0], 'route_short_name': x[2], 'route_desc': x[4]})
    data = transformer(data)
"""


class DataTransformer():
    """This class can be used to transform data

    arguments:
        func (callable): transformation function

    note:
        data should be in format list[list]

    """

    def __init__(self, func: callable):
        self.func = func

    def transform(self, data: list[list]) -> list[list]:
        """Transformation function

        Returns:
            data in format list[list]
        """
        self.data = [self.func(item) for item in data]
        return self.data
