from sqlalchemy import Column, String, Float, Integer
from db.config import Base, engine


class AccommodationType(Base):
    __tablename__ = 'accommodation_type'
    id = Column(Integer, primary_key=True)
    accommodation_type_name = Column(String)
    paid_accommodation = Column(String)
    data_type = Column(String)
    year = Column(Integer)
    month = Column(Integer)
    total = Column(Float)

Base.metadata.create_all(engine)
