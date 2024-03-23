#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State  # Importing Base and State classes from model_state module

from sqlalchemy import (create_engine) # Importing create_engine function from SQLAlchemy

if __name__ == "__main__":
     # Create an SQLAlchemy engine object to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

     # Create the tables defined in the Base class (if they do not exist already)
    Base.metadata.create_all(engine)
