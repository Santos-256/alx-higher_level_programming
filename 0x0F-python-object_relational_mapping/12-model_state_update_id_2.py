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
    # Query the State table to retrieve the State object with the specified ID (2 in this case)
    new_instance = session.query(State).filter_by(id=2).first()
    # Update the name attribute of the retrieved State object to the new name passed as an argument
    new_instance.name = 'New Mexico'
    # Commit the transaction to apply the changes to the database
    session.commit()
