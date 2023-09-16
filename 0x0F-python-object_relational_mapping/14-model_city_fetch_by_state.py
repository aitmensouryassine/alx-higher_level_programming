#!/usr/bin/python3
"""script that prints all City objects
from the database hbtn_0e_14_usa by using sqlalchemy
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_engine = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(mysql_engine.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State) \
                    .join(State, City.state_id == State.id) \
                    .order_by(City.id).all()
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
