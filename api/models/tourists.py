from sqlalchemy import Column, String, Float, Integer
from db.config import Base, engine


class Tourists(Base):
    __tablename__ = 'tourists'
    id = Column(Integer, primary_key=True)
    autonomous_community = Column(String)
    data_type = Column(String)
    year = Column(Integer)
    month = Column(Integer)
    total = Column(Float)

Base.metadata.create_all(engine)
