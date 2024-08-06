#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
import sqlalchemy
from model_state import Base, State


if __name__ == '__main__':
    engine = sqlalchemy.create_engine("mysql+mysqldb://{}:{}@\
localhost:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)
    state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))
    session.close()
