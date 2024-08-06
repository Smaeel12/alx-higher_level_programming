#!/usr/bin/python3
"""
file that contains the class definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A State class that inherits from Base linked to the MySQL table states

    Attributes:
    id (int): an auto-generated, unique integer, can’t be null and
    is a primary key representes the id of a state
    name (str): a string with maximum 128 characters and can’t be
    null holds the name of the states
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement='auto')
    name = Column(String(128), nullable=False)
