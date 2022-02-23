from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase

Base = declarative_base()


class Cities(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String, nullable=False)

    def __repr__(self):
        return "<Cities(city_id={0}, city_name={1})>".format(self.city_id, self.city_name)


class Routes(AbstractConcreteBase, Base):
    route_id = Column(String, primary_key=True)
    route_short_name = Column(String, nullable=False)
    route_desc = Column(String, nullable=False)

    @classmethod
    def __repr__(self):
        return "<Routes(route_id={0}, route_short_name={1}, route_desc={2})>" \
            .format(self.route_id, self.route_short_name, self.route_desc)
