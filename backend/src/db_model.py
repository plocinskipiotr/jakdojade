from sqlalchemy import Column, Integer, String, VARCHAR, FLOAT
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase

Base = declarative_base()


class Cities(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(VARCHAR, nullable=False)

    def __repr__(self):
        return "<Cities(city_id={0}, city_name={1})>".format(self.city_id, self.city_name)

    def serialize(self):
        return {self.city_id: self.city_name}


class Routes(AbstractConcreteBase, Base):
    route_id = Column(String, primary_key=True)
    route_short_name = Column(String, nullable=False)
    route_desc = Column(String, nullable=False)

    def __repr__(self):
        return "<Routes(route_id={0}, route_short_name={1}, route_desc={2})>" \
            .format(self.route_id, self.route_short_name, self.route_desc)

    def serialize(self):
        return {'route_id': self.route_id,
                'route_short_name': self.route_short_name,
                'route_desc': self.route_desc}


class StopTimes(AbstractConcreteBase, Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    trip_id = Column(String)
    arrival_time = Column(String)
    departure_time = Column(String)
    stop_id = Column(Integer)


class Stops(AbstractConcreteBase, Base):
    stop_id = Column(Integer, primary_key=True)
    stop_name = Column(String)
    stop_lat = Column(FLOAT)
    stop_lon = Column(FLOAT)

    def serialize(self):
        return {'stop_id': self.stop_id,
                'stop_name': self.stop_name,
                'stop_lat': self.stop_lat,
                'stop_lon': self.stop_lon}


class Trips(AbstractConcreteBase, Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    route_id = Column(String, primary_key=True)
    trip_id = Column(String)
    trip_headsign = Column(String)
    direction_id = Column(Integer)
