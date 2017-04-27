import sys

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Good(Base):
    __tablename__ = 'good'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    manufacturer = Column(String(80))
    price = Column(String(10))
    store_id = Column(Integer, ForeignKey('store.id'))
    store = relationship(Store)


engine = create_engine('sqlite:///storegood.db')
Base.metadata.create_all(engine)
