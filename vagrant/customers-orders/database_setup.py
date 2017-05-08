import sys

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    manufacturer = Column(String(80))
    price = Column(String(10))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship(Customer)


engine = create_engine('sqlite:///customerorder.db')
Base.metadata.create_all(engine)
