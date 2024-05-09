from sqlalchemy import Column, String, Float, Integer
from db.config import Base, engine


class Tourists(Base):
    __tablename__ = 'tourists'
    id = Column(Integer, primary_key=True)
    comunidad_autonoma = Column(String)
    tipo_dato = Column(String)
    periodo = Column(String)
    total = Column(Float)

Base.metadata.create_all(engine)
