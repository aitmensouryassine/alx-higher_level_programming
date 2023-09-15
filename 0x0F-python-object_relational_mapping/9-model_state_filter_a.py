#!/usr/bin/python3
"""This script lists all State objects that contain
the letter a from the database hbtn_0e_6_usa by using
SQLAlchemy
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_engine = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(mysql_engine.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%"))
    for state in states:
        print("{}: {}".format(state.id, state.name))
