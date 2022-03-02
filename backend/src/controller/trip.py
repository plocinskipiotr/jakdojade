class Trip:

    def __init__(self):
        self.city: str = ''
        self.id: str = ''
        self.stop_timetables: dict[str, tuple[str, str]] = dict()

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __hash__(self):
        return int(self.id)
