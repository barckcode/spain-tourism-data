from sqlalchemy import Column, String, Float, Integer
from db.config import Base, engine


class AccessRoad(Base):
    __tablename__ = 'access_road'
    id = Column(Integer, primary_key=True)
    access_road_type = Column(String)
    data_type = Column(String)
    year = Column(Integer)
    month = Column(Integer)
    total = Column(Float)

Base.metadata.create_all(engine)
