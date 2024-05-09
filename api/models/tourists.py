from sqlalchemy import Column, String, Float, Integer
from db.config import Base, engine


class Tourists(Base):
    __tablename__ = 'tourists'
    id = Column(Integer, primary_key=True)
    autonomous_community = Column(String)
    data_type = Column(String)
    period = Column(String)
    total = Column(Float)

Base.metadata.create_all(engine)
