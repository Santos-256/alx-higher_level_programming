#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
     # Establishing a connection to the MySQL database using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

# Creating a new State object named 'California'
    newState = State(name='California')
    # Creating a new City object named 'San Francisco'
    newCity = City(name='San Francisco')
    # Establishing a relationship between the state and the city by-
    # -appending the city to the cities attribute of the state
    newState.cities.append(newCity)

# Adding both the state and the city objects to the session
    session.add(newState)
    session.add(newCity)
     # Committing the transaction, making the changes persistent in the database
    session.commit()
