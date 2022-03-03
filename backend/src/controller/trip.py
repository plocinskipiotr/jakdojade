class Trip:

    def __init__(self):
        self.id: str = ''
        self.stop_timetables: dict = dict()

    def arrival_time(self, stop_id: int):
        return self.stop_timetables[stop_id]['arrival']

    def departure_time(self, stop_id: int):
        return self.stop_timetables[stop_id]['departure']

    def serialize(self):
        return {'id': self.id,
                'stop_timetables': self.stop_timetables
                }

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __hash__(self):
        return int(self.id)