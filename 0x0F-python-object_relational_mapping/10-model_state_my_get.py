#!/usr/bin/python3
"""This script prints the State object with the name
passed as argument from the database hbtn_0e_6_usa by
using SQLAlchemy
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_engine = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(mysql_engine.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == argv[4])
    if states.count():
        for state in states:
            print(state.id)
    else:
        print("Not found")
