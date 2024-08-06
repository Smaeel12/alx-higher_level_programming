#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints all City objects from the
database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import Session
from model_city import Base, City
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    cities = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
