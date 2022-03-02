class Trip:

    def __init__(self):
        self.city: str = ''
        self.id: str = ''
        self.stop_timetables: dict = dict()

    def arrival_time_by_stop_id(self, id: int):
        return self.stop_timetables[id]['arrival']

    def departure_time_by_stop_id(self, id: int):
        return self.stop_timetables[id]['departure']

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __hash__(self):
        return int(self.id)
