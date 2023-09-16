#!/usr/bin/python3
"""script that creates the State 'California' with the City
'San Francisco' from the database hbtn_0e_100_usa
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    mysql_engine = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(mysql_engine.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="California")
    newCity = City(name="San Francisco", state=newState)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
