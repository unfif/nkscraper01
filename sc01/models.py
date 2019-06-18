from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Text, Date, DateTime, Float#, Boolean, LargeBinary, SmallInteger

from scrapy.utils.project import get_project_settings
# import settings

DeclarativeBase = declarative_base()

def db_connect():
    """Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance"""
    return create_engine(get_project_settings().get('URI'))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class nkdb_races(DeclarativeBase):
    __tablename__ = "nkdb_races"

    id = Column('id', Text, primary_key=True)
    place = Column('place', Text)
    racenum = Column('racenum', Integer)
    title = Column('title', Text)
    date = Column('date', Date)
    schedule = Column('schedule', Text)
    classification = Column('classification', Text)
    category = Column('category', Text)
    placenum = Column('placenum', Integer, primary_key=True)
    postnum = Column('postnum', Integer)
    horsenum = Column('horsenum', Integer)
    horsename = Column('horsename', Text)
    sex = Column('sex', Text)
    age = Column('age', Integer)
    weight = Column('weight', Float)
    jockey = Column('jockey', Text)
    time = Column('time', Text)
    margin = Column('margin', Text)
    position = Column('position', Text)
    last3f = Column('last3f', Float)
    odds = Column('odds', Float)
    fav = Column('fav', Integer)
    horseweight = Column('horseweight', Integer)
    horseweightdiff = Column('horseweightdiff', Integer)
    trainer = Column('trainer', Text)
    owner = Column('owner', Text)
    addedmoney = Column('addedmoney', Integer)
