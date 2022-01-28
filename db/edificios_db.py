from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class EdificioDB(Base):
    __tablename__ = "edificio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    altura = Column(Integer)
    ano = Column(Integer)
    pais = Column(String)
    descripcion = Column(String)
    srcimagen = Column(String)
    altimagen = Column(String)


Base.metadata.create_all(bind=engine)