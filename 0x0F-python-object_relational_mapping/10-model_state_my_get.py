#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create an SQLAlchemy engine object to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create the tables defined in the Base class (if they do not exist already)
    Base.metadata.create_all(engine)

    # Create a Session class bound to the engine
    Session = sessionmaker(bind=engine)

    # Instantiate a Session object
    session = Session()

    # Query the State table to filter instances by the name passed as an argument
    instance = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        # Try to access the first instance returned by the query and print its id
        print(instance[0].id)
    except IndexError:
        # If no instance is found (IndexError), print "Not found"
        print("Not found")
