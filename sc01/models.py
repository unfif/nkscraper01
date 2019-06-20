from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Text, Date, DateTime, Float#, Boolean, LargeBinary, SmallInteger

from scrapy.utils.project import get_project_settings
# import settings

Base = declarative_base()

def db_connect():
    """Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance"""
    return create_engine(get_project_settings().get('URI'))

def create_table(engine):
    Base.metadata.create_all(engine)

class nkdb_races(Base):
    __tablename__ = "nkdb_races"

    id = Column(Text, primary_key=True)
    place = Column(Text)
    racenum = Column(Integer)
    title = Column(Text)
    date = Column(Date)
    schedule = Column(Text)
    classification = Column(Text)
    category = Column(Text)
    placenum = Column(Integer, primary_key=True)
    postnum = Column(Integer)
    horsenum = Column(Integer)
    horsename = Column(Text)
    sex = Column(Text)
    age = Column(Integer)
    weight = Column(Float)
    jockey = Column(Text)
    time = Column(Text)
    margin = Column(Text)
    position = Column(Text)
    last3f = Column(Float)
    odds = Column(Float)
    fav = Column(Integer)
    horseweight = Column(Integer)
    horseweightdiff = Column(Integer)
    trainer = Column(Text)
    owner = Column(Text)
    addedmoney = Column(Integer)
