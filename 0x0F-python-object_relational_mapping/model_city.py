#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
file that contains the class definition of a City and an instance Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# from model_state import Base, State
# from sqlalchemy.orm import relationship


Base = declarative_base()


class City(Base):
    """
    A City class that inherits from Base linked to the MySQL table cities

    Attributes:
    id (int): an auto-generated, unique integer, can’t be null and
    is a primary key representes the id of a city
    name (str): a string with maximum 128 characters and can’t be
    null holds the name of the city
    state_id (int): represents a column of an integer, can’t be null
    and is a foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


# # using relationships
#     state = relationship('State', back_populates='cities')

# # Now we define the relationship in State class after City
# # class is fully defined
# State.cities = relationship('City', order_by=City.id, back_populates='state')
