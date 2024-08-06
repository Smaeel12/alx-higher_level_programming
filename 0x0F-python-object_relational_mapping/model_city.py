#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# from model_state import Base, State
# from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
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
